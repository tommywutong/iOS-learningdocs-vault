---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Test-Idioms.html
archived_at: '2026-07-15T07:31:00.907360Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Test Directives](Test-Directives.md#apple-krsxg5bniruxezldoruxmzlt),
Up: [Testsuites](Testsuites.md#apple-krsxg5dtovuxizlt)

---

#### 6.4.1 Idioms Used in Testsuite Code

In general C testcases have a trailing `-n.c`, starting
with `-1.c`, in case other testcases with similar names are added
later. If the test is a test of some well-defined feature, it should
have a name referring to that feature such as
`feature-1.c`. If it does not test a well-defined feature
but just happens to exercise a bug somewhere in the compiler, and a
bug report has been filed for this bug in the GCC bug database,
`prbug-number-1.c` is the appropriate form of name.
Otherwise (for miscellaneous bugs not filed in the GCC bug database),
and previously more generally, test cases are named after the date on
which they were added. This allows people to tell at a glance whether
a test failure is because of a recently found bug that has not yet
been fixed, or whether it may be a regression, but does not give any
other information about the bug or where discussion of it may be
found. Some other language testsuites follow similar conventions.

In the `gcc.dg` testsuite, it is often necessary to test that an
error is indeed a hard error and not just a warning—for example,
where it is a constraint violation in the C standard, which must
become an error with `-pedantic-errors`. The following idiom,
where the first line shown is line line of the file and the line
that generates the error, is used for this:

```
     /* { dg-bogus "warning" "warning in place of error" } */
     /* { dg-error "regexp" "message" { target *-*-* } line } */
```

It may be necessary to check that an expression is an integer constant
expression and has a certain value. To check that E has
value V, an idiom similar to the following is used:

```
     char x[((E) == (V) ? 1 : -1)];
```

In `gcc.dg` tests, `__typeof__` is sometimes used to make
assertions about the types of expressions. See, for example,
`gcc.dg/c99-condexpr-1.c`. The more subtle uses depend on the
exact rules for the types of conditional expressions in the C
standard; see, for example, `gcc.dg/c99-intconst-1.c`.

It is useful to be able to test that optimizations are being made
properly. This cannot be done in all cases, but it can be done where
the optimization will lead to code being optimized away (for example,
where flow analysis or alias analysis should show that certain code
cannot be called) or to functions not being called because they have
been expanded as built-in functions. Such tests go in
`gcc.c-torture/execute`. Where code should be optimized away, a
call to a nonexistent function such as `link_failure ()` may be
inserted; a definition

```
     #ifndef __OPTIMIZE__
     void
     link_failure (void)
     {
       abort ();
     }
     #endif
```

will also be needed so that linking still succeeds when the test is
run without optimization. When all calls to a built-in function
should have been optimized and no calls to the non-built-in version of
the function should remain, that function may be defined as
`static` to call `abort ()` (although redeclaring a function
as static may not work on all targets).

All testcases must be portable. Target-specific testcases must have
appropriate code to avoid causing failures on unsupported systems;
unfortunately, the mechanisms for this differ by directory.

FIXME: discuss non-C testsuites here.
