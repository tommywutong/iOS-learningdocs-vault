---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Test-Directives.html
archived_at: '2026-07-15T07:31:02.981008Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Ada Tests](Ada-Tests.md#apple-ifsgclkumvzxi4y),
Previous: [Test Idioms](Test-Idioms.md#apple-krsxg5bnjfsgs33nom),
Up: [Testsuites](Testsuites.md#apple-krsxg5dtovuxizlt)

---

#### 6.4.2 Directives used within DejaGnu tests

Test directives appear within comments in a test source file and begin
with `dg-`. Some of these are defined within DejaGnu and others
are local to the GCC testsuite.

The order in which test directives appear in a test can be important:
directives local to GCC sometimes override information used by the
DejaGnu directives, which know nothing about the GCC directives, so the
DejaGnu directives must precede GCC directives.

Several test directives include selectors which are usually preceded by
the keyword `target` or `xfail`. A selector is: one or more
target triplets, possibly including wildcard characters; a single
effective-target keyword; or a logical expression. Depending on the
context, the selector specifies whether a test is skipped and reported
as unsupported or is expected to fail. Use ``*-*-*`' to match any
target.
Effective-target keywords are defined in `target-supports.exp` in
the GCC testsuite.

A selector expression appears within curly braces and uses a single
logical operator: one of ``!`', ``&&`', or ``||`'. An
operand is another selector expression, an effective-target keyword,
a single target triplet, or a list of target triplets within quotes or
curly braces. For example:

```
     { target { ! "hppa*-*-* ia64*-*-*" } }
     { target { powerpc*-*-* && lp64 } }
     { xfail { lp64 || vect_no_align } }
```

**`{ dg-do` do-what-keyword `[{ target/xfail` selector `}] }`**
: do-what-keyword specifies how the test is compiled and whether
it is executed. It is one of:

**`preprocess`**
: Compile with `-E` to run only the preprocessor.

**`assemble`**
: Compile with `-S` to produce an assembly code file.

**`compile`**
: Compile with `-c` to produce a relocatable object file.

**`link`**
: Compile, assemble, and link to produce an executable file.

**`run`**
: Produce and run an executable file, which is expected to return
an exit code of 0.

The default is `compile`. That can be overridden for a set of
tests by redefining `dg-do-what-default` within the `.exp`
file for those tests.

If the directive includes the optional ``{ target selector }`'
then the test is skipped unless the target system is included in the
list of target triplets or matches the effective-target keyword.

If the directive includes the optional ``{ xfail selector }`'
and the selector is met then the test is expected to fail. For
`dg-do run`, execution is expected to fail but compilation
is expected to pass.

**`{ dg-options` options `[{ target` selector `}] }`**
: This DejaGnu directive provides a list of compiler options, to be used
if the target system matches selector, that replace the default
options used for this set of tests.

**`{ dg-skip-if` comment `{` selector `} {` include-opts `} {` exclude-opts `} }`**
: Skip the test if the test system is included in selector and if
each of the options in include-opts is in the set of options with
which the test would be compiled and if none of the options in
exclude-opts is in the set of options with which the test would be
compiled.

Use ``"*"`' for an empty include-opts list and ``""`' for
an empty exclude-opts list.

**`{ dg-xfail-if` comment `{` selector `} {` include-opts `} {` exclude-opts `} }`**
: Expect the test to fail if the conditions (which are the same as for
`dg-skip-if`) are met.

**`{ dg-require-`support `args }`**
: Skip the test if the target does not provide the required support;
see `gcc-dg.exp` in the GCC testsuite for the actual directives.
These directives must appear after any `dg-do` directive in the test.
They require at least one argument, which can be an empty string if the
specific procedure does not examine the argument.

**`{ dg-require-effective-target` keyword `}`**
: Skip the test if the test target, including current multilib flags,
is not covered by the effective-target keyword.
This directive must appear after any `dg-do` directive in the test.

**`{ dg-shouldfail` comment `{` selector `} {` include-opts `} {` exclude-opts `} }`**
: Expect the test executable to return a nonzero exit status if the
conditions (which are the same as for `dg-skip-if`) are met.

**`{ dg-error` regexp `[`comment `[{ target/xfail` selector `} [`line`] }]] }`**
: This DejaGnu directive appears on a source line that is expected to get
an error message, or else specifies the source line associated with the
message. If there is no message for that line or if the text of that
message is not matched by regexp then the check fails and
comment is included in the `FAIL` message. The check does
not look for the string ``"error"`' unless it is part of regexp.

**`{ dg-warning` regexp `[`comment `[{ target/xfail` selector `} [`line`] }]] }`**
: This DejaGnu directive appears on a source line that is expected to get
a warning message, or else specifies the source line associated with the
message. If there is no message for that line or if the text of that
message is not matched by regexp then the check fails and
comment is included in the `FAIL` message. The check does
not look for the string ``"warning"`' unless it is part of regexp.

**`{ dg-bogus` regexp `[`comment `[{ target/xfail` selector `} [`line`] }]] }`**
: This DejaGnu directive appears on a source line that should not get a
message matching regexp, or else specifies the source line
associated with the bogus message. It is usually used with ``xfail`'
to indicate that the message is a known problem for a particular set of
targets.

**`{ dg-excess-errors` comment `[{ target/xfail` selector `}] }`**
: This DejaGnu directive indicates that the test is expected to fail due
to compiler messages that are not handled by ``dg-error`',
``dg-warning`' or ``dg-bogus`'.

**`{ dg-output` regexp `[{ target/xfail` selector `}] }`**
: This DejaGnu directive compares regexp to the combined output
that the test executable writes to `stdout` and `stderr`.

**`{ dg-prune-output` regexp `}`**
: Prune messages matching regexp from test output.

**`{ dg-additional-files "`filelist`" }`**
: Specify additional files, other than source files, that must be copied
to the system where the compiler runs.

**`{ dg-additional-sources "`filelist`" }`**
: Specify additional source files to appear in the compile line
following the main test file.

**`{ dg-final {` local-directive `} }`**
: This DejaGnu directive is placed within a comment anywhere in the
source file and is processed after the test has been compiled and run.
Multiple ``dg-final`' commands are processed in the order in which
they appear in the source file.

The GCC testsuite defines the following directives to be used within
`dg-final`.

**`cleanup-coverage-files`**
: Removes coverage data files generated for this test.

**`cleanup-repo-files`**
: Removes files generated for this test for `-frepo`.

**`cleanup-rtl-dump` suffix**
: Removes RTL dump files generated for this test.

**`cleanup-tree-dump` suffix**
: Removes tree dump files matching suffix which were generated for
this test.

**`cleanup-saved-temps`**
: Removes files for the current test which were kept for `--save-temps`.

**`scan-file` filename regexp `[{ target/xfail` selector `}]`**
: Passes if regexp matches text in filename.

**`scan-file-not` filename regexp `[{ target/xfail` selector `}]`**
: Passes if regexp does not match text in filename.

**`scan-hidden` symbol `[{ target/xfail` selector `}]`**
: Passes if symbol is defined as a hidden symbol in the test's
assembly output.

**`scan-not-hidden` symbol `[{ target/xfail` selector `}]`**
: Passes if symbol is not defined as a hidden symbol in the test's
assembly output.

**`scan-assembler-times` regex num `[{ target/xfail` selector `}]`**
: Passes if regex is matched exactly num times in the test's
assembler output.

**`scan-assembler` regex `[{ target/xfail` selector `}]`**
: Passes if regex matches text in the test's assembler output.

**`scan-assembler-not` regex `[{ target/xfail` selector `}]`**
: Passes if regex does not match text in the test's assembler output.

**`scan-assembler-dem` regex `[{ target/xfail` selector `}]`**
: Passes if regex matches text in the test's demangled assembler output.

**`scan-assembler-dem-not` regex `[{ target/xfail` selector `}]`**
: Passes if regex does not match text in the test's demangled assembler
output.

**`scan-tree-dump-times` regex num suffix `[{ target/xfail` selector `}]`**
: Passes if regex is found exactly num times in the dump file
with suffix suffix.

**`scan-tree-dump` regex suffix `[{ target/xfail` selector `}]`**
: Passes if regex matches text in the dump file with suffix suffix.

**`scan-tree-dump-not` regex suffix `[{ target/xfail` selector `}]`**
: Passes if regex does not match text in the dump file with suffix
suffix.

**`scan-tree-dump-dem` regex suffix `[{ target/xfail` selector `}]`**
: Passes if regex matches demangled text in the dump file with
suffix suffix.

**`scan-tree-dump-dem-not` regex suffix `[{ target/xfail` selector `}]`**
: Passes if regex does not match demangled text in the dump file with
suffix suffix.

**`output-exists [{ target/xfail` selector `}]`**
: Passes if compiler output file exists.

**`output-exists-not [{ target/xfail` selector `}]`**
: Passes if compiler output file does not exist.

**`run-gcov` sourcefile**
: Check line counts in `gcov` tests.

**`run-gcov [branches] [calls] {` opts sourcefile `}`**
: Check branch and/or call counts, in addition to line counts, in
`gcov` tests.
