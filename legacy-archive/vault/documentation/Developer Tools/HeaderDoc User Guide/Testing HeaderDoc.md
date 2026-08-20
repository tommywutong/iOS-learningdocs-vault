---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/testing/testing.html
archived_at: '2026-07-15T07:24:28.374288Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](HeaderDoc%20Release%20Notes.md)[Previous](Using%20the%20MPGL%20Suite.md)

# Testing HeaderDoc

Beginning in version 8.7, HeaderDoc includes a regression test suite that makes it easier to modify the parser code without causing regressions. This chapter describes how to use the test suite.

Beginning in HeaderDoc 8.8, the test suite is installed as part of the HeaderDoc installation. Thus, you can run the test suite without downloading a source tarball. However, the main reason to run it is if you are modifying the source code, in which case it is much easier to work with a standalone copy of HeaderDoc.

You can download the HeaderDoc tarball from [www.opensource.apple.com](http://www.opensource.apple.com/release/mac-os-x-106/). Click the latest version of OS X on that page, then search for `headerdoc` on the resulting page and click the download link to the right.

You can run tests in two ways: all at once or individually.

- To run all of the tests at once, type the following commands:

```
# From an installed copy:
headerdoc2html -T run

# From a standalone copy:
cd /path/to/headerdoc-version
./headerDoc2HTML.pl -T run
```

  HeaderDoc runs the complete battery of tests and produces a summary of the results at the end.
- To run a single test or a group of tests, specify their path or paths after the `run` subcommand. For example:

```
# From an installed copy
headerdoc2html -T run /path/to/Xcode.app/Contents/Developer/usr/share/headerdoc/testsuite/parser_tests/PHP_function_1.test

# From a standalone copy:
./headerDoc2HTML.pl -T run testsuite/parser_tests/PHP_function_1.test
```


When using the `run` subcommand, you get only a summary output telling what test failed. Finding out exactly what went wrong can be more challenging. Here are the basic steps:

1. Use the `update` subcommand as though you were trying to update test results (`headerDoc2HTML.pl -T update` _[optional list of tests]_). When a test fails, HeaderDoc displays the test result differences.
2. Type `less` and press return to get a contextual diff of some of the more verbose sections of the result.
3. If you see that the change is expected (if you made a change to the code and the new results reflect a desired change), type `confirm` to update the test results with the new data.
4. If the test results are not as expected, type `skip` to go on to the next test without updating the test results.

Creating a test is somewhat more involved than running one. To create a test, you need to have a problematic HeaderDoc comment block and declaration. After you have these, perform the following steps:

1. Create a minimal test case header or script that contains only the declaration that causes the problem (and the class surrounding it, if applicable).
2. Rename all classes, functions, variables, and so on to have a name that is unique across the entire test set.
3. Fix the bugs in HeaderDoc so that the code is parsed correctly.
4. Run the existing tests to make sure you didn’t break anything else.
5. Type `headerDoc2HTML.pl -T create` to create a new test.
6. Choose a unique name for the test. The name for the test must be unique after spaces and special characters are replaced by underscores. For a list of existing tests, look in the subdirectories within the `testsuite` directory.

   In general, the names of tests in languages other than C or C++ should begin with the name of the programming language.
7. Choose a programming language for the test. (This must match the declaration.)
8. If you are creating a C language test, choose whether you are creating a C preprocessor test or a parser test.

   Parser tests are intended to test both the code parser and comment handling code. Most of the time, you should be writing a parser test. Parser tests are limited to a single declaration per test, however, and thus are unsuitable for determining whether a C preprocessor directive correctly modifies a declaration.

   C preprocessor tests are intended to test whether a C preprocessor macro correctly alters a declaration. Unlike a parser test, the C preprocessor test does not test the comment handling code. It takes two blocks of code. The first block is a series of C preprocessor macros that are all parsed. The second is a declaration to operate on. This declaration is parsed and information about that declaration is stored in the test results.

From this point on, the steps differ based on the type of test you choose.

To create a parser test, after completing the steps in [Creating a Test](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmjnknlte), do the following:

1. Paste the HeaderDoc comment block, then press Control-D on a new line to end the comment.
2. Paste the code, then press Control-D on a new line to end the declaration.
3. Type in an explanatory message to describe how the test case differs from other similar tests, then press Control-D on a new line to end the message.
4. If you are overwriting an existing test case, HeaderDoc asks you to confirm that you intended to do so. In general, say no unless you made a mistake previously and are overwriting a test you just created.
5. Wait for HeaderDoc to build the test data.
6. Submit the test case and patches via [bugreport.apple.com](http://bugreport.apple.com/).

C preprocessor macro tests apply a series of C preprocessor macros to a declaration (which can be anything from a C preprocessor macro to a class).

To create a C preprocessor test, complete the steps in [Creating a Test](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmjnknlte), then do the following:

1. Paste the block of C preprocessor macros, then press Control-D on a new line to end the list of macros.
2. Paste the declaration that the C preprocessor macros should modify, then press Control-D on a new line to end the declaration.
3. Type an explanatory message to describe how the test case differs from other similar tests, then press Control-D on a new line to end the message.
4. If you are overwriting an existing test case, HeaderDoc asks you to confirm that you intended to do so. In general, say no unless you made a mistake previously and are overwriting a test you just created.
5. Wait for HeaderDoc to build the test data.
6. Submit the test case and patches via [bugreport.apple.com](http://bugreport.apple.com/).

[Next](HeaderDoc%20Release%20Notes.md)[Previous](Using%20the%20MPGL%20Suite.md)

