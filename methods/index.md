---
---

Empirical software engineering research relies primarily on three methods.

<span class="fixme">rewrite intro</span>

<span class="fixme">Excel and evidence; Scottish verdict https://github.com/gvwilson/buildtogether.tech/issues/52</span>

## Controlled Experiments

<span class="fixme">Revise description of experimental method https://github.com/gvwilson/buildtogether.tech/issues/15</span>

The first method is controlled experiments: subjects are given a task and some
aspect of their performance is measured. Subjects are typically divided into a
<span g="control_group">control group</span> (who do things as normal) and a
<span g="treatment_group">treatment group</span> (who do things in an
alternative way). If the difference between the groups is large enough
statistically, the experimenter publishes a paper and moves on.

There are several traps in this approach for the unwary
<cite>deOliveiraNeto2019</cite>:

Experimenter bias.
:   People have many biases, both conscious and unconscious.  In order to make
    sure that these don't inadvertently affect the results, subjects should be
    assigned to groups at random. Going even further, experiments in medicine
    are often <span g="double_blind">double blind</span>: neither the subject
    nor the person administering the treatment knows which subjects are getting
    the new heart medication and which are getting a <span
    g="placebo">placebo</span>. It's usually not possible to achieve this when
    doing software engineering experiments.

Significance hacking.
:   If you measure enough things and look for enough correlations, you will
    almost certainly find *something* that passes a test for statistical
    significance. For example, there is a strong correlation between the number
    of letters in winning words in spelling competitions and the number of
    people killed by venomous spiders <cite>Vigen2015</cite>. To guard against
    this, researchers should <span g="pre_registration">pre-register</span>
    their analyses, i.e., say in advance what they're going to compare against
    what, and then use various statistical techniques that require a higher
    standard of proof when they are checking more possible combinations.

Failure to publish negative results.
:   An experiment isn't a failure if it doesn't find something that is
    statistically significant: ruling something out is just as useful as finding
    something new. However, negative results are not as exciting (and not as
    beneficial to a researcher's career), so they often go unreported.

Controlled experiments are expensive.
:   Getting a few undergraduates in a lab for an hour each is easy; getting
    professional programmers to do something new or different for several months
    is not. As a result, researchers often rely on <span
    g="quasi_experiment">quasi-experiments</span> and look at pre-existing
    groups (e.g., compare programmers who have decided for themselves to use a
    new IDE against ones who have not). Quasi-experiments are cheaper and easier
    to set up, but researchers must be careful to account for <span
    g="confounding_variables">confounding variables</span>. For example, are
    programmers who choose to use an IDE younger and therefore less experienced
    than ones who use legacy text editors? If so, how does that difference
    skew the results?

## Data Mining

Quasi-experiments blend into the second major research approach, which uses
statistics and machine learning to find patterns in whatever data the researcher
can get her hands on. Doing this is called <span g="data_mining">data
mining</span>, and most studies of this kind make use of the wealth of
information available online at sites like GitHub and Stack Overflow or from
millions of crash reports collected online <cite>Glerum2009</cite>.  Data mining
has produced many valuable insights, but has challenges of its own.  The largest
of these is that people who work in the open aren't typical, so any results we
get from studying them must be interpreted cautiously.

<div class="callout" markdown="1">

### Dark matter developers

In 2012, Scott Hanselman coined the term "[dark matter
developers][hanselman-dark-matter]" to describe programmers who don't blog,
don't answer questions in online forums, don't have their work in public
repositories, and so on. Just as dark matter makes up most of the universe, dark
matter developers make up most of our industry, and just as the matter we can
see is vanishingly atypical, so too are developers who radiate information.

One reason for this is that the web ranges from unwelcoming to actively hostile
for people from under-represented groups <cite>Ford2016,May2019</cite>.
Unfortunately, in-person workplaces are often no better: many are filled with
small signs that make many people feel out of place <cite>Cheryan2009</cite>.
<span x="rights"></span> takes a closer look at these issues.

</div>

## Qualitative Methods

The third set of approaches are called <span g="qualitative_method">qualitative
methods</span>, and involve close analysis of a small number of cases to tease
out common patterns.  Articles like <cite>Sharp2016</cite> do an excellent job
of explaining how these methods work and what their strengths and limitations
are.

<cite>Washburn2016</cite> demonstrates the kinds of insights these methods can
produce. They analyzed 155 <span g="post_mortem">post mortem</span> reviews of
game projects to identify characteristics of game development, link the
characteristics to positive and negative experiences, and distill a set of best
practices and pitfalls for game development. Their results are shown in <span
f="washburn-2016-what-went-right"></span> and <span
f="washburn-2016-what-went-wrong"></span>, and their description of their method
is worth repeating in full:

<blockquote markdown="1">

Initially, we started with 12 categories of common aspects of development…  In
order to identify additional categories, we performed 3 iterations of analysis
and identification.  The first week, we each read and analyzed 3 postmortem
reviews each, classifying the items discussed in each section into the 12
predetermined categories of common aspects that impact development.  While
analyzing these reviews, we identified additional categories of items that went
right or wrong during development, and revisited the reviews we had already
analyzed to update the categorization of items. For the next two weeks we
repeated this process of analyzing postmortems and identifying categories,
analyzing 10 postmortems each in week 2, and 15 postmortems each in week
3. After each iteration, we discussed the additional categories we identified,
and determined if they were viable.

After our initial iterations for identifying additional categories, we had
completed the analysis of 60 postmortem reviews.  We then stopped identifying
new categories, and began analyzing postmortems at a combined rate of about 40
postmortem reviews per week.  After each week we reviewed what we had done to
ensure we both had the same understanding of each category.  This continued
until we had analyzed all the postmortem reviews.

</blockquote>

{% include figure
   id="washburn-2016-what-went-right"
   img="washburn-2016-what-went-right.png"
   alt="What went right"
   cap="What went right in game development (from Washburn et al)." %}

{% include figure
   id="washburn-2016-what-went-wrong"
   img="washburn-2016-what-went-wrong.png"
   alt="What went wrong"
   cap="What went wrong in game development (from Washburn et al)." %}

<div class="callout" markdown="1">

### Small is beautiful

My classes in engineering taught me to look down on anything that wasn't a
controlled laboratory experiment whose results could be neatly displayed in a
scatterplot or bar chart.  It wasn't until I was in my 30s that I accepted that
the "fuzzy" methods of the social sciences were just as rigorous when used
properly and the only ones that could produce certain valuable insights.

</div>
