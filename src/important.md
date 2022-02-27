---
title: "The Important Stuff"
lede: "If you read nothing else…"
template: page
---

The things that go wrong most often in software projects have nothing to do with
software.  Instead, the worst mistakes people make are related to the human side
of things. Before we look at teamwork or tools, we need to talk about overwork,
how to run a meeting, and how to resolve arguments.

> ### Not writing software takes less time
>
> [% b Sedano2017 %] found that software development projects have
> <span i="waste (in software development)">nine types of waste</span>: building the
> wrong feature or product, mismanaging the backlog, rework, unnecessarily complex
> solutions, extraneous <span i="cognitive load">cognitive load</span>
> (<a section="thinking"/>), psychological distress, waiting and <span
> i="multitasking">multitasking</span>, knowledge loss, and ineffective
> communication.  *None of these are software issues,* so if you only think about
> the software side of your project, it's going to take longer and hurt more than
> it needs to.

## Crunch Mode

I used to brag about the hours I was working.  Not in so many words, of
course---I had *some* social skills.  Instead, I'd show up for work around noon,
unshaven and yawning, and casually mention how I'd been up until 6:00 a.m.
hacking away at some monster bug.

Looking back, I can't remember who I was trying to impress.  Instead, what I
remember is how much of the code I wrote in those all-nighters I threw away once
I'd had some sleep, and how much damage the bugs I created in those bleary-eyed
stupors did to my teammates' productivity.

My mistake was to confuse "long hours" with "getting things done".  You can't
produce software (or anything else) without doing some work, but you can easily
do lots of work without producing anything of value.  Scientific study of <span
i="overwork">overwork</span> goes back to at least the 1890s---see
[% b Robinson2005 %] for a short, readable summary.  The most important
results for developers are:

1.  Working more than eight hours a day for more than a couple of weeks of time
    lowers your total productivity, not just your hourly productivity---i.e.,
    you get less done *in total* (not just per hour) when you're in
    <span g="crunch_mode" i="crunch mode">crunch mode</span> than you do when you work
    regular hours.

1.  Working over 21 hours in a stretch increases the odds of you making a
    catastrophic error just as much as being legally drunk.

These facts have been verified through hundreds of experiments over the course
of more than a century, including some on novice software developers
[% b Fucci2020 %].  The data behind them is as solid as the data linking
smoking to lung cancer.  However, while most smokers will acknowledge that their
habit is killing them, people in the software industry still talk and act as if
science somehow didn't apply to them.  To quote <span i="Robinson,
Evan">Robinson</span>'s article:

> When <span i="Ford, Henry">Henry Ford</span> famously adopted a 40-hour workweek
> in 1926, he was bitterly criticized by members of the National Association of
> Manufacturers.  But his experiments, which he'd been conducting for at least 12
> years, showed him clearly that cutting the workday from ten hours to eight
> hours---and the workweek from six days to five days---increased total worker
> output and reduced production cost…  the core of his argument was that reduced
> shift length meant more output.
>
> …many studies, conducted by businesses, universities, industry associations and
> the military, …support the basic notion that, for most people, eight hours a
> day, five days per week, is the best sustainable long-term balance point between
> output and exhaustion.  Throughout the 30s, 40s, and 50s, these studies were
> apparently conducted by the hundreds; and by the 1960s, the benefits of the
> 40-hour week were accepted almost beyond question in corporate America.  In
> 1962, the Chamber of Commerce even published a pamphlet extolling the
> productivity gains of reduced hours.
>
> But, somehow, Silicon Valley didn't get the memo…

I was part of a data visualization startup in the mid-1990s.  Three months
before our first release, the head of development "asked" us to start coming in
on Saturdays.  We were already pulling one late night a week at that point
(without overtime pay---our boss seemed to think that ten dollars' worth of
pizza was adequate compensation for four hours of work) and most of us were also
working at least a couple of hours at home in the evenings.  It's hardly
surprising that we missed our "can't miss" deadline by ten weeks, and had to
follow up our 1.0 release with a 1.1 and then a 1.2 in order to patch the
crash-and-lose-data bugs we'd created.  We were all zombies, and zombies can't
code.

Those kinds of hours are sadly still normal in many parts of the software
industry.  Everyone knows that designing and building software is a creative act
that requires a clear head, but many people then act as if it was like digging a
ditch.  The big difference is that it's hard to lose ground when digging (though
not impossible).  In software, on the other hand, it's very easy to go backward.
It only takes me a couple of minutes to create a bug that will take hours to
track down later---or days, if someone else is unlucky enough to have to track
it down.  This is summarized in Robinson's first rule:

> <span i="productivity">Productivity</span> varies over the course of the
> workday, with the greatest productivity occurring in the first four to six
> hours.  After enough hours, productivity approaches zero; eventually it becomes
> negative.

It's hard to quantify the productivity of programmers, testers, and UI
designers, but five eight-hour days per week has been proven to maximize
long-term total output in every industry that has ever been studied. There is no
reason to believe that ours is any different.

Ah, you say, that's "long-term total output".  What about short bursts now and
then, like pulling an all-nighter to meet a deadline?  That's been studied too,
and the results aren't pleasant.  Your ability to think drops by 25 points for
each 24 hours you're awake.  Put it another way, the average person's IQ is only
75 after one <span i="all-nighters">all-nighter</span>, which puts them in the
bottom 5% of the population.  Two all nighters in a row and their effective IQ
is 50---the level at which people are usually judged incapable of independent
living.

The catch in all of this is that people usually don't notice their abilities
declining.  Just like drunks who think they're still able to drive, people who
are deprived of sleep don't realize that they're not finishing their sentences
(or thoughts).  They certainly don't realize that they're passing parameters
into function calls the wrong way around or that the reason the tests are
failing is that they've forgotten to redeploy the application again.

The moral of this story is to think very hard about what's more important to
you---how much good work you produce or how much of a martyr you appear to
be---and pace yourself accordingly.

## Time Management

"But I have so many assignments to do!", you say.  "And they're all due at once!
I *have* to work extra hours to get them all done!" Sadly, that is often true:
while people in industry joke that having two bosses means living in hell, most
students can only dream of having just two, since most schools do a lousy job of
coordinating due dates across different courses.  [% b Tregubov2017 %]
found strong correlation between the number of projects and the number of
interruptions that developers reported, while [% b Edwards2009 %] found
that starting assignments early and working consistently both predicted good
grades.

The best strategy for <span i="time management">time management</span> is to
prioritize and focus.  Prioritizing is important because most of us are very
good at spending hours on things that don't need to be done and then finding
themselves with too little time for the things that actually count. A little bit
of organizing can help a lot---as [% b Mark2008 %] reported, "…people
compensate for interruptions by working faster, but this comes at a price:
experiencing more stress, higher frustration, time pressure and effort."

> ### How bad is it?
>
> A student of mine kept a stopwatch beside his computer for a couple of weeks
> during term.  Every time he read mail, put Twitter in the foreground, or went to
> Manchester United's web site he hit the button to stop it.  At the end of two
> weeks he discovered that he only spent 28% of his "working" time working.  Put
> it another way, he could have finished his assignments in a third of the time
> they actually took.

Make a list of the things you have to do.
:   I still use a hardcover lab notebook for this so that I can doodle in it
    when I'm thinking, but a lot of people keep a personal wiki or send
    themselves email messages that then go into a folder titled "To Do".
    However you do it, the important thing is to *write it all down*.  You can
    only keep a handful of things in short-term memory at once
    (<a section="thinking"/>); if you try to manage a <span i="to-do list">to-do
    list</span> longer than that in your head, you will forget things.

Weed out everything that you don't need to do right away.
:   If you want to try out a new editor theme that's play time not work time,
    and we're talking about getting work done.

Sort the list so that the most important tasks are at the top.
:   I don't worry about getting the stuff below the first three or four lines
    into order, since I'm going to re-check my list before I get to them anyway.

Make sure you have everything you need to see the first task through.
:   The most recent files from <span i="version control">version control</span>
    (<a section="git-solo"/>), the assignment specification, a fresh cup of
    tea---whatever it is, don't give yourself an excuse to interrupt your work,
    because the world will provide enough of those.

Turn off <span i="interruptions">interruptions</span>.
:   Shut down your mail client, instant messaging, and your cell phone.  Don't
    panic, it's only for an hour---most people can't stay focused longer than
    that, and you'll need to stretch your muscles and get rid of that tea you
    drank by then anyway.

Set an alarm to go off in fifty minutes.
:   Don't switch tasks in that time unless you absolutely have to.  Instead, if
    you remember an email message that needs to be sent or discover a couple of
    tests that really should be written, add a note to your to-do list.  This is
    another reason I keep mine in a lab notebook: the few seconds it takes to
    pick up a pen and jot something down gives my hands a rest from the
    keyboard, and I'm less likely to be distracted by a notebook than by a text
    editor.

Take a ten-minute <span i="breaks (importance of regular)">break</span>.
:   Get up and move around a little during these ten minutes, even if it's just
    to refill your water bottle, visit the toilet, or do a few stretches. You
    will be able to work longer if your back doesn't ache, and being away from
    the keyboard for a few minutes gives your brain a chance to reflect on what
    you've just been doing. (It's amazing how often a problem that has baffled
    me for an hour can be solved by a five-minute walk.) When you're done, check
    that your to-do list is still in the right order and start again.

If any task on your list is more than an hour long, break it down into
smaller pieces and prioritize those separately.  And keep in mind that the
future is approaching at a fixed rate of one day every 24 hours: if something's
going to take sixty hours to do you had better allow at least ten working days
for it, which means you'd better tackle the first piece two working weeks before
the deadline.  Since breaking large tasks down into small ones takes time, don't
be surprised if "plan XYZ" appears as a task in your list.

The point of all this organization and preparation is to get yourself into the
most productive mental state possible.  [% b Csikszentmihalyi1991 %]
popularized the term <span g="flow" i="flow">flow</span> for this; athletes call
it "being in the zone", while musicians talk about losing themselves in what
they're playing.  Whatever name you use, you will produce much more in this
state than normal.

The bad news is that it takes anywhere from several seconds to several minutes
to get back into a productive flow after an interruption
[% b Parnin2010 Borst2015 %].  This means that if you are interrupted half
a dozen times per hour you are *never* at your productive peak. Ironically, the
cost of self-interruptions may be even worse than the cost for external
interruptions [% b Abad2018 %].  It's very much like processes being paged
in and out by an operating system: if it happens too often, the CPU spends all
its time moving things around and none doing useful work.

Making lists and setting 50-minute alarms will seem a little earnest at first,
but your friends will stop mocking you when they see that you're able to finish
your assignments and still have time to play some badminton and catch a movie.
They may even start to imitate you.

> ### Open offices suck
>
> <span i="open offices (evils of)">Open offices</span> were created so that
> (mostly male) managers could keep an eye on (mostly female) office workers, and
> to reduce air conditioning costs [% b Eley1995 %].  In every other way we
> can measure, they lower productivity [% b Bernstein2018 %].

> ### Nihil de nobis sine nobis
>
> The rules laid out above were created by and for people near the middle of the
> bell curve with respect to focus and attention span. People who are <span
> g="neurodivergent" i="neurodivergent">neurodivergent</span>, i.e., whose brains
> work differently from the average when it comes to sociability, learning,
> attention, and mood, may find that other approaches work better for them.
>
> But while society accepts that people of different heights need different desks
> and seating to be comfortable, there is still a lot of <span i="mental health
> (stigma associated with)">stigma</span> associated with differences in mental
> function, which are often measured by [how inconvenient they are to other
> people][adhd-thread].  One example is how tests for <span g="adhd"
> i="ADHD">attention-deficit/hyperactivity disorder</span> (ADHD) are
> phrased. "Subject is overly talkative": compared to who? "Subject does X when it
> is inappropriate": by whose rules? "Struggles to pay attention": in fact, most
> people with ADHD can pay very close attention, but not when they are in
> environments that are full of distractions (like noisy classrooms).
>
> The title of this callout is Latin for, "Nothing about us without us." It means
> that no decisions should be made without the full participation of those who
> will be affected.  If you are neurodivergent, you probably have a set of
> strategies for managing time and attention. If you are <span g="neurotypical"
> i="neurotypical">neurotypical</span> and have neurodivergent teammates, ask them
> what works well for them rather than ignoring the difference or guessing what
> they might want. Please do the same if you have teammates who have difficulty
> seeing, hearing, or moving about: they have expertise you don't.

## Meetings

The previous section explained how to be productive individually---what about
being productive in a team?  The most important thing is running <span
i="meetings">meetings</span> efficiently.  The rules doing so are simple but
rarely followed:

Agree on the rules.
:   Bridge and ping pong are both fun games, but you can't play both on the same
    table at the same time. (Please don't take this as a challenge, or if you
    do, please post a video.) Similarly, exactly what rules you use to run
    meetings matters less than everyone agreeing on what the rules are.

Keep discussion meetings and decision meetings separate.
:   A <span g="discussion_meeting" i="meetings! discussion">discussion
    meeting</span>'s purpose is to explore design alternatives or figure out
    what next term's goals should be.  A <span g="decision_meeting"
    i="meetings!decision">decision meeting</span> on the other hand, is for
    choosing which alternatives to pursue.  Discussion meetings are meant to be
    wide-ranging (and fun); decision meetings should be short and focused.  The
    two are never completely distinct in practice, but decision-making is more
    efficient if it isn't mixed with brainstorming. The rest of these rules
    focus on decision meetings.

Decide if there actually needs to be a meeting.
:   If the only purpose is to share information, have everyone send a brief
    email instead.  Most people can read faster than they can speak: if someone
    has facts for the rest of the team to absorb, the most polite way to
    communicate them is to type them in.

Write an agenda.
:   If nobody cares enough about the meeting to prepare a point-form list of
    what's to be discussed, the meeting probably doesn't need to happen.  Note
    that "the agenda is all the open issues in our GitHub repo" doesn't count.

Include timings in the agenda.
:   Doing this helps prevent early items stealing time from later ones.  The
    first estimates with any new group are inevitably optimistic, so expect to
    revise them upward for subsequent meetings.  But don't have second or third
    meeting just because the first one ran over time: instead, try to figure out
    *why* it ran over and fix the underlying problem.

Prioritize.
:   Tackle issues that will have high impact but take little time first, and
    things that will take more time but have less impact later.  That way the
    meeting will still have accomplished something if the first items run over
    time.

Make one person responsible for keeping things moving.
:   One person should be made moderator and be responsible for keeping items to
    time, chiding people who are having side conversations or checking email,
    and asking people who are talking too much to get to the point.  The
    moderator should *not* do all the talking: in fact, whoever is in charge
    will talk less in a well-run meeting than most other participants.

Require politeness.
:   No one gets to be rude, no one gets to ramble, and if someone goes off
    topic, it's the moderator's job to say, "Let's discuss that elsewhere."  As
    discussed below, this is *not* the same as assuming that everyone has good
    intentions, and that if they say something rude it was just an accident.

No interruptions.
:   This rule is a special case of the one above, since treating other people
    with respect is the sincerest form of politeness.  Participants should raise
    a finger, hand, put up a sticky note, or make another well understood
    gesture to indicate when they want to speak.  The moderator should keep
    track of who wants to speak and give them time in turn.

No distractions.
:   Side conversations make meetings less efficient because nobody can actually
    pay attention to two things at once.  Similarly, if someone is checking
    their email or texting a friend during a meeting, it's a clear signal that
    they don't think the speaker or their work is important.  This doesn't mean
    a complete ban on technology---people may need accessibility aids, or may be
    waiting for a call from a dependent---but by default, phones should be face
    down and laptops should be closed during in-person meetings.

Take minutes.
:   Someone other than the moderator should take <span i="minutes (of
    meetings)">point-form notes</span> about the most important information that
    was shared, and about every decision that was made or every task that was
    assigned to someone.  This responsibility should rotate each meeting so that
    everyone has to take a turn; otherwise, as discussed in <a section="teams"/>,
    the burden will fall unfairly on some people.

End early.
:   If the meeting is scheduled for 10:00--11:00, aim to end at 10:50 to give
    people a break before whatever they're doing next.

> ### I don't like your tone
>
> <span g="tone_policing" i="tone policing">Tone policing</span> is a tactic used
> to shut down discussion by criticizing people for expressing emotion.  It is
> often used against women, who are told to "calm down" when they show any sign of
> being angry at being excluded or not taken seriously. As [this
> article][flower-good-intent] by [Annalee Flower][flower-annalee] says:
>
> *People often reach for positive statements like "assume good intent" because
> they're worried about people being "shamed" over innocent mistakes. But society
> at large is already inclined to assume good intent in people with power and
> privilege–even when they're not demonstrating it. If you want to build a culture
> of "assuming good intent," start by assuming good intent in marginalized people.*
>
> *Assume that they already tried being nice. Assume that their feelings are
> valid. Assume that, after a lifetime of practice, they are responding to harmful
> behavior in the way that is safest for them.  Prioritize that safety over the
> momentary discomfort people feel when they realize they've done something
> hurtful.*

As soon as the meeting is over, add a summary to the project's wiki, version
control repository, or wherever else things are being stored:

People who weren't at the meeting can follow what's going on.
:   We all have to juggle tasks from several projects or courses, which means
    that sometimes we can't make it to meetings.  Checking a written record is a
    more accurate and efficient way to catch up than asking a colleague, "What
    did I miss?"

Everyone can check what was actually said or promised.
:   More than once, I have looked over a set of minutes and thought, "Did I say
    that?" or, "I didn't promise to have it ready then!"  Accidentally or not,
    people often remember things differently; writing them down gives everyone a
    chance to correct mistakes, misinterpretations, or misrepresentations.

People can be held accountable at subsequent meetings.
:   There's no point making lists of questions and action items if you don't
    follow up on them later.  If you are using an <span i="issue-tracking
    system">issue-tracking system</span> (<a section="tooling"/>), create an issue
    for each new question or task right after the meeting and update those that
    are being carried forward.  This helps a lot when the time comes to draw up
    the agenda for the next meeting.

Please don't email minutes to everyone: our inboxes are full enough, and the
more places new team members need to search in order to find things, the more
likely they are to miss something important.

> ### Are you a blowfish or a clam?
>
> [NOAA's guide][noaa-disruptive] to dealing with disruptive behaviors has useful
> labels and even more useful advice for handling people who may send meetings off
> course.

If you would like to become better at sharing information and making decisions,
there is no better place to start than [% b Brookfield2016 %]. This book
catalogs fifty different techniques and explains when and why each is useful.

## Air Time

One of the problems in a synchronous meeting is the tendency of some people to
speak far more than others.  Other meeting members may be so accustomed to this
that they don't speak up even when they have valuable points to make.

One way to combat this is to give everyone <span i="meetings!three sticky notes;
three sticky notes (in meetings)">three sticky notes</span> (or coins, or
paperclips---anything inedible will do).  at the start of the meeting.  Every
time they speak, they have to give up one sticky note.  When they're out of
stickies, they aren't allowed to speak until everyone has used at least one, at
which point everyone gets all of their sticky notes back.  This ensures that
nobody talks more than three times as often as the quietest person in the
meeting, and completely changes group dynamics.  People who have given up trying
to be heard suddenly have space to contribute, and the overly frequent speakers
realize how unfair they have been.

Another useful technique is called <span i="meetings!interruption bingo;
interruption bingo (in meetings)">interruption bingo</span>.  Draw a grid and
label the rows and columns with the participants' names.  Each time one person
interrupts another, add a tally mark to the appropriate cell; halfway through
the meeting, take a moment to look at the results.  In most cases it will be
clear that one or two people are doing all of the interrupting.  After that,
saying, "All right, I'm adding another tally to the bingo card," is often enough
to get them to throttle back.

Online meetings provide special challenges, both in the context of regulating
how often individuals speak, as well as running meetings in general.
[% b Troy2018 %] discusses why <span i="meetings (online)">online
meetings</span> are often frustrating and unproductive and points out that in
most online meetings, the first person to speak during a pause gets the floor.
As a result, "If you have something you want to say, you have to stop listening
to the person currently speaking and instead focus on when they're gonna pause
or finish so you can leap into that nanosecond of silence and be the first to
utter something.  The format…encourages participants who want to contribute to
say more and listen less."

The solution is to run a text chat beside the video conference where people can
signal that they want to speak.  The moderator can then select people from the
waiting list.  This practice can be reinforced by having everyone mute
themselves, and only allowing the moderator to unmute people.

## Making Decisions

The purpose of a meeting is to make decisions, so sooner or later, the members
of a project must decide who has a say in what.  The first step is to
acknowledge that every team has a power structure: the question is whether it's
formal or informal---in other words, whether it's accountable or unaccountable
[% b Freeman1972 %].  The latter can work for groups of up to half a dozen
people in which everyone knows everyone else.  Beyond that, groups need to spell
out who has the authority to make which decisions and how to achieve consensus.
In short, they need explicit <span g="governance"
i="governance">governance</span>.

<span g="marthas_rules" i="Martha's Rules">Martha's Rules</span> are a practical
way to do this in groups with up to a few dozen members
[% b Minahan1986 %], and work very well for smaller teams too:

1.  Before each meeting, anyone who wishes may sponsor a proposal.  Proposals
    must be filed at least 24 hours before a meeting in order to be considered
    at that meeting, and must include:
    -   a one-line summary
    -   the full text of the proposal
    -   any required background information
    -   pros and cons
    -   possible alternatives

2.  A quorum is established in a meeting if half or more of voting members are
    present.

3.  Once a person has sponsored a proposal, they are responsible for it.  The
    group may not discuss or vote on the issue unless the sponsor or their
    delegate is present.  The sponsor is also responsible for presenting the
    item to the group.

4.  After the sponsor presents the proposal a <span g="sense_vote" i="sense
    vote">sense vote</span> is cast for the proposal prior to any discussion:
    -   Who likes the proposal?
    -   Who can live with the proposal?
    -   Who is uncomfortable with the proposal?

5.  If all of the group likes or can live with the proposal, it passes with no
    further discussion.

6.  If most of the group is uncomfortable with the proposal, it is sent back to
    its sponsor for further work.  (The sponsor may decide to drop it if it's
    clear that the majority isn't going to support it.)

7.  If some members are uncomfortable with the proposal, a timer is set for a
    brief discussion moderated by the meeting moderator.  After 10 minutes or
    when no one has anything further to add, the moderator calls for a straight
    yes-or-no vote on the question: "Should we implement this decision over the
    stated objections?"  If a majority votes "yes" the proposal is implemented.
    Otherwise, it is returned to the sponsor for further work.

Every group that uses Martha's Rules must make two procedural decisions:

How are proposals put forward?
:   The easiest way to do this in a software project is to file an issue in the
    project's issue tracker tagged *Proposal*.  Team members can then comment on
    the proposal, and the sponsor can revise it before bringing it to a vote.

Who gets to vote?
:   In a course project the answer is "whoever is part of the team," but if the
    project grows and attracts volunteer contributors, a more explicit rule is
    needed.  One common method is for existing members to nominate new ones, and
    for the team to hold a straight yes-or-no vote on each.  Another is <span
    i="Apache Software Foundation">[Apache][apache]</span>'s "<span
    i="do-ocracy">do-ocracy</span>" approach: if you have done the work and
    no-one explicitly objects, the proposal is accepted or the change is
    merged. This "put up or shut up" approach is a good way to test if someone
    *really* wants a change, but in practice it often means projects are driven
    by people who are extroverted or self-confident rather than by those with
    the best technical skills or the best understanding of what users
    need. We'll revisit this in <a section="fairness"/>.

Rules that people don't know about can't help them.  Once your team agrees on a
project structure, a workflow, how to get items on a meeting agenda, or how to
make decisions, you should document this for newcomers (and to prevent disputes
among people already in the team).  This information may be included as a
section in the project's <span i="README file">`README`</span> file
(<a section="starting"/>) or put into a separate file called
<span i="CONTRIBUTING file">`CONTRIBUTING`</span>.  This material should describe the naming
conventions to use for functions, what tags to put on issues, or how to install
and configure the software needed to start work on the project.  Wherever it
goes, remember that the easier it is for people to get set up, the more likely
they are to contribute [% b Steinmacher2014 %].
