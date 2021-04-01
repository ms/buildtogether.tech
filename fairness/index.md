---
---

This book is about course projects, but as <span x="starting"/> said, these are
often designed to prepare you for real jobs.  Since the transition from being a
student to working full time is one of the most important in your career, this
chapter looks at the hiring process and what happens afterward.

There is no way to discuss these topics without talking about fairness and bias
in the tech industry.  I was interviewing for a new job as I was writing this
book; some companies' interviewing processes were designed to create a level
playing field, but others were not (and that's putting it politely).  The ways
in which companies get this wrong are reflected in, and contribute to, the ways
in which the things they build sometimes harm society as well as embarrassing
their creators.

It's easy to avoid these mistakes *if* you are willing to look beyond the code
you write. As with so many things, the best place to start is with a little bit
of history.

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
that, like most institutions, their first priority is to perpetuate themselves:
if it wasn't, they probably wouldn't still be around.  In a similar way, the
hiring process at many tech companies isn't designed to find the best
programmers: it's designed to find the people who are most like the people doing
the hiring.  Phrases like "cultural fit" are almost always code for "people like
us"; consciously or not, we are all biased toward those who look like us, talk
like us, dress like us, and make the same pop culture references as us, none of
which has anything to do with actual ability.

One way this shows up in tech hiring is in whiteboard coding questions about
linked lists, dynamic programming, and other topics from second-year classes on
data structures and algorithms. These have little or no bearing on most
programmers' day-to-day work (and by "most" I mean "virtually all") As [Hillel
Wayne][wayne-hillel] discovered when he looked at [the history of these
questions][wayne-linked-lists], they might have indicated how much experience
someone had using C or Pascal in the 1980s, but they became institutionalized in
the way that all hazing does ("I survived so it must be good for you"); all they
really do now is check how much you know about the hiring process..

Tech trivia questions are no more objective than the essay questions used by
Harvard and other Ivy League schools to select the "right" people.  As
<cite>Tiku2021</cite> reported, when [April Christina Curley][curley-april]
began coaching Black students how to prepare for interviews with Google that
included questions like these the company shut her down, even though schools
like Stanford had been running coaching sessions for their students for years.

<cite>Behroozi2019,Behroozi2020a,Behroozi2020b</cite> summarize many other
things that often go wrong in hiring, from interviewers not knowing which job
someone had actually applied for and long delays waiting for feedback to asking
candidates to spend several days working for free on programming assignments.
These are all signs of a dysfunctional company culture, and it's usually safe to
assume that you won't be any happier working there than you were while you were
interviewing.

<div class="callout" markdown="1">

### A sign of privilege

In the first draft of this section I wrote, "If a company does any of the things
described above, you should find somewhere else to work."  One of the early
reviewers wrote, "Gosh, it must be nice to be able to walk away from a job."
They were right: most people don't have the privilege and financial security I
do, so they may have to smile and put up with whatever the company does.

</div>

So how can companies do hiring well?

Write inclusive job ads.
:   <cite>Gaucher2011</cite> is just one of many studies showing that gendered
    wording in job ads reinforces gender inequality in male-dominated
    occupations. [Gender Decoder][gender-decoder] and [GenderMag][gendermag] can
    help you find bugs like this in ads and software
    <cite>Hilderbrand2020</cite>. Tools for finding and eliminating racial bias
    and other problems aren't as common, but <cite>Washington2020</cite> is a
    good starting point for thinking about what to aim for.

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

These principles apply to your school and your courses as well.  Are course
descriptions and course websites inclusive? Are instructors required to use
blinded grading to ensure that personal likes and dislikes don't affect grades?
If the answers are "no", the next questions to ask is, "How can we fix this?"
[Julia Evans][evans-julia] has a good list of [other questions to ask in
interviews][evans-interviews] as well.

## On the Job

Tech trivia questions in interviews are an example of <span
g="preparatory_privilege">preparatory privilege</span>, which is the advantage
someone has in an supposedly objective assessment as a result of growing up
affluent, well-educated, or well-connected.  Ignoring it is like ignoring the
difference between professional athletes who are paid to train all day and
amateurs whose jobs only allow them to train in the evening or on weekends, or
pretending that people doing interviews in their second or third language are on
an equal footing with people who are interviewing in their native language.

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
Similarly, studies show that female students are less likely to be called on in
class and more likely to be given non-coding tasks in team projects than male
students.  If they can get a B despite that, they will probably outperform a
male student who only gets an A with the deck stacked in his favor, provided the
company treats both equally after they are hired.

That last statement is where many companies and universities fail despite good
intentions.  Hiring more people from under-represented groups isn't going to
matter if they have to work twice as hard to be taken half as seriously, if they
are constantly passed over for promotion, or if discussions about who would make
a good department chair continue to take place in the men's locker room after
the department's Friday afternoon hockey game.  The Centre for Community
Organizations has a depressing summary of what it's like to be [the "problem"
woman of color in the workplace][coco-problem]; if what it describes isn't
familiar, you might be a part of the problem, just as I was when I was a
student.

There are no easy fixes to these problems, but there are things companies can
do, and it's fair to ask during an interview if they are:

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

## Why and How to Care

But suppose you are a straight, physically able, white or Asian male without
mental health issues---why should you feel compassion toward people who are
marginalized because they aren't all of these things?  One argument is that
study after study has shown that more diverse teams perform better, that
companies with more diverse management are more profitable, and so on.

Despite the benefits of diversity, research also consistently shows that members
of under-represented groups have less successful careers: as
<cite>Hofstra2020</cite> reports, "…their novel contributions are devalued and
discounted: For example, novel contributions by gender and racial minorities are
taken up by other scholars at lower rates than novel contributions by gender and
racial majorities, and equally impactful contributions of gender and racial
minorities are less likely to result in successful scientific careers than for
majority groups." If this comes as a surprise to you, you might be part of the
problem rather than part of the solution.

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

Another reason to care about these issues is that discussion of fair play stops
being theoretical as soon as we talk about your rights as an employee.  Until
recently there has been a lot less discussion of this in tech than of
intellectual property rights, in part because the people who run companies would
rather talk about who owns what than about the limits to their own power.
High-profile incidents like [Google's decision to fire the AI researcher Timnit
Gebru][gebru-firing] has changed that, as tech workers have belatedly realized
that the industry they have created will treat them just as callously as it
treats everyone else.

Standing up to a bad boss or an unfair professor is easier in theory than in
practice, because the student's evaluation of the professor doesn't affect the
professor nearly as much as the professor's evaluation of the student affects
the student.  This imbalance is why management fads like "radical candor" are
<span g="bullshit">bullshit</span> (in the technical sense of the word): they
brush aside reality in order to avoid having to acknowledge unwelcome truths.

The only way society has found to manage imbalances like these is collective
action: many people with relatively little power coming together and organizing.
However, forty years of sustained disinformation from the rich and powerful have
made many people believe that collectives are intrinsically inefficient or that
they stifle innovation.  (Ironically, the entrepreneurs and CEOs who are most
vocal about the advantages of unrestricted capitalism all organize their
companies along socialist lines <cite>Phillips2019</cite>.)

As an example of what this looks like in practice, consider the difference
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
startups backed by private investors and venture capital.  Choosing those topics
is just as political---it's just more common.

</div>

## Being an Ally

<cite>Dobbin2019</cite> (summarized in <cite>Dobbin2020</cite>) found that most
of what American companies have done over the past twenty years to reduce sexual
harassment and discrimination has either had no effect or has actually made
things worse. The reason is that the people who care don't gain anything from
being told they should, while the people who are part of the problem resent
being told that and tend to take out their anger on the people the training is
meant to protect.

People who are privileged are often not aware of it, as they've lived in a
system that provides unearned advantages their entire lives.  In John Scalzi's
memorable phrase, they've been playing on the lowest difficulty setting there is
their whole lives, and as a result don't realize how much harder things are for
others <cite>Scal2012</cite>.  An <span g="ally">ally</span> is a member of a
privileged group who is working to understand their own privilege and end
oppression.  If we are privileged, we should educate ourselves and call out
peers who are marginalizing others, even if (or especially if) they aren't
conscious of doing it.  As <cite>Lee1962</cite> said, "With great power comes
great responsibility."

## Outside

<span class="fixme">ethics in the context of AI: https://github.com/gvwilson/buildtogether.tech/issues/26</span>

<span class="fixme">lending privilege as a form of allyship https://github.com/gvwilson/buildtogether.tech/issues/70</span>

<span class="fixme">being an active bystander https://github.com/gvwilson/buildtogether.tech/issues/78</span>
