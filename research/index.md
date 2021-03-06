---
---

There are a lot of citations in the preceding chapters, both to back up various
claims and to introduce the idea that we actually know stuff about things.
Researchers have been studying programs and programmers since at least the
1960s, and while there are still many unknowns, we actually do know a lot about
what works and what doesn't.

Sadly, most people in industry still don't know what researchers have found out,
or even what kinds of questions they could answer. One reason is their belief
that software engineering research is so divorced from real-world problems that
it has nothing of value to offer them (an impression that is reinforced by how
irrelevant most popular software engineering textbooks seem to the
undergraduates who are forced to wade through them, and by how little software
most software engineering professors have ever built).

Another reason is many programmers' disdain for qualitative research methods,
which are often dismissed out of hand (and out of ignorance) as "soft". A third
reason is ignorance---often willful---among practitioners themselves. People
will cling to creationism, refuse to accept the reality of anthropogenic climate
change, or insist that vaccines cause autism; it is therefore no surprise that
many programmers continue to act as if a couple of pints and a quotation from
some self-appointed guru constitute "proof" that one programming language is
better than another.

As with all research, though, some caution is required when interpreting
results:

Theories change as more data becomes available.
:   Computing education research (CER) is a young discipline: the American
    Society for Engineering Education was founded in 1893 and the National
    Council of Teachers of Mathematics in 1920, but the Computer Science
    Teachers Association didn't exist until 2005.  While a steady stream of new
    insights are reported at conferences, we simply don't know as much about
    learning to program as we do about learning to read, play a sport, or do
    basic arithmetic.

Most of these studies' subjects are WEIRD.
:   They are from Western, Education, Industrialized, Rich, and Democratic
    societies <cite>Henrich2010</cite>.  What's more, they are also mostly young
    and in institutional classrooms, since that's the population most
    researchers have easiest access to.  We know much less about adults, members
    of marginalized groups, learners in free-range settings, or <span
    g="end_user_programmer">end user programmers</span>, even though there are
    far more of them.

The data we have doesn't capture everything.
:   <cite>Aranda2009</cite> found that in every one of the bugs they traced,
    some key insight or action wasn't captured digitally. Similarly,
    <cite>Herzig2013</cite> carefully examined thousands of bug reports from
    several projects and found that many mis-report themselves in ways that will
    inevitably skew the results of simplistic data mining. This doesn't mean
    results are wrong, but it *does* mean we have to look closely at what was
    measured and what wasn't.

<div class="callout" markdown="1">
### A cautionary tale

<cite>Zeller2011</cite> did what too many researchers in too many fields do on a
regular basis: throw some data at some machine learning algorithms and then
claim that whatever comes out the other end is significant. Luckily for us, they
did it on purpose to make a point.

They took data on code and errors for the Eclipse IDE and correlated the two to
find good predictors of bugs. Which sounds sensible---except they did the
correlation at the ASCII character level. It turns out that the characters that
are most highly correlated with errors are 'i', 'r', 'o', and 'p'. What is a
sensible researcher to do facing these findings? Well take those letters out of
the keyboard, of course!  The authors then go over everything that's wrong with
their approach, from lack of theoretical grounding to dishonest use of
statistics. Before you read too much research, make sure to read this.
</div>

If this was an academic treatise, I would therefore preface most claims with
qualifiers like, "Some research may seem to indicate that…"  But since
programmers have to make decisions regardless of whether research has produced
an unambiguous answer or not, this chapter presents actionable best guesses
rather than nuanced perhapses.

## What Methods Do Researchers Use?

FIXME: controlled experiments

FIXME: data mining

The third set of approaches are called <span g="qualitative_method">qualitative
methods</span>, and involve close analysis of a small number of cases to tease
out common patterns.  My classes in engineering taught me to look down on
anything that wasn't a controlled laboratory experiment whose results could be
neatly displayed in a scatterplot or bar chart.  It wasn't until I was in my 30s
that I realized (grudgingly at first) that the "fuzzy" methods used by the
social sciences were just as rigorous when used properly and the only ones that
could produce certain valuable insights. Articles like <cite>Sharp2016</cite> do
an excellent job of explaining how these methods work and what their strengths
and limitations are.

<cite>Washburn2016</cite> is just one example of the kinds of valuable insights
these methods can produce. They analyzed 155 <span g="post_mortem">post
mortem</span> reviews of game projects to identify characteristics of game
development, link the characteristics to positive and negative experiences, and
distill a set of best practices and pitfalls for game development. Their results
are shown in <span f="washburn-2016-what-went-right"></span> and <span
f="washburn-2016-what-went-wrong"></span>, and their description of their method
is worth repeating in full:

>   Initially, we started with 12 categories of common aspects of development…
>   In order to identify additional categories, we performed 3 iterations of
>   analysis and identification.  The first week, we each read and analyzed 3
>   postmortem reviews each, classifying the items discussed in each section
>   into the 12 predetermined categories of common aspects that impact
>   development.  While analyzing these reviews, we identified additional
>   categories of items that went right or wrong during development, and
>   revisited the reviews we had already analyzed to update the categorization
>   of items. For the next two weeks we repeated this process of analyzing
>   postmortems and identifying categories, analyzing 10 postmortems each in
>   week 2, and 15 postmortems each in week 3. After each iteration, we
>   discussed the additional categories we identified, and determined if they
>   were viable.
>
>   After our initial iterations for identifying additional categories, we had
>   completed the analysis of 60 postmortem reviews.  We then stopped
>   identifying new categories, and began analyzing postmortems at a combined
>   rate of about 40 postmortem reviews per week.  After each week we reviewed
>   what we had done to ensure we both had the same understanding of each
>   category.  This continued until we had analyzed all the postmortem reviews.

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

## What Do We Know About Novice Programmers?

<cite>Soloway1984,Soloway1986</cite> pioneered the exploration of novice and
expert programming strategies.  The key finding is that experts know both "what"
and "how", i.e., they understand what to put into programs *and* they have a set
of program patterns or plans to guide their construction.  Novices lack both,
but most teachers focus solely on the former, even though bugs are often caused
by not having a strategy for solving the problem rather than to lack of
knowledge about the language.  <cite>Muller2007</cite> is just one of many
studies proving the benefits of teaching common patterns explicitly, and
decomposing problems into patterns creates natural opportunities for creating
and labeling subgoals <cite>Margulieux2012,Margulieux2016</cite>.

The biggest misconception novices have---sometimes called the "superbug" in
coding---is the belief that computers understand what people mean in the way
that another human being would <cite>Pea1986</cite>.  <cite>Sorva2018</cite>
presents over forty other misconceptions that teachers can also try to clear up,
many of which are also discussed in <cite>Qian2017</cite>'s survey.

The mistakes novices make can tell us what to prioritize in our teaching, but it
turns out that most teachers don't know how common different kinds of mistakes
actually are.  The largest study of this is <cite>Brown2017</cite>, which found
that mismatched quotes and parentheses are the most common type of errors in
novice Java programs, but also the easiest to fix, while some mistakes (like
putting the condition of an `if` in `{…}` instead of `(…)` are most often made
only once.  Unsurprisingly, mistakes that produce compiler errors are fixed much
faster than ones that don't.  Some mistakes, however, are made many times, like
invoking methods with the wrong arguments (e.g., passing a string instead of an
integer).

<cite>Brown2017</cite> also compared the mistakes novices actually make with what
their teachers thought they made.  They found that, "…educators formed only a
weak consensus about which mistakes are most frequent, that their rankings bore
only a moderate correspondence to the students in the…data, and that educators'
experience had no effect on this level of agreement."  For example, mistaking
`=` (assignment) and `==` (equality) wasn't nearly as common as most teachers
believed.

More than a decade ago, <cite>McCauley2008</cite> wrote, "It is surprising how
little page space is devoted to bugs and debugging in most introductory
programming textbooks."  Little has changed since: there are hundreds of books
on compilers and operating systems, but only a handful about debugging, and I
have never seen an undergraduate course devoted to the subject.

<cite>Fitzgerald2008,Murphy2008</cite> found that good debuggers were good
programmers, but not all good programmers were good at debugging.  Those who
were used a symbolic debugger to step through their programs, traced execution
by hand, wrote tests, and re-read the spec frequently, which are all teachable
habits.  However, tracing execution step by step was sometimes used
ineffectively: for example, a novice might put the same `print` statement in
both parts of an `if`-`else`.  Novices would also comment out lines that were
actually correct as they tried to isolate a problem; teachers can make both of
these mistakes deliberately, point them out, and correct them to help novices
get past them.

Teaching novices how to debug can also help make classes easier to manage.
<cite>Alqadi2017</cite> found that learners with more experience solved
debugging problems significantly faster, but times varied widely: 4--10 minutes
was a typical range for individual exercises, which means that some learners
need 2--3 times longer than others to get through the same exercises.  Teaching
the slower learners what the faster ones are doing will help make the group's
overall progress more uniform.

Debugging depends on being able to read code, which multiple studies have shown
is the single most effective way to find bugs
<cite>Basili1987,Kemerer2009,Bacchelli2013</cite>.  The code quality rubric
developed in <cite>Stegeman2014,Stegeman2016</cite> is a good checklist of
things to look for, though it is best presented in chunks rather than all at
once.

Novice programmers seem just as reluctant to test software as professionals.
There's no doubt that doing it is valuable---<cite>Carter2017</cite> found that
high-performing novices spent a lot of time testing, while low performers spent
much more time working on code with errors---and many teachers require learners
to write tests for assignments.  But how well do they do this?  One answer comes
from <cite>Brian2015</cite>, which scored learners' programs by how many
teacher-provided test cases those programs passed, and conversely scores test
cases written by learners according to how many deliberately-seeded bugs they
caught.  They found that novices' tests often have low coverage (i.e., they
don't test most of the code) and that they often test many things at once, which
makes it hard to pinpoint the causes of errors.

Another answer comes from <cite>Edwards2014</cite>, which looked at all of the
bugs in all novices' code submissions combined and identified those detected by
the novices' test suite.  They found that novices' tests only detected an
average of 13.6% of the faults present in the entire program population.  What's
more, 90% of the novices' tests were very similar, which indicates that novices
mostly write tests to confirm that code is doing what it's supposed to rather
than to find cases where it isn't.

Finally, incomprehensible error messages are a major source of frustration for
novices (and for experienced programmers as well).  Several researchers have
therefore explored whether better error messages would make a difference.  For
example, <cite>Becker2016</cite> rewrote some of the Java compiler's messages so
that instead of:

```out
C:\stj\Hello.java:2: error: cannot find symbol
        public static void main(string[ ] args)
^
1 error
Process terminated ... there were problems.
```

{: .continue}
learners would see:

```out
Looks like a problem on line number 2.
If "string" refers to a datatype, capitalize the 's'!
```

{: .continue}
Sure enough, novices given these messages made fewer repeated errors and fewer
errors overall.

<cite>Barik2017</cite> went further and used eye tracking to show that despite
the grumblings of compiler writers, people really do read error messages---in
fact, they spend 13--25% of their time doing this.  However, reading error
messages turns out to be as difficult as reading source code, and how difficult
it is to read the error messages strongly predicts task performance.

<div class="callout" markdown="1">

### Does visualization help?

Visualizing program execution is a perennially popular idea, but people learn
more from constructing visualizations than they do from viewing visualizations
constructed by others <cite>Stasko1998,Cetin2016</cite>, so does visualization
actually help learning?  To answer this, <cite>Cunningham2017</cite> replicated
an earlier study of the kinds of sketching learners do when tracing code
execution.  They found that not sketching at all correlates with lower success,
while tracing changes to variables' values by writing new values near their
names as they change was the most effective strategy.

One possible confounding effect they checked was time: since sketchers take
significantly more time to solve problems, do they do better just because they
think for longer?  The answer is no: there was no correlation between the time
taken and the score achieved.

One often-overlooked finding about visualization is that people understand
flowcharts better than pseudocode *if both are equally well structured*
<cite>Scanlan1989</cite>.  Earlier work showing that pseudocode outperformed
flowcharts used structured pseudocode and tangled flowcharts; when the playing
field was leveled, novices did better with the graphical representation.

</div>

## What Do We Know About Programming Style?

A programming language is a user interface, and can be studied and evaluated
like any other. For example, <cite>Stylos2007</cite> assessed how programmers
use APIs with required parameters in objects' constructors as opposed to
parameterless default constructors. They hypothesized that required parameters
would create more usable and self-documenting APIs by guiding programmers toward
the correct use of objects and preventing errors. Contrary to expectations,
programmers strongly preferred and were more effective with APIs that did not
require constructor parameters.  They then analyzed subjects' behavior using the
<span g="cognitive_dimensions">cognitive dimensions framework</span>, which
showed that that requiring constructor parameters interfered with common
learning strategies and caused <span g="premature_commitment">premature
commitment</span>.

<cite>Binkley2012</cite> reported that reading and understanding code is
fundamentally different from reading prose: "…the more formal structure and
syntax of source code allows programmers to assimilate and comprehend parts of
the code quite rapidly independent of style.  In particular…beacons and program
plans play a large role in comprehension."  It also found that experienced
developers are relatively unaffected by identifier style, so just to use
consistent style in all examples.  Since most languages have style guides (e.g.,
[PEP8][pep8] for Python) and tools to check that code follows these guidelines.

Programmers have argued for decades about whether variables' data types should
have to be declared or not, usually based on their personal experience as
professionals rather than on any kind of data.
<cite>Endrikat2014,Fischer2015</cite> found that requiring variable type
declarations does add some complexity to programs, but it pays off fairly
quickly by acting as documentation for a method's use---in particular, by
forestalling questions about what's available and how to use it.

<cite>Kernighan1999</cite> wrote, "Programmers are often encouraged to use long
variable names regardless of context.  This is a mistake: clarity is often
achieved through brevity."  Lots of programmers believe this, but
<cite>Hofmeister2017</cite> found that using full words in variable names led to
an average of 19% faster comprehension compared to letters and abbreviations.
In contrast, <cite>Beniamini2017</cite> found that using single-letter variable
names didn't affect novices' ability to modify code.  This may be because their
programs are shorter than professionals' or because some single-letter variable
names have implicit types and meanings.  For example, most programmers assume
that `i`, `j`, and `n` are integers and that `s` is a string, while `x`, `y`,
and `z` are either floating-point numbers or integers more or less equally.

## What Can We Learn From Analyzing Code?

If engineering is applied science, then <cite>Eichberg2015</cite> is a great
example of software engineering.  In it, the authors show that it's possible to
identify a wide range of problems in code by comparing the actual control flow
graph (which is the set of all possible paths through the program) with the
abstract interpretation flow graph (which is the set of all paths once possible
data values are taken into account).  To make this more concrete, the control
flow graph (CFG) for:

```python
01: x = 0
02: if x > 0:
03:     x = 1
```

{: .continue}
includes the statement on line 3, but the abstract interpretation flow graph
(AIFG) doesn't, because there's no way it could ever be executed given the
possible value(s) of `x`.  Code paths that are in the CFG but not in the AIFG
signal dead code, which in turn usually signals logic errors, such as use of
`and` instead of `or` in a logical test.  The results from analyzing CFGs are
impressive; in particular, the authors found that a lot of code in widely-used
libraries is littered with unnecessary `null` checks, and that even experienced
developers don't seem to understand Boolean operators as well as they should.

Program analysis can tell us many other things as well, all of which should
influence the design of future systems. For example, Python, JavaScript, and
many other languages are <span g="dynamic_typing">dynamically typed</span>: a
variable can refer to values with many different types, as opposed to the <span
g="static_typing">static typing</span> in languages like Java that restrict
variables to particular types of data. <cite>Akerblom2015</cite> looked at how
often Python programs actually rely on dynamic typing, and found that it was
taken advantage of in only 2.5% of cases. Adding generics (i.e., type
declarations like `Array<int>`) only makes half a percent of different.  This
doesn't mean that languages shouldn't include more complex type systems, but it
does (or should) mean that the onus is on their designers to show that the
complexity is worthwhile.

Meanwhile, lots of people say that copy-pasting code is bad practice: if you
find yourself copy-pasting code (or, in academic parlance, creating "code
clones"), you should refactor it: abstract the repeated code into its own method
and call it from all the original copies. That way, if you need to change it, or
if it has some bugs, you only have to fix it in one place. Some researchers have
built pretty sophisticated tools that will help you find your code clones, so
that you can go and exterminate them wherever they are.

<cite>Kapser2008</cite> explored *why* developers create code clones, and found
out that many code clones are OK. They discuss several kinds of clones---those
that are caused, for instance, by platform variations, boiler-plating, or
language idioms---and show that often the right approach is to go ahead and
copy-paste code. But they note that whether to clone or not is a decision that
requires some thinking on a case by case basis:

> …the results of the case study identify a set of patterns that are most often
> harmful, namely *verbatim snippets* and *parameterized code*. While there were
> several examples of good usage of these clone patterns, the majority were
> deemed harmful. This may be an indication that developers should avoid this
> form of cloning. On the other hand several patterns were found to be mostly
> good: *boiler-plating*, *replicate and specialize*, and *cross-cutting
> concerns*. While not always good, when used with care (as with any form of
> design or implementation decision) these patterns are more likely to achieve
> an overall beneficial effect on the software system.

## What Do We Know About Software Quality?

The answer to the question in this section's title is, "A lot, and it's not good
news." For example, <cite>Nakshatri2016</cite> looked at how exceptions are
actually used in Java programs.  Rather than being used to make software more
robust, exceptions are either ignored or used as a debugging aid.  For example,
the most common `catch` block is one that logs the error rather than
trying to recover from it; the next most common are to do nothing at all (20% of
cases), or to convert the checked exception into an unchecked exception so that
it can be ignored.  Similarly, most programmers ignore Java's carefully thought
out exception hierarchy and simply catch `Exception` (78%) or `Throwable` (84%)
rather than any of their more specific subclasses.

In a similar vein, <cite>Yuan2015</cite> analyzed the <span g="root_cause">root
cause</span> of around 200 confirmed failures in large distributed systems. They
report many findings, but the key one is that 92% of the catastrophic system
failures are the result of incorrect handling of non-fatal errors explicitly
signaled in software, i.e., the software said, "Something's wrong," but nothing
was in place to handle the error. In 58% of those cases, the underlying faults
could easily have been detected through simple testing of error-handling code.
The lesson is clear: make sure your tests check that your program does the right
thing when things go wrong.

<div class="callout" markdown="1">
### What actually goes wrong?

<cite>Pritchard2015</cite> reported that the most common errors in Python
programs were (in order):

-   SyntaxError: invalid syntax
-   NameError: name *name* is not defined
-   EOFError: EOF when reading a line
-   SyntaxError: unexpected EOF while parsing
-   IndentationError: unindent does not match any outer indentation level

{: .continue}
while the most common in Java were:

-   cannot find symbol - variable NAME
-   ’;’ expected
-   cannot find symbol - method NAME
-   cannot find symbol - class NAME
-   incompatible types

In a better world than ours, the next generation of programming languages and
tools would be designed so that people simply couldn't make these mistakes.

</div>

One reason things go wrong is that developers don't make use of the tools they
have. <cite>Beller2019</cite> monitored 2,443 software engineers over the course
of 2.5 years in four IDEs. They found that:

> …half of the developers in our study does not test; developers rarely run
> their tests in the IDE; only once they start testing, do they do it heftily;
> most programming sessions end without any test execution; only a quarter of
> test cases is responsible for three quarters of all test failures; 12% of
> tests show flaky behavior; Test-Driven Development (TDD) is not widely
> practiced; and software developers only spend a quarter of their time
> engineering tests, whereas they think they test half of their time.

Another factor that affects quality is how comprehensible the software is: in
particular, how easy or difficult it is to set it up.  <cite>Xu2015</cite>
looked at how often various configuration parameters are actually used, and how
correctly; they report that:

-   Only a small percentage (6.1%-16.7%) of configuration parameters are set by
    the majority of users; a significant percentage (up to 54.1%) of parameters
    are rarely set by any user.

-   A small percentage (1.8%-7.8%) of parameters are configured by more than 90%
    of the users.

-   A significant percentage (up to 47.4%) of numeric parameters have no more than
    five distinct settings among all the users' settings.  Similarly, for
    enumerative parameters with many options, typically only two to three of the
    options are actually used by the users, indicating once again the
    over-designed flexibility.

-   Too many knobs do come with a cost: users encounter tremendous difficulties in
    knowing which parameters should be set among the large configuration
    space. This is reflected by the following two facts: (1) a significant
    percentage (up to 48.5%) of configuration issues are about users'
    difficulties in finding or setting the parameters to obtain the intended
    system behavior; (2) a significant percentage (up to 53.3%) of configuration
    errors are introduced due to users' staying with default values incorrectly.

## What Do We Know About Software Projects?

If there is one "law" of software development that most practitioners have heard
of, it is Brooks' Law: adding people to a late project makes it
later. <cite>Meneely2011</cite> explores the correlation between adding people
to a team and the quality of the software the team works on.

The paper reports that adding people is correlated with a later increase in
software quality, but adding them too quickly (that is, at a faster pace than in
previous months) is correlated with a *decrease* in quality.  This is puzzling
because theoretically, adding people to a project increases its coordination
costs, which in turn should impact all metrics of team success negatively,
including quality. But <cite>Meneely2011</cite> isn't an isolated finding:
<cite>Mockus2010</cite> found that more newcomers are not correlated with more
defects, which supports this finding. One possibility is that newcomers are
assigned easy tasks, and so they can't really break things too dramatically or
in a way that won't get caught internally in time. Another possibility is that
the product has matured over time---that software quality would go up no matter
the team size simply because there's less new functionality added as time goes
on.

<cite>Posnett2011</cite> present an interesting twist on this. In the open
source projects they studied, they found that although code changes in general
are associated with future defect fixing activity, as we might expect, those
changes that correspond to new feature development and to code improvements are
*not*. That's interesting and counter-intuitive---one would expect new feature
code commits to be among the buggiest. The authors offer a possible explanation:
well-established open source projects tend to be quite conservative, and new
feature code is heavily scrutinized, so that most defects are found and sorted
out before the code is integrated.

Another surprising result comes from <cite>Khomh2012</cite>. They examined the
effects of Mozilla's switch from a yearly (or longer) release cycle to a much
more frequent cycle. Their raw material is bug and crash data; their conclusions
are:

1.  Users experience crashes earlier during the execution of versions developed
    following a rapid release model.

1.  The Firefox rapid release model fixes bugs faster than using the traditional
    model, but fixes proportionally less bugs.

1.  With a rapid release model, users adopt new versions faster compared to the
    traditional release model.

#3 is good news; #2 is (mostly) good, but #1 is a puzzle for which the authors
don't have an explanation.

One of the many reasons software projects fail is poor estimation, and one of
the reasons people estimate badly is that they don't keep track of what's
happened before. <cite>McIntosh2011</cite> provides a baseline for both how much
effort is required to keep the build system in working order, and how much those
figures can be improved:

> …despite the difference in scale, the build system churn rate is comparable to
> that of the source code, and build changes induce more relative churn on the
> build system than source code changes induce on the source code. Furthermore,
> build maintenance yields up to a 27% overhead on source code development and a
> 44% overhead on test development. Up to 79% of source code developers and 89%
> of test code developers are significantly impacted by build maintenance, yet
> investment in build experts can reduce the proportion of impacted developers
> to 22% of source code developers and 24% of test code developers.

How reliable are results like these?  Albert Einstein once defined insanity as
doing the same thing over and over again and expecting different results.
That's also a good definition of science: we repeat our experiments so that we
can gather statistics about their outcomes, which in turn give us deeper insight
into what the universe is doing.  <cite>Anda2009</cite> is a good example: they
had four teams build the same software independently and in parallel so that
they could look at how much variation there was in what happened.

-   High reproducibility: actual lead time and usability

-   Medium reproducibility: planned development process and cost

-   Low reproducibility: firm price, planned schedule, schedule overrun,
    reliability, and maintainability

Note that putting something in the "low" category doesn't mean that it was
uniformly poor.  Instead, it means that there was wide variation, i.e., that
results were unpredictable.  Their results match software engineering folklore,
and are a guide to what research should focus on improving.
  
## What Do We Know About the Psychology of Programming?

Do happy developers produce better code? If they do, then looking at what tools
they use may be missing the point: it may be their environment and colleagues
that matter more.  Unfortunately, researchers haven't yet discovered how to
induce happiness, so a randomized controlled trial isn't an option. Instead,
<cite>Graziotin2014</cite> measured <span g="affective_state">affective
states</span> (the term psychology researchers use to describe emotional state)
using a questionnaire developed by psychology researchers.  They divided up the
study participants into a positive group (POS) and a non-positive group (N-POS),
then looked at how the groups performed on an analytical task and a creative
task.  They scored performance as a function of how many trials the participant
passed and how long it took to solve each trial.  The result was that the POS
group did better at the analytic task, but there was no statistically
significant difference on the creative task.

The topic of personality often comes up in discussions of pair programming: do
you need to be an extravert to reap its benefits, is the contrast in personality
with your peer important, and so on. Several studies have addressed these
questions; <cite>Hannay2010</cite> is a good place to start reading about them.
As they say, personality tests are commonly used in recruitment, but research
suggests that other human-related factors such as motivation and general mental
ability also affect performance.  They studied the impact of the <span
g="big_five">Big Five</span> personality traits on the performance of pair
programmers using 196 professionals in three countries and report, "We found no
strong indications that personality affects pair programming performance or pair
gain in a consistent manner." They go on to suggest that industry and research
should "focus on other predictors of performance, including expertise and task
complexity" instead, as these factors overshadow any personality effects.
