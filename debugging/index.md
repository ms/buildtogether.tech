---
---

Finding errors is good; fixing them is better, so learning how to debug is as
important as learning how to program in the first place.  However, while most
schools teach defensive programming and unit testing, I have yet to find any
that offers a course on debugging.  This is a significant omission when you
consider that most programmers spend anywhere from a quarter to three quarters
of their time finding and fixing bugs.  While a single chapter can't make up for
that, I hope the guidance below will help make you more efficient.

## Build Habits

Software can fail in many different ways, but the process for tracking problems
down is remarkably consistent.  The first rule of debugging is therefore to make
good practices a habit.  You are more likely to make mistakes when you're tired
or under pressure; if writing assertions and unit tests isn't automatic by then,
the odds are that how you work will actually make things worse.

Make sure you understand what the code is supposed to do.
:   As we'll see when discussing Boehm's Curve in <span x="process"/>, any time
    you invest in reducing the number of bugs you write will reduce the overall
    time needed to complete your project.  The first step in debugging is
    therefore to make sure you built the right thing. <span
    g="requirements_error">Requirements errors</span> are a major cause of
    software projects failing in the real world, and every instructor has horror
    stories about students misinterpreting assignments and spending days
    building the wrong thing. When in doubt, ask; to make your question and its
    answer clear, provide an example and describe what you think the code is
    supposed to do in that case.

Make sure you understand what the bug actually is.
:   "It doesn't work" isn't good enough: what exactly is going wrong and how do
    you know? If I can't spot a problem in less than a minute, I jot down a note
    to myself like, "shouldn't recurse into footer elements".  Without this, I
    often find myself <span g="rabbit_hole">going down a rabbit hole</span> and
    losing sight of what I was originally trying to fix.

    Writing down what's supposed to be happening also helps you check that you
    are actually exercising the problem that you think you are.  Are you giving
    it the right test data?  Is it configured the way you think it is?  Is it
    the version you think it is?  Has the feature actually been implemented yet?
    Are you sure?  Maybe the reason you can't isolate the problem is that it's
    not there---again, a couple of minutes talking it through with a teammate
    can save you an hour of trying to fix something that isn't actually broken.

Make it fail.
:   You can only debug things when you can see them going wrong, so as we
    discussed in <span x="communicate"/>, you should try to create a reprex---a
    minimal reproducible example.  Just doing this isolates the problem in a
    surprising number of cases, since each time you throw out part of the
    original program or dataset because the bug reoccurs without it, you are
    also throwing out a bunch of possible causes.

    The easiest way to create a reprex is to divide and conquer.  The fault
    responsible for a failure has to occur before the failure, so check the
    input to the function that's failing.  If that's wrong, check the inputs to
    the function calling it, and so on.  Add assertions to make these checks
    explicit: they'll help you keep track of what you have looked at for this
    bug, and will help prevent others in future.

Change one thing at a time.
:   Replacing random pieces of code in the hope of fixing a bug is unlikely to
    solve your problem: if you got something wrong the first time, the odds
    think you'll get it right the second?  (Or ninth, or twenty-third?)
    Instead, you should change one thing and then re-run your tests to see if
    the program works, breaks in the same way, or breaks in a new way.  (This is
    another place where version control helps: if you have made a change and it
    hasn't fixed things, `git restore` will put your code back exactly the way
    it was so that you're not debugging ever-more-mutated versions of your
    code.)

<div class="callout" markdown="1">

### Programs concurrent to debug hard are

Concurrent systems in which many things are happening simultaneously are much
harder to debug than sequential systems.  It's not just that the order of events
is unpredictable; it's often not repeatable, so creating a reliable reprex may
be impossible.  What's worse, the act of observing can hide the bug: a `print`
statement or a breakpoint can change timing in a way that makes the bug
disappear.  Modeling tools can help (<span x="tooling"/>), as can the use of
immutable data structures, but the best solutions are to test components in
isolation using mock objects in place of the things they communicate with (<span
x="testing"/>) and to add *lots* of assertions to check the consistency of data
structures.  In particular, giving every class a method called `isOK` to check
that it's in good shape can save hours of later debugging, as well as helping
the next programmer understand what the data is supposed to look like.

</div>

## Common Errors

As <span x="novices"/> describes, instructors' beliefs about what mistakes
novice programmers make most often bear little relation to the actual frequency
of different mistakes.  For experienced programmers, <cite>Pritchard2015</cite>
reported that the most common errors in Python programs were (in order):

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

Complex errors are one of a kind: that's part of what makes them complex.  But
some simple errors crop up again and again, and you can use those patterns as a
checklist for finding problems.  If you do this consciously, you will train
yourself not to make those mistakes in future. <span t="common-errors"/> lists
some mistakes that come up frequently.

{% include table
   id="common-errors"
   file="common-errors.tbl"
   cap="Common Errors" %}

## Using a Debugger

A <span g="symbolic_debugger">symbolic debugger</span> is a program that allows
you to control and inspect the execution of another program. You can step
through the target program a line at a time, display the values of variables or
expressions, look at the call stack, or (my personal favorite) set *breakpoints*
to say "pause the program when it reaches this line" . Depending on the language
you're using, you may have to compile your program with certain options turned
on to make it debuggable, but that's a small price to pay for the hours or days
a debugger can save you when you're trying to track down a problem.

Some debuggers, like GDB, are standalone programs; others are build into IDEs.
Both are better than adding `print` statements to your program, recompiling it,
and re-running it because:

-   adding `print` statements takes longer than clicking on a line and setting a
  breakpoint;

-   adding `print` statements distorts the code you're debugging by moving things
  around in memory, altering the flow of control, and/or changing the timing
  of thread execution; and

-   it's all too easy to make a mistake in the `print` statement---few things are
  as frustrating as wasting an afternoon debugging a problem, only to realize
  that the `print` statement you copied and pasted isn't displaying the values
  you thought it was.

<div class="callout" markdown="1">

### If it was important, it would be on the exam

Over the years I've been surprised by how few programmers know how to use a
debugger <cite>Beller2018</cite>. The reason can't be the five or ten minutes it
takes to learn how to use one---that pays for itself almost immediately.  The
best explanation I've been able to come up with relates to [Goodhart's
Law][goodhart-law], which says that as soon as you use some measure to evaluate
people it ceases to be a good measure because people will start to game the
system.

The inverse of that is that if something *isn't* being evaluated, it isn't
important---or rather, if you're juggling five or six courses, you can't afford
to put time into things that aren't going to affect your grades.  Most students
have to learn version control because it's the only way to submit their work,
but "show that you can use the debugger" is (almost) never part of gradable
work.  As a result, there's no point at which students have to master it.  I
think this could now be fixed by having students submit screencasts of
themselves setting breakpoints, inspecting variables, and so on; if you ever try
this in your class, please let me know how it goes.

</div>

<span class="fixme">automated repair https://github.com/gvwilson/buildtogether.tech/issues/66</span>
