---
---

Which of these do you believe is true?

1.  As a student, you own every piece of software you write for course
    assignments.  If the university wants to use that software in any way other
    than for giving you a grade, they need your permission: you can say "no" or
    ask for payment.

1.  You own the software you write for course assignments *as long as you do
    the work on your own computer*. If you use a university's machines, they
    have an equal right to the software: you can continue developing it or
    sell it if you want, but they can too, and they don't need your permission.

1.  If you are an undergraduate and paying fees to attend a university, you
    own the software you produce. If you are a graduate student being paid a
    stipend, on the other hand, the university owns what you produce.

1.  If you a graduate student then you, your supervisor, and your university
    all have a right to what you produce.

The answer is, "It depends where you are."  Different schools can have very
different rules, even if they are in the same legal jurisdiction (i.e., the same
country, state, or province). In fact, some universities' rules depend not only
on who you are but on which faculty you are in.

The rules in industry are less complex---anything you do on company time or with
company resources belongs to the company---but there are many gray areas. For
example, I wrote some of the first drafts of this book on a company laptop while
traveling for work. Does that mean I owe my former employer a share of the
royalties?

Who owns what is just one of the rights that societies recognize.  Others
guaranteed by the [Universal Declaration of Human Rights][udhr] include the
right to say what you want, the right to live free from fear, and the right to
be treated the same way as everyone else regardless of your race, sex,
orientation, religion, or disability.  Most countries have signed this
declaration, meaning that in theory at least, it has the force of law.

However, the phrase "in theory" in the previous paragraph is doing a lot of
work.  In practice, most societies still treat people unequally and unfairly;
the question is, do we acknowledge that and try to fix it, or ignore it in the
hope that when bad things happen, they'll only happen to other people?  What's
more, all of our rights have been profoundly affected by what software engineers
have built. If the first rule of being compassionate is to do no harm, the first
step in becoming a compassionate programmer is to learn what rights people have
so that you don't violate them.

## Intellectual Property

<span g="intellectual_property">Intellectual property</span> (IP) is a catch-all
term that covers four separate kinds of rights: copyrights, patents, trade
secrets, and trademarks. Each of these has evolved over several centuries to
address the economic and moral concerns of people powerful enough to influence
law-making. What ties them together is that, compared with physical goods,
information is expensive to produce but cheap to copy. IP exists to ensure that
creators can earn enough from producing intangible goods that they can keep
doing it. Each kind of IP therefore gives its holder some kind of limited
monopoly over some kind of information.

<span g="copyright">Copyrights</span> apply to any original expression that
anyone creates. While people can't (yet) own facts, they *can* own any
representation of those facts that contains an element of creativity.  As a
result of this broad scope, there are several exceptions to copyright, making it
the weakest protection available. When placed in the proper context, however,
copyright is a powerful tool for IP protection.

<span g="patent">Patents</span> apply to inventions, technological improvements,
certain designs, business methods, and a few other things. They grant a
monopoly---the right to exclude others from using the patented idea---for a
fixed period of time (usually twenty years).  Since the right is stronger, the
requirements for obtaining a patent are more stringent: it can take years,
hundreds of pages of paperwork, and thousands of dollars to secure one.

Patents are intended to be a bargain between the inventor and the public: the
inventor discloses how the invention works (so that other people can learn from)
and in exchange society ensures that she is the only one who can profit from it
for a reasonable time. If an inventor doesn't want anyone to know how her
invention works she can treat it as a <span g="trade_secret">trade
secret</span>.  This isn't a property right as such, but rather the practice of
relying on things like <span g="non_disclosure_agreement">non-disclosure
agreements</span> to keep something secret. There is less risk of someone being
inspired by your idea to create something better, but if the idea *does* leak,
the inventor has less legal protection.

Finally, <span g="trademark">trademarks</span> allow people to tell whether a
product is authentic or not. Given that everyone has limited time in which to
make decisions, a brand name acts as a form of mental shorthand: if company XYZ
has a reputation for high quality or low prices, or if a particular medication
has been proven to be effective against an ailment like heart disease, the name
itself has commercial value.

## Software Licenses

A <span g="license">license</span> dictates how project materials can be used
and redistributed.  If the license or a publication agreement makes it difficult
for people to contribute, the project is less likely to attract new members, so
the choice of license is crucial to the project's long-term sustainability.

Every creative work has some sort of license; the only question is whether
authors and users know what it is and choose to enforce it.  Choosing a license
for a project can be complex, not least because the law hasn't kept up with
everyday practice.  (<cite>Lindberg2008</cite> is a good exploration of these
issues if you want details.)  Depending on country, institution, and job role,
most creative works are automatically eligible for intellectual property
protection.  However, members of the team may have different levels of copyright
protection.  For example, students and faculty may have a copyright on the
research work they produce, but university staff members may not, since their
employment agreement may state that what they create on the job belongs to their
employer.

To avoid legal messiness, every project should include an explicit license.
This license should be chosen early, since changing a license can be
complicated.  For example, each collaborator may hold copyright on their work
and therefore need to be asked for approval when a license is changed.
Similarly, changing a license does not change it retroactively, so different
users may wind up operating under different licensing structures.

<div class="callout" markdown="1">

### Leave it to the professionals

Don't write your own license.  Legalese is a highly technical language, and
words don't mean what you think they do.  What's more, it's often hard to
understand the interactions between multiple licenses on different kinds of
material <cite>Almeida2017</cite>.

</div>

Just as the project's Code of Conduct is usually placed in a root-level file
called `CONDUCT.md` (<span x="versioning"></span>), its license is usually put
in a file called `LICENSE.md` that is also in the project's root directory.  To
make license selection for code as easy as possible, GitHub allows us to select
one of several common software licenses when creating a repository.
Unfortunately, their list does not include common licenses for data or written
works like papers and reports.

The Open Source Initiative maintains [a list][osi-license-list] of <span
g="open_license">open licenses</span>, and [choosealicense.com][choose-license]
will help us find a license that suits our needs.  In order to choose the right
one, we need to understand the difference between two kinds of license.  The
<span g="mit_license">MIT License</span> and its close sibling the <span
g="bsd_license">BSD License</span> say that people can do whatever they want to
with the software as long as they cite the original source, and that the authors
accept no responsibility if things go wrong.  The <span g="gpl">GNU Public
License</span> (GPL) gives people similar rights, but requires them to share
their own work on the same terms:

> You may copy, distribute and modify the software as long as you track
> changes/dates in source files.  Any modifications to or software including
> (via compiler) GPL-licensed code must also be made available under the GPL
> along with build and install instructions.
>
> --- [tl;dr][tldr-gpl]

In other words, if someone modifies GPL-licensed software or incorporates it
into their own project, and then distributes what they have created, they have
to distribute the source code for their own work as well.

The GPL was created to prevent companies from taking advantage of open software
without contributing anything back.  The last thirty years have shown that this
restriction isn't necessary: many projects have survived and thrived without
this safeguard.  We therefore recommend that projects choose the MIT license, as
it places the fewest restrictions on future action.

<div class="callout" markdown="1">

### First, do no harm

The [Hippocratic License][hippocratic-license] is a newer license that is
quickly becoming popular.  Where the GPL requires people to share their work,
the Hippocratic License requires them to do no harm.  More precisely, it forbids
people from using the software in ways that violate the Universal Declaration of
Human Rights.  We have learned the hard way that software and science can be
mis-used; adopting the Hippocratic License is a small step toward preventing
this.

</div>

## Creative Commons Licenses

The MIT license, the GPL, and the Hippocratic License are intended for use with
software.  When it comes to data and reports, the most widely used family of
licenses are those produced by [Creative Commons][creative-commons].  These have
been written and checked by lawyers and are well understood by the community.

The most liberal option is referred to as <span g="cc0">CC0</span> where the "0"
stands for "zero restrictions".  This puts work in the public domain, i.e.,
allows anyone who wants to use it to do so however they want with no
restrictions.  CC-0 is usually the best choice for data, since it simplifies
aggregate analysis involving datasets from different sources.  It does not
negate the scholarly tradition and requirement of citing sources; it just
doesn't make it a legal requirement.

The next step up from CC-0 is the Creative Commons--Attribution license, usually
referred to as <span g="cc_by">CC-BY</span>. This allows people to do whatever
they want to with the work as long as they cite the original source.  This is
the best license to use for manuscripts: we want people to share them widely but
also want to get credit for our work.

Other Creative Commons licenses incorporate various restrictions, and are
usually referred two using the two-letter abbreviations listed below:

-   ND (no derivative works) prevents people from creating modified versions of
    our work.  Unfortunately, this also inhibits translation and reformatting.

-   SA (share-alike) requires people to share work that incorporates ours on the
    same terms that we used.  Again, it is fine in principle but in practice
    makes aggregation and recombination difficult.

-   NC (no commercial use) does *not* mean that people cannot charge money for
    something that includes our work, though some publishers still try to imply
    that in order to scare people away from open licensing.  Instead, the NC
    clause means that people cannot charge for something that uses our work
    without our explicit permission, which we can give under whatever terms we
    want.

<div class="callout" markdown="1">

### Why be open?

<cite>Hippel2006</cite> reports that 85% of all interesting innovations in all
industries come not from the suppliers but from the users.  The more open work
is, the better able users are to tinker with it and do things that the first
contributors would never have thought of trying.

</div>

## Employment

FIXME: what rights do you have (or what myths can we dispel)?

- Point out that there's a lot less about this on the web because companies
  would much rather talk about who owns what than about workers' rights.

## Fair Play

A few pages in a book like this can't change what you believe is fair or unfair.
What it *can* do, I hope, is get you to start thinking in ways that will lead
you to notice more and care more.

<div class="callout" markdown="1">

### See what I did there?

Take a moment and re-read the preceding paragraph. Did you notice the first time
through that it assumes you *aren't* someone who is routinely on the receiving
end of discriminatory behavior? I wouldn't have spotted that when I was 20 years
old; the handful of women in my classes certainly would have, just as they would
known that they were half as likely to be called on when they raised their hand
in class as I was.

</div>

To start, why should you care? One argument is that study after study has shown
that more diverse teams perform better, that companies with more diverse
management are more profitable, and so on. Note, however, that this finding is
sometimes abused---men who want an excuse to continue to be jerks will talk
about "diversity of thought," meaning, "I should be allowed to ask whether
someone else deserves to be treated as a person or not."

> We can disagree and still love each other unless your disagreement is rooted
> in my oppression and denial of my humanity and right to exist.
>
> --- James Baldwin

Another argument is based on fair play <cite>Rawls1999</cite>.  Imagine that you
get to decide what principles society will follow, but you have to do that
*without* knowing what position in that society you will occupy. If you didn't
know in advance whether you were going to be male, female, or non-binary, for
example, you probably wouldn't design a tech industry that treated people the
way ours does.

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

That last statement is where many companies and universities fail despite
claiming to have good intentions.  Hiring more people from under-represented
groups isn't going to matter if they have to work twice as hard to be taken half
as seriously, if they are constantly passed over for promotion, or if
discussions about who would make a good department chair continue to take place
in the men's locker room after the department's Friday afternoon hockey game.
The Centre for Community Organizations has a depressing summary of what it's
like to be [the "problem" woman of color in the workplace](coco-problem); if
what it describes isn't familiar, you might be a part of the problem, just as I
was when I was a student.

<div class="callout" markdown="1">

## Cookies

You're due to have a meeting with someone.  There's a box with half a dozen
cookies in the room, so you help yourself to a couple before the other person
shows up. When they do, you have to make a choice: do you say, "I've already had
two, so I should only have one more and you should get three?"  or, "There were
four cookies in the box when you arrived, so we get two each" (meaning that you
will have had four in total). Most people would say that the first answer is the
moral one; in my experience, people who don't aren't people you'd want on your
team.

</div>

## Next Steps

<cite>Dobbin2019</cite> (summarized in <cite>Dobbin2020</cite>) found that most
of what American companies have done over the past twenty years to reduce sexual
harassment and discrimination has either had no effect or has actually made
things worse. The reason is that the people who care don't gain anything from
being told they should, while the people who are part of the problem resent
being told that and tend to take out their anger on the people the training is
meant to protect.

A bit of terminology can help here.  <span g="privilege">Privilege</span> is an
unearned advantage given to some people but not all, while <span
g="oppression">oppression</span> is systemic inequality that benefits the
privileged and harms those without privilege <cite>Aurora2018</cite>.  In
Europe, the Americas, Australia, and New Zealand, a straight, white, affluent,
physically able male is less likely to be interrupted when speaking, more likely
to be called on in class, and more likely to get a job interview based on an
identical CV than someone who is outside these categories.  People who are
privileged are often not aware of it, as they've lived in a system that provides
unearned advantages their entire lives.  In John Scalzi's memorable phrase,
they've been playing on the lowest difficulty setting there is their whole
lives, and as a result don't realize how much harder things are for others
<cite>Scal2012</cite>.

The targets of oppression are often called "members of a marginalized group,"
but targets don't choose to be members, or to be marginalized: people with
privilege marginalize them.  Finally, an <span g="ally">ally</span> is a member
of a privileged group who is working to understand their own privilege and end
oppression.  If we are privileged, we should educate ourselves and call out
peers who are marginalizing others, even if (or especially if) they aren't
conscious of doing it.  As <cite>Lee1962</cite> said, "With great power comes
great responsibility."

FIXME:

- Cheryan2009
- Ford2016
- May2019
- Patitsas2016
- Washington2020
- Gaucher2011
- https://www.schneier.com/blog/archives/2021/03/national-security-risks-of-late-stage-capitalism.html
- https://www.askamanager.org/
- https://newrepublic.com/article/117088/silicons-valleys-brutal-ageism
- https://www.usatoday.com/story/tech/2014/10/12/silicon-valley-diversity-tech-hiring-computer-science-graduates-african-american-hispanic/14684211/

## Ten Simple Rules for Being Fired

These rules are based on [my experience with DataCamp][buzzfeed-datacamp] and on
the experiences of friends and colleagues there and at other companies.

1. Insist on a record of all conversations.
:   The biggest mistake you can make is to assume good faith on the part of
    those who fired you.  In most jurisdictions you have a right to record any
    phone calls you are part of, and if that feels too confrontational, insist
    on communicating by email.  If they insist on communicating by phone or
    video call, follow up immediately with an email summary and make sure you
    send a copy to your personal account.

2. Pause before speaking, posting, or tweeting.
:   If possible, have someone you trust look everything over before you say it
    or send it.  (Don't use someone who still works for the company, even if
    they are your closest friend: it puts them in a legally and morally
    difficult position.)

3. Keep your public statements brief.
:   People may care, but most won't care as much as you do.  A simple recitation
    of facts is usually damning enough.

4. If you want to correct something online, add a timestamped amendment.
:   Don't just take it down or edit it: if you do, you will be accused of
    rewriting history, and muddied waters only help whoever fired you.  Also, be
    prepared for them to dig through everything you've ever said online and
    re-post parts selectively to discredit you.

5. Speak directly to all the issues rather than omitting or ignoring things you'd rather not discuss.
:   Your honesty is your greatest asset, and it's hypocritical to criticize your
    opponents for spin or selective reporting if you're doing it too,

6. Don't sign any agreement that might prevent you from speaking about moral or legal concerns,
:   or make sure the agreement explicitly excludes your concerns before signing
    it.  (And yes, it's very privileged of me to be able to say this: someone
    whose immigration status, essential health benefits, or family income is
    being threatened may not have a choice.  That is why I think people who do
    have a choice also have an obligation to fight.)

7. Don't cite the law unless a lawyer tells you to.
:   The law probably doesn't mean what you think it means, and they almost
    certainly do have lawyers on their side who will seize on any misstatement
    or mistake you make.

8. Don't try to get them to acknowledge that they were wrong.
:   Whatever happened probably wouldn't have if they were the sort of people who
    could do that.

9. Go for long walks.
:   Or cook some healthy meals, or pick up the guitar you haven't touched in
    years---anything that requires you to focus on something else for a while.
    This isn't just for your mental health: exhausted people make poor
    decisions, and you need to be at the top of your game.

10. Remember that it's OK to cry.
:   And that other people do care about you.

## Ten Simple Rules for Changing the World

> One reason people insist that you use the proper channels to change things is
> because they have control of the proper channels and they're confident it
> won't work.
>
> - [Jon Stone][stone-quote]

1. Be sure this is where you want to focus your efforts.
:   It's going to take years, it could well fail, and there are many other
    things you could do, so be sure this particular change is the one you want
    to fight for.

2. Ask those who will be affected.
:   *Nihil pro nobis sine nobis* (nothing for us, without us) is always a good
    motto, and asking for opinions often reveals potential allies.

3. Be specific.
:   Few people would argue in public against fair hiring practices, but the
    organization has to implement something specific in order for that to mean
    anything, and people very well might argue against those specifics.  You
    should therefore pick something specific and achievable and make a concrete
    plan for achieving it.  And start with whatever is likely to have broadest
    support, because success breeds success.

4. Figure out who has the power to make that change and what they care about.
:   Your neighbors don't make policy for your local public school: school board
    trustees do, so that's who you need to influence.  Help someone who wants
    the same change as you get elected, or help someone who doesn't oppose your
    change with something they care about in exchange for support for your
    cause, but whatever you do, do it for the people whose vote counts.
    Conversely, figure out who is going to be negatively impacted by the change
    you want and what you can do to help them: for example, if it's going to
    eliminate jobs, what else can those people usefully do?

5. Build alliances,
:   "I'll help you if you'll help me" makes the world go around.  It's hard when
    people want the same thing for very different reasons, but this rule is
    *not* cynical: people whose beliefs are aligned may still have different
    priorities.  (The flip side of this rule is to accept that some people will
    never be your allies: if everyone wanted it, you wouldn't have to push for
    the change.)  People who want the same thing you do, who have a high profile
    (either inside your group or externally), or who have a wide range of
    connections are all useful allies.

6. Test the waters.
:   At every stage, refine your idea and presentation in front of a small group
    first.  But remember: when done honestly, refining your idea sometimes means
    accepting that you wanted the wrong thing.  And note that it can be useful
    to ask someone to be the official skeptic: giving them a way to critique in
    private may temper their public criticism, and you just might convert them.

7. Keep it visible.
    It's easy to start a blog and create a Twitter account, but that very ease
    has reduced these channels' impact.  Is there a newsletter you can be
    included in (which makes you look more official)?  Can you make a
    presentation as part of some other event (rather than organizing a gathering
    of your own)?  Can you get someone with a higher profile to mention what
    you're doing and point people your way?  Can you post notices in the
    lunchroom? The elevator? The washrooms? Local restaurants?  And always share
    a single point of contact that someone actually checks (frequently).

8. Collect data but tell stories.
:   Sooner or later someone is going to ask what financial impact this change is
    going to have, so be ready for that.  Data about other changes or from other
    organizations helps a lot, but data doesn't have nearly as powerful an
    impact as stories.  Don't explain what *kind* of people this will help:
    explain how it helped a specific person, or how it would make a specific
    person's life better.  And if you've never cried when telling that story,
    tell a better story.

9. Learn how to run meetings and make decisions.
:   You can get the change you want without being a great public speaker, but
    you *must* know how to run a meeting and make decisions <span
    x="important"></span>.

10. Celebrate when you can, grieve when you need to.
:   [Burnout][thirdbit-burnout] is an occupational hazard for everyone trying to
    make meaningful change, in part because we get so used to doing things on
    our own at the start that we don't share the load even when there are people
    to share it with.  Not all of your allies will become your friends, but
    those who do will be able to share your victories and commiserate with your
    defeats like no one else.
