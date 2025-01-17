---
title: "Tooling"
lede: "A few other things that can make your life easier"
template: page
---

Tools don't just help us do things more easily; they shape what we consider
possible and encourage some working practices while discouraging others. They
also advertise how seriously we take our craft: people who want to be good at
something are willing to invest time in learning how to do it better.

I believe that processes are more important than tools, but that's because I
know how to use whatever tools I have to support productive working practices.
However, I focus on tools when talking to students because they are more
tangible: it's easier to tell if someone is using version control or a style
checker than it is to tell if they're designing or estimating sensibly.

[% x automation %] introduced build managers, style checkers, and profilers;
the sections below discuss some other tools you might want in your toolbox.  You
shouldn't try to adopt all of them in a single semester unless the focus of your
project course is to try out as many tools as possible (which is actually a good
theme for a project course).  If you'd rather not improve your tools, but are
afraid that someone on your team might want to do so, [% b Farmer2006 %] is
a not-entirely-serious guide to preventing something new from being adopted.

## Programming Language

You may not get to choose what programming language you use for your project,
but it may be the most important choice there is.  Programmers have argued about
which language is best for as long as there have *been* programmers. In my
experience, it makes a lot less difference than most people think…

…as long as you use the right one, that is. Twenty years ago there was a pretty
clear tradeoff between how quickly you can get a program running and how fast it
ran.  [% i "programming language!interpreted" %][% g interpreted_language %]Interpreted languages[% /g %][% /i %] like [% i "Perl" %]Perl[% /i %] optimized programmers' time; [% i "programming language!compiled" %][% g compiled_language %]compiled languages[% /g %][% /i %] like [% i "C" %]C[% /i %] optimized the machine's.

Today, the balance has shifted in favor of higher-level languages. One reason is
that processors have gotten faster but people haven't, so one programmer-hour is
worth many more computer-hours than before. Another reason is that
[% i "just-in-time compiler" %][% g jit %]just-in-time compilers[% /g %][% /i %] (JITs) and
[% i "generational garbage collection" "garbage collection!generational" %][% g generational_garbage_collection %]generational garbage collection[% /g %][% /i %]
have made higher-level languages intrinsically faster. The biggest, though, is that
the execution time of a modern application depends less on squeezing cycles out
of processors than it used to. The bottleneck in a web site is almost always
network latency or the time required to perform database operations; your code
probably accounts for only a few percent of the total, so doubling or tentupling
its speed has less effect than you'd think.

That said, there are three things to keep in mind:

Some languages are [% i "programming language!ease of learning" %]easier to learn[% /i %] than others.
:   [% b Stefik2013 %] did a controlled experiment to see how quickly
    people could learn to recognize correct and incorrect syntax in several
    different languages. They found that [% g curly_brace_language %]curly-brace languages[% /g %] like [% i "Java" %]Java[% /i %] and [% i "Perl" %]Perl[% /i %] were as hard for people
    to learn as a language with a randomly designed syntax. (They rolled
    *Dungeons & Dragons* dice to pick random names and characters for a made-up
    language.) Other languages like [% i "Ruby" %][Ruby][ruby][% /i %] and [% i "Python" %][Python][python][% /i %] were significantly easier to learn, and
    they are now building a language called [% i "Quorum" %][Quorum][quorum][% /i %] by testing the usability of every
    language feature.

Static typing helps, but only a little.
:   A [% i "static typing" "typing!static" "programming language!statically typed" %][% g static_typing %]statically-typed[% /g %][% /i %] language like [% i "Java" %]Java[% /i %] requires programmers to specify the data type of each
    variable; a [% i "dynamic typing" "typing!dynamic" "programming language!dynamically typed" %][% g dynamic_typing %]dynamically-typed[% /g %][% /i %]
    one like [% i "Python" %]Python[% /i %] doesn't require them, though you can add
    them if you want, while [% i "TypeScript" %]TypeScript[% /i %] adds types as
    a layer on top of [% i "JavaScript" %]JavaScript[% /i %].
    [% b Endrikat2014 %] found that declaring types does add complexity to
    programs, but it pays off fairly quickly by acting as documentation and by
    making [% i "auto-completion" %][% g auto_completion %]auto-completion[% /g %][% /i %]
    more accurate.

The most important thing about a language is its community.
:   Some programming communities work hard to welcome newcomers and treat
    everyone respectfully. Others are more likely to call naïve questions
    "stupid" or to make excuses when [% i "Linux!toxic leadership" %]their
    leaders harass people[% /i %] [% b Cohen2018 %]. As a junior programmer,
    you will learn more from the former than from the latter.

[% b Stefik2017 %] is a good short summary of what we know and why we
believe it's true. If someone disagrees with it, ask them to show you their
evidence.

## Package Management

There is no point building software if you can't install it.  Inspired by the
[% i "Comprehensive TeX Archive Network (CTAN)" %][Comprehensive TeX Archive
Network][ctan][% /i %], most languages now have an online archive from which
developers can download packages.  Each package typically has a name and one or
more version(s); each version may have a list of dependencies, and the package
may specify a version or range of versions for each dependency.

A [% i "package manager" %][% g package_manager %]package manager[% /g %][% /i %] is a
program that keeps track of which packages are installed on your computer and
how they depend on each other.  Package managers became popular out of necessity
in the 1990s along with Linux: so many distributions were being updated so often
that people needed tools to keep track of what they had.

Some package managers, like [% i "APT" "package manager!APT" %][APT][apt][% /i %]
for [% i "Linux" %]Linux[% /i %] and [% i "Homebrew" "package
manager!Homebrew" %][Homebrew][homebrew][% /i %] for [% i "MacOS" %]MacOS[% /i %],
can handle many languages. Others, like [% i "pip" "package
manager!pip" %][pip][pip][% /i %] for [% i "Python" %]Python[% /i %] and [% i "NPM" "package manager!NPM" %][NPM][npm][% /i %] for [% i "JavaScript" %]JavaScript[% /i %], are language-specific. No matter which one you
use, the biggest challenge you'll face is finding the packages you need: at the
time of writing, [this search][npm-xml-search] turns up over 700 XML parsers for
a JavaScript. To help narrow the search, NPM allows the results to be sorted by
popularity, quality, and maintenance. This obviously creates a feedback
loop—if NPM labels a package "more popular" then more people will find it,
which raises its popularity score even further—but [% i "NPMS" "package
manager!package ratings" %][NPMS][npms][% /i %] is open about how these scores are
calculated, so package authors can find out what they need to do in order to
improve their scores.

Whatever package manager you use, your project should follow these rules:

Keep a record.
:   NPM automatically updates a project's [% i "Node.js!package.json
    file" %]`package.json`[% /i %] file to show which packages have been installed
    explicitly, and its `package-lock.json` file keeps track of exactly which
    versions of their dependencies have been installed as well, so in theory,
    someone else can duplicate your environment exactly. If you are using pip
    for Python, on the other hand, it's up to you to create a file (typically
    called `requirements.txt`) that lists the packages someone needs to make
    your project work.

To install is beautiful, to uninstall divine.
:   You should install packages to try them out before committing to using them,
    but if you decide that something doesn't do what you want, please remember
    to uninstall it. (I have worked with projects that used less than half of
    their "requirements".)

Keep an eye on security updates.
:   NPM will warn you if there are security problems with things you depend on.
    The world would be a slightly safer place if other package managers did this
    as well.

<blockquote markdown="1">
### Docker

[% i "Docker" %][Docker][docker][% /i %] uses some clever tricks to run one
operating system on top of another to create a
[% i "virtual machine" %][% g "virtual_machine" %]virtual machine[% /g %][% /i %]
(VM) that is isolated from everything
beneath it.  It and other tools like it are used by most cloud computing
services and to run continuous integration systems ([% x automation %]), but
they are essentially an admission that we haven't figured out how to manage
packaging reliably.
</blockquote>

## Integrated Development Environment

You are going to spend a lot of time editing code, documentation, and reports,
so choosing a good editor is as important as choosing a comfortable chair.
There are literally thousands to consider, from very small plain-text editors
such as [% i "Notepad" "editor!Notepad" %]Notepad[% /i %] (which comes with [% i "Windows" %]Windows[% /i %]) to very large ones like [% i "Emacs" "editor!Emacs" %]Emacs[% /i %] (which some people claim is actually Lisp-based
operating system in disguise).

<blockquote markdown="1">
### Stuck in the punchcard era

In many ways, programming is still stuck in the punchcard era: we still insist
that source code be represented as lines of characters that are drawn
one-for-one on the screen.  [% g wysiwyg %]WYSIWYG[% /g %] editors like
Microsoft Word did away with this model decades ago; they store the file in a
machine-friendly format and then render it in a human-friendly way. There's no
reason we couldn't do the same with programs.  There's no reason we shouldn't be
able to draw a diagram directly in our source code like we can in a Google Doc;
if you are looking for a project to tackle, this would be a good one.
</blockquote>

You might already have a favorite editor. If you're like most programmers, you
will change jobs, languages, operating systems, and nationality before you'll
switch to another, because it has taken weeks or months for your hands to master
the current one. However, if it is not an [% i "IDE" %][% g ide %]integrated development environment[% /g %][% /i %] (IDE) that combines an editor with other
programming tools then getting work done will take longer and hurt more than it
needs to.

IDEs were invented in the 1970s, but didn't really catch on until [% i "Borland" %]Borland[% /i %] released [% i "Turbo Pascal" %]Turbo Pascal[% /i %]
in the 1980s.  They usually include these tools:

-   A [% i "console" "IDE!console" %][% g console %]console[% /g %][% /i %] so that you can
    type in expressions or call functions and see the results without having to
    start (or restart) your program.

-   A [% i "code browser" %][% g code_browser %]code browser[% /g %][% /i %] that helps you
    navigate the packages, classes, methods, and data in your program.

-   A [% i "GUI designer" %][% g gui_designer %]GUI designer[% /g %][% /i %] that lets you
    build GUIs by dragging and dropping components;

-   A [% i "test runner" %]test runner[% /i %] to display the results of tests and
    let you jump directly to ones that have failed. This is usually a GUI built
    on top of whatever unit testing framework you are using
    ([% x testing %]), just as graphical interfaces for version control are usually
    built on top of the command-line tools.

The most popular IDE today is probably [% i "VS Code" "Microsoft Visual Studio
Code" "IDE!VS Code" %][Microsoft Visual Studio Code][vs-code][% /i %], often
referred to simply as "VS Code".  Along with all the tools above, it has
hundreds of [% i "plugin!for IDE" %][% g plugin %]plugins[% /g %][% /i %] of varying
quality to support database design, reverse engineering, dozens of different
programming languages, and more.  These all make you more productive than their
disconnected counterparts. Since most of these store project data (including
build instructions) in a proprietary format, your team will do much better if
you all adopt the same IDE. This will also let you help one another solve
problems and share plugins.

But calling VS Code is the world's most popular IDE is misleading.  If you open
[% i "IDE!in browser" %]developer tools[% /i %]. in Firefox, Chrome, or Edge, you
will be shown an HTML browser that's smart enough to tell you which bits of CSS
are in effect where, a console that displays messages from the JavaScript
running in the page, a breakpointing debugger ([% x debugging %]), a network
monitor, and much more. It won't help you with your C# or Python—at least, not
yet—but it will make all of your front-end work a lot easier.

## Refactoring

After a debugger, the most under-appreciated power of most IDEs is their ability
to [% i "refactoring" %][% g refactoring %]refactor[% /g %][% /i %] code, i.e., to change
its structure without changing what it does [% b Fowler2018 %].  It is just
as much a part of programming as writing code in the first place: nobody gets
things right the first time, and needs or insights can change over time
[% b Brand1995 %].

Some common refactoring patterns include "hoist repeated calculation out of
loop" and "replace repeated test with flag". As [% b Kerievsky2004 %]
showed, many refactorings make code fit a design pattern or move code from one
design pattern to another.  If you highlight a variable name in an IDE like VS
Code and say, "Rename", it parses the code to find all uses of that variable and
changes their names and *only* their names, so that (for example) you don't
accidentally turn `alfred` into `alfblue`. "Extract method" is another favorite
of mine: if a method is getting too long or you want to re-use part of its
implementation, you can highlight a few lines, click, and enter a name, and the
IDE will do the rest of the work for you.

Using refactoring tools doesn't just save you a few seconds of typing: it also
reduces the chances of making a mistake so that you don't lose time later trying
to figure out what's gone wrong.  (The `alfblue` error mentioned in the previous
paragraph cost me about ten minutes.)  It also helps you maintain concentration,
since you don't have to make a mental switch from the code you're writing to the
refactoring you're doing and then back again ([% x important %]).

## The Next Level

You and your teammates could use many other tools to make yourselves more
productive. Some aren't part of the standard undergraduate curriculum yet, even
though good developers have been relying on them for a decade or more. Others
may be touched on, but only briefly, so a quick recap won't hurt.

The first is a [% i "documentation generator" %][% g doc_generator %]documentation generator[% /g %][% /i %] like [% i "JSDoc" "documentation
generator!JSDoc" %][JSDoc][jsdoc][% /i %]. This is a compiler of a sort, but
instead of translating source code into something executable, it extracts
information from specially-formatted comments and strings, and turns it into
human-readable documentation.  The justification for this is that when code and
documentation are stored separately, programmers won't keep the latter up to
date. Since "rusty" documentation can be worse than no documentation at all, it
makes a lot of sense to keep the source of the documentation right beside the
code. Many introductory courses require students to document their packages,
classes, and methods this way; it's a good habit, and one you should cultivate.

Another set of tools complement the style checkers discussed in [% x automation %].
Style checkers do static analysis, i.e., they look at the
text of your program while it's at rest.  Other tools do [% i "dynamic analysis" %][% g dynamic_analysis %]dynamic analysis[% /g %][% /i %]: tools like
[% i "Valgrind" "dynamic analysis!Valgrind" %]Valgrind[% /i %] watch your [% i "C" %]C[% /i %] or [% i "C++" %]C++[% /i %] program run and look for things like
memory leaks, or inconsistent locking that might lead to deadlocks or race
conditions.

Real development projects rely on a lot of other tools as well: schedule
builders like [% i "Microsoft Project" %]Microsoft Project[% /i %], requirements
tracing tools, and so on. Most are bigger hammers than undergraduate projects
really require, but good programmers don't just use tools, they build them.  For
example, I have written two dozen short programs to help me write and maintain
this book and others like it.  These tools do things like check
cross-references, make sure I'm using the right CSS attributes for elements, and
so on.  If you and your teammates find yourselves typing in the same commands
over and over again, write a program to do it for you.

<blockquote markdown="1">
### From seeds to trees

A lot of open source projects and commercial products began with one programmer
solving a problem for themselves and then discovering that other people found it
useful as well. [% i "Grand Perspective" %][Grand
Perspective][grand-perspective][% /i %] displays a tree map to show what's using
disk space on a Mac; [% i "Carnac" %][Carnac][carnac][% /i %] shows what special
keys you're pressing on Windows so that if you're doing a demo, people can see
the keyboard shortcuts you're using, and so on.  Building one small thing well
is a lot more useful, and a lot more likely to be used, than building half of
something larger.
</blockquote>

## Modeling

If you want to go one big step further, you can start using modeling tools like
[% i "Alloy" "modeling tools!Alloy" %][Alloy][alloy][% /i %]
[% b Jackson2016 %] and [% i "TLA+" "modeling
tools!TLA+" %][TLA+][tla-plus][% /i %] [% b Wayne2018 %].  Instead of
analyzing source code, you use these tools to build and analyze a [% g model %]model[% /g %] of what the code is supposed to do so that you can look
for flaws in your algorithms.

Alloy focuses on describing complex relationships, such as the integrity of data
structures; TLA+ is designed to help you reason about sequences of concurrent
actions, such as the different ways microservices can exchange messages. Both of
them can find counter-examples, i.e., situations that break the rules you have
described, but both have interfaces that make Git look simple.
[These][gritter-alloy] [articles][gritter-tla-plus] give an idea of what they
can do; you probably won't have time to learn them along the way while working
on a project, but if your school offers a course devoted to them, it will
probably change your view of programming just as much as it changed mine.
