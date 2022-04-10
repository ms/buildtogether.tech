---
title: "Organizing Analyais"
lede: "What goes where in a data analysis project"
template: page
---

-   The steps in most data analysis projects are:
    1.  Find data
    2.  Collect it
    3.  Tidy it
    4.  Do calculations
    5.  Report results
-   How can we make all of this easier to understand, reproduce, and extend?
-   To illustrate, let's find out how many versions of Python packages there are

## Getting Data

-   Data source is simple [PyPI][pypi] package index page <https://pypi.org/simple/>
    -   Has HTML links to one page per package
-   Each package's page has links to released versions in various formats
    -   205K entries in total
-   Some redundancy, e.g., [% g wheel "wheels" %] and [% g gzip "gzip'd" %] [% g tar "tar" %] files
    -   We have to decide whether to count these separately or fold them together
    -   Every statistical result is the product of many decisions
    -   Different decisions produce different results

## Scraping Web Pages

-   Use the [`requests`][requests] library to get page
-   HTML is very highly structured,
    so we can get away with using [% g regular_expression "regular expressions" %] to extract fields
    -   [This is a sin][regular-expressions-html]
    -   Look at better ways in an exercise

```{.python title="get-index-page-initial.py"}
import sys
import requests
import re
import time


# Match package URL in main index page.
RE_PACKAGE = re.compile(r'<a href="(.+?)">')

# Match release URL in package index page.
RE_RELEASE = re.compile(r'<a href=".+?">(.+?)</a>')

# PyPI domain.
DOMAIN = 'https://pypi.org'


index_response = requests.get(f'{DOMAIN}/simple/')
print('Package,Releases')
all_packages = RE_PACKAGE.findall(index_response.text)
for package in all_packages:
    name = package.strip('/').split('/')[-1]
    url = f'{DOMAIN}{package}'
    package_response = requests.get(url)
    count = len(RE_RELEASE.findall(package_response.text))
    print(f'{name},{count}')
```

-   First run crashed after a few minutes because of a missing sub-page
-   So add a check on the HTTP status codes from queries
    -   Record [% g na "`NA`" %] for those pages
    -   And hope that analysis software interprets this as "not available"
        rather than Namibia or the element sodium
-   Add some logging so that we can tell how long the program is going to take to run
    -   About 30K seconds, or 8.5 hours

<div class="callout" markdown="1">
### A Small Grumble

Ideally, the code above would morph into the code shown below
so that you could see what was the same and what was different.
A second-best solution would be an easy way to highlight modified lines,
with an emphasis on "easy".
One day...
</div>

```{.python title="get-index-page.py"}
#!/usr/bin/env python

import sys
import requests
import re
import time


# Match package URL in main index page.
RE_PACKAGE = re.compile(r'<a href="(.+?)">')

# Match release URL in package index page.
RE_RELEASE = re.compile(r'<a href=".+?">(.+?)</a>')

# PyPI domain.
DOMAIN = 'https://pypi.org'


# Get main index page.
index_response = requests.get(f'{DOMAIN}/simple/')
assert index_response.status_code == 200, \
    f'Unexpected status for index page {index_response.status_code}'

# Get sub-pages and count releases in each.
num_seen = 0
t_start = time.time()
print('Package,Releases')
all_packages = RE_PACKAGE.findall(index_response.text)
for package in all_packages:
    name = package.strip('/').split('/')[-1]
    url = f'{DOMAIN}{package}'
    package_response = requests.get(url)
    if package_response.status_code != 200:
        print(f'Unexpected status for package page {url}: {package_response.status_code}',
              file=sys.stderr)
        count = 'NA'
    else:
        count = len(RE_RELEASE.findall(package_response.text))
    print(f'{name},{count}')
    num_seen += 1
    if (num_seen % 10) == 0:
        t_elapsed = time.time() - t_start
        t_expected = len(all_packages) * t_elapsed / num_seen
        print(f'{num_seen} @ {t_elapsed:.1f} / {len(all_packages)} @ {t_expected:.1f}',
              file=sys.stderr)
```

-   Still not a friendly program
    -   If several thousand people run this program at the same time it will slow PyPI down
-   Unlikely in this case,
    but a school could easily wind up being blacklisted
    if a hundred students are grabbing data at the same time
-   Popular data sources have to manage floods of requests
-   Programs should [% g throttle "throttle" %] their own activity

## Reporting Results

-   [% g descriptive_statistics "Descriptive statistics" %] are key facts about data
-   The [% g median "median" %] is the middle value
    -   If \\(  N \\) is odd, sort and take the middle
    -   If \\(  N \\) is even, sort and average the two middle values
-   The [% g mean "mean" %] is the weighted center of the data
    -   \\(   \mu = \frac{1}{N} \sum x_i  \\)
-   If there are a few outliers, the mean can be very different from the median
    -   Mean of `[1, 2, 3, 4, 100]` is 22, but median is 3
    -   Which is why those who have like to quote means rather than medians
-   [% g variance "Variance" %] measures the spread of values
    -   \\(   \sigma^2 = \frac{1}{N} \sigma (x_i - \mu)^2  \\)
    -   Squaring the differences gives extra weight to outliers...
    -   ...but makes variance hard to use directly, since its units are (for example) lines squared
-   Instead, use the [% g standard_deviation "standard deviation" %]
    -   Square root of the variance, so it has the same units as the data

```{.python title="version-statistics.py"}
import sys
import pandas as pd

datafile = sys.argv[1]
packages = pd.read_csv(datafile)
print(packages.agg(['mean', 'median', 'var', 'std']))
```
```sh
python version-statistics.py release-count.csv
```
```txt
            Releases
mean       11.236351
median      4.000000
var      2501.398099
std        50.013979
min         0.000000
max     10797.000000
```

-   Half of all packages have had fewer than four releases
-   The mean is only slightly higher (1/5 of a standard deviation)
-   And yeah, a package with almost 11,000 releases will pull things up
    -   `ccxt` is a cryptocurrency, so they might be using releases as ledger updates

## Displaying Results

-   Again, a histogram shows the distribution of values
    -   Its shape (and hence our interpretation) depends on how we [% g bin "bin" %] the data
-   Given how long data collection takes,
    most sensible thing is to collect the data once and write separate plotting programs to view it
    -   Provide name of data file on the command line

```{.python title="version-histogram.py"}
import sys
import pandas as pd
import plotly.express as px

datafile = sys.argv[1]
packages = pd.read_csv(datafile)

print('Distribution of Releases')
print(packages.groupby('Releases').count())
print(f'{packages["Releases"].isna().sum()} missing values')

fig = px.histogram(packages, x='Releases', nbins=100, log_y=True, width=600, height=400)
fig.show()
fig.write_image('figures/release-count.svg')
```
```sh
python version-histogram.py release-count.csv
```
```txt
Distribution of Releases
          Package
Releases         
0.0         11721
1.0         33992
2.0         32829
3.0         14999
4.0         18339
5.0          8946
...
4505.0          1
5133.0          1
6460.0          1
10797.0         1

[561 rows x 1 columns]
14 missing values
```

[% figure slug="release-count" img="figures/release-count.svg" caption="Release Count" alt="Histogram showing steeply declining curve from X equals 0 to X above 10,000 with peak over 200,000 at X equals 0." %]

-   Printed output includes the value for packages with zero releases
-   But does the histogram?
    -   What does Plotly do with `log(0)`?
-   Let's try:

```{.python title="version-histogram.py"}
slice = packages[packages['Releases'] < 100]
fig = px.histogram(slice, x='Releases', nbins=100, log_y=True, width=600, height=400)
fig.show()
fig.write_image('figures/release-count-low.svg')
```

[% figure slug="release-count-low" img="figures/release-count-low.svg" caption="Release Count (Low End)" alt="Histogram showing smoothly declining curve from X equals 0 to X equals 100 with over 10,000 values at X equals zero and alternating high and low bars." %]

-   It seems to include zero
-   But that double-stepping looks weird
-   Is it a plotting artifact or a result of double-counting packages that are released in multiple formats?
    -   For that, we need better data

-   Use a [% g violin_plot "violin plot" %] to get a feel for the shape of the data

```{.python title="version-other-plots.py"}
datafile = sys.argv[1]
packages = pd.read_csv(datafile)
slice = packages[packages['Releases'] < 100]
fig = px.violin(slice, y='Releases', width=600, height=400)
fig.show()
fig.write_image('figures/release-count-violin.svg')
```

[% figure slug="release-count-violin" img="figures/release-count-violin.svg" caption="Violin Plot (Low End)" alt="Symmetric vertical violin plot with almost all values in bulge at bottom end." %]

-   Can also use a [% g box_and_whisker_plot "box-and-whisker plot" %]
    -   Lines show minimum, first [% g quartile "quartile" %], median, third quartile, and maximum
    -   Box shows first quartile to third quartile (so half the data lies inside the box)
-   Distance from first quartile to third quartile is the [% g iqr "inter-quartile range" %]
    -   Lower and upper lines cut off at 1.5\\(  \times \\)IQR
    -   Anything beyond that is considered an outlier and shown as a point

```{.python title="version-other-plots.py"}
fig = px.box(slice, y='Releases', width=600, height=400)
fig.show()
fig.write_image('figures/release-count-box.svg')
```

[% figure slug="release-count-box" img="figures/release-count-box.svg" caption="Box-and-Whisker Plot (Low End)" alt="Symmetric vertical box plot with almost all values at low end." %]

## More Project Structure

-   Data analysis projects are a special case of software development projects
-   Starting point is [% g taschuks_rules "Taschuk's Rules" %]:
    1.  Use version control.
    1.  Document your code and usage
    1.  Make common operations easy to control.
    1.  Version your releases.
    1.  Reuse software (within reason)
    1.  Rely on build tools and package managers for installation.
    1.  Do not require root or other special privileges to install or run.
    1.  Eliminate hard-coded paths.
    1.  Include a small test set that can be run to ensure the software is actually working.
    1.  Produce identical results when given identical inputs.
-   The first three rules are the most important
    -   We assume you are already using version control
-   Restructure our program
-   The [% g main_driver "main driver" %] lays out the overall flow of the program
    -   Parse command-line options
    -   Set up
    -   Produce output incrementally while processing data
        (rather than read-process-write)
-   Include a [% g docstring "docstring" %] for help

```{.python title="bin/get-all-versions.py"}
def main():
    '''
    Main driver.
    '''
    args = parse_args()
    all_packages = get_package_list(args)
    progress = initialize_progress(args, all_packages)
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(['Package', 'Release'])
    for package in all_packages:
        get_package_info(package, writer)
        report_progress(progress)

# ...

if __name__ == '__main__':
    main()
```

-   Uses the [`csv`][csv-py] package to format output instead of printing strings ourselves
    -   Takes care of [% g escape_character "escaping" %] special characters

-   Parse command-line arguments

```{.python title="bin/get-all-versons.py"}
def parse_args():
    '''
    Parse command-line arguments.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--restart', type=str, help='restart from this package')
    parser.add_argument('--verbose', action='store_true', help='show progress')
    return parser.parse_args()
```

-   Use [`argparse`][argparse] to parse command-line arguments
    -   `--verbose` to track progress (because it takes hours)
    -   `--restart` to start from a specified point because networks fail
        -   May result in redundant records
        -   Definitely results in header appearing multiple times
        -   Clean up afterward

-   Get the main package list

```{.python title="bin/get-all-versons.py"}
# Match package URL in main index page.
RE_PACKAGE = re.compile(r'<a href="(.+?)">')

# ...

def get_package_list(args):
    '''
    Get main package listing page and extract values.
    '''
    response = requests.get(f'{BASE_URL}')
    assert response.status_code == 200, \
        f'Unexpected status for index page {response.status_code}'
    all_packages = RE_PACKAGE.findall(response.text)
    all_packages = [p.strip('/').split('/')[-1] for p in all_packages]
    if (args.restart):
        start = all_packages.index(args.restart)
        if (start < 0):
            print(f'Unable to find {args.restart} in package list',
                  file=sys.stderr)
            sys.exit(1)
        all_packages = all_packages[start:]
    return all_packages
```

-   Regular expression is at the top of the file with other "constants"
    -   Unfortunately no way to attach a docstring
-   Get the main package listing page
    -   Fail if it can't be found rather than supporting restart
    -   Slice here to get the package list
-   Handle restart here as well (and fail if that isn't going to work)
-   Use `all_packages` rather than just `packages` as a name
    so that the code reads aloud more clearly
    -   Look at consistent variable naming in the exercises

-   Get information about a single package

```{.python title="bin/get-all-versions.py"}
def get_package_info(name, writer):
    '''
    Get and print information about a specific package.
    '''
    url = f'{BASE_URL}{name}'
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Unexpected status for package page {url}: {response.status_code}',
              file=sys.stderr)
        writer.writerow([name, 'NA'])
    else:
        all_releases = RE_RELEASE.findall(response.text)
        for release in all_releases:
            writer.writerow([name, release])
```

-   Get packages one at a time
    -   Some attempts fail (status code is not 200)
    -   Record these as `NA` rather than failing because we *can* proceed

-   Report progress
-   Anything that takes long enough to worry about should tell users it's OK
    -   But that should be an option so that it *doesn't* ask for attention in a production pipeline
-   Could initialize the record-keeping in `main`,
    but that function reads more cleanly if this low-level detail is hidden away
-   Goes to `sys.stderr` so that regular output can be redirected to file

```{.python title="bin/get-all-versions.py"}
def initialize_progress(args, packages):
    '''
    Initialize record keeping for progress monitoring.
    '''
    return {
        'report': args.verbose,
        'start': time.time(),
        'expected': len(packages),
        'seen': 0
    }


def report_progress(progress):
    '''
    Report progress, updating the progress record as a side effect.
    '''
    if (not progress['report']):
        return
    progress['seen'] += 1
    if (progress['seen'] % 10) == 0:
        elapsed = time.time() - progress['start']
        duration = progress['expected'] * elapsed / progress['seen']
        print(f"{progress['seen']} @ {elapsed:.1f} / {progress['expected']} @ {duration:.1f}",
              file=sys.stderr)
```

-   This program does not have an option for output file
    -   Should probably have one option to create a new file and another to append to an existing file
-   Should probably also have an option to stop trying if enough pages fail

## Noble's Rules

[% g nobles_rules "Noble's Rules" %] are a way to organize small data analysis projects.
Each one lives in a separate Git repository
whose subdirectories are organized by purpose:

-   `src` (short for "source") holds source code
    for programs written in languages like C or C++ that need to be compiled.
    Many projects don't have this directory
    because all of their code is written in languages that don't need compilation.

-   Runnable programs go in `bin` (an old Unix abbreviation for "binary", meaning "not text").
    This includes the compiled and runnable versions of C and C++ programs,
    and also shell scripts,
    Python or R programs,
    and everything else that can be executed.

-   Raw data goes in in `data` and is never modified after being stored.

-   Results are put in `results`.
    This includes cleaned-up data
    and everything else that can be rebuilt using what's in `bin` and `data`.
    If intermediate results can be re-created quickly and easily,
    they might not be stored in version control,
    but anything that is included in a report should be here.

-   Finally,
    documentation and manuscripts go in `doc`.

Documentation is often generated from source code,
and it's usually a bad idea to mix handwritten and machine-generated files,
so most projects now use separate subdirectories for software documentation (`doc`)
and reports (`reports` or `papers`).
People also often create a `figures` directory to hold generated figures
rather than putting them in `results`.

The directories in the top level of each project are organized by purpose,
but the directories within `data` and `results` are organized chronologically
so that it's easy to see when data was gathered and when results were generated.
These directories all have names in [% g iso_date_format "ISO date format" %] like `YYYY-MM-DD`
to make it easy to sort them chronologically.
This naming is particularly helpful when data and results are used in several reports.

At all levels,
filenames should be easy to match with simple patterns.
For example,
a project might use <code><em>species</em>_<em>organ</em>_<em>treatment</em>.csv</code>
as a file-naming convention,
giving filenames like `human_kidney_cm200.csv`.
This allows `human_*_cm200.csv` to match all human organs
or `*_kidney_*.csv` to match all kidney data.
It does produce long filenames,
but tab completion means you only have to type them once.
Long filenames are just as easy to match in programs:
Python's [`glob`][glob] module will take a pattern and return a list of matching filenames.

## Tracking Data

-   Data should be published along with reports
    -   How else can people check or extend your work?
-   Large datasets that are archived and maintained by trusted institutions (e.g., open government data)
    don't need to be stored
    -   Just include a link, a method for downloading, and a date
-   If a report involves a new dataset:
    -   Always use [% g tidy_data "tidy data" %].
    -   Include keywords describing the data in the project's `README.md`
        so that they appear on its home page and can easily be found by search engines.
    -   Give every dataset and every report a unique identifier.
    -   Use well-known formats like CSV and HDF5.
    -   Include an explicit license.
    -   Include units and other metadata.

The last point is often the hardest for people to implement,
since many researchers have never seen a well-documented dataset.
The [% g data_manifest "data manifest" %] for [% b Diehm2018 %] is a good example;
each dataset is described by an entry like this:

<div class="callout" markdown="1">

-   What is this?: This file contains all of the measurements for 80 pairs of blue jeans from the most popular and widely available brands in the US.
-   Source(s): All data was collected from manual measurements by Jan Diehm and Amber Thomas at brick and mortar stores in Nashville, New York, and Seattle.
    All measurements of front pockets were taken of the right-hand-side front pocket of empty jeans.
-   Last Modified: August 13, 2018
-   Contact Information: Amber Thomas
-   Spatial Applicability: United States
-   Temporal Applicability: All measurements were collected between June 29 and August 6, 2018
-   Observations (Rows): Each row represents data from a single pair of jeans.
-   Variables (Columns):

| Header | Datatype | Description |
|---|---|---|
| `brand` | text | The full brand name. |
| `style` | text | The cut of each pair of jeans (in our analysis, we combined straight and boot-cut styles and skinny and slim styles, but these remain separated here). |
| `menWomen` | text | Whether the jeans were listed as "men's" or "women's". |
| `name` | text | The name of the specific style of measured pair of jeans as indicated by the tag. (e.g., `Fave Super Skinny Jean`). |
| `brandSize` | text | The size of jeans we measured. Each size reflects the sizing for each brand closest to a 32-inch waistband as indicated by the brand's website. |
| `waistSize` | number | The waistband size (in inches) of each measured pair as reported on the brand's website. |
| ... | ... | ... |

</div>

<div class="callout" markdown="1">
### FAIR play

The [FAIR Principles][fair-principles] [% b Brock2019 %]
state that data should be *findable*, *accessible*, *interoperable*, and *reusable*.
They are still aspirational for most researchers,
but they tell us what to aim for.
</div>

## Exercises

### Why `NA`?

Why do statistical packages prefer `NA` to (for example) an empty cell in a table?

### Getting All Releases

Rewrite the data collection script to capture all release filenames
so we can filter duplicates,
look at numbering, etc.
(When you're getting data,
get *all* the data.)

### Controlling Logging

Rewrite the script to make progress logging controllable with command-line option.

### Beautiful Soup

Rewrite the script to parse the HTML using [Beautiful Soup][beautiful-soup].
(You may find the documentation on searching the document tree helpful.)

### Logarithmic Zeroes

How should packages with zero releases be displayed when we are scaling logarithmically?
(Those entries are currently discarded because \\(  log(0) \\) is undefined.)

### Fifty Per Cent

Suppose that 50% of the links in the index page failed to resolve.
How would this change our script?
How would it change what statistics we calculate or how we report them?
