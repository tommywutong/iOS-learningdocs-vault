---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Ada-Tests.html
archived_at: '2026-07-15T07:30:59.213248Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [C Tests](C-Tests.md#apple-imwvizltorzq),
Previous: [Test Directives](Test-Directives.md#apple-krsxg5bniruxezldoruxmzlt),
Up: [Testsuites](Testsuites.md#apple-krsxg5dtovuxizlt)

---

#### 6.4.3 Ada Language Testsuites

The Ada testsuite includes executable tests from the ACATS 2.5
testsuite, publicly available at
[http://www.adaic.org/compilers/acats/2.5](http://www.adaic.org/compilers/acats/2.5)

These tests are integrated in the GCC testsuite in the
`gcc/testsuite/ada/acats` directory, and
enabled automatically when running `make check`, assuming
the Ada language has been enabled when configuring GCC.

You can also run the Ada testsuite independently, using
`make check-ada`, or run a subset of the tests by specifying which
chapter to run, e.g.:

```
     $ make check-ada CHAPTERS="c3 c9"
```

The tests are organized by directory, each directory corresponding to
a chapter of the Ada Reference Manual. So for example, c9 corresponds
to chapter 9, which deals with tasking features of the language.

There is also an extra chapter called `gcc` containing a template for
creating new executable tests.

The tests are run using two `sh` scripts: `run_acats` and
`run_all.sh`. To run the tests using a simulator or a cross
target, see the small
customization section at the top of `run_all.sh`.

These tests are run using the build tree: they can be run without doing
a `make install`.
