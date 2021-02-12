---
---

## Including Everyone

FIXME: allyship from a legal and moral standpoint

## Licensing

A license dictates how project materials can be used and redistributed.  If the
license or a publication agreement makes it difficult for people to contribute,
the project is less likely to attract new members, so the choice of license is
crucial to the project's long-term sustainability.

<div class="callout" markdown="1">

### Open except…

Projects that are only developing software may not have any problem making
everything open.  Teams working with sensitive data, on the other hand, must
be careful to ensure that what should be private isn't inadvertently shared. 
In particular, people who are new to Git (and even people who aren't)
occasionally add raw data files containing personal identifying information to
repositories.  It's possible to rewrite the project's history to remove things
when this happens, but that doesn't automatically erase copies people may have
in forked repositories.

</div>

Every creative work has some sort of license; the only question is whether
authors and users know what it is and choose to enforce it.  Choosing a license
for a project can be complex, not least because the law hasn't kept up with
everyday practice.  FIXME lightweight intro while <cite>Lindberg2008</cite> is a
deeper dive for those who want details.  Depending on country, institution, and
job role, most creative works are automatically eligible for intellectual
property protection.  However, members of the team may have different levels of
copyright protection.  For example, students and faculty may have a copyright on
the research work they produce, but university staff members may not, since
their employment agreement may state that what they create on the job belongs to
their employer.

To avoid legal messiness, every project should include an explicit license.
This license should be chosen early, since changing a license can be
complicated.  For example, each collaborator may hold copyright on their work
and therefore need to be asked for approval when a license is changed.
Similarly, changing a license does not change it retroactively, so different
users may wind up operating under different licensing structures.

<div class="callout" markdown="1">

### Leave it to the professionals

Don't write your own license.  Legalese is a highly technical language, and
words don't mean what you think they do.

</div>

To make license selection for code as easy as possible, GitHub allows us to
select one of several common software licenses when creating a repository.  The
Open Source Initiative maintains [a list][osi-license-list] of <span
g="open_license">open licenses</span>, and [choosealicense.com][choose-license]
will help us find a license that suits our needs.  Some of the things we need to
think about are:

1.  Do we want to license the work at all?

1.  Is the content we are licensing source code?

1.  Do we require people distributing derivative works to also distribute their code?

1.  Do we want to address patent rights?

1.  Is our license compatible with the licenses of the software we depend on?

1.  Do our institutions have any policies that may overrule our choices?

1.  Are there any copyright experts within our institution who can assist us?

Unfortunately, GitHub's list does not include common licenses for data or
written works like papers and reports.  Those can be added in manually, but it's
often hard to understand the interactions between multiple licenses on different
kinds of material <cite>Almeida2017</cite>.

Just as the project's Code of Conduct is usually placed in a root-level file
called `CONDUCT.md`, its license is usually put in a file called `LICENSE.md`
that is also in the project's root directory.

### Software

In order to choose the right license for our software, we need to understand the
difference between two kinds of license.  The <span g="mit_license">MIT
License</span> and its close sibling the <span g="bsd_license">BSD
License</span> say that people can do whatever they want to with the software as
long as they cite the original source, and that the authors accept no
responsibility if things go wrong.  The <span g="gpl">GNU Public License</span>
(GPL) gives people similar rights, but requires them to share their own work on
the same terms:

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
people from using the software in ways that violate the [Universal Declaration
of Human Rights][udhr].  We have learned the hard way that software and science
can be mis-used; adopting the Hippocratic License is a small step toward
preventing this.

</div>

### Data and reports

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

- ND (no derivative works) prevents people from creating modified versions of
    our work.  Unfortunately, this also inhibits translation and reformatting.

- SA (share-alike) requires people to share work that incorporates ours on the
    same terms that we used.  Again, it is fine in principle but in practice
    makes aggregation and recombination difficult.

- NC (no commercial use) does *not* mean that people cannot charge money for
    something that includes our work, though some publishers still try to imply
    that in order to scare people away from open licensing.  Instead, the NC
    clause means that people cannot charge for something that uses our work
    without our explicit permission, which we can give under whatever terms we
    want.

## Intellectual Property

I asked:

1. Who has what rights to the software that undergrad students produce for courses at your institution? (I'm asking it this way instead of asking "who owns it?" because it appears that at some institutions, both the student and the school have some rights.)

2. What about software that grad students produce during their research?

3. Where and how did you find this out and how sure are you of your answers?

Prof. Joanne Atlee (University of Waterloo)

That's easy.  At Waterloo, the inventor is the owner (unless work is done by an
employee as an "assigned task" in the course of administrative activities). And
the university has a free, non-exclusive, and irrevocable license to copy and
use the work in support of teaching and research activities (but not to
commercialize or distribute outside of the university community).

This applies to

1.  software that undergraduates write
2.  research/software produced by graduate students during their research
3.  Policy 73.  I am very confident in my answers.  I teach this material to CS students.
    https://uwaterloo.ca/secretariat/policies-procedures-guidelines/policies/policy-73-intellectual-property-rights

Prof. Kelly Blincoe (University of Auckland)

Students at the University of Auckland maintain their own IP unless they
specifically sign it over.

We have an IP document which explains things in legal jargon:
https://www.auckland.ac.nz/en/about/the-university/how-university-works/policy-and-administration/research/conduct/intellectual-property-created-by-staff-and-students-policy.html

I became aware of this because of my involvement in a course that has
undergraduate students work with industry partners. Unless the industry partner
negotiates an IP agreement, then the students maintain ownership over the
products they produce. Though, the industry partners maintain ownership of the
IP that they bring as well, so typically there is a joint ownership.

Prof. Davide Fucci (Blekinge Technical College)

I have asked around, and the short answer to Q1 and Q2  is "the student, unless otherwise stated."

Prof. Reid Holmes (University of British Columbia)

Grad students and faculty have joint ownership of their inventions.  Undergrads
own their solutions, but many courses add course licenses to prevent them from
posting their solutions online as they are often to larger projects that persist
between terms. I'll admit to doing this myself
<https://github.com/ubccpsc/310/tree/2018sept#license>

> The readings for this course are licensed using CC-by-SA. However, it is
> important to note that the deliverable descriptions, code implementing the
> deliverables, exams, and exam solutions are considered private materials. We
> go to considerable lengths to make the project an interesting and useful
> learning experience for this course. This is a great deal of work, and while
> future students may be tempted by your solutions, posting them does not do
> them any real favours. Please be considerate with these private materials and
> not pass them along to others, make your repos public, or post them to other
> sites online.

This is an awkward space, but in my course none of the implementations are
really original materials so it isn't like anyone could claim them as novel IP
anyways.

For courses that have open-ended projects though students own their IP and are
encouraged to continue them after the course is over / publish them as they
desire.

The university IP office has pretty robust materials for these things
<https://uilo.ubc.ca/researchers/commercialize-invention/inventions-inventorship-faq/ownership-inventions-ubc>.

Prof. Andreas Stefik (University of Nevada Las Vegas)

1.  At UNLV, it's the students.

2.  This depends on how they were funded. Federal law in the U.S. has different
    rules for different things. For example, if it's done under an NSF grant,
    the university claims they own it, although my understanding is this gets
    tricky. States have rules too, which are also tricky. If they are funding
    themselves, they own it all.

3.  Been talking to our commercialization office... I'm pretty sure and have
    looked at the actual laws/policies myself.

Prof. Igor Steinmacher (Universidade Tecnológica Federal do Paraná)

1.  Here it is like this, institution and school have rights. The supervisor can
    also have a share and, if a company is involved, an agreement needs to be
    made up front.  Usually, when no company is involved, we have a 1/3 each
    division.

2.  Again, depends. On grad school this is usually ruled by an agreement among
    all parties involved. It may be the case in which a company will hold the
    rights; the most common is having shares including student, institution,
    supervisor and company.

3.  We have a department responsible for this relationship with companies and IP.

Prof. Christoph Treude (University of Adelaide)

This depends on whether there was any agreement signed with the industry partner
that grants the industry partner rights over the student-created IP. If there
is, we would need to look at the terms of that agreement.
 
It also depends on whether there was any co-authoring of the code by the
industry partner, in which case the industry partner may have rights as a joint
owner.
 
If the students wrote the code themselves and if there is no any agreement with
the industry partner, students own the IP that they create and are free to
choose how they deal with the source code. If the students would like to pursue
commercial opportunities for the IP, they can (but, unlike staff, are under no
obligation to) contact Adelaide Enterprise. If they are happy to release it open
source, that is up to them.

Prof. Bogdan Vasilescu (Carnegie-Mellon University)

<https://www.cmu.edu/policies/administrative-and-governance/intellectual-property.html>

## Employment

FIXME: what rights do you have (or what myths can we dispel)?

## Ten Simple Rules for Being Fired

These rules are based on [my experience with DataCamp][thirdbit-datacamp] and on
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
