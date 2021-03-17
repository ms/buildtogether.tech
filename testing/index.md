---
---

<span class="fixme">intro to testing</span>

<span class="fixme">fuzz testing https://github.com/gvwilson/buildtogether.tech/issues/65</span>

## Unit Testing

Preventing errors is good, but preventing them is better, so responsible
programmers test their code.  As the name suggests, a <span g="unit_test">unit
test</span> checks the correctness of a single unit of software.  Exactly what
constitutes a "unit" is subjective, but it typically means the behavior of a
single function in one situation.

A single unit test will typically have:

-   a <span g="fixture">fixture</span>, which is the thing being tested (e.g., an
    array of numbers);

-   an <span g="actual_result">actual result</span>, which is what the code
    produces when given the fixture; and

-   an <span g="expected_result">expected result</span> that the actual result is
    compared to.

The fixture is typically a subset or smaller version of the data the function
will typically process. In fact, it should be a reprex (<span
x="collaborate"></span>), i.e., exactly the same kind of minimal example you
would post online if you were asking for help.

Writing one unit test is easy enough, but we should check other cases as well.
To manage them, we can use a <span g="test_framework">test framework</span>
(also called a <span g="test_runner">test runner</span>).  Like logging
frameworks and many other things, most are very similar because they were
inspired by the same forerunners. The most widely-used test framework for Python
is called [`pytest`][pytest], which structures tests as follows:

1.  Tests are put in files whose names begin with `test_`.
2.  Each test is a function whose name also begins with `test_`.
3.  These functions use `assert` to check results.

The `pytest` library comes with a command-line tool that is also called
`pytest`.  When run with no options, it searches for all files in or below the
working directory whose names match the pattern `test_*.py`.  It then runs the
tests in these files and summarizes their results.

<div class="callout" markdown="1">

### Testing visualizations

Testing visualizations is hard: any change to the dimension of the plot, however
small, can change many pixels in a <span g="raster_image">raster image</span>,
and cosmetic changes such as moving the legend up a couple of pixels will cause
all of the tests to fail.  The simplest solution is therefore to test the data
used to produce the image rather than the image itself.  Unless you suspect that
the drawing library itself contains bugs, the correct data should always produce
the correct plot.

</div>

## Performance Testing

<span class="fixme">profiling and performance testing</span>
