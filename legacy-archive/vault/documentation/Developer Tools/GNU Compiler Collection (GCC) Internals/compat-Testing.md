---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/compat-Testing.html
archived_at: '2026-07-15T07:31:01.024700Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [profopt Testing](profopt-Testing.md#apple-obzg6ztpob2c2vdfon2gs3th),
Up: [Testsuites](Testsuites.md#apple-krsxg5dtovuxizlt)

---

#### 6.4.8 Support for testing binary compatibility

The file `compat.exp` provides language-independent support for
binary compatibility testing. It supports testing interoperability of
two compilers that follow the same ABI, or of multiple sets of
compiler options that should not affect binary compatibility. It is
intended to be used for testsuites that complement ABI testsuites.

A test supported by this framework has three parts, each in a
separate source file: a main program and two pieces that interact
with each other to split up the functionality being tested.

**`testname_main.suffix`**
: Contains the main program, which calls a function in file
`testname_x.suffix`.

**`testname_x.suffix`**
: Contains at least one call to a function in
`testname_y.suffix`.

**`testname_y.suffix`**
: Shares data with, or gets arguments from,
`testname_x.suffix`.

Within each test, the main program and one functional piece are
compiled by the GCC under test. The other piece can be compiled by
an alternate compiler. If no alternate compiler is specified,
then all three source files are all compiled by the GCC under test.
You can specify pairs of sets of compiler options. The first element
of such a pair specifies options used with the GCC under test, and the
second element of the pair specifies options used with the alternate
compiler. Each test is compiled with each pair of options.

`compat.exp` defines default pairs of compiler options.
These can be overridden by defining the environment variable
`COMPAT_OPTIONS` as:

```
     COMPAT_OPTIONS="[list [list {tst1} {alt1}]
       ...[list {tstn} {altn}]]"
```

where tsti and alti are lists of options, with tsti
used by the compiler under test and alti used by the alternate
compiler. For example, with
`[list [list {-g -O0} {-O3}] [list {-fpic} {-fPIC -O2}]]`,
the test is first built with `-g -O0` by the compiler under
test and with `-O3` by the alternate compiler. The test is
built a second time using `-fpic` by the compiler under test
and `-fPIC -O2` by the alternate compiler.

An alternate compiler is specified by defining an environment
variable to be the full pathname of an installed compiler; for C
define `ALT_CC_UNDER_TEST`, and for C++ define
`ALT_CXX_UNDER_TEST`. These will be written to the
`site.exp` file used by DejaGnu. The default is to build each
test with the compiler under test using the first of each pair of
compiler options from `COMPAT_OPTIONS`. When
`ALT_CC_UNDER_TEST` or
`ALT_CXX_UNDER_TEST` is `same`, each test is built using
the compiler under test but with combinations of the options from
`COMPAT_OPTIONS`.

To run only the C++ compatibility suite using the compiler under test
and another version of GCC using specific compiler options, do the
following from `objdir/gcc`:

```
     rm site.exp
     make -k \
       ALT_CXX_UNDER_TEST=${alt_prefix}/bin/g++ \
       COMPAT_OPTIONS="lists as shown above" \
       check-c++ \
       RUNTESTFLAGS="compat.exp"
```

A test that fails when the source files are compiled with different
compilers, but passes when the files are compiled with the same
compiler, demonstrates incompatibility of the generated code or
runtime support. A test that fails for the alternate compiler but
passes for the compiler under test probably tests for a bug that was
fixed in the compiler under test but is present in the alternate
compiler.

The binary compatibility tests support a small number of test framework
commands that appear within comments in a test file.

**`dg-require-*`**
: These commands can be used in `testname_main.suffix`
to skip the test if specific support is not available on the target.

**`dg-options`**
: The specified options are used for compiling this particular source
file, appended to the options from `COMPAT_OPTIONS`. When this
command appears in `testname_main.suffix` the options
are also used to link the test program.

**`dg-xfail-if`**
: This command can be used in a secondary source file to specify that
compilation is expected to fail for particular options on particular
targets.
