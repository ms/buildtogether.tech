---
---

This book is about team projects, but as <span x="starting"/> said, these are
supposed to simulate real jobs, and often have industry partners or overlap with
internships and co-ops.  This chapter therefore looks at what many tech
companies do wrong and what others do right.

## What's Wrong

<span class="fixme">cite Behroozi 2019 and Behroozi2020</span>

<span class="fixme">forward ref to <span x="hiring"/></span>

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
programmers' day-to-day work (and by "most" I mean "virtually all").  As
[Hillel Wayne][wayne-hillel] discovered when he looked at [the history of these
questions][wayne-linked-lists], they might have indicated how much experience
someone had using C or Pascal in the 1980s, but they became institutionalized in
the way that all hazing does ("I survived so it must be good for you").

Tech trivia questions like these are no more objective than the essay questions
used by Harvard and other Ivy League schools to select the "right" people.  As
<cite>Tiku2021</cite> reported, when [April Christina Curley][curley-april]
began coaching Black students how to prepare for interviews with Google that
included questions like these the company shut her down, even though schools
like Stanford had been running coaching sessions for their students for years.

This is an example of <span g="preparatory_privilege">preparatory
privilege</span>: the advantage someone has in an supposedly objective
assessment as a result of growing up affluent, well-educated, or well-connected.
Ignoring it is like ignoring the difference between professional athletes who
are paid to train all day and amateurs whose jobs only allow them to train in
the evening or on weekends.

<div class="callout" markdown="1">

### Myers-Briggs and other danger signs

The <span g="myers_briggs" i="Myers-Briggs Type Indicator;
pseudoscience!Myers-Briggs Type Indicator">Myers-Briggs Type Indicator</span>
(MBTI) advertises itself as personality profiling tool.  It is popular on dating
sites and some companies use it as part of their interview process---despite the
fact that it is complete bullshit.  Half or more of people who repeat the test
within a few weeks get a different personality classification, it fails to
predict job performance, and its categories are based on outdated (and very
Western-centric) psychological theories.  If a potential employer asks you to do
it as part of the interview process, ask them if they would like a horoscope as
well.

Myers-Briggs has given the whole notion of personality profiling a bad
reputation, but there *are* models of personality that have a scientific basis
and are repeatable and cross-cultural.  For example, the <span
g="ocean_model">OCEAN model</span> has five dimensions: Openness to experience,
Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Studies of
twins and other research has found that about half of personality variation
comes from genetics and about half from environment, and work like
<cite>Hannay2010</cite> has used this model in studies of programmers.

</div>

<div class="callout" markdown="1">

### A sign of privilege

In the first draft of this section I wrote, "If a company does any of the things
described above, you should consider finding somewhere else to work."  One of
the early reviewers wrote, "Gosh, it must be nice to be able to walk away."
They were right: most people don't have the privilege and financial security I
do, so they have to smile and put up with whatever the company does.

</div>

## Fair Play

<span class="fixme">Cite Nafus2011</span>

You're due to have a meeting with someone.  There's a box with half a dozen
cookies in the room, so you help yourself to a couple before the other person
shows up. When they do, you have to make a choice: do you say, "I've already had
two, so I should only have one more and you should get three?"  or, "There were
four cookies in the box when you arrived, so we get two each" (meaning that you
will have had four in total). Most people would say that the first answer is the
moral one; in my experience, people who don't aren't people you'd want on your
team.

A few pages in a book like this can't change what you believe is fair or unfair.
What it *can* do, I hope, is get you to start thinking in ways that will lead
you to notice more and care more so that you will use the advantages you have as
an accident of birth for the greater good.

<div class="callout" markdown="1">

### See what I did there?

Take a moment and re-read the preceding paragraph. It assumes you *aren't*
someone who is routinely on the receiving end of discriminatory behavior.  I
wouldn't have spotted that when I was 20 years old; the handful of women in my
classes certainly would have, just as they would known that they were half as
likely to be called on when they raised their hand in class as I was.

</div>

To start, why should you care? One argument is that study after study has shown
that more diverse teams perform better, that companies with more diverse
management are more profitable, and so on. (This finding is sometimes
abused---men who want an excuse to continue to be jerks try to be clever with
words and talk about "diversity of thought," meaning, "I should be allowed to be
offensive as long as I don't raise my voice.")

<blockquote markdown="1">

We can disagree and still love each other unless your disagreement is rooted
in my oppression and denial of my humanity and right to exist.

--- James Baldwin

</blockquote>

Despite the benefits of diversity, research also consistently shows that members
of underrepresented groups have less successful careers: as
<cite>Hofstra2020</cite> reports, "…their novel contributions are devalued and
discounted: For example, novel contributions by gender and racial minorities are
taken up by other scholars at lower rates than novel contributions by gender and
racial majorities, and equally impactful contributions of gender and racial
minorities are less likely to result in successful scientific careers than for
majority groups." If this comes as a surprise to you, you might be part of the
problem rather than part of the solution.

Another argument for fair play is based on a "veil of ignorance"
<cite>Rawls1999</cite>.  Imagine that you get to decide what principles society
will follow, but you have to do that *without* knowing what position in that
society you will occupy. If you didn't know in advance whether you were going to
be male, female, or non-binary, for example, you probably wouldn't design a tech
industry that treated people the way ours does.

Many people object to taking race or gender into account in hiring, saying that
companies should pick whoever is the best candidate on the day. But suppose I
can run a mile in five minutes, while you can do it in six minutes with a
fifty-pound pack on your back.  You are probably the better athlete, and will
probably do better *if the pack is removed*. Similarly, someone who can get a B
despite being systematically overlooked or underestimated will probably do
better in a job than someone who only got an A despite all the advantages that
come from being straight, white or Asian, male, physically able, and
economically secure---if, and only if, they are treated fairly after being
hired.

<span class="fixme">https://github.com/gvwilson/buildtogether.tech/issues/76</span>

That last statement is where many companies and universities fail despite
claiming to have good intentions.  Hiring more people from under-represented
groups isn't going to matter if they have to work twice as hard to be taken half
as seriously, if they are constantly passed over for promotion, or if
discussions about who would make a good department chair continue to take place
in the men's locker room after the department's Friday afternoon hockey game.
The Centre for Community Organizations has a depressing summary of what it's
like to be [the "problem" woman of color in the workplace][coco-problem]; if
what it describes isn't familiar, you might be a part of the problem, just as I
was when I was a student.

As another example, <cite>Dobbin2019</cite> (summarized in
<cite>Dobbin2020</cite>) found that most of what American companies have done
over the past twenty years to reduce sexual harassment and discrimination has
either had no effect or has actually made things worse. The reason is that the
people who care don't gain anything from being told they should, while the
people who are part of the problem resent being told that and tend to take out
their anger on the people the training is meant to protect.

## Leveling the Playing Field

Discussion of fair play stops being theoretical as soon as we talk about your
rights as an employee.  Until recently there has been a lot less discussion of
this than of intellectual property rights, in part because the people who run
companies would rather talk about who owns what than about the limits to their
own power.  High-profile incidents like [Google's decision to fire the AI
researcher Timnit Gebru][gebru-firing] has changed that, as tech workers have
belatedly realized that the industry they have been instrumental in creating
will treat them just as callously as it treats everyone else.

Your rights as an employee may not be immediately relevant to you as a student
doing a project course, but those courses are often tied to, or meant to lead
to, internships and co-op placements.  A bit of terminology can help you find
your way.

<span g="privilege">Privilege</span> is an unearned advantage given to some
people but not all, while <span g="oppression">oppression</span> is systemic
inequality that benefits the privileged and harms those without privilege
<cite>Aurora2018</cite>.  In Europe, the Americas, Australia, and New Zealand, a
straight, white, affluent, physically able male is less likely to be interrupted
when speaking, more likely to be called on in class, and more likely to get a
job interview based on an identical CV than someone who is outside these
categories.  People who are privileged are often not aware of it, as they've
lived in a system that provides unearned advantages their entire lives.  In John
Scalzi's memorable phrase, they've been playing on the lowest difficulty setting
there is their whole lives, and as a result don't realize how much harder things
are for others <cite>Scal2012</cite>.

The targets of oppression are often called "members of a marginalized group,"
but targets don't choose to be members, or to be marginalized: people with
privilege marginalize them.  Finally, an <span g="ally">ally</span> is a member
of a privileged group who is working to understand their own privilege and end
oppression.  If we are privileged, we should educate ourselves and call out
peers who are marginalizing others, even if (or especially if) they aren't
conscious of doing it.  As <cite>Lee1962</cite> said, "With great power comes
great responsibility."

So here are a few things companies can do to level the playing field during the
hiring process. *Every well-run company knows about these practices.* If they
don't do most or all of these things when they interview you, you should regard
them the same way you'd regard a programming team that didn't use version
control.

Write inclusive job ads.
:   <cite>Gaucher2011</cite> is just one of many studies showing that gendered
    wording in job ads reinforces gender inequality in male-dominated
    occupations. [Gender Decoder][gender-decoder] and [GenderMag][gendermag]
    can help you find bugs like this in ads and software. Tools for finding
    and eliminating racial bias and other problems aren't as common, but
    <cite>Washington2020</cite> is a good starting point for thinking about
    what to aim for.

Post a public description of the hiring process.
:   [Automattic's description][automattic-hiring] is a good model: it lays out
    what's going to happen in what order, how much time is expected, and the
    principles everything is based on.

Use blinded screening.
:   Everyone has unconscious biases, and many of the rules scientists follow
    when running experiments are designed to prevent them contaminating results
    (<span x="research"/>).  The same is true of hiring, and so is the
    solution. For example, my first-round interview with Automattic was done by
    text over Slack so that my appearance, my accent, or the fact that I
    sometimes need a couple of moments to collect my thoughts wouldn't bias the
    interviewer. Similarly, companies should redact things like a candidate's
    age, race, and gender when evaluating resumes.

Use diverse interview panels.
:   People tend to be biased toward hiring people who are like them; Silicon
    Valley calls this "cultural fit" rather than "discrimination", but they are
    functionally indistinguishable. Giving people from under-represented
    backgrounds a say in who's hired next gives other people with similar
    backgrounds a better chance of being treated fairly.

Have an org chart.
:   A company probably won't share this with you until you're hired, but you
    should ask whether they have one. As we said in <span x="important"/>,
    everyone organization has a power structure: the only question is whether
    it's public and accountable, or whether the organization runs on who you
    know and how willing people are to barge in on strangers.

Have written criteria for performance reviews.
:   The ones shown in <span x="evaluation"/> are a good model, and these
    *are* something a company can share before hiring you. If a company doesn't
    have criteria, or if performance reviews are only done when an employee asks
    for one, the system is once again biased toward the extroverted and the
    well-connected.

These principles apply to your school and your courses as well.  Are course
descriptions and course websites inclusive? Are instructors required to use
blinded grading to ensure that personal likes and dislikes don't affect grades?
How easily can you find out where to go for help, and does anyone act on the
feedback you give in course evaluations?


<span class="fixme">ethics in the context of AI: https://github.com/gvwilson/buildtogether.tech/issues/26</span>

<span class="fixme">diversity and inclusivity data https://github.com/gvwilson/buildtogether.tech/issues/5</span>

<span class="fixme">power dynamics https://github.com/gvwilson/buildtogether.tech/issues/24</span>

<span class="fixme">how to tell if fairness has been achieved (opportunity or outcome?) https://github.com/gvwilson/buildtogether.tech/issues/61 - refer back to product management and the build trap</span>

<span class="fixme">lending privilege as a form of allyship https://github.com/gvwilson/buildtogether.tech/issues/70</span>

<span class="fixme">being an active bystander https://github.com/gvwilson/buildtogether.tech/issues/78</span>

<span class="fixme">build a good enough system with imperfect people https://github.com/gvwilson/buildtogether.tech/issues/79</span>

<span class="fixme">lack of inclusive culture https://github.com/gvwilson/buildtogether.tech/issues/72</span>
