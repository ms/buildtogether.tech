---
---

<span class="fixme">https://github.com/gvwilson/buildtogether.tech/issues/14</span>

<span class="fixme">brief description of Make and then talk about `package.json` and other approaches</span>

## Build Manager

No matter what language you use, you're going to need a <span
g="build_manager">build manager</span>---a tool that will transform what you've
typed into what you want to deliver. The best-known build manager in the Unix
world is [Make][make], which was invented in 1975 by a summer intern at Bell
Labs. To use Make, you create a Makefile that specifies the dependencies between
the files in your project and the commands needed to update them. For example:

```make
game.exe : game.bc graphics.bc utils.bc
        tx -E -o game.exe game.bc graphics.bc utils.bc

%.bc : %.grace
        tx -C $<
```

{: .continue}
tells Make that `game.exe` can't be built until `game.bc`, `graphics.bc`, and
`utils.bc` exist, and that once they do, the way to create `game.exe` is to run
the `tx` compiler with several options.  Below that is a <span
g="pattern_rule">pattern rule</span> telling Make how to create any `.bc` file
from a `.grace` file with the same root name; the cryptic expression `$<` is
Make's way of saying "the first thing the target depends on".

Make has been used by hundreds of thousands of programmers for more than thirty
years, but has some fundamental flaws. The first is its syntax, which looks like
something produced by a cat dancing on the keyboard. The second is that it runs
commands by handing them over to whatever operating system it is running on,
which make portability a constant headache. (Quick, should you use `rm` or `del`
to delete a file?) Third, Make doesn't have a debugger: the only way to track
down problems in your build configuration is to stare at the configuration file
until little drops of blood form on your forehead.

I could live with ugly syntax---if Ie kan lurn Inglish speling, Ie kan lurn
eneething. But the lack of a debugger is a never-ending headache, because real
build systems aren't just configured: they're programmed. Take this book, for
example: its Makefile checks the consistency of cross-references and glossary
entries, makes sure all the bibliography citations are in place, and copies
files to my web site, and is more complex than many programs I've
written. Thinking of it as a "configuration" file is a mistake: you *have* to
approach system builds as a programming problem.

The current generation of build managers dispense with custom configuration file
syntaxes and use the data structures of dynamic languages like Python and
Ruby. [Snakemake][snakemake] and [Rake][rake] are examples of such a system: its
users write their "configurations" as small Python or Ruby programs, making use
of an extensive support library that handles dependencies, invokes appropriate
compilers, and so on.  Debugging is still problematic, but at least it's
possible.

Whatever you choose (or are told to use), stick to the following rules:

Pick something that plays nicely with your other tools.
:   For example, most Java editors and IDEs integrate with a build tool called
    [Ant][ant], which means they can jump directly to compilation errors when
    they occur.

Always use the build manager---never compile or copy things by hand.
:   This isn't just for efficiency's sake: if any of the twelve things you need
    to do to get your application up on your web site have to be done by hand,
    the odds are that you'll forget a crucial step right before your end-of-term
    demo, and wind up looking silly.

Always use the build manager---never compile or copy things by hand.
:   Yes, I'm repeating myself, but this time the reason is different. If you do
    something by hand, one of your teammates might do it differently.  "But it
    works on my machine!" isn't something you want to hear an hour before a
    deadline…

A good way to start using a builder is to create a "version zero" of the
project. Set up the build and make sure it works even when there isn't anything
to compile, run, test, or copy. Now add something---anything.  Does the build
still work? If it does, you're on your way.

Once you've got that, never check anything into version control that breaks the
build. This is one of the golden rules of working in a team: if your code won't
compile, or doesn't pass whatever automated tests you have, then putting it into
the repository means putting every other person on your team into exactly the
same broken state you're in. When you're working on your own, it's OK to use
version control as a way to transfer files from one machine to another, or as a
way to back things up at the end of the day. Do *not* carry this habit over to
teamwork.

## Continuous Integration

All of these tools will do a lot more for you if you adopt some kind of <span
g="ci">continuous integration</span> system such as [Travis CI][travis-ci] or
[GitHub Actions][github-actions].  These can be set up to run either at regular
intervals (e.g., every hour or at three a.m.), or every time someone checks into
version control (which I find more useful). Each time they run, they check a
fresh copy of the project out of version control, build it, re-run all the
tests, and post the results to the project's blog, web site, and mailing list.

Research has proven the benefits of CI <cite>Hilton2016</cite>.  It acts as a
"heartbeat" for the project: as soon as anything goes wrong, everyone knows. It
also encourages good development practices: if someone checks something in that
doesn't compile, run, or pass the project's tests, everyone will know very
quickly. (Funnily enough, after the system has shamed you a couple of times,
you'll stop checking in broken code…) <cite>Zampetti2020</cite> looks at how
*not* to use CI, and can serve as a good checklist of things to avoid.
