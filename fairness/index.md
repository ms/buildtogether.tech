---
---

This book is about course projects, but as <span x="starting"/> said, these are
often designed to prepare you for real jobs.  Since the transition from being a
student to working full time is one of the most important in your career, this
chapter looks at the hiring process and what happens afterward.

There is no way to discuss these topics without talking about fairness and bias
in the tech industry.  I was interviewing for a new job as I was writing this
book, and while some companies' interviewing processes were designed to create a
level playing field, others were not (and that's putting it politely).  How
companies get this wrong is reflected in, and contributes to, how the things
they build sometimes harm society as well as embarrassing their creators.

It easy to avoid these mistakes *if* you are willing to look beyond the code you
write.  As with so many things, the best place to start is with a little bit of
history.

## How Tech Companies Get Hiring Wrong

In 1905, Harvard began selecting students based on their College Entrance Exam
Board results.  As a result, Jewish enrolment began to rise, and by the early
1920s they made up more than a fifth of the incoming class.  This wasn't an
outcome the establishment was willing to accept, but neither were explicit
quotas, so they moved the goalposts <cite>Karabel2006</cite>.  Admissions
officers began asking questions about the "character" of prospective students,
and the university began asking for personal essays that could be graded however
the university found most convenient. By 1933, the rate of Jewish admission was
back down to an "acceptable" 15%.

This story doesn't make sense if you think that a university's job is to find
and train the smartest people it can.  It makes a lot of sense when you realize
that most institutions' first priority is to perpetuate themselves---if it
wasn't, they probably wouldn't still be around.  In a similar way, the hiring
process at many tech companies isn't designed to find the best programmers: it's
designed to find the people who are most like the people doing the hiring.
Phrases like "cultural fit" are almost always code for "people like us";
consciously or not, we are all biased toward those who look like us, talk like
us, and make the same pop culture references as us, none of which has anything
to do with actual ability.

One way this shows up in tech hiring is in whiteboard coding questions about
linked lists, dynamic programming, and other topics from computer science
classes on data structures and algorithms.  As [Hillel Wayne][wayne-hillel]
discovered when he looked at [their history][wayne-linked-lists], they might
have indicated how much experience someone had using C or Pascal in the 1980s,
but they have no more to do with on-the-job performance than the essay questions
used by Ivy League schools have to do with your ability to learn.  When [April
Christina Curley][curley-april] began coaching Black students how to prepare for
interviews with Google that included questions like these the company shut her
down, even though schools like Stanford had been running coaching sessions for
their students for years <cite>Tiku2021</cite>.

<cite>Behroozi2019,Behroozi2020a,Behroozi2020b</cite> summarize many other
things that often go wrong in hiring, from interviewers not knowing which job
someone had actually applied for and long delays waiting for feedback to asking
candidates to spend several days working for free on programming assignments.
These are all signs of dysfunctional company culture, and it's usually safe to
assume that you won't be treated with any more respect once you start work than
you were while you were interviewing.

<div class="callout" markdown="1">

### A sign of privilege

In the first draft of this section I wrote, "If a company does any of these
things, you should find somewhere else to work."  One of the early reviewers
wrote, "Gosh, it must be nice to be able to walk away from a job."  They were
right: most people don't have the privilege and financial security I do, so they
don't have as many options open to them as I do.

</div>

So how can companies do hiring well?

Write inclusive, accessible job ads.
:   <cite>Gaucher2011</cite> is just one of many studies showing that gendered
    wording in job ads reinforces gender inequality in male-dominated
    occupations. [Gender Decoder][gender-decoder] and [GenderMag][gendermag] can
    help you find bugs like this in ads and software
    <cite>Hilderbrand2020</cite>. Tools for finding and eliminating racial bias
    and other problems aren't as common, but <cite>Washington2020</cite> will
    tell you what to aim for, and if [WebAIM WAVE][webaim-wave] doesn't give
    your online job ads a clean bill of health, please fix them.

Post a public description of the hiring process.
:   [Automattic's description][automattic-hiring] is a good model: it lays out
    what's going to happen in what order, how much time is expected, and the
    principles everything is based on.

Use blinded screening.
:   Everyone has <span g="unconscious_bias">unconscious biases</span>, and many
    of the rules scientists follow when running experiments are designed to
    prevent them contaminating results (<span x="research"/>).  The same is true
    of hiring, and so is the solution. For example, my first-round interview
    with Automattic was done by text over Slack so that my appearance, my
    accent, or the fact that I sometimes need a couple of moments to collect my
    thoughts wouldn't bias the interviewer. Similarly, companies should redact
    things like a candidate's age, race, and gender when evaluating resumes.

Use diverse interview panels.
:   People tend to be biased toward hiring people who are like them; Silicon
    Valley calls this "cultural fit" rather than "discrimination", but they are
    functionally indistinguishable. Giving people from under-represented
    backgrounds a say in who's hired next gives other people with similar
    backgrounds a better chance of being treated fairly.

Have candidates solve realistic problems with their preferred tools---including search.
:   Most programmers have laptops, and video calls are now a part of everyday
    life in industrialized countries, so there's no reason *not* to give people
    an hour to show what they can do using the IDE of their choice.  There is
    also no reason to stop them using online search while they do this: every
    working programmer relies on our external collective memory, so telling a
    candidate they can't during an interview is like telling a chef to make a
    meal without using saucepans or knives.

These principles apply to your school and your courses as well.  Are course
descriptions and course websites inclusive? Are instructors required to use
blinded grading to ensure that personal likes and dislikes don't affect grades?
If the answers are "no", the next questions to ask is, "How can we fix this?"

<div class="callout" markdown="1">

### You're interviewing them while they're interviewing you

I have interviewed people who didn't ask a single question about the company,
what an average day would look like, or how their career might evolve over time.
[Julia Evans][evans-julia] has a good list of [questions to ask in
interviews][evans-interviews]; there probably isn't time to get to them all,
but asking two or three that matter to you most will impress your interviewer as
well as giving you valuable information.

</div>

## On the Job

<span g="preparatory_privilege">Preparatory privilege</span> is the advantage
someone has in an supposedly objective assessment as a result of having
opportunities earlier in life that other people didn't have.  Ignoring it is
like ignoring the difference between professional athletes who are paid to train
all day and amateurs whose jobs only allow them to train in the evening or on
weekends, or pretending that people doing interviews in their second or third
language are on an equal footing with people who are interviewing in their
native language.

But imagine you're about to have a meeting with someone.  There's a box with
half a dozen cookies in the room, so you help yourself to a couple before the
other person shows up. When they do, you have to make a choice: do you say,
"I've already had two, so I should only have one more and you should get three?"
or, "There were four cookies in the box when you arrived, so we get two each"
(meaning that you will have had four in total).

Most people would say that the first answer is the moral one---in my experience,
people who don't aren't people you'd want on your team.  On the other hand, if I
had a couple of cookies yesterday or last week, I probably won't feel obliged to
give you more than half today.  Is it really a company's responsibility to take
past inequities into account when hiring?

If the company is interested in on-the-job performance, the answer is "yes".
Going back to the athletic analogy, an amateur who can run a hundred meters in
11 seconds could well perform better than a professional who can do it in 10.5
*once they start training full-time*, i.e., once their disadvantage is removed.
Similarly, female students are less likely to be called on in class and more
likely to be given non-coding tasks in team projects than male students.  If
they can get a B despite that, they will probably outperform a male student who
only gets an A with the deck stacked in his favor, provided the company treats
both equally after they are hired.

That last statement is where many companies and universities fail despite good
intentions.  Hiring more people from under-represented groups doesn't matter if
they have to work twice as hard to be taken half as seriously, if they are
constantly passed over for promotion, or if discussions about who would make a
good department chair continue to take place in the men's locker room after the
department's Friday afternoon hockey game.  The [Centre for Community
Organizations][coco] has a depressing summary of what it's like to be [the
"problem" woman of color in the workplace][coco-problem]; if what it describes
isn't familiar, you might be a part of the problem, just as I was when I was a
student.

There are no easy fixes to these problems, but there are things companies can
do, and it's fair to ask about them during an interview:

Share data on how well the company has been doing recently.
:   It's reasonable to ask during an interview what proportion of a company's
    staff (technical and otherwise) come from under-represented backgrounds and
    what the average length of stay at the company is.  If the interviewer
    doesn't know the answer they should be able to get it; if the company
    doesn't have that data or won't share it, you've just learned something.

Have an org chart.
:   As we said in <span x="important"/>, everyone organization has a power
    structure: the only question is whether it's public and accountable, or
    whether the organization runs on who you know and how willing people are to
    barge in on strangers.

Have written criteria for performance reviews.
:   The ones shown in <span x="evaluation"/> are a good model, and these
    *are* something a company can share before hiring you. If a company doesn't
    have criteria, or if performance reviews are only done when an employee asks
    for one, the system is once again biased toward the extroverted and the
    well-connected.

Specify how much time employees can take off.
:   Some tech companies have an "unlimited vacation" policy, meaning that
    employees can take as much time as they want as long as their work is
    getting done.  This sounds very attractive, but [people actually take *less*
    time off][namely-time-off] under these policies, both because they feel
    guilty and because they worry about taking too much.  It also saves
    companies money: if someone is owed vacation days when they're laid off, the
    company has to compensate them, but if there's no target, they don't.

## Being an Ally

But suppose you are a straight, physically able, white or Asian male without
mental health issues---why should you feel compassion toward people who are
marginalized because they aren't all of these things?  One argument is
self-interest: study after study has shown that more diverse teams perform
better, that companies with more diverse management are more profitable, and so
on <cite>Zhan2020</cite>.

<div class="callout" markdown="1">

### Setting limits

This finding is sometimes abused---men who want an excuse to continue to be
assholes try to be clever with words and talk about "diversity of thought,"
meaning, "I should be allowed to be offensive as long as I don't raise my
voice."  This is an example of the [paradox of tolerance][paradox-of-tolerance]:
if a group is tolerant without limit, it will eventually be undermined by the
intolerant taking advantage of that.

<blockquote markdown="1">

We can disagree and still love each other unless your disagreement is rooted
in my oppression and denial of my humanity and right to exist.

--- James Baldwin

</blockquote>

</div>

Despite the benefits of diversity, research consistently shows that members of
under-represented groups have less successful careers.  In science, for example,
"…novel contributions by gender and racial minorities are taken up by other
scholars at lower rates than novel contributions by gender and racial
majorities, and equally impactful contributions of gender and racial minorities
are less likely to result in successful…careers than for majority groups."
<cite>Hofstra2020</cite> If this comes as a surprise to you, you might be part
of the problem rather than part of the solution.

Another reason to care about these issues is that discussion of fair play stops
being theoretical as soon as we talk about your rights as an employee.  Until
recently there has been a lot less discussion of this in tech than of
intellectual property rights, but in the wake of high-profile incidents like
[Google's decision to fire the AI researcher Timnit Gebru][gebru-firing], tech
workers are belatedly realizing that the industry they have created will treat
them just as callously as it treats everyone else.

Standing up to a bad boss or an unfair professor is easier in theory than in
practice, because the student's evaluation of the professor doesn't affect the
professor nearly as much as the professor's evaluation of the student affects
the student.  This imbalance is why management fads like "radical candor" are
<span g="bullshit">bullshit</span>: they brush aside reality in order to avoid
having to acknowledge unwelcome truths.

The only effective way to address power disparities like these is collective
action: many people with relatively little power each can defend their rights if
they organize.  However, forty years of sustained disinformation from the rich
and powerful have made many people believe that collectives are intrinsically
inefficient or that they stifle innovation.  (Ironically, the entrepreneurs and
CEOs who are most vocal about the advantages of unrestricted capitalism all
organize their companies along socialist lines <cite>Phillips2019</cite>.)

As an example of what organizing looks like in practice, consider the difference
between a ride-sharing company like Uber and the house-cleaning company Up & Go
<cite>Thompson2019</cite>.  Uber controls the app that connects customers with
drivers, and uses that control to extract profits by squeezing drivers. In
contrast, the people who work for Up & Go own the app as a group; 5% of what
customers pay goes to its upkeep, and the rest goes to the workers.  There might
be one less billionaire in the world, but everyone else benefits.

Up & Go is an example of a <span g="commons">commons</span: something managed
jointly by a community according to rules they themselves have evolved and
adopted <cite>Ostrom2015</cite> As <cite>Bollier2014</cite> explains, all three
parts of that definition are essential: a commons isn't just a shared pasture or
a set of software libraries, but also includes the community that shares it and
the rules they use to do so.  Before reading either of those books, though, you
should read <cite>Mildenberger2019</cite>, which explains why the idea of "the
tragedy of the commons" is completely wrong.

<div class="callout" markdown="1">

### Your politics is showing

An early reviewer of this material asked whether it was appropriate for me to
put so much of my personal politics into it.  I pointed out that many schools
have a course on the business of software that talk exclusively about for-profit
startups backed by private investors and venture capital.  Choosing to discuss
those topics is equally political---it's just more common.

</div>

You might think there isn't a lot you can do as a student or as a junior
programmer to fix what's broken in our industry, but there is.  An <span
g="ally">ally</span> is a member of a privileged group who is working to
understand their own privilege and create an environment that's fair for
everyone.  As [this guide][dlf-active-bystander] from the [Digital Library
Foundation][dlf] explains, there are several ways in which you can be an <span
g="active_bystander">active bystander</span>, i.e., several ways in which you
can <span g="lending_privilege">lend your privilege</span> to defuse the
situation and defend the person who is being attacked.

<div class="callout" markdown="1">

### Not acting is a choice as well

Always remember that not acting is just as much a choice as acting.  <span
x="10-newcomers"/> said that your organization's culture is defined by the worst
behavior it tolerates; I have come to believe that who we really are as
individuals is defined in the same way.

</div>

<cite>Dobbin2019</cite> (summarized in <cite>Dobbin2020</cite>) found that most
of what American companies have done over the past twenty years to reduce sexual
harassment and discrimination has either had no effect or has actually made
things worse. The reason is that the people who care don't gain anything from
being told they should, while the people who are part of the problem resent
being told that and tend to take out their anger on the people the training is
meant to protect.

<cite>Dobbin2019</cite> also found that what did make a difference was showing
people how to intervene, since this made them more likely to do so in the same
way that having some first aid training makes you more likely to take action in
a crisis.  An example of this is the guidelines in <cite>Aurora2018</cite> for
responding to Code of Conduct violations (<span x="starting"/>). On a smaller
scale, your instructor can have you work through scenarios like this with your
teammates and the rest of your class:

<blockquote markdown="1">

Some of the students in a team project course are openly gay.  Some other
students have privately told the instructor that for religious reasons they
would rather not be in the same teams as the gay students.  How should the
instructor respond?

</blockquote>

Another scenario might be:

<blockquote markdown="1">

Your and your teammates frequently work together in the library of the business
school (which has better WiFi and more comfortable chairs than the computer
labs).  Every time you do, one of your teammates makes a point of sitting beside
younger students that they find attractive and talking with them.  It's clear
from those students' body language that they find the attention unwelcome;
you've pointed this out to your teammate, but their behavior has continued.
What should you do next?

</blockquote>

Neither of these scenarios is about programming, but I hope you understand by
now that the success or failure of your project depends on a lot more than just
the code you write.  Learning how to handle situations like these may also help
you become more compassionate: if you've never had to worry about them before,
the odds are that (in John Scalzi's memorable analogy) you've been playing on
the lowest difficulty setting there is my whole life, and as a result don't
realize how much harder things are for others whose default setting isn't "easy
mode" <cite>Scalzi2012</cite>.

## Outside

<span class="fixme">ethics in the context of AI: https://github.com/gvwilson/buildtogether.tech/issues/26</span>

<span class="fixme">lending privilege as a form of allyship https://github.com/gvwilson/buildtogether.tech/issues/70</span>

<span class="fixme">being an active bystander https://github.com/gvwilson/buildtogether.tech/issues/78</span>

As <cite>Lee1962</cite> said, "With great power comes great responsibility."
