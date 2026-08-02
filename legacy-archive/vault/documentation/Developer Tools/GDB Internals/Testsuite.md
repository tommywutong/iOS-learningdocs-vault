---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_17.html
archived_at: '2026-07-15T07:31:03.759319Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Releasing%20GDB.md), [next](Hints.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Testsuite](GDB%20Internals.md#apple-krhugmjugy)

The testsuite is an important component of the GDB package.
While it is always worthwhile to encourage user testing, in practice
this is rarely sufficient; users typically use only a small subset of
the available commands, and it has proven all too common for a change
to cause a significant regression that went unnoticed for some time.

The GDB testsuite uses the DejaGNU testing framework.
DejaGNU is built using `Tcl` and `expect`. The tests
themselves are calls to various `Tcl` procs; the framework runs all the
procs and summarizes the passes and fails.

## [Using the Testsuite](GDB%20Internals.md#apple-krhugmjug4)

To run the testsuite, simply go to the GDB object directory (or to the
testsuite's objdir) and type `make check`. This just sets up some
environment variables and invokes DejaGNU's `runtest` script. While
the testsuite is running, you'll get mentions of which test file is in use,
and a mention of any unexpected passes or fails. When the testsuite is
finished, you'll get a summary that looks like this:

```
                === gdb Summary ===

# of expected passes            6016
# of unexpected failures        58
# of unexpected successes       5
# of expected failures          183
# of unresolved testcases       3
# of untested testcases         5
```

The ideal test run consists of expected passes only; however, reality
conspires to keep us from this ideal. Unexpected failures indicate
real problems, whether in GDB or in the testsuite. Expected
failures are still failures, but ones which have been decided are too
hard to deal with at the time; for instance, a test case might work
everywhere except on AIX, and there is no prospect of the AIX case
being fixed in the near future. Expected failures should not be added
lightly, since you may be masking serious bugs in GDB.
Unexpected successes are expected fails that are passing for some
reason, while unresolved and untested cases often indicate some minor
catastrophe, such as the compiler being unable to deal with a test
program.

When making any significant change to GDB, you should run the
testsuite before and after the change, to confirm that there are no
regressions. Note that truly complete testing would require that you
run the testsuite with all supported configurations and a variety of
compilers; however this is more than really necessary. In many cases
testing with a single configuration is sufficient. Other useful
options are to test one big-endian (Sparc) and one little-endian (x86)
host, a cross config with a builtin simulator (powerpc-eabi,
mips-elf), or a 64-bit host (Alpha).

If you add new functionality to GDB, please consider adding
tests for it as well; this way future GDB hackers can detect
and fix their changes that break the functionality you added.
Similarly, if you fix a bug that was not previously reported as a test
failure, please add a test case for it. Some cases are extremely
difficult to test, such as code that handles host OS failures or bugs
in particular versions of compilers, and it's OK not to try to write
tests for all of those.

DejaGNU supports separate build, host, and target machines. However,
some GDB test scripts do not work if the build machine and
the host machine are not the same. In such an environment, these scripts
will give a result of "UNRESOLVED", like this:

```
UNRESOLVED: gdb.base/example.exp: This test script does not work on a remote host.
```

## [Testsuite Organization](GDB%20Internals.md#apple-krhugmjuha)

The testsuite is entirely contained in `gdb/testsuite'. While the
testsuite includes some makefiles and configury, these are very minimal,
and used for little besides cleaning up, since the tests themselves
handle the compilation of the programs that GDB will run. The file
`testsuite/lib/gdb.exp' contains common utility procs useful for
all GDB tests, while the directory `testsuite/config' contains
configuration-specific files, typically used for special-purpose
definitions of procs like `gdb_load` and `gdb_start`.

The tests themselves are to be found in `testsuite/gdb.\*' and
subdirectories of those. The names of the test files must always end
with `.exp'. DejaGNU collects the test files by wildcarding
in the test directories, so both subdirectories and individual files
get chosen and run in alphabetical order.

The following table lists the main types of subdirectories and what they
are for. Since DejaGNU finds test files no matter where they are
located, and since each test file sets up its own compilation and
execution environment, this organization is simply for convenience and
intelligibility.

**`gdb.base'**
: This is the base testsuite. The tests in it should apply to all
configurations of GDB (but generic native-only tests may live here).
The test programs should be in the subset of C that is valid K&R,
ANSI/ISO, and C++ (`#ifdef`s are allowed if necessary, for instance
for prototypes).

**`gdb.lang'**
: Language-specific tests for any language lang besides C. Examples are
`gdb.cp' and `gdb.java'.

**`gdb.platform'**
: Non-portable tests. The tests are specific to a specific configuration
(host or target), such as HP-UX or eCos. Example is `gdb.hp', for
HP-UX.

**`gdb.compiler'**
: Tests specific to a particular compiler. As of this writing (June
1999), there aren't currently any groups of tests in this category that
couldn't just as sensibly be made platform-specific, but one could
imagine a `gdb.gcc', for tests of GDB's handling of GCC
extensions.

**`gdb.subsystem'**
: Tests that exercise a specific GDB subsystem in more depth. For
instance, `gdb.disasm' exercises various disassemblers, while
`gdb.stabs' tests pathways through the stabs symbol reader.

## [Writing Tests](GDB%20Internals.md#apple-krhugmjuhe)

In many areas, the GDB tests are already quite comprehensive; you
should be able to copy existing tests to handle new cases.

You should try to use `gdb_test` whenever possible, since it
includes cases to handle all the unexpected errors that might happen.
However, it doesn't cost anything to add new test procedures; for
instance, `gdb.base/exprs.exp' defines a `test_expr` that
calls `gdb_test` multiple times.

Only use `send_gdb` and `gdb_expect` when absolutely
necessary, such as when GDB has several valid responses to a command.

The source language programs do _not_ need to be in a consistent
style. Since GDB is used to debug programs written in many different
styles, it's worth having a mix of styles in the testsuite; for
instance, some GDB bugs involving the display of source lines would
never manifest themselves if the programs used GNU coding style
uniformly.

---

Go to the [first](Requirements.md), [previous](Releasing%20GDB.md), [next](Hints.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
