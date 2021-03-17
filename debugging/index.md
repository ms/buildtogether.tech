---
---

<span class="fixme">debugging techniques https://github.com/gvwilson/buildtogether.tech/issues/63</span>

<span class="fixme">automated repair https://github.com/gvwilson/buildtogether.tech/issues/66</span>

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

<span class="fixme">remove this anecdote or explain what's wrong with it https://github.com/gvwilson/buildtogether.tech/issues/30</span>

A company I used to work for never hired people immediately. Instead,
prospective employees were put on a three-month contract.  Two things meant
automatic disqualification: checking broken code into version control and using
`print` statements instead of a symbolic debugger. The first was justified
because we didn't want to hire people who put themselves ahead of their
teammates. The second was justified because we didn't want to hire people who
were too stupid or stubborn to program efficiently.

Over the years, I've been surprised by how few programmers know how to use a
debugger <cite>Beller2018</cite>. The reason can't be the five or ten minutes it
takes to learn how to use one---that pays for itself almost immediately.  The
only explanation I've been able to come up with is that some people *enjoy*
being inefficient.  Typing in `print` statements and paging through screens of
output lets them feel like they're being productive, when in fact they're just
being busy (which isn't the same thing at all). If your brain needs a break
(which it sometimes will), then take a break: stretch your legs, stare out a
window, practice your juggling, or do whatever else you can to take your mind
away from your problem for a few minutes. Don't drag out the process of finding
and fixing your bug by using sloppy technique just to let your brain idle for a
while.

And by the way: if you're allowed to choose your teammates at the start of the
course, treat it like a job interview. Ask the people you think you might want
to work with whether they use a debugger. If they say "no", ask yourself what
impact that's going to have on your grade in the course…
