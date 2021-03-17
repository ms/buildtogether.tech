---
---

<span class="fixme">https://github.com/gvwilson/buildtogether.tech/issues/10 (other tools)</span>

<span class="fixme">https://github.com/gvwilson/buildtogether.tech/issues/60 (the advantages of minimizing tool usage)</span>

<span class="fixme">section on browser tools https://github.com/gvwilson/buildtogether.tech/issues/73</span>

<span class="fixme">online note-taking tools https://github.com/gvwilson/buildtogether.tech/issues/74</span>

A carpenter shows up to put an extension on your house, and all she's brought
with her is a hammer and a Swiss army knife. How confident are you that she'll
do the job well?  A programmer shows up to fix a couple of bugs and add a new
splash screen to your game, and all she's going to use are a plain-text editor
and `print` statements. Are you any more confident?

Tools don't just help us do things more easily; they shape what we consider
possible and encourage some working practices while discouraging others. They
also advertise how seriously we take our craft: people who want to be good at
something are willing to invest time in learning how to do it better. In
programming, that means mastering new tools and the practices that go with them.

I actually believe that processes are more important than tools, but that's
because I know how to use whatever tools I have to support the working
practices I think are most productive. However, I focus on tools when talking to
students because they are are more tangible: it's easier to tell if someone is
using version control or a style checker than it is to tell if they're designing
or estimating sensibly.

So here, in more-or-less priority order, are the tools you should learn *after*
you are comfortable with version control and a unit testing framework.

<div class="callout" markdown="1">

### If you'd rather not…

If you'd rather not improve your tools, but are afraid that someone on your team
might want to do so, <cite>Farmer2006</cite> is a not-entirely-serious guide to
preventing something new from being adopted.

</div>

## Programming Language

<span class="fixme">https://github.com/gvwilson/buildtogether.tech/issues/59 (TypeScript)</span>

You may not get to choose what programming language you use for your project,
but it may be the most important choice there is.  Programmers have fought
religious wars over what's language is best for as long as there have *been*
programmers. In my experience, which one you use makes a lot less difference
than most people think…

…as long as you use the right one, that is. Twenty years ago there was a pretty
clear tradeoff between how quickly you can get a program running and how fast it
ran. <span g="interpreted_language">Interpreted languages</span> like Perl
optimized programmers' time; <span g="compiled_language">compiled
languages</span> like C optimized the machine's.

Today, the balance has shifted in favor of higher-level languages. One reason is
that processors have gotten faster but people haven't, so one programmer-hour is
worth many more computer-hours than before. Another reason is that <span
g="jit">just-in-time compilers</span> (JITs) and <span
g="generational_garbage_collection">generational garbage collection</span> have
made higher-level languages intrinsically faster. The biggest, though, is that
the execution time of a modern application depends less on squeezing cycles out
of processors than it used to. The bottleneck in a web site is almost always
network latency or the time required to perform database operations; your code
probably accounts for only a few percent of the total, so doubling or tentupling
its speed has less effect than you'd think.

That said, there are three things to keep in mind:

Some languages are easier to learn than others.
:   <cite>Stefik2013</cite> did a controlled experiment to see how quickly
    people could learn to recognize correct and incorrect syntax in several
    different languages. They found that <span
    g="curly_brace_language">curly-brace languages</span> like Java and Perl
    were as hard for people to learn as a language with a randomly designed
    syntax. (They really did roll *Dungeons & Dragons* dice to pick random names
    and characters for a made-up language as an <span
    g="experimental_control">experimental control</span>.) Other languages like
    [Ruby][ruby] and [Python][python] were significantly easier to learn, and
    they are now building a language called [Quorum][quorum] by testing the
    usability of every language feature.

Strong typing helps, but only a little.
:   A <span g="strong_typing">strongly-typed</span> language like Java requires
    programmers to specify the data type of each variable; a <span
    g="dynamic_typing">dynamically-typed</span> one like Python doesn't.
    <cite>Endrikat2014</cite> found that declaring types does add complexity to
    programs, but it pays off fairly quickly by acting as documentation and by
    making <span g="auto_completion">auto-completion</span> more accurate.

The most important thing about a language is its community.
:   Some programming communities work hard to welcome newcomers and treat
    everyone respectfully. Others are more likely to call naïve questions
    "stupid" or to make excuses when their leaders harass people. (Looking at
    you, Linux…) As a junior programmer, you will learn more from the former
    than from the latter.

<cite>Stefik2017</cite> is a good short summary of what we know and why we
believe it's true. If someone disagrees with it, ask them to show you their
evidence.

## Integrated Development Environment

You are going to spend a lot of time editing code, documentation, and reports,
so choosing a good editor is as important as choosing a comfortable chair.
There are literally thousands to consider, from very small plain-text editors
such as Notepad (which comes with Windows) to very large ones like Emacs (which
some people claim is actually Lisp-based operating system in disguise).

<div class="callout" markdown="1">

### Punchcards once again

As we noted in <span x="using-git"></span>, programming is still stuck in the
punchcard era: we still insist that source code be represented as lines of
characters that are drawn one-for-one on the screen.  <span
g="wysiwyg">WYSIWYG</span> editors like Microsoft Word did away with this model
decades ago; they store the file in a machine-friendly format and then render it
in a human-friendly way. There's no reason we couldn't do the same with
programs.  There's no reason we shouldn't be able to draw a diagram directly in
our source code like we can in a Google Doc.

</div>

You might already have a favorite editor. If you're like most programmers, you
will change jobs, languages, operating systems, and nationality before you'll
switch to another, because it has taken weeks or months for your hands to master
the current one. However, if it is not an <span g="ide">integrated development
environment</span> (IDE) that combines an editor with other programming tools
then getting work done will take longer and hurt more than it needs to.

IDEs were invented in the 1970s, but didn't really catch on until Borland
released Turbo Pascal in the 1980s.  They usually include these tools:

-   A <span g="console">console</span> so that you can type in expressions or call
    functions and see the results without having to start (or restart) your
    program.

-   A <span g="style_checker">style checker</span> that can warn you when your
    code doesn't meet naming and indentation conventions.

-   A <span g="code_browser">code browser</span> that helps you navigate the
    packages, classes, methods, and data in your program.

-   A <span g="gui_designer">GUI designer</span> that lets you build GUIs by
    dragging and dropping components;

-   A <span g="test_runner">test runner</span> to display the results of tests and
    let you jump directly to ones that have failed. This is usually a GUI built
    on top of whatever unit testing framework you are using, just as graphical
    interfaces for version control are usually built on top of the command-line
    tools.

-   Some refactoring tools to help you reorganize your code.  For example, instead
    of searching and replacing strings, an IDE can parse your source code and
    look for all uses of a class name in order to replace it with a new one, or
    move a method from one class to another.

The most popular IDE today is probably [Microsoft Visual Studio Code][vs-code],
often referred to simply as "VS Code".  Along with all the tools above, it has
hundreds of <span g="plugin">plugins</span> of varying quality to support
database design, reverse engineering, dozens of different programming languages,
and more.  These all make you more productive than their disconnected
counterparts. Since most of these store project data (including build
instructions) in a proprietary format, your team will do much better if you all
adopt the same IDE. This will also let you help one another solve problems and
share plugins.

## Refactoring

To <span g="refactoring">refactor</span> code means to change its structure
without changing what it does <cite>Fowler2018</cite>.  It is just as much a
part of programming as writing code in the first place: nobody gets things right
the first time <cite>Brand1995</cite>, and needs or insights can change over
time.

Some common refactoring patterns include "hoist repeated calculation out of
loop" and "replace repeated test with flag". As <cite>Kerievsky2004</cite>
showed, many refactorings make code fit a design pattern or move code from one
design pattern to another. If changes that fit these patterns are easy to make,
your design is probably a good one.

<span class="fixme">https://github.com/gvwilson/buildtogether.tech/issues/7</span>

## The Next Level

<span class="fixme">expand each of these to a section</span>

You and your teammates could use many other tools to make yourselves more
productive. Some aren't part of the standard undergraduate curriculum yet, even
though good developers have been relying on them for a decade or more. Others
may be touched on, but only briefly, so a quick recap won't hurt.

The first is a <span g="doc_generator">documentation generator</span> like
[JSDoc][jsdoc]. This is a compiler of a sort, but instead of translating source
code into something executable, it extracts information from specially-formatted
comments and strings, and turns it into human-readable documentation.  The
justification for this is that when code and documentation are stored
separately, programmers won't keep the latter up to date. Since "rusty"
documentation can be worse than no documentation at all, it makes a lot of sense
to keep the source of the documentation right beside the code. Many introductory
courses require students to document their packages, classes, and methods this
way; it's a good habit, and one you should cultivate.

Along with testing frameworks, style checkers have become a lot more popular
since the turn of the century. Early style checkers looked at code to make sure
that it obeyed formatting rules, such as "no method can be longer than 100
lines" or "class names must be written in CamelCase". Today's, like PMD and
CheckStyle, can do a lot more: they can find code that is never called,
parameters that are never used, duplicated code that could be factored out, and
a lot more.

Style checkers are more properly called *static analysis* tools, since they work
by parsing the source code for your programs and looking for patterns that might
indicate problems. Compilers also do a lot of static analysis; the non-fatal
warnings they produce are a lot more useful than many students realize, and a
"zero warnings" policy can prevent a lot of subtle bugs.

<span class="fixme">Reviews are much more straightforward when you don't have to worry about style choices that much.</span>

Another class of tools uses *dynamic analysis*: they watch your program run, and
look for things like memory leaks, or inconsistent locking that might lead to
deadlocks or race conditions. FindBugs is the best-known in the Java world; the
Valgrind toolset is a lifesaver if you're using C or C++.

Real development projects rely on a lot of other tools as well: schedule
builders like Microsoft Project, requirements tracing tools, visual editors for
GUIs and class diagrams, and so on. Most are bigger hammers than undergraduate
projects really require (except possibly the GUI editors), so I'd like to close
this section by asking you to invest some time in something else:
scripting. Good programmers don't just use tools, they build them. I have dozens
of small programs in my `tools` directory that do things like update my working
copies of all the projects I'm involved in or check whether the links to Amazon
in my course notes are still valid. Anything worth doing repeatedly is worth
automating; if you and your teammates find yourselves typing in the same
commands over and over again, *write a program to do it for you*. And please,
use a language like Python or Ruby rather than Java or C#: the "try it and see"
nature of the former is a lot better suited to one-of-a-kind scripts than the
latter's type checking and compilation.

## Building for Everyone

Tools like [WebAIM WAVE][webaim-wave] are easy to use, and most of the problems
they identify are easy to fix. It only takes a few minutes, and it's the
compassionate thing to do.

<span class="fixme">more about tools</span>

## Formal Methods

<span class="fixme">Alloy and TLA+ https://github.com/gvwilson/buildtogether.tech/issues/53</span>
