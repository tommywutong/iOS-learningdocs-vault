---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/libgcj-Tests.html
archived_at: '2026-07-15T07:31:03.162724Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [gcov Testing](gcov-Testing.md#apple-m5rw65rnkrsxg5djnztq),
Previous: [C Tests](C-Tests.md#apple-imwvizltorzq),
Up: [Testsuites](Testsuites.md#apple-krsxg5dtovuxizlt)

---

#### 6.4.5 The Java library testsuites.

Runtime tests are executed via ``make check`' in the
`target/libjava/testsuite` directory in the build
tree. Additional runtime tests can be checked into this testsuite.

Regression testing of the core packages in libgcj is also covered by the
Mauve testsuite. The [Mauve Project](http://sourceware.org/mauve/)
develops tests for the Java Class Libraries. These tests are run as part
of libgcj testing by placing the Mauve tree within the libjava testsuite
sources at `libjava/testsuite/libjava.mauve/mauve`, or by specifying
the location of that tree when invoking ``make`', as in
``make MAUVEDIR=~/mauve check`'.

To detect regressions, a mechanism in `mauve.exp` compares the
failures for a test run against the list of expected failures in
`libjava/testsuite/libjava.mauve/xfails` from the source hierarchy.
Update this file when adding new failing tests to Mauve, or when fixing
bugs in libgcj that had caused Mauve test failures.

The [Jacks](http://sourceware.org/mauve/jacks.html) project provides a testsuite for Java compilers that can be used
to test changes that affect the GCJ front end. This testsuite is run as
part of Java testing by placing the Jacks tree within the libjava
testsuite sources at `libjava/testsuite/libjava.jacks/jacks`.

We encourage developers to contribute test cases to Mauve and Jacks.
