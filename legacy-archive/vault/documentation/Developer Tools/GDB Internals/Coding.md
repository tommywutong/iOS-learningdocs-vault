---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_13.html
archived_at: '2026-07-15T07:31:03.724078Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Support%20Libraries.md), [next](Porting%20GDB.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Coding](GDB%20Internals.md#apple-krhugmjqg4)

This chapter covers topics that are lower-level than the major
algorithms of GDB.

## [Cleanups](GDB%20Internals.md#apple-krhugmjqha)

Cleanups are a structured way to deal with things that need to be done
later.

When your code does something (e.g., `xmalloc` some memory, or
`open` a file) that needs to be undone later (e.g., `xfree`
the memory or `close` the file), it can make a cleanup. The
cleanup will be done at some future point: when the command is finished
and control returns to the top level; when an error occurs and the stack
is unwound; or when your code decides it's time to explicitly perform
cleanups. Alternatively you can elect to discard the cleanups you
created.

Syntax:

**`struct cleanup *old_chain;`**
: Declare a variable which will hold a cleanup chain handle.

**`old_chain = make_cleanup (function, arg);`**
: Make a cleanup which will cause function to be called with
arg (a `char *`) later. The result, old_chain, is a
handle that can later be passed to `do_cleanups` or
`discard_cleanups`. Unless you are going to call
`do_cleanups` or `discard_cleanups`, you can ignore the result
from `make_cleanup`.

**`do_cleanups (old_chain);`**
: Do all cleanups added to the chain since the corresponding
`make_cleanup` call was made.

**`discard_cleanups (old_chain);`**
: Same as `do_cleanups` except that it just removes the cleanups from
the chain and does not call the specified functions.

Cleanups are implemented as a chain. The handle returned by
`make_cleanups` includes the cleanup passed to the call and any
later cleanups appended to the chain (but not yet discarded or
performed). E.g.:

```
make_cleanup (a, 0);
{
  struct cleanup *old = make_cleanup (b, 0);
  make_cleanup (c, 0)
  ...
  do_cleanups (old);
}
```

will call `c()` and `b()` but will not call `a()`. The
cleanup that calls `a()` will remain in the cleanup chain, and will
be done later unless otherwise discarded.

Your function should explicitly do or discard the cleanups it creates.
Failing to do this leads to non-deterministic behavior since the caller
will arbitrarily do or discard your functions cleanups. This need leads
to two common cleanup styles.

The first style is try/finally. Before it exits, your code-block calls
`do_cleanups` with the old cleanup chain and thus ensures that your
code-block's cleanups are always performed. For instance, the following
code-segment avoids a memory leak problem (even when `error` is
called and a forced stack unwind occurs) by ensuring that the
`xfree` will always be called:

```
struct cleanup *old = make_cleanup (null_cleanup, 0);
data = xmalloc (sizeof blah);
make_cleanup (xfree, data);
... blah blah ...
do_cleanups (old);
```

The second style is try/except. Before it exits, your code-block calls
`discard_cleanups` with the old cleanup chain and thus ensures that
any created cleanups are not performed. For instance, the following
code segment, ensures that the file will be closed but only if there is
an error:

```
FILE *file = fopen ("afile", "r");
struct cleanup *old = make_cleanup (close_file, file);
... blah blah ...
discard_cleanups (old);
return file;
```

Some functions, e.g. `fputs_filtered()` or `error()`, specify
that they "should not be called when cleanups are not in place". This
means that any actions you need to reverse in the case of an error or
interruption must be on the cleanup chain before you call these
functions, since they might never return to your code (they
`` `longjmp' `` instead).

## [Per-architecture module data](GDB%20Internals.md#apple-krhugmjqhe)

The multi-arch framework includes a mechanism for adding module
specific per-architecture data-pointers to the `struct gdbarch`
architecture object.

A module registers one or more per-architecture data-pointers using:

**Function: struct __gdbarch_data__ _\*gdbarch_data_register_pre_init (gdbarch_data_pre_init_ftype \*pre_init)_**
: 
pre_init is used to, on-demand, allocate an initial value for a
per-architecture data-pointer using the architecture's obstack (passed
in as a parameter). Since pre_init can be called during
architecture creation, it is not parameterized with the architecture.
and must not call modules that use per-architecture data.

**Function: struct __gdbarch_data__ _\*gdbarch_data_register_post_init (gdbarch_data_post_init_ftype \*post_init)_**
: 
post_init is used to obtain an initial value for a
per-architecture data-pointer _after_. Since post_init is
always called after architecture creation, it both receives the fully
initialized architecture and is free to call modules that use
per-architecture data (care needs to be taken to ensure that those
other modules do not try to call back to this module as that will
create in cycles in the initialization call graph).

These functions return a `struct gdbarch_data` that is used to
identify the per-architecture data-pointer added for that module.

The per-architecture data-pointer is accessed using the function:

**Function: void __\*gdbarch_data__ _(struct gdbarch \*gdbarch, struct gdbarch_data \*data_handle)_**
: 
Given the architecture arch and module data handle
data_handle (returned by `gdbarch_data_register_pre_init`
or `gdbarch_data_register_post_init`), this function returns the
current value of the per-architecture data-pointer. If the data
pointer is `NULL`, it is first initialized by calling the
corresponding pre_init or post_init method.

The examples below assume the following definitions:

```
struct nozel { int total; };
static struct gdbarch_data *nozel_handle;
```

A module can extend the architecture vector, adding additional
per-architecture data, using the pre_init method. The module's
per-architecture data is then initialized during architecture
creation.

In the below, the module's per-architecture _nozel_ is added. An
architecture can specify its nozel by calling `set_gdbarch_nozel`
from `gdbarch_init`.

```
static void *
nozel_pre_init (struct obstack *obstack)
{
  struct nozel *data = OBSTACK_ZALLOC (obstack, struct nozel);
  return data;
}
```

```swift
extern void
set_gdbarch_nozel (struct gdbarch *gdbarch, int total)
{
  struct nozel *data = gdbarch_data (gdbarch, nozel_handle);
  data->total = nozel;
}
```

A module can on-demand create architecture dependant data structures
using `post_init`.

In the below, the nozel's total is computed on-demand by
`nozel_post_init` using information obtained from the
architecture.

```swift
static void *
nozel_post_init (struct gdbarch *gdbarch)
{
  struct nozel *data = GDBARCH_OBSTACK_ZALLOC (gdbarch, struct nozel);
  nozel->total = gdbarch... (gdbarch);
  return data;
}
```

```swift
extern int
nozel_total (struct gdbarch *gdbarch)
{
  struct nozel *data = gdbarch_data (gdbarch, nozel_handle);
  return data->total;
}
```

## [Wrapping Output Lines](GDB%20Internals.md#apple-krhugmjrga)

Output that goes through `printf_filtered` or `fputs_filtered`
or `fputs_demangled` needs only to have calls to `wrap_here`
added in places that would be good breaking points. The utility
routines will take care of actually wrapping if the line width is
exceeded.

The argument to `wrap_here` is an indentation string which is
printed _only_ if the line breaks there. This argument is saved
away and used later. It must remain valid until the next call to
`wrap_here` or until a newline has been printed through the
`*_filtered` functions. Don't pass in a local variable and then
return!

It is usually best to call `wrap_here` after printing a comma or
space. If you call it before printing a space, make sure that your
indentation properly accounts for the leading space that will print if
the line wraps there.

Any function or set of functions that produce filtered output must
finish by printing a newline, to flush the wrap buffer, before switching
to unfiltered (`printf`) output. Symbol reading routines that
print warnings are a good example.

## [GDB Coding Standards](GDB%20Internals.md#apple-krhugmjrge)

GDB follows the GNU coding standards, as described in
`etc/standards.texi'. This file is also available for anonymous
FTP from GNU archive sites. GDB takes a strict interpretation
of the standard; in general, when the GNU standard recommends a practice
but does not require it, GDB requires it.

GDB follows an additional set of coding standards specific to
GDB, as described in the following sections.

### [ISO C](GDB%20Internals.md#apple-krhugmjrgi)

GDB assumes an ISO/IEC 9899:1990 (a.k.a. ISO C90) compliant
compiler.

GDB does not assume an ISO C or POSIX compliant C library.

### [Memory Management](GDB%20Internals.md#apple-krhugmjrgm)

GDB does not use the functions `malloc`, `realloc`,
`calloc`, `free` and `asprintf`.

GDB uses the functions `xmalloc`, `xrealloc` and
`xcalloc` when allocating memory. Unlike `malloc` et.al.
these functions do not return when the memory pool is empty. Instead,
they unwind the stack using cleanups. These functions return
`NULL` when requested to allocate a chunk of memory of size zero.

_Pragmatics: By using these functions, the need to check every
memory allocation is removed. These functions provide portable
behavior._

GDB does not use the function `free`.

GDB uses the function `xfree` to return memory to the
memory pool. Consistent with ISO-C, this function ignores a request to
free a `NULL` pointer.

_Pragmatics: On some systems `free` fails when passed a
`NULL` pointer._

GDB can use the non-portable function `alloca` for the
allocation of small temporary values (such as strings).

_Pragmatics: This function is very non-portable. Some systems
restrict the memory being allocated to no more than a few kilobytes._

GDB uses the string function `xstrdup` and the print
function `xstrprintf`.

_Pragmatics: `asprintf` and `strdup` can fail. Print
functions such as `sprintf` are very prone to buffer overflow
errors._

### [Compiler Warnings](GDB%20Internals.md#apple-krhugmjrgq)

With few exceptions, developers should include the configuration option
`` `--enable-gdb-build-warnings=,-Werror' `` when building GDB.
The exceptions are listed in the file `gdb/MAINTAINERS'.

This option causes GDB (when built using GCC) to be compiled
with a carefully selected list of compiler warning flags. Any warnings
from those flags being treated as errors.

The current list of warning flags includes:

**`` `-Wimplicit' ``**
: Since GDB coding standard requires all functions to be declared
using a prototype, the flag has the side effect of ensuring that
prototyped functions are always visible with out resorting to
`` `-Wstrict-prototypes' ``.

**`` `-Wreturn-type' ``**
: Such code often appears to work except on instruction set architectures
that use register windows.

**`` `-Wcomment' ``**
:

**`` `-Wtrigraphs' ``**
:

**`` `-Wformat' ``**
:

**`` `-Wformat-nonliteral' ``**
: Since GDB uses the `format printf` attribute on all
`printf` like functions these check not just `printf` calls
but also calls to functions such as `fprintf_unfiltered`.

**`` `-Wparentheses' ``**
: This warning includes uses of the assignment operator within an
`if` statement.

**`` `-Wpointer-arith' ``**
:

**`` `-Wuninitialized' ``**
:

**`` `-Wunused-label' ``**
: This warning has the additional benefit of detecting the absence of the
`case` reserved word in a switch statement:

```
enum { FD_SCHEDULED, NOTHING_SCHEDULED } sched;
...
switch (sched)
  {
  case FD_SCHEDULED:
    ...;
    break;
  NOTHING_SCHEDULED:
    ...;
    break;
  }
```

**`` `-Wunused-function' ``**
:

_Pragmatics: Due to the way that GDB is implemented most
functions have unused parameters. Consequently the warning
`` `-Wunused-parameter' `` is precluded from the list. The macro
`ATTRIBUTE_UNUSED` is not used as it leads to false negatives ---
it is not an error to have `ATTRIBUTE_UNUSED` on a parameter that
is being used. The options `` `-Wall' `` and `` `-Wunused' `` are also
precluded because they both include `` `-Wunused-parameter' ``._

_Pragmatics: GDB has not simply accepted the warnings
enabled by `` `-Wall -Werror -W...' ``. Instead it is selecting warnings
when and where their benefits can be demonstrated._

### [Formatting](GDB%20Internals.md#apple-krhugmjrgu)

The standard GNU recommendations for formatting must be followed
strictly.

A function declaration should not have its name in column zero. A
function definition should have its name in column zero.

```
/* Declaration */
static void foo (void);
/* Definition */
void
foo (void)
{
}
```

_Pragmatics: This simplifies scripting. Function definitions can
be found using `` `^function-name' ``._

There must be a space between a function or macro name and the opening
parenthesis of its argument list (except for macro definitions, as
required by C). There must not be a space after an open paren/bracket
or before a close paren/bracket.

While additional whitespace is generally helpful for reading, do not use
more than one blank line to separate blocks, and avoid adding whitespace
after the end of a program line (as of 1/99, some 600 lines had
whitespace after the semicolon). Excess whitespace causes difficulties
for `diff` and `patch` utilities.

Pointers are declared using the traditional K&R C style:

```
void *foo;
```

and not:

```
void * foo;
void* foo;
```

### [Comments](GDB%20Internals.md#apple-krhugmjrgy)

The standard GNU requirements on comments must be followed strictly.

Block comments must appear in the following form, with no `/*`- or
`*/`-only lines, and no leading `*`:

```
/* Wait for control to return from inferior to debugger.  If inferior
   gets a signal, we may decide to start it up again instead of
   returning.  That is why there is a loop in this function.  When
   this function actually returns it means the inferior should be left
   stopped and GDB should read more commands.  */
```

(Note that this format is encouraged by Emacs; tabbing for a multi-line
comment works correctly, and `M-q` fills the block consistently.)

Put a blank line between the block comments preceding function or
variable definitions, and the definition itself.

In general, put function-body comments on lines by themselves, rather
than trying to fit them into the 20 characters left at the end of a
line, since either the comment or the code will inevitably get longer
than will fit, and then somebody will have to move it anyhow.

### [C Usage](GDB%20Internals.md#apple-krhugmjrg4)

Code must not depend on the sizes of C data types, the format of the
host's floating point numbers, the alignment of anything, or the order
of evaluation of expressions.

Use functions freely. There are only a handful of compute-bound areas
in GDB that might be affected by the overhead of a function
call, mainly in symbol reading. Most of GDB's performance is
limited by the target interface (whether serial line or system call).

However, use functions with moderation. A thousand one-line functions
are just as hard to understand as a single thousand-line function.

_Macros are bad, M'kay._
(But if you have to use a macro, make sure that the macro arguments are
protected with parentheses.)

Declarations like `` `struct foo *' `` should be used in preference to
declarations like `` `typedef struct foo { ... } *foo_ptr' ``.

### [Function Prototypes](GDB%20Internals.md#apple-krhugmjrha)

Prototypes must be used when both _declaring_ and _defining_
a function. Prototypes for GDB functions must include both the
argument type and name, with the name matching that used in the actual
function definition.

All external functions should have a declaration in a header file that
callers include, except for `_initialize_*` functions, which must
be external so that `init.c' construction works, but shouldn't be
visible to random source files.

Where a source file needs a forward declaration of a static function,
that declaration must appear in a block near the top of the source file.

### [Internal Error Recovery](GDB%20Internals.md#apple-krhugmjrhe)

During its execution, GDB can encounter two types of errors.
User errors and internal errors. User errors include not only a user
entering an incorrect command but also problems arising from corrupt
object files and system errors when interacting with the target.
Internal errors include situations where GDB has detected, at
run time, a corrupt or erroneous situation.

When reporting an internal error, GDB uses
`internal_error` and `gdb_assert`.

GDB must not call `abort` or `assert`.

_Pragmatics: There is no `internal_warning` function. Either
the code detected a user error, recovered from it and issued a
`warning` or the code failed to correctly recover from the user
error and issued an `internal_error`._

### [File Names](GDB%20Internals.md#apple-krhugmjsga)

Any file used when building the core of GDB must be in lower
case. Any file used when building the core of GDB must be 8.3
unique. These requirements apply to both source and generated files.

_Pragmatics: The core of GDB must be buildable on many
platforms including DJGPP and MacOS/HFS. Every time an unfriendly file
is introduced to the build process both `Makefile.in' and
`configure.in' need to be modified accordingly. Compare the
convoluted conversion process needed to transform `COPYING' into
`copying.c' with the conversion needed to transform
`version.in' into `version.c'._

Any file non 8.3 compliant file (that is not used when building the core
of GDB) must be added to `gdb/config/djgpp/fnchange.lst'.

_Pragmatics: This is clearly a compromise._

When GDB has a local version of a system header file (ex
`string.h') the file name based on the POSIX header prefixed with
`gdb_' (`gdb_string.h'). These headers should be relatively
independent: they should use only macros defined by `configure',
the compiler, or the host; they should include only system headers; they
should refer only to system types. They may be shared between multiple
programs, e.g. GDB and GDBSERVER.

For other files `` `-' `` is used as the separator.

### [Include Files](GDB%20Internals.md#apple-krhugmjsge)

A `.c' file should include `defs.h' first.

A `.c' file should directly include the `.h` file of every
declaration and/or definition it directly refers to. It cannot rely on
indirect inclusion.

A `.h' file should directly include the `.h` file of every
declaration and/or definition it directly refers to. It cannot rely on
indirect inclusion. Exception: The file `defs.h' does not need to
be directly included.

An external declaration should only appear in one include file.

An external declaration should never appear in a `.c` file.
Exception: a declaration for the `_initialize` function that
pacifies @option{-Wmissing-declaration}.

A `typedef` definition should only appear in one include file.

An opaque `struct` declaration can appear in multiple `.h'
files. Where possible, a `.h' file should use an opaque
`struct` declaration instead of an include.

All `.h' files should be wrapped in:

```
#ifndef INCLUDE_FILE_NAME_H
#define INCLUDE_FILE_NAME_H
header body
#endif
```

### [Clean Design and Portable Implementation](GDB%20Internals.md#apple-krhugmjsgi)

In addition to getting the syntax right, there's the little question of
semantics. Some things are done in certain ways in GDB because long
experience has shown that the more obvious ways caused various kinds of
trouble.

You can't assume the byte order of anything that comes from a target
(including values, object files, and instructions). Such things
must be byte-swapped using `SWAP_TARGET_AND_HOST` in
GDB, or one of the swap routines defined in `bfd.h',
such as `bfd_get_32`.

You can't assume that you know what interface is being used to talk to
the target system. All references to the target must go through the
current `target_ops` vector.

You can't assume that the host and target machines are the same machine
(except in the "native" support modules). In particular, you can't
assume that the target machine's header files will be available on the
host machine. Target code must bring along its own header files --
written from scratch or explicitly donated by their owner, to avoid
copyright problems.

Insertion of new `#ifdef`'s will be frowned upon. It's much better
to write the code portably than to conditionalize it for various
systems.

New `#ifdef`'s which test for specific compilers or manufacturers
or operating systems are unacceptable. All `#ifdef`'s should test
for features. The information about which configurations contain which
features should be segregated into the configuration files. Experience
has proven far too often that a feature unique to one particular system
often creeps into other systems; and that a conditional based on some
predefined macro for your current system will become worthless over
time, as new versions of your system come out that behave differently
with regard to this feature.

Adding code that handles specific architectures, operating systems,
target interfaces, or hosts, is not acceptable in generic code.

One particularly notorious area where system dependencies tend to
creep in is handling of file names. The mainline GDB code
assumes Posix semantics of file names: absolute file names begin with
a forward slash `/', slashes are used to separate leading
directories, case-sensitive file names. These assumptions are not
necessarily true on non-Posix systems such as MS-Windows. To avoid
system-dependent code where you need to take apart or construct a file
name, use the following portable macros:

**`HAVE_DOS_BASED_FILE_SYSTEM`**
: 
This preprocessing symbol is defined to a non-zero value on hosts
whose filesystems belong to the MS-DOS/MS-Windows family. Use this
symbol to write conditional code which should only be compiled for
such hosts.

**`IS_DIR_SEPARATOR (c)`**
: Evaluates to a non-zero value if c is a directory separator
character. On Unix and GNU/Linux systems, only a slash `/' is
such a character, but on Windows, both `/' and `\' will
pass.

**`IS_ABSOLUTE_PATH (file)`**
: Evaluates to a non-zero value if file is an absolute file name.
For Unix and GNU/Linux hosts, a name which begins with a slash
`/' is absolute. On DOS and Windows, `d:/foo' and
`x:\bar' are also absolute file names.

**`FILENAME_CMP (f1, f2)`**
: Calls a function which compares file names f1 and f2 as
appropriate for the underlying host filesystem. For Posix systems,
this simply calls `strcmp`; on case-insensitive filesystems it
will call `strcasecmp` instead.

**`DIRNAME_SEPARATOR`**
: Evaluates to a character which separates directories in
`PATH`-style lists, typically held in environment variables.
This character is `` `:' `` on Unix, `` `;' `` on DOS and Windows.

**`SLASH_STRING`**
: This evaluates to a constant string you should use to produce an
absolute filename from leading directories and the file's basename.
`SLASH_STRING` is `"/"` on most systems, but might be
`"\\"` for some Windows-based ports.

In addition to using these macros, be sure to use portable library
functions whenever possible. For example, to extract a directory or a
basename part from a file name, use the `dirname` and
`basename` library functions (available in `libiberty` for
platforms which don't provide them), instead of searching for a slash
with `strrchr`.

Another way to generalize GDB along a particular interface is with an
attribute struct. For example, GDB has been generalized to handle
multiple kinds of remote interfaces--not by `#ifdef`s everywhere, but
by defining the `target_ops` structure and having a current target (as
well as a stack of targets below it, for memory references). Whenever
something needs to be done that depends on which remote interface we are
using, a flag in the current target_ops structure is tested (e.g.,
`target_has_stack`), or a function is called through a pointer in the
current target_ops structure. In this way, when a new remote interface
is added, only one module needs to be touched--the one that actually
implements the new remote interface. Other examples of
attribute-structs are BFD access to multiple kinds of object file
formats, or GDB's access to multiple source languages.

Please avoid duplicating code. For example, in GDB 3.x all
the code interfacing between `ptrace` and the rest of
GDB was duplicated in `\*-dep.c', and so changing
something was very painful. In GDB 4.x, these have all been
consolidated into `infptrace.c'. `infptrace.c' can deal
with variations between systems the same way any system-independent
file would (hooks, `#if defined`, etc.), and machines which are
radically different don't need to use `infptrace.c' at all.

All debugging code must be controllable using the `` `set debug
module' `` command. Do not use `printf` to print trace
messages. Use `fprintf_unfiltered(gdb_stdlog, ...`. Do not use
`#ifdef DEBUG`.

---

Go to the [first](Requirements.md), [previous](Support%20Libraries.md), [next](Porting%20GDB.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
