---
---

<span x="versioning"></span> described how to use version control to manage
individual work, but it really comes into its own when we are working with other
people.  Forges like [GitHub][github], [GitLab][gitlab], and
[BitBucket][bitbucket] are all designed to support this, and they all provide
other tools for managing and reviewing shared information. This chapter looks at
how to use those tools so that <span x="process"></span>'s discussion of
software development processes will make more sense.

## Using Git Together

People can share work through a Git repository in one of two ways:

1.  Everyone has read and write access to a single shared repository.

2.  Everyone can read from the project's main repository, but only a few people
    can commit changes to it.  The project's other contributors <span
    g="fork_git">fork</span> the main repository to create one that they own, do
    their work in that, and then submit their changes to the main repository.

The first approach works well for teams of up to half a dozen people who are all
comfortable using Git, but if the project is larger, or if contributors are
worried that they might make a mess in the `main` branch, the second approach is
safer.

Git itself doesn't have any notion of a "main repository", but GitHub and other
software forges all encourage people to use Git as if there was one.  For
examle, suppose that Amira wants to contribute to the assignment that Sami is
hosting on GitHub at `https://github.com/sami/homework5`.  Amira can go to that
URL and click on the "Fork" button in the upper right corner.  GitHub goes ahead
and creates a copy of Sami's repository within Amira's account on GitHub's own
servers. When the command completes, nothing has happened yet on Amira's own
machine: the new repository exists only on GitHub.  When Amira explores its
history, she sees that it contains all of the changes Sami made (<span
f="after-fork"></span>).

{% include figure id="after-fork" alt="After forking" cap="What repositories are where after forking." fixme=true %}

A fork of a repository is a clone just like the ones you have created earlier;
it's just hosted on the forge's servers instead of your laptop.  In order to
start working on the project, Amira needs a clone of *their* repository (not
Sami's) on their own computer.  We will modify Amira's prompt to include their
desktop user ID (`amira`) and working directory (initially `~`) to make it
easier to follow what's happening:

```sh
amira:~ $ git clone https://github.com/amira/homework5.git
```

This command creates a new directory with the same name as the project on
Amira's machine (<span f="after-clone"></span>).  When Amira goes into this
directory and runs `ls` and `git log`, she sees all of the project's files and
history:

```sh
amira:~ $ cd homework5
amira:~/homework5 $ ls
```

```sh
amira:~/homework5 $ git log --oneline -n 4
```

{% include figure id="after-clone" alt="After cloning" cap="What repositories are where after cloning." fixme=true %}

Amira also sees that Git has automatically created a remote for their repository
that points back at their repository on GitHub:

```sh
amira:~/homework5 $ git remote -v
```
```out
origin  https://github.com/amira/homework5.git (fetch)
origin  https://github.com/amira/homework5.git (push)
```

Amira can pull changes from their fork and push work back there, but needs to
add a remote pointing at Sami's repository first (<span f="after-remote"></span>):

```sh
amira:~/homework5 $ git remote add upstream https://github.com/sami/homework5.git
amira:~/homework5 $ git remote -v
```
```out
origin      https://github.com/amira/homework5.git (fetch)
origin      https://github.com/amira/homework5.git (push)
upstream    https://github.com/sami/homework5.git (fetch)
upstream    https://github.com/sami/homework5.git (push)
```

{: .continue}
Amira has called their new remote `upstream` because it points at the repository
theirs is derived from.  She could use any name, but `upstream` is a nearly
universal convention.

{% include figure id="after-remote" alt="Git remotes" cap="Which Git remotes point where." fixme=true %}

With this remote in place, Amira is finally set up.  Suppose, for example, that
Sami has modified the project's `README.md` file to add Amira as a contributor.
(Again, we show Sami's user ID and working directory in her prompt to make it
clear who's doing what):

```txt
# Homework 5

Our homework project

## Contributors

- Sami
- Amira
```

Sami commits their changes and pushes them to *their* repository on GitHub:

```sh
sami:~/homework5 $ git commit -a -m "Adding Amira as a contributor"
sami:~/homework5 $ git push origin main
```

Sami's changes are now on their desktop computer and in their GitHub repository
but not in either of Amira's repositories (local or remote).  Since Amira has
created a remote that points at Sami's GitHub repository, though, she can easily
pull those changes to their desktop:

```sh
amira:~/homework5 $ git pull upstream main
```

Pulling from a repository owned by someone else is no different than pulling
from a repository you own.  In either case, Git merges the changes and asks you
to resolve any conflicts that arise.  The only significant difference is that,
as with `git push` and `git pull`, you have to specify both a remote and a
branch: in this case, `upstream` and `main`.

Amira can now get Sami's work, but how can Sami get Amira's?  They could create
a remote that pointed at Amira's repository on GitHub and periodically pull in
Amira's changes, but that would lead to chaos, since they could never be sure
that everyone's work was in any one place at the same time.  Instead, almost
everyone uses <span g="pull_request">pull requests</span> (PR).  A PR is
essentially a note saying, "Someone would like to merge branch A of repository B
into branch X of repository Y".  The PR does not contain the changes, but
instead points at two particular branches.  That way, the difference displayed
is always up to date if either branch changes.

But a PR can store more than just the source and destination branches: it can
also store comments people have made about the proposed merge.  Users can
comment on the PR as a whole, or on particular lines, and mark comments as out
of date if the author of the PR updates the code that the comment is attached
to.  Complex changes can go through several rounds of review and revision before
being merged, which makes PRs the review system we all wish journals actually
had.

To see this in action, suppose Amira wants to add their email address to
`README.md`.  She creates a new branch and switches to it:

```sh
amira:~/homework5 $ git checkout -b adding-email
```

{: .continue}
then makes a change and commit it:

```sh
amira:~/homework5 $ git commit -a -m "Adding my email address"
```

```sh
amira:~/homework5 $ git diff HEAD~1
```

Amira's changes are only in her local repository.  She cannot create a pull
request until those changes are on GitHub, so she pushes her new branch to her
repository on GitHub:

```sh
amira:~/homework5 $ git push origin adding-email
```

When Amira views her repository in the browser, GitHub notices that she has just
pushed a new branch and asks her if she wants to create a PR.  When she clicks
on the button, GitHub displays a page showing the default source and destination
of the PR and a pair of editable boxes for the pull request's title and a longer
comment.

If she scrolls down, Amira can see a summary of the changes that will be in the
PR.  Whe she clicks "Create Pull Request", Git gives it a unique serial number
(which is *not* a commit ID).  The PR is displayed in Sami's repository rather
than Amira's since it is Sami's repository that will be affected if the PR is
merged.

Clicking on the "Pull requests" tab in Sami's repository brings up a list of PRs
and clicking on the PR link itself displays its details.  Amira and Sami can
both see and interact with these pages, though only Sami has permission to
merge.

Since there are no conflicts, GitHub will let Sami merge the PR immediately
using the "Merge pull request" button.  They could also discard or reject it
without merging using the "Close pull request" button.  Instead, they click on
the "Files changed" tab to see what Amira has changed.

If Amira changes `README.md`, commits, and pushes to her branch while the pull
request is open, the PR is immediately updated.  As explained above, a PR is a
note asking that two branches be merged, so if either end of the merge changes,
the PR updates automatically.

If Sami has merged several PRs, Amira can update her desktop repository by
pulling from her `upstream` repository (i.e., Sami's repository):

```sh
amira:~/homework5 $ git checkout main
amira:~/homework5 $ git pull upstream main
```

Finally, Amira can their those changes back to the `main` branch in her own
repository on GitHub:

```sh
amira:~/homework5 $ git push origin main
```

All four repositories are now synchronized. If there are any conflicts along the
way, Sami and Amira can resolve them just as they would resolve conflicts
between branches in a single repository.  GitHub and other forges do allow
people to merge conflicts through their browser-based interfaces, but doing it
on our desktop means we can use our favorite editor to resolve the conflict.  It
also means that if the change affects the project's code, we can run everything
to make sure it still works.

But what if Amira or someone else merges another change while Sami is resolving
this one, so that by the time she pushes to her repository there is another,
different, conflict?  In theory this cycle could go on forever; in practice, it
reveals a communication problem that Sami (or someone) needs to address.  If two
or more people are constantly making incompatible changes to the same files,
they should discuss who's supposed to be doing what, or rearrange the project's
contents so that they aren't stepping on each other's toes.

## Code Reviews

There's no point creating PRs if they are all merged as-is. The reason they
exist is to allow <span g="code_review">code review</span>.  One study after
another since the mid-1970s has proven that code review is the most
cost-effective way to find bugs in software <cite>Cohen2010</cite>. It is also
the most effective way to share knowledge between team members: if you read
someone else's code, you have a chance to learn all the things that you didn't
know to ask and they didn't realize they should tell you.

There are lots of guides online for doing code reviews, most of them based on
their authors' personal experience. A notable exception is the [SmartBear
guide][smartbear-code-review], which draws on a large study of code review in
industry. The rules below present some of their findings with modifications for
students' situations.

Have the instructor do a demonstration review.
:   Even if you have done code reviews before, you may not know what's expected
    for this class. The instructor can show you by putting up some sample code
    and going through it, thinking aloud as they notice things worth commenting
    on so that you have an idea of how much detail they expected.

Review at most 200 lines of a code at a time.
:   The SmartBear guide recommends reviewing at most 400 lines at a time, which
    should take 60-90 minutes. You will probably get there eventually, but in
    our experience it's better to start with something smaller and work up to
    that.

    A corollary of this rule is that no PR should be more than 200 lines long.
    If one is, the odds are that reviewers won't be able to hold it all in their
    head at once (<span x="thinking"></span>) and so will miss things.

Authors should clean up code before review.
:   If the person creating the PR goes through and adds some more comments,
    cleans up some variable names, and does a bit of refactoring (<span
    x="design"></span>), they won't just make reviewing easier: the odds are
    very good that they will find and fix a few problems on their own.

Use checklists.
:   <cite>Gawande2011</cite> popularized the idea that using checklists improves
    results even for experts.  If you are new to code reviews, ask the
    instructor for a list of the dozen most common problems to check for.
    (Anything more than that is likely to be overhwelming.) If you and your
    teammates have been working together for a while, look at your own code
    reviews and make a list of the things that keep coming up.  Having the list
    will make you more aware of the issues while you're coding, which in turn
    will make you less likely to keep making the same mistakes.

Follow up.
:   The author of the code doesn't have to accept every suggestion, but should
    have a better reason than "I don't want to" for rejecting any of them.
    GitHub and other platforms allow people to create discussion threads for
    each comment, and will mark threads as being out of date when the pull
    request is updated. Whoever did the review should then scan the changes to
    make sure their points have been addressed, and to give themselves a chance
    to learn a few more things from the author.

Don't tolerate rudeness.
:   Most code review guidelines say, "Be respectful."  The problem is that if
    you are, you probably don't need to be told that. What *will* is teammates
    defending the victims of rudeness by telling the offender, "That's not how
    we speak to each other." A Code of Conduct (<span x="versioning"></span>)
    helps prevent this; we will look at other strategies in <span
    x="rights"></span>.

So what does a code review actually look like? Here's a short Python program
that searches for duplicated files (i.e., ones that have exactly the same
content). <span t="collaborate-code-review"></span> shows the comments I left
when reviewing it.

{% include file file="dup.py" %}

{% include table id="collaborate-code-review" file="code-review.tbl" cap="Code Review" %}

## Tracking Issues

You probably have a to-do list somewhere. It might be scribbled in a calendar or
lab notebook, kept in a text file on your laptop, or in your head; wherever and
however you maintain it, it lists the things you're supposed to do, when they're
due, and (possibly) how urgent they are.

At its simplest, an <span g="issue_tracker">issue tracker</span> is a shared
to-do list. Issue tracking systems are also called ticketing systems and bug
trackers, because most software projects use one to keep track of the bugs that
developers and users find. These days, issue trackers are almost invariably
web-based. To create a new issue, you enter a title and a short description; the
system then assigns it a unique serial number. You can usually also specify:

-   what kind of issue it is (such as a bug report, a request for a new feature,
    or a question to be answered);

-   who is responsible for the issue (i.e., who's supposed to fix the bug, test
    the fix, or update the documentation);

-   how important it is; and

-   when it's due.

If version control keeps track of where your project has been, your ticketing
system keeps track of where you're going. After version control, it is the most
important part of a team project; without it, you and your teammates will have
to constantly ask each other "What are you working on?", "What am I supposed to
be working on?", and "Who was supposed to do that?" Once you start using one
it's easy to find out what the project's status is: just look at the open
tickets, and at those that have been closed recently.  You can use this to
create agendas for your status meetings, and to remind yourself what you were
doing three months ago when the time comes to write your final report.

Of course, a issue tracker is only as useful as what you put into it.  If you're
describing a bug in a large application, you should include enough information
to allow someone to reproduce the problem. This is why industrial-strength
systems like [Jira][jira] can have a couple of dozen fields for each issue,
including:

-   what version of the software you were using;

-   what platform it was running on;

-   what you did to make it crash;

-   any data or configuration files the program relies on;

-   whatever stack traces, error reports, or log messages the program produced;

-   its severity (i.e., how much damage the bug might do); and

-   other tickets that might be related.

This is a lot more information than student projects require. In addition,
students are almost always working on several courses at once, and it's common
for students to have to put their team project aside for a few days to work on
assignments for other courses. For these reasons, I've found that most student
teams won't actually use anything more sophisticated than a web-base to-do list:
unless, of course, they're forced to by the grading scheme. In that case, most
come away with the impression that tickets are something you only use when you
have to.

So what does a good issue look like?  <cite>Bettenburg2008</cite> found that the
information users supply when they file a bug report tends not to be that which
the relevant developers need the most, and most importantly, it differs in
fairly predictable ways and for understandable reasons.  Here's one I filed for
the duplicate file finder reviewed in the previous section:

{% include file file="bug-report.txt" %}

The ID on the first line is assigned by the issue tracker, an often serves as a
short-hand name for the issue in conversation. ("Hey, is anyone working on
number fifty-five yet?") The date is in <span g="utc">UTC</span> so that it is
unambiguous: while your team may all be in one place, it's increasingly likely
that you are scattered across several timezones.

The title on line 3 is probably the most important part of the issue. Projects
will accumulate hundreds of issues over time; a good subject line makes it much
easier to find the ones you need. The `type`, `severity`, and `tags` fields also
improve <span g="discoverability">discoverability</span>; while `type` and
`severity` could be tags, having them in fields of their own makes it easier to
sort and filter issues.

Finally, the description briefly summarizes the problem. If the author hadn't
already identified the cause, it would include a <span g="reprex">reproducible
example</span>, or reprex. This helps the person understand what the issue is
much more than, "The program crashes when I open strange files," but experience
shows that if people are required to come up with a reprex when filing an issue,
they will often solve their own problem along the way.

<div class="callout" markdown="1">

### Triage

As we will see in <span x="process"></span>, one purpose of a schedule is to
tell you when to start cutting corners. Similarly, one of the main reasons to
keep issues in one place is to help you prioritize them when time starts to run
short.

</div>

## Other Ways to Communicate

Issues are the best way to keep track of where you are, but there are lots of
other ways the team can and should communicate. The most popular is easily
email, which has been used to run projects since the 1970s.  It brings content
directly to people while allowing everyone to deal with issues when it's
convenient for them, and supports long-running conversations. Email really comes
into its own, though, when messages are routed through a central mailing list,
so that people don't have to remember to CC the other five people on their team,
and a shared archive can be created for later searching. The second point is as
important as the first: if you can't go back and find out what was said a month
ago---or, just as importantly, if someone *else* can't do that---you might as
well not have said it.

Wikis seem like a good way to keep notes, create documentation, and so on. Their
main strength is the fact that content is automatically and immediately visible
on the web.  These days, you will probably get more mileage out of a bunch of
Markdown pages under version control---you have to set up a repository anyway,
and version control systems are much better at reconciling conflicts between
concurrent authors than wikis.

Blogs, on the other hand, have proven more useful. One kind of project blog
consists of articles written by the team's members as a journal of their
progress. This is most useful for people who are watching the project from the
outside, like instructors.

The second kind of blog is one created automatically by tools. In many project
management systems, every project has a blog.  Every time someone checks code
into version control, creates or closes an issue, or sends email, an entry is
added to that blog. This allows the project's members to see changes scroll by
in their usual blog reader, which is a handy way to keep track of what their
teammates are doing.

If you are going to create a blog, it's best to use a <span
g="static_site_generator">static site generator</span> to format and publish
content consistently.  If you are using GitHub, you can create a site with
[GitHub Pages][github-pages] using a tool called [Jekyll][jekyll]; lots of
different themes are available, and there are many good tutorials online.

Finally, there are instant messaging tools like Slack. It is more conversational
than email, but:

1.  Instant messaging is the most effective method ever invented for disrupting
    the state of flow that is so essential to productivity.

2.  Conversations tend to be permanently out of phase: if you ask, "Can we move
    on to the next item?", and someone doesn't say either "yes" or "no", what
    usually happens is that you wait a minute, then move on, and then they pop
    up with a lengthy comment on the preceding item.

I think these faults can all be fixed, but until they are---oh, who am I
kidding? You're going to use IM no matter what I say. If there's more than two
people in the conversation, follow the same rules you would for a meeting. In
particular, post a summary of the conversation to your project's web site, just
as you would post meeting minutes.
