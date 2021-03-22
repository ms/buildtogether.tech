---
---

*Part of this material is adapted from <cite>Smalls2021</cite>.*

We can't rely on companies, universities, and other institutions to protect us
from online threats, for the simple reason that they are not penalized if they
don't.  Much of what institutions force us to go through is <span
g="security_theater">security theater</span> intended to make us believe
something is being done rather than to actually make us safer.  For example,
forcing people to change passwords every three months encourages people to
choose memorable (and therefore easy-to-guess) passwords.

What we *can* do, as programmers, it try to make our software less vulnerable to
attack.  Hundreds of guides to doing this have been written, but in my opinion,
the best place to start is to think about the threats people face and then ask
whether the software you're building is preventing these or making them worse.

## Threat Models

The first step is to realize that digital security is rarely the weakest link.
Most attacks take place offline, and that the most effective ones are often the
simplest. At an airport several years ago, one author heard a professor of
computer science try to reset an online account over the phone. In just a couple
of minutes, they had inadvertently told everyone in the lounge their full name,
their date of birth, the three-digit verification code on the back of their
credit card, and what was almost certainly their mother's maiden name.

<span g="social_engineering">Social engineering</span> is far more common than
hacking: in practice it is far easier to trick someone into giving you their
password than to break into their devices digitally.  The key practice is to pay
attention to what's happening and respond accordingly.  The corollary is to
de-escalate when you can: being on guard all the time is exhausting

Edward Snowden and the journalists who worked with him took extraordinary
measures to safeguard themselves against state-level actors
<cite>Snowden2019</cite>, but most of us aren't involved in issues of national
security and don't need to take those kinds of precautions.  Instead, we
typically face one of three kinds of threat:

-   <span g="casual_threat">Casual threats</span> are opportunistic. For example,
    Monica, a professor, is targeted by Mohan, an undergraduate who spends hours
    every day in online echo chambers complaining about how "SJW bullshit" is
    ruining tech. He thinks it would be a laugh to make her the target of
    anonymous abuse online; he is unlikely to invest significant effort in his
    attack, but his attack may be backed up by more knowledgeable members of
    online forums.

-   <span g="intimate_threat">Intimate threats</span> come from people who know
    their targets' passwords or have a chance to install spyware on their
    targets' devices <cite>Leitao2019</cite>. For example, Elena has ended an
    abusive relationship and is rebuilding her life; her ex, Eric, is obsessed
    with the idea that she left him for someone else and is now stalking her.

-   <span g="insider_threat">Insider threats</span> come from people who have
    legitimate access to accounts and devices. For example, Boris, a professor,
    may have agreed to serve as an expert witness in an upcoming lawsuit;
    Bethany, a sys admin in his department, has been asked by a former colleague
    to find out what he is going to say in order to discredit his testimony.

## Authentication

Using a weak password is a good way to ensure that your account will eventually
be compromised, in part because <span g="dictionary_attack">dictionary
attacks</span> can be run offline against encrypted password files to find
passwords that match common patterns. Using a clever password scheme, such as
the name of the site plus a word only you know, does not increase security by
much: whatever scheme you have thought of, attackers have seen before.  And
since people are often identified on multiple sites by the same email address,
as soon as one site where you've used that scheme is compromised, attackers can
guess the scheme and use it elsewhere.

Reusing passwords ensures that damage spreads, so using a different password for
each site helps limit harm if any are compromised. However, strong passwords are
hard to remember and to type, so always use a password manager that generates
strong passwords and saves them all under a master passphrase. Your passphrase
should be several words long and something you are unlikely to forget. It does
create a single point of attack, but is still safer than choosing passwords
yourself, since password managers aren't fooled by similar-seeming sites like
paypaI.com.

<div class="callout" markdown="1">

### I know how to do that

Writing passwords down and keeping them in your wallet is not necessarily a bad
practice---it depends on who is doing it. For example, an elderly person who
finds tech confusing might well choose simple, easy-to-guess passwords for their
accounts if they have to be remembered. On the other hand, they have a lifetime
of practice keeping track of bits of paper, and will probably notice if their
purse or wallet is stolen.

</div>

Authentication relies on something you know (like a password), something you
have (like a security key), or something you are (like your fingerprints).
<span g="2fa">Two-factor authentication</span> (2FA) requires two of these
together to establish your identity, e.g., a password (which can be stolen
electronically) plus a random code generated by an app on your phone (which
means attackers need access to you).

2FA is as important to security as using a password manager, but where possible,
you should rely on an app for 2FA instead of using text messages. What you
should *never* do is share a confirmation code, since a common attack is to
trigger a password reset and then call the victim pretending to be from the IT
department and ask them to read the code back to "verify" your account. As soon
as you do this, the attacker can change your password and get into your account.

Many security experts now recommend using a physical 2FA key such as a YubiKey,
which fits on a keychain and plugs into a standard USB port.  Sites like [Tech
Solidarity][tech-solidarity] have easy-to-follow instructions explaining how to
set them up for a range of popular social networking sites.

## Don't Open That

Much of the software we use was designed in more innocent times, and since
companies are almost never held liable for the damage caused by their software,
they have consistently prioritized convenience for the many over harm to the
few. One common example is documents that contain macros that automatically
execute when the document is opened. Used for good, a macro can check that an
address field has been filled in correctly. Used for evil, it can email everyone
in your address book, or send a copy of those addresses to anyone in the world.
Microsoft Word and Excel are particularly notorious for this vulnerability, but
many other kinds of documents have the same flaw.

Attempts to get you to open an email attachment, click on a link, install
software, or log into a website are called <span g="phishing">phishing</span>
attacks.  The strongest defense is to never do these things, but in the modern
world that would make most work impossible. The second-best defense is to take
sensible precautions. If you are able, invest in virus scanning software to scan
email attachments before you download them. While many email clients have virus
scanning technology built-in, this will offer an extra layer of protection.

Similarly, don't click links in emails without checking them first: instead,
hover over the link and see if it matches the site it claims to
be. Alternatively, log into the site manually rather than following the provided
link. It takes more time, but is still faster than fixing your credit
rating. And when you go to a web site, check the real domain name in the URL:
paypaI.com with an upper-case "I" instead of a lower-case "l" is not the site it
pretends to be, and `wwwpaypal.com` is a different domain than `www.paypal.com`.

<div class="callout" markdown="1">

### Trained to do the wrong thing

Many sites send an email with a random URL to confirm your identity when you are
resetting your password. On the one hand, this means that an attacker has to get
access to your email in order to break into your account. On the other hand,
random URLs are hard to type in, so these emails encourage us to click on links
in emails. If you are not expecting a password reset email, don't click on the
link.  And if your bank sends you a secure message as an encrypted HTML
attachment that you're supposed to download and double-click (as mine once did),
it's probably time to look for a new bank.

</div>

While phishing attacks are wide-ranging, <span
g="spearphishing">spearphishing</span> uses data harvested from previous victims
to attack specific targets.  Here, the best defense is to very suspicious
emails, e.g., by phoning people to confirm their identity. It's particularly
important to do this when you are sent things like password reset instructions.
Many IT departments send out messages that are indistinguishable from
spearphishing attacks, which just trains people to be victims.

## Delete Before Discarding

Moving files into the trash and then emptying it does not actually erase the
data: it just tells the computer that the space is available for reuse. (This is
why reporters and private investigators regularly go dumpster diving.) The best
way to address this problem is to encrypt your hard drive, which is a quick
setup option for all major operating systems these days.

Even with that, you should act as if any device you throw away is going to fall
into unfriendly hands. Use a secure deletion tool like [BleachBit][bleachbit]
(for Linux or Windows) or [FileShredder][fileshredder] (for MacOS) before
selling, recycling, or discarding your hardware, but keep in mind that this
doesn't affect backups or files stored online on sites like Dropbox. And keep in
mind that it is practically impossible to truly delete data from social
networking sites: in most cases, their "delete" usually means "don't show any
more" rather than "erase all past record of".

That brings us to the fact that many tech companies who offer free products and
services make money by selling targeted advertising to you using the data they
have about you, or by selling the data you've given them to third parties.  (As
they saying goes, if you're not paying for it, you are probably the product.)
Companies do give users some control over personal data, but they frequently
change their terms of service in opaque ways. Seemingly-innocuous information
can give attackers valuable clues: restaurant "likes" reveal where you were at
specific times, while funny stories about childhood birthday parties reveal
likely answers to security questions. Again, it's a good practice to get into
the habit of checking your privacy settings every time you do some other regular
task.

Unfortunately, even if you do this, information may leak through other
means. For example, attackers can friend your friends in an attempt to get
information about you, such as the name of your first school. And as bad as
social media sites are for social engineering in this way, cell phone
applications are often worse. In general, if a game wants access to your camera
and address book, you should probably find a different game to play.

Since social media is a fact of life for most of us, you should check your
settings periodically, just as you would take your car in for an oil change. (I
do these things at the same time in order to remember both.) Turn off everything
you can and then use a tracking blocker such as Ghostery to reduce information
leakage.

Many experts recommend using separate devices or accounts for work and personal
life, but this is increasingly unrealistic. Everyone checks their personal email
from their work device eventually, and everyone uses their personal phone for
2FA. However, you should consider getting a second phone for international
travel: the legalities around who can take your devices and/or force you to
unlock them are complicated and frequently overstepped, so you should assume
that anything on or connected to the devices you are traveling with will be
compromised.

<div class="callout" markdown="1">

### Don't put that in there

Never plug a random USB drive into your device: it's like letting a complete
stranger into your home unsupervised.

</div>

## Fighting Back

Casual attackers may eventually get bored and move on, but like all bullies,
they will also often revisit previous victims, and even if they don't, they are
likely to pick new ones. It's unfair to ask people who have been targeted to do
extra work, but if you have been, please consider these steps.

Do not engage directly.
:   Casual attackers are often seeking attention, so a direct response often
    encourages further attacks (and can draw attention from like-minded
    attackers).

Find support.
:   Being targeted is frightening and wearying, particularly if you belong to one
    of the many groups that are targeted in real life as well as online. Let
    family, friends, and colleagues know what is happening so that they can
    support you. They may also be able to offer advice if they have been in
    similar situations.

Use anti-harassment apps like [Block Party][block-party].
:   And document everything: save emails and take screenshots of sites like
    Facebook and Twitter in case attackers delete or alter material.

Report the attack.
:   Social media sites have done everything they can to avoid legal
    accountability for online attacks, but companies and universities will
    usually take what steps they can once they know there is a problem. In the
    authors' experience, they are more inclined to take real action against the
    attacker if they believe that you might speak publicly about what has
    happened and thereby damage their reputation, so never agree to a
    non-disclosure agreement that would prevent you from doing so.

Above all, remember that it's not just about you. We don't just wear masks to
prevent ourselves from becoming infected: we also wear them so that we will not
infect others. Similarly, if you do not take precautions with online security
then you are putting others at risk.  Simple steps like putting passwords on
PDFs that contain sensitive information can go a long way to deter attackers, in
the same way that a sturdy-looking bike lock encourages would-be thieves to go
after some other bike. And if you *are* compromised, let those affected know as
soon as you can.

The only long-term way to improve everyone's online safety is to pressure
politicians to strengthen liability legislation so that companies, universities,
and other institutions have real incentives to take meaningful action. Cars and
drugs are as safe as they are because their manufacturers are liable for
negligence and harm. The sooner software companies and social media sites are
liable as well, the safer all of us will be.

<span class="fixme">demonstrate an SQL injection attack https://github.com/gvwilson/buildtogether.tech/issues/64</span>
