---
---

This book isn't intended for complete novices (<span x="introduction"></span>),
but you may have been one recently, and may find these results interesting
additions to those presented in <span x="research"></span>.

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
