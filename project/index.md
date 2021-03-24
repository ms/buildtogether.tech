---
---

All right: you know how to work with other people by sharing files through
Git. But what files should you share and where should they go? 

Every language has its own conventions for what files should go where in a
project, for the simple reason that they all need different files.  In a Jekyll
website like this one, for example, the layout is:

`_config.yml`
:   A configuration file with the author's name, a list of any plugins that the
    site needs to build, the rules for generating URLs for blog posts, and so
    on.

`_layouts`
:   A directory containing templates for pages.

`_includes/`
:   A directory containing any snippets shared between those templates.

`_site`
:   The directory containing the generated web pages. If the site doesn't need
    any special plugins, this directory doesn't have to be included in version
    control: GitHub will re-create it automatically. If the site does use
    plugins, on the other hand, the authors have to generated the HTML and
    commit it themselves.

Learning what goes where for your languages of choice is like learning when to
signal when driving a car: the rules may vary from place to place, but
everywhere *has* rules, and knowing them will help prevent you from crashing.
There are, however, a few things that every project needs.

## What Goes Where

Every project should have a handful of files in its root directory; these may
have UPPERCASE names without an extension, or may be plain text (`.txt)` or
Markdown (`.md`) files.

`README`
:   A brief overview of the project that often serves as its home page on
    GitHub.

`CONTRIBUTING`
:   How to contribute to the project. Should people file an issue when they have
    a question, email a list, or post something on chat, and if so, where?  What
    code formatting conventions does the project use?  Research shows that clear
    contribution guidelines increase the odds of people contributing (<span
    x="wide-world"/>); in my experience, they also reduce friction between
    team members.

`CONDUCT`
:   The project's Code of Conduct, i.e., how people are required to treat one
    another.  As we'll discuss below, "be polite" or "use your common sense"
    aren't enough.

`LICENSE`
:   Describes who can do what with the project materials.  We discuss various
    licenses below as well.

## Packages

<span class="fixme">https://github.com/gvwilson/buildtogether.tech/issues/3</span>

## Code of Conduct

In order to get the most out of a team, it must do more than *allow* people to
contribute: it has to be clear that the teams *wants* contributions.  Saying
"the door is open" is not enough, since many people have painful personal
experience of being less welcome than others.  In order to create a truly
welcoming environment for everyone, the project must explicitly acknowledge that
some people are treated unfairly in society and actively take steps to remedy
this.  Doing this isn't just compassionate: it essential to making the team more
diverse, which makes it more productive <cite>Zhan2020</cite>:

-   It reassures people who have experienced harassment or unwelcoming behavior
    before that this project takes inclusion seriously.

-   It ensures that everyone knows what the rules are.  What you think is polite
    or common sense depends on where you are from; since many projects have
    participants from different backgrounds, making the rules explicit avoids
    angry arguments starting with, "But *I* thought that…"

-   It prevents people who misbehave from <span g="feigning_ignorance">feigning
    ignorance</span>, i.e., claiming after they do something offensive that they
    didn't realize it was out of bounds.  (See also <span
    g="schrodingers_asshole">Schrödinger's asshole</span>.)

<div class="callout" markdown="1">

### What they really mean

In the early 2010s a lot of open source developers resisted the adoption of
codes of conduct, saying that they were unnecessary or that that they infringed
freedom of speech.  What they usually meant, and what the few people still
arguing against them usually mean today, is that thinking about how they might
have benefited from past inequity makes them feel uncomfortable.  If having a
Code of Conduct leads to them going elsewhere, that will probably make the
project run more smoothly.

</div>
