---
---

<span class="fixme">more research results https://github.com/gvwilson/buildtogether.tech/issues/4</span>

<span class="fixme">Soften claims https://github.com/gvwilson/buildtogether.tech/issues/18</span>

There are a lot of citations in the preceding chapters to back up various
claims, but also to introduce the idea that we actually know stuff about things.
Researchers have been studying programs and programmers since at least the
1960s, and while there are many unknowns, we have learned a lot about what works
and what doesn't.

Sadly, most people in industry still don't know what researchers have found out,
or even what kinds of questions they could answer. One reason is their belief
that software engineering research is divorced from real-world problems; another
is that many programmers haven't done any science themselves since high school.
(The average biology students does forty to sixty experiments during their
undergraduate degree.  The average computer science student does one.)

A third reason is that many people would rather fail than change. People cling
to creationism, refuse to accept the reality of anthropogenic climate change, or
insist that vaccines cause autism. Given that, it's not surprising that many
programmers continue to act as if a couple of quotations from some
self-appointed guru constitute "proof".

This chapter therefore presents a few evidence-based results that are relevant
to the kind of work you may be doing in your project and that your instructor
might want to incorporate into your course <cite>Fagerholm2017</cite>; <span
x="methods"/> discusses the methods researchers use, and <span
x="novices"/> presents a few more results that are specific to novice
programmers.

I hope you will find them interesting enough to want to dig further, but as with
all research, some caution is required when interpreting results:

Theories change as more data becomes available.
:   Software engineering is a comparatively young discipline---in fact, the term
    itself wasn't used until 1968.

Most of these studies' subjects are WEIRD.
:   They are from Western, Education, Industrialized, Rich, and Democratic
    societies <cite>Henrich2010</cite>.

The data we have doesn't capture everything.
:   <cite>Aranda2009</cite> found that in every one of the bugs they traced,
    some key insight or action wasn't captured digitally. Similarly,
    <cite>Herzig2013</cite> carefully examined thousands of bug reports from
    several projects and found that many mis-report themselves in ways that will
    inevitably skew the results of simplistic analysis.

<div class="callout" markdown="1">

### A cautionary tale

<cite>Zeller2011</cite> did what too many researchers in too many fields do on a
regular basis: throw some data at some machine learning algorithms and then
claim that whatever comes out the other end is significant. Luckily for us, they
did it on purpose to make a point.

They took data on code and errors for the Eclipse IDE and correlated the two to
find good predictors of bugs. Which sounds sensible---except they did the
correlation at the level of individual characters. It turns out that 'i', 'r',
'o', and 'p' are most strongly correlated with errors. What is a sensible
researcher to do facing these findings? Take those letters out of the keyboard,
of course.  The authors then go over everything that's wrong with their
approach, from lack of theoretical grounding to dishonest use of
statistics. Before you read too much research, make sure to read this.

</div>

## What Do We Know About Programmer Productivity?

<span class="fixme">SPACE model https://github.com/gvwilson/buildtogether.tech/issues/23</span>

<span class="fixme">privilege defines performance https://github.com/gvwilson/buildtogether.tech/issues/34</span>

<span class="fixme">productivity measures from <cite>Forsgren2018</cite> https://github.com/gvwilson/buildtogether.tech/issues/71</span>

Let's start our explanation of research results with the often-repeated claim
that some programmers are ten times more productive than others.  Is it actually
true?  The short answer is, "It's complicated."  As <cite>Prechelt2019</cite>
shows, the answer depends on what exactly the question is intended to
mean. Looking at exactly the same data, you could conclude that some programmers
are 105 times more productive than others---except this doesn't take into
account whether people's code actually works or what language they were using.

If you only look at one language, the ratio goes down to 17:1, but that's still
comparing the very best to the very worst.  Now the discussion starts to get
statistical: if you compare the median of the slower half of programmers with
the median of the top 10%, the ratio is 5:1 or 11:1, depending on whether you
use everyone in the sample or restrict it to those who used the same language
respectively.

<cite>Sadowski2019a</cite> summarizes of what we know, and more importantly, how
to think about the problem.  The chapter <cite>Sadowski2019b</cite> lays out a
three-axis framework for discussion based on the <span
g="gqm">goal-question-metric</span> approach.

Velocity: how fast work gets done.
:   A typical question is, "Are developers able to deploy their features more
    quickly?" which might be answered by looking at the time from creating a
    patch to patch release or the time to reach team milestones.

Quality: how well work gets done.
:   A question might be, "Is the committed code of a higher quality?" Answers
    could be obtained by measuring test coverage or the number of bugs found
    after a release.

Satisfaction: how satisfying the work is.
:   The question could be, "Are developers more satisfied with the engineering
    process using the new tool?" Answers could be found by collecting developer
    ratings for the new system or of team communication enabled by a new tool.

What's most important to remember in all of this is [Goodhart's
Law][goodhart-law]: as soon as you use some measure to evaluate people it ceases
to be a good measure because people will start to game the system.  For example,
<cite>Gitinabard2020</cite> reports that it's possible to classify student
software teams as collaborative, cooperative, or solo-submit by analyzing the
history of their version control repositories. If these measures are ever used
for grading, students will immediately start making extra commits (or fewer, or
whatever else is needed) in order to get the "right" profile.

<div class="callout" markdown="1">

### What don't you want to know?

<cite>Begel2014</cite> asked one set of developers what questions they most
wanted researchers to answer, then asked another set of developers to rate those
questions.  Respondents favored questions about how customers typically use
their applications, but were opposed questions related to assessing the
performance of individual employees or comparing them with one another;
<cite>Huijgens2020</cite> found that data scientists viewed most possible
research topics the same way.

</div>

## What Do We Know About Programming Style?

As we mentioned in <span x="tooling"/> <cite>Stefik2013</cite> did a
controlled experiment to see how quickly people could learn to recognize correct
and incorrect syntax in several different languages. They found that languages
like C, Java, and Perl were as hard for people to learn as a language with a
randomly designed syntax, while languages like Ruby and Python were
significantly easier to learn. This result is one of many showing that a
programming language is a user interface that can be studied and evaluated like
any other.

For example, <cite>Stylos2007</cite> assessed how programmers use APIs with
required parameters in objects' constructors as opposed to parameterless default
constructors. They hypothesized that required parameters would create more
usable and self-documenting APIs by guiding programmers toward the correct use
of objects and preventing errors. Contrary to expectations, programmers strongly
preferred and were more effective with APIs that did not require constructor
parameters.  They then analyzed subjects' behavior using the <span
g="cognitive_dimensions">cognitive dimensions framework</span>, which showed
that that requiring constructor parameters interfered with common learning
strategies and caused <span g="premature_commitment">premature
commitment</span>.

<cite>Binkley2012</cite> reported that reading and understanding code is
fundamentally different from reading prose: "…the more formal structure and
syntax of source code allows programmers to assimilate and comprehend parts of
the code quite rapidly independent of style.  In particular…beacons and program
plans play a large role in comprehension."  It also found that experienced
developers are relatively unaffected by identifier style, so just to use
consistent style in all examples.  Since most languages have style guides (e.g.,
[PEP8][pep8] for Python) and tools to check that code follows these guidelines.
In contrast, <cite>Schankin2018</cite> found that:

<blockquote markdown="1">

With descriptive identifier names, developers spent more time in the lines of
code before the actual defect occurred and changed their reading direction less
often, finding the semantic defect about 14% faster than with shorter but less
descriptive identifier names. These effects disappeared when developers searched
for a syntax error, i.e., when no in-depth understanding of the code was
required. Interestingly, the style of identifier names had a clear impact on
program comprehension for more experienced developers but not for less
experienced developers.

</blockquote>

More recently, studies like <cite>Floyd2017,Krueger2020,Peitek2021</cite> have
used <span g="fmri">fMRI</span> to look at what programmers' brain do when they
are reading or writing code. The main findings are that reading code is
cognitively different from reading prose, but that the more experienced
programmers are, the less of a difference there is. This corroborates earlier
work with eye tracking like <cite>Hansen2013</cite>, which also found that
experience increases performance in most cases, but can actually *hurt*
performance when assumptions about what code is supposed to do are violated
(i.e., when the eye sees what the brain expects).

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

Similarly, programmers have argued for decades about whether variables' data
types should have to be declared or not, usually based on their personal
experience as professionals rather than on any kind of data.
<cite>Hanenberg2013,Endrikat2014,Fischer2015</cite> found that requiring
variable type declarations does add some complexity to programs, but it pays off
by acting as documentation for a method's use---in particular, by forestalling
questions about what's available and how to use it. <cite>Gao2017</cite> looked
at how many bugs in JavaScript programs would have been caught if the code had
been written in TypeScript (which adds types), and came up with a figure of
15%, which is either low (one in seven) or high (sales tax) depending on how you
want to look at it.

## What Can We Learn From Analyzing Code?

If engineering is applied science, then <cite>Eichberg2015</cite> is a great
example of software engineering.  In it, the authors show that it's possible to
identify a wide range of problems in code by comparing the actual control flow
graph (which is the set of all possible paths through the program) with the
abstract interpretation flow graph (which is the set of all paths once possible
data values are taken into account).  To make this more concrete, the control
flow graph for:

```python
01: x = 0
02: if x > 0:
03:     x = 1
```

{: .continue}
includes the statement on line 3, but the abstract interpretation flow graph
doesn't, because there's no way it could ever be executed given the possible
value(s) of `x`.  Code paths that are never executed signal <span
g="dead_code">dead code</span>, which in turn usually signals logic errors, such
as use of `and` instead of `or` in a logical test.  The results from this kind
of analysis impressive: the authors found that a lot of code in widely-used
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

<blockquote markdown="1">

…the results of the case study identify a set of patterns that are most often
harmful, namely *verbatim snippets* and *parameterized code*. While there were
several examples of good usage of these clone patterns, the majority were deemed
harmful. This may be an indication that developers should avoid this form of
cloning. On the other hand several patterns were found to be mostly good:
*boiler-plating*, *replicate and specialize*, and *cross-cutting
concerns*. While not always good, when used with care (as with any form of
design or implementation decision) these patterns are more likely to achieve an
overall beneficial effect on the software system.

</blockquote>

<div class="callout" markdown="1">

### What *can't* we learn?

Many people have put forward <span g="code_metric">code metrics</span> that are
supposed to measure the complexity or likely number of bugs in a piece of
software. However, <cite>ElEmam2001</cite> found that these metrics are no
better at predicting things than simply counting the number of lines of code,
because the longer the program is, the more likely it is to contain whatever
kinds of problems those more sophisticated metrics are looking for.

</div>

<span class="fixme">boilerplate https://github.com/gvwilson/buildtogether.tech/issues/36</span>

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
-   ';' expected
-   cannot find symbol - method NAME
-   cannot find symbol - class NAME
-   incompatible types

In a better world than ours, the next generation of programming languages and
tools would be designed so that people simply couldn't make these mistakes.

</div>

One reason things go wrong is that developers don't make use of the tools they
have. <cite>Beller2019</cite> monitored 2,443 software engineers over the course
of 2.5 years in four IDEs. They found that:

<blockquote markdown="1">

…half of the developers in our study does not test; developers rarely run their
tests in the IDE; only once they start testing, do they do it heftily; most
programming sessions end without any test execution; only a quarter of test
cases is responsible for three quarters of all test failures; 12% of tests show
flaky behavior; Test-Driven Development (TDD) is not widely practiced; and
software developers only spend a quarter of their time engineering tests,
whereas they think they test half of their time.

</blockquote>

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

That said, most software actually *does* run despite the fact that programmers
don't do things the "right" way. One possible reason comes from the study of
trivial packages reported in <cite>Abdalkareem2017</cite>, which looked at
230,000 NPM packages and 38,000 JavaScript applications. It turns out that less
than half of the trivial packages include tests; instead, they are "deployment
tested", i.e., their authors fix the breakages that users report.

## What Do We Know About Software Projects?

If there is one "law" of software development that most practitioners have heard
of, it is <span g="brooks_law">Brooks' Law</span>: adding people to a late
project makes it later. <cite>Meneely2011</cite> explores the correlation
between adding people to a team and the quality of the software the team works
on.

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

<blockquote markdown="1">

…despite the difference in scale, the build system churn rate is comparable to
that of the source code, and build changes induce more relative churn on the
build system than source code changes induce on the source code. Furthermore,
build maintenance yields up to a 27% overhead on source code development and a
44% overhead on test development. Up to 79% of source code developers and 89%
of test code developers are significantly impacted by build maintenance, yet
investment in build experts can reduce the proportion of impacted developers
to 22% of source code developers and 24% of test code developers.

</blockquote>

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
you need to be an extrovert to reap its benefits, is the contrast in personality
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

But the most important result is the one in <cite>Patitsas2016</cite>. Its
abstract is worth repeating in full:

<blockquote markdown="1">

Although it has never been rigourously demonstrated, there is a common belief
that CS grades are bimodal. We statistically analyzed 778 distributions of final
course grades from a large research university, and found only 5.8% of the
distributions passed tests of multimodality. We then devised a psychology
experiment to understand why CS educators believe their grades to be bimodal.

We showed 53 CS professors a series of histograms displaying ambiguous
distributions and asked them to categorize the distributions. A random half of
participants were primed to think about the fact that CS grades are commonly
thought to be bimodal; these participants were more likely to label ambiguous
distributions as bimodal. Participants were also more likely to label
distributions as bimodal if they believed that some students are innately
predisposed to do better at CS. These results suggest that bimodal grades are
instructional folklore in CS, caused by confirmation bias and instructor beliefs
about their students.

</blockquote>

In plain language, if some people are born programmers and others aren't, there
ought to be two humps in the grade distribution. There isn't, but if people
believe some people are "just better" at coding, they're more likely to *see*
two humps. These beliefs matter because they are a self-fulfilling prophecy
<cite>Brophy1983</cite>: if a teacher believes that student A is more likely to
succeed than student B, they will give student A more attention, which *makes*
them more likely to succeed, which confirms the teacher's bias.
