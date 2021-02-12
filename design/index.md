---
---

> A week of hard work can sometimes save an hour of thought.
>
> --- Robert Wilson

Building large programs with other people is different from building small
programs on your own in two important ways. The first is communication: in order
for you and your teammates to collaborate, you need to agree about what you're
collaborating *on*, which means you need to tell each other how you are breaking
the problem up into pieces and how those pieces will interact.

The second difference between programming on small problems and large ones is
that while you can hack your way from an empty `.js` or `.py` file to a
hundred-line program in a reasonable time, the re-work that strategy requires
becomes unaffordable when your final product is a thousand lines long.

To see why, let's build a simple model to capture the cost of re-working old
code when adding new code.  Suppose the final program is $$N$$ lines long and is
made up of chunks that are each $$L$$ lines long, so there are $$C = N/L$$
chunks in total.  You write chunks one by one; each time you add one, there is a
probability $$p$$ that each of the chunks already written needs to be rewritten.
How many chunks do you actually wind up writing?

-   The first chunk always needs to be written, so that's 1.

-   When you write the second chunk you need to rewrite the first chunk with
    probability $$p$$, so the likely cost of the second chunk is $$1+p$$.

-   The likely cost of the third chunk is $$1+2p$$, since you might have to
    rewrite either or both of the first two chunks.

-   In general, the cost of adding chunk $$i$$ is $$1+(i-1)p$$, so the total cost
    of writing $$C$$ chunks is $$C + p\sum_{i=0}^{C-1}{i}$$, which is
    $$C + p(C-1)(C-2)/2$$ or $$pC^{2}/2 + (1-p)C + 1$$.

This model is unrealistic in several ways---the odds of rewriting code goes down
the older it is, for example---but it captures a key point: the cost of rework
grows faster than the number of pieces of work. Your goal when designing
software is to reduce the cost of reworking things by lowering $$p$$.

I can't *tell* you how to design software.  I don't know anyone who can,
either. I can *show* you by working through examples on a whiteboard, asking
rhetorical questions, and setting problems for you to think about, but that
doesn't translate well to print.  I can also tell you how to describe designs
and how to tell a good design from a bad one, so we'll start with that.

## Describing Designs

<cite>Cherubini2007</cite> found that developers usually don't draw diagrams as
part of the permanent record. Instead, they use diagrams as an aid to
conversation in the moment---essentially, as a temporary store for ideas that
they wouldn't otherwise be able to keep track of (<span
x="thinking"></span>). In many cases, the people who drew the diagrams couldn't
make sense of them a day later; it could be that the benefit of diagrams
therefore comes from the act of drawing, not from having them to study.

When experienced developers draw on the whiteboard as they're talking to one
another, they generally draw the following:

Data structures.
    These are blob-and-arrow pictures of the objects and containers that make up
    the program and the references that stitch them together. The more
    experience someone has, the fewer of these they need to draw, but everyone
    falls back on them eventually (particularly during difficult debugging
    sessions).

Schemas or data models.
    These can be fairly literal pictures of the tables in a database, possibly
    augmented with arrows to show what's a foreign key for what, or <span
    g="er_diagram">entity-relationship diagrams</span> that show the things the
    system stores, and the relationships between them.

The <span g="conceptual_architecture">conceptual architecture</span> of the system.
:   This shows how the important parts of the system fit together. It's also
    the least constrained, since it can include everything from specific
    sections of configuration files to class hierarchies to replicated web
    servers. What qualifies as "important" depends on what aspect(s) of the
    system you're currently concerned with. If I'm trying to explain a bug that
    only arises when the application is configured incorrectly, I might draw its
    configuration files, and the database tables that store user preferences,
    but leave out the password database and log files entirely. If we're trying
    to figure out a better load balancing strategy, on the other hand, I would
    draw most of what would go into a physical architecture diagram, plus just
    enough of the class inheritance hierarchy to show how the servers will load
    user request handlers dynamically.

The system's physical architecture.
:   This is the files, processes, sockets, database tables, etc., that make it
    up. In most cases, this consists of a bunch of boxes representing the
    machines the application's components run on, trees showing files and
    directories, and circles showing running processes. A lot of this stuff can
    show up in the conceptual architecture as well.

<span g="workflow_diagram">Workflow diagrams</span> that show how users accomplish things.
:   Workflows are almost always drawn as <span g="fsm">finite state
    machines</span>. Each node represents a state the user and the system can be
    in, while the arcs show how to get from one state to another.

The two kinds of diagram that I find most useful are the entity-relationship
diagram and a combination of conceptual and workflow diagrams called a <span
g="use_case_map">use-case map</span> <cite>Reekie2006</cite>.  The background is
the system's conceptual architecture; the overlay traces what happens during a
particular workflow.  It's easy to understand, and I found it very useful for
checking the behavior of moderately complex systems, particularly ones built
from lots of <span g="microservice">microserves</span>.

<div class="callout" markdown="1">

### UML and why not

I'm not a fan of the <span g="uml">Unified Modeling Language</span> (UML). It
defines over a dozen different types of diagrams for showing the relationships
between classes, the order in which things happen when methods are invoked, the
states a system goes through when performing an action, and so on.  Hundreds of
books and thousands of articles have been written about UML, but in all the
years I've been programming, I've only ever met one person who drew UML diagrams
of his own free will on a regular basis. I've known a handful of other people
who occasionally sketched class diagrams as part of a larger description of a
design, and that's pretty much it. Unlike blueprints in architecture or flow
diagrams in chemical engineering, UML doesn't actually seem to help
practitioners very much <cite>Petre2013</cite>.

</div>

## Getting Started

What if you're starting with a blank sheet of paper (or an empty whiteboard)?
How do you describe something that doesn't exist yet? The best way to start is
to write your elevator pitch. Next, write one or two point-form stories
describing how the application, feature, or library would be used. Be as
concrete as possible: instead of saying, "Allows the user to find overlaps
between their calendar and their friends' calendars," say:

1.  The user selects one of her friends' calendars.

1.  The system displays a page showing how the busy/not-busy times in that
    person's calendar overlaps with the user's.

1.  The user can then add more of her friends' calendars one by one or remove
    any calendars except her own. The system updates the display after each
    action to show how many people overlap where.

As short as it is, this story tells us that:

-   People have friends.

-   Calendars are added one at a time rather than in a batch.

-   The user's own calendar is always displayed.

-   We need to decide how to show the density of overlaps, not just all-or-none.

Once you have half a dozen of these stories, go through and highlight the key
things and relationships you have described. In the example above, you would
highlight "user", "friend", "calendar", and "page". As soon as you try to draw a
diagram showing how these are related to one another, you'll have to start
making design decisions: for example, is "friend" an entity, or a relationship
between two entities (i.e., is it a blob or an arrow)?

If, during this process, you hear yourself say, "We'll use a linked list to…"
step back and catch your breath. Details like that do need to be worked out at
some point, but:

-   you're probably worrying about that as a way to *not* think about the bigger
    design questions (which are scarier for beginners);

-   you probably don't know enough yet about your design to make the right
    decision; and

-   you're probably a good enough coder by now that you can worry about that
    when the time comes to actually write the code. Remember, not everything
    actually needs to be designed.

Once you have a diagram---any kind of diagram---start iterating around it. Pick
one open problem like, "How do users control who can see their calendars?"),
think of a way to solve it ("they can mark them as 'public', or invite specific
people to view them"), figure out how to implement your solution, then revisit
any previous decisions that your most recent decisions affect. Design is a very
cyclic process: every time you add or change one thing, no matter how small, you
may need to go back and re-design other things.

There are two traps here for the inexperienced. The first is <span
g="analysis_paralysis">analysis paralysis</span>, where you find yourself
revisiting issues over and over again without ever making any decisions that
stick. The second is <span g="aih">already invented here</span> syndrome, in
which someone says, "Look, we've already made a decision about that, let's not
reopen the debate." Either can sink a project; together, they show why it's so
hard to teach design, since what I'm basically saying is, "Argue enough, but not
too much."

<div class="callout" markdown="1">

### How experts do it

One of the biggest differences between experts and non-experts in any field is
how quickly experts can rule out possibilities
<cite>Schon1984,Petre2016</cite>. Whether it is software design, chess, or
medical diagnosis, beginners check to see if their plan will work; experts, on
the other hand, search for a refutation---a reason why it won't---so that they
can narrow their focus as early as possible. One way to do this is to jump back
and forth between a high-level plan and its low-level consequences; if one of
those consequences reveals a flaw in the plan, they go back to the high level
and make a correction. Doing this efficiently depends on having experience of
past failures so that you know how a good idea might fail in practice.

</div>

## Design for Testability

When most developers hear the word "design", they think about either the
application's structure or its user interface. If you don't think about how
you're going to test your application while you're designing it, though, the
odds are very good that you'll build something that cannot (or cannot easily) be
tested.  Conversely, if you <span g="design_for_test">design for test</span>,
it'll be a lot easier to check whether your finished application actually does
what it's supposed to.

Thinking about testability from the start turns out to be a good <span
g="heuristic">heuristic</span> for design in general <cite>Feathers2004</cite>,
since it forces you to think in terms of small components with well-defined
interfaces. Not only can these be tested more easily, they can also be modified
or replaced in isolation, which significantly reduces the probability of
requiring rework in the naïve model presented at the start of this chapter.

For example, let's consider a typical three-tier web site that uses the <span
g="mvc">Model-View-Controller</span> (MVC) design pattern. The model, which is
stored in a relational database, is the data that the application manipulates,
such as purchase orders and game states. The controller encapsulates the
application's business rules: who's allowed to cancel games while they're in
progress, how much interest to add on out-of-province orders, and so on.
Finally, the view translates the application's state into HTML for display
and handles the button clicks and form submissions that drive the system from
one state to another.

This architecture presents several challenges for testing:

Unit testing libraries are designed to run within a single process.
:   As the word "library" implies, they're made up of code that's meant to be
    loaded into a single running program. Most debuggers and testing libraries
    don't track interactions *between* processes.

Configuring a test environment is a pain.
:   You have to set up a database server, clear the browser's cache, make sure
    the right clauses are in your web server's configuration file, and so on.

Running tests is slow.
:   In order to ensure that tests are independent, you have to create an
    entirely new fixture for each test. This means reinitializing the database,
    restarting the web server, and so on, which can take several seconds per
    test. That translates into an hour or more for a thousand tests, which is
    pretty much a guarantee that developers won't run them routinely while
    they're coding, and might not even run them before checking changes in.

The first step in fixing this is to get rid of the browser and web server. One
way to do this is to replace the browser with a script that generates HTTP
requests as multi-line strings and passes them via a function call to a library
that does whatever the web server's HTTP handler would do. After invoking our
actual program, this library passes the text of an HTTP response back to our
script, which then checks that the right values are present (about which more in
a moment). The library's job is to emulate the environment the web app under
test would see if it was being invoked by the real server: environment variables
are set, standard input and output are replaced by <span g="string_io">string
I/O</span> objects, and so on, so that the application has no (easy) way to tell
how it's being invoked.

Why go through this rigmarole? Why not just have a top-level function in the web
app that takes a URL, a dictionary full of header keys and values, and a string
containing the POST data, and check the HTML page it generates? The answer is
that structuring our tests in this way allows us to run them both in this test
harness, and against a real system. By replacing the fake HTTP handler with code
that sends the HTTP request through a socket connected to an actual web server,
and reads that server's response, we can check that our application still does
what it's supposed to when it's actually deployed. The tests will run much more
slowly, but that's OK: if we've done our job properly, we'll have caught most of
the problems in our faked environment, where debugging is much easier to do.

Now, how to check the result of the test? We're expecting HTML, which is just
text, so why not store the HTML page we want in the test and do a string
comparison? The problem with that literal approach is that every time we make
any change at all to the format of the HTML, we have to rewrite every test that
produces that page. Even something as simple as introducing white space, or
changing the order of attributes within a tag, will break string comparison.

A better strategy is to add unique IDs to significant elements in the HTML page,
and only check the contents of those elements. For example, if we're testing
login, then somewhere on the page there ought to be an element like this:

```
<div id="currentuser">Logged in as <strong>marian</strong>
(<a href="http://www.example.org/logout">logout</a>
|
<a href="http://www.example.org/preferences">preferences</a>)
</div>
```

We can find that pretty easily with a <span g="css_selector">CSS selector</span>
that looks for a `div` with the ID `currentuser`.  We can then move the `div`
around without breaking any of our tests; if we were a little more polite about
formatting its internals (i.e., if we used something symbolic to highlight the
user name and trusted CSS to do the formatting), we'd be in even better shape.

We've still only addressed half of our overall problem, though: our web
application is still talking to a database, and reinitializing it each time a
test runs is slow.  We can solve this by moving the database into memory. Most
applications rely on an external database server, which is a long-lived process
that manages data on disk. An alternative is an <span
g="embedded_database">embedded database</span>, in which the database
manipulation code runs inside the user's application as a normal library;
[SQLite][sqlite] is probably the best known of these.

The advantage of using an embedded database from a testing point of view is that
it can be told to store data in memory, rather than on disk. This would be a
silly thing to do in a production environment (after all, the whole point of a
database is that it persists), but in a testing environment, an <span
g="in_memory_database">in-memory database</span> can speed things up by a factor
of thousands, since the hard drive never has to come into play. The cost of
doing this is that you have to either commit to using one database in both
environments, or avoid using the "improvements" that different databases have
added to SQL.

Once these changes have been made, the application zips through its tests
quickly enough that developers actually will run the test suite before checking
in changes to the code. The downside is the loss of <span
g="fidelity">fidelity</span>: the system we're testing is a close cousin to what
we're deploying, but not exactly the same. However, this is a good economic
tradeoff: we may miss a few bugs because our fake HTTP handler doesn't translate
HTTP requests exactly the same way as the real web server, but we catch (and
prevent) a lot more by making testing cheap.

## Design for Evolution

How easily we can swap one component for another in order to test a system is
one way to tell how well designed that system is. Another is how easily we can
modify or extend the system to do new things. If our design is perfect, we can
implement changes by adding code without modifying what's already there.  This
is called the <span g="open_closed_principle">Open-Closed Principle</span>:
systems should be open for extension, but closed for modification.

For example, suppose that we are simulating a hospital emergency room. We could
write the function that simulates someone's response to a cardiac arrest like
this:

```python
def handle_cardiac_arrest(all_actors):
    for actor in all_actors:
        if actor.kind == 'nurse':
            ...do something...
        elif actor.kind == 'doctor':
            ...do something else...
        else:
            ...do some default action...
```

{: .continue}
(The term <span g="actor">actor</span> is often used in simulations to mean
"anything that can take actions".) If we want to add another kind of actor, we
need to modify this code to add another `elif` clause, and if we want to add
another kind of event, we have to write another function *and* make sure we
have an `if` or `elif` for kind of actor.

A better design is to create a <span g="base_class">base class</span> that
defines a generic behavior for all actors:

```python
class Actor:
    def __init__(...):
        ...do generic setup...
    def handle_cardiac_arrest(self):
        pass # by default, don't do anything
```

{: .continue}
and then <span g="derive">derive</span> one class for each type of actor:

```python
class Nurse(Actor):
    def handle_cardiac_arrest(self):
        ...do something...

class Doctor(Actor):
    def handle_cardiac_arrest(self):
        ...do something else...
```

We can then ask each actor to handle the cardiac arrest however they're supposed
to:

```python
def handle_cardiac_arrest(all_actors):
    for actor in all_actors:
        actor.handle_cardiac_arrest()
```

If we want to add another kind of actor, we derive another class from `Actor`
and <span g="key">override</span> methods to give it the behaviors we want:
the general `handle_cardiac_arrest` function doesn't need to change.

This design isn't perfect, though.  If we want to add another kind of event, we
need to define a default response to it by adding a method to `Actor`, then
override that method for the specific kinds of actors that have different
behaviors. A more sophisticated design would define classes to represent events
and select a method to call based on the event:

```python
class Actor:
    def __init__(...):
        ...do generic setup...
    def handle_event(self, event):
        if self.has_handler_for(event):
            handler = self.get_handler_for(event)
            handler(event)
        else:
            self.default_action(event)
```

This design makes it harder to figure out exactly who's doing what, but ensures
that we can add new actors *and* new events without having to go back and change
old code.

But how can we be sure that our new code is going to do what the old code
expects? The answer is a technique called <span g="design_by_contract">design by
contract</span>. Every function or method specifies <span
g="pre_condition">pre-conditions</span> that must be true of its inputs in order
for it to run successfully and <span g="post_condition">post-conditions</span>
that are guaranteed to be true of its results. <span g="type_declaration">Type
declarations</span> are the most common kind of pre-condition and
post-condition: they say things like, "The input must be a list of strings,"
and, "The output is a single string." More sophisticated pre-conditions and
post-conditions can be written as assertions that (for example) check that all
the input strings are at least one character long or that the output is one of
the input strings.

Design by contract gets its name from the fact that a function's pre-conditions
and post-conditions work like a business contract: if the caller guarantees that
the inputs meet the pre-conditions, then the function guarantees that the output
meets the post-conditions. Contracts like these are particularly useful when
overriding methods or when software evolves:

Pre-conditions can only be made weaker.
:   This rule is another way of saying that the new version of the code can only
    put *fewer* restrictions on the inputs it accepts, or equivalently, it must
    handle everything the old version could, but may handle more. If code breaks
    this rule, then it might fail in cases where the old code ran.

Post-conditions can only be made stronger.
:   This rule ensures that the new function can't produce anything that the old
    function might not have produced, and ensures that anything using the
    function's output will be able to handle everything the new version gives
    it.

A programming language called [Eiffel][eiffel] demonstrated how powerful design
by contract can be. Most other languages don't support it directly; we can
emulate it by putting assertions at the start and end of our functions and
methods, but there's no guarantee they'll be checked or enforced in derived
versions.

## Scriptability

Rule \#3 of <cite>Taschuk2017</cite> is, "Make common operations easy to
control."  Like testing, it's a lot easier to do if you design programs with
this goal in mind.

You can make programs controllable in at least three different ways:

Command-line flags.
:   Enable users to run it from the command line and control its operation via
    flags. For example, the `-a` or `--all` flag could tell the program to
    process all files even if there are errors, while `-o` or `--output` could
    specify the name of the output directory.

Configuration files.
:   Have the program load settings from one or more configuration files.  This
    option saves them typing in common settings over and over, and also provides
    a record of exactly what the settings were (which can be helpful when
    testing).

    Configuration files are often <span g="layered_configuration">layered</span>:
    the program reads a global configuration file with general settings, then a
    user-specific configuration file (typically in the user's home directory)
    with the user's preferences, and finally a project-specific file. Those
    settings can then often be overridden using command-line flags.

A programming interface.
:   If the application is written as a set of libraries, each with its own API,
    then the interface the general user sees can be written as a thin layer that
    combines those libraries. Users can then write code of their own to control
    the libraries if they want to extend the application's behavior.  Most large
    games are written this way, and languages like [Lua][lua] are designed to be
    embedded in applications so that users can write modifications right then
    and there.

## Logging

Something else you can design into your system to make your life easier later on
is <span g="logging">logging</span>, which is the professional alternative to
`print` statements. Instead of writing:

```python
def extrapolate(basis, case):
    print "entering extrapolate..."
    trials = count_basis_width(basis)
    if not trials:
        print "...no trials!"
        raise InvalidDataException("no trials")
    print "...running", len(trials), "trials"
    result = run_trial(trials[0])
    for t in range(1, len(trials)):
        result = max(result, run_trial(trials[i]))
    print "...exiting extrapolate with", result
```

{: continue}
you use your language's logging library like this:

```python
import logging

def extrapolate(basis, case):
    logging.debug("entering extrapolate...")
    trials = count_basis_width(basis)
    if not trials:
        logging.warning("...no trials!")
        raise InvalidDataException("no trials")
    logging.debug(f"...running {len(trials)} trials")
    result = run_trial(trials[0])
    for t in range(1, len(trials)):
        result = max(result, run_trial(trials[i]))
    logging.debug(f"...exiting extrapolate with {result}")
```

At first glance this is just more verbose. The benefit, though, is that your
messages are now divided into two classes. If you want to get all the messages,
you put:

```python
logging.basicConfig(level=logging.DEBUG)
```

{: .continue} somewhere near the start of your program. The `DEBUG` flag
identifies the least important messages in your program---the ones you probably
only want to see when you're trying to figure out what's gone wrong. In order,
the more important levels in most logging libraries are `INFO`, `WARNING`,
`ERROR`, and `CRITICAL`. If you only want messages at the `WARNING` level and
above, you change the configuration to:

```python
logging.basicConfig(level=logging.WARNING)
```

{: .continue}
so that `DEBUG` and `INFO` messages aren't printed.

A logging library allows you to control how much your program tells you about
its execution by making one change, in one place. It also means that you can
leave these messages in your code, even when you release it---there's no more
commenting out `print` statements only to add them back in later. (And no more
embarrassment from inappropriately-worded messages that *weren't* commented out
but should have been before your demo…)

Logging libraries also let you divide messages into groups by component, so that
you can (for example) turn on debugging-level messages from the database
interface but only see errors and above from the image processing functions.
They also let you control where your messages are sent. By default, they go to
the screen, but you can send them to a file instead simply by changing the
configuration:

```python
logging.basicConfig(level=logging.ERROR,
                    filename="/tmp/mylog.txt",
                    filemode="append")
```

This is handy if it takes your program a while to get to the point where the
error occurs. It's also handy if you don't know whether your program contains an
error or not: if you leave logging turned on every time you run it, then
whenever it does something unexpected (like crashing), you will have at least
some idea of what it was doing beforehand.

Most logging libraries also support <span g="rotating_file">rotating
files</span>, i.e., they will write to `log.1` on the first day, `log.2` on the
second day, and so on until they reach (for example) `log.7`, then wrap around
and overwrite `log.1`. Web servers and other long-lived programs are usually set
up to do this so that they don't fill up the disk with log information.  It's
all straightforward to set up, and once it's in place, it gives you a lot more
insight into what your program is actually doing.
