---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/profopt-Testing.html
archived_at: '2026-07-15T07:31:01.072458Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [compat Testing](compat-Testing.md#apple-mnxw24dboqwvizltoruw4zy),
Previous: [gcov Testing](gcov-Testing.md#apple-m5rw65rnkrsxg5djnztq),
Up: [Testsuites](Testsuites.md#apple-krsxg5dtovuxizlt)

---

#### 6.4.7 Support for testing profile-directed optimizations

The file `profopt.exp` provides language-independent support for
checking correct execution of a test built with profile-directed
optimization. This testing requires that a test program be built and
executed twice. The first time it is compiled to generate profile
data, and the second time it is compiled to use the data that was
generated during the first execution. The second execution is to
verify that the test produces the expected results.

To check that the optimization actually generated better code, a
test can be built and run a third time with normal optimizations to
verify that the performance is better with the profile-directed
optimizations. `profopt.exp` has the beginnings of this kind
of support.

`profopt.exp` provides generic support for profile-directed
optimizations. Each set of tests that uses it provides information
about a specific optimization:

**`tool`**
: tool being tested, e.g., `gcc`

**`profile_option`**
: options used to generate profile data

**`feedback_option`**
: options used to optimize using that profile data

**`prof_ext`**
: suffix of profile data files

**`PROFOPT_OPTIONS`**
: list of options with which to run each test, similar to the lists for
torture tests
