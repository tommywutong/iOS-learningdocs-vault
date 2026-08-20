---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_8.html
archived_at: '2026-07-15T07:31:03.885469Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Language%20Support.md), [next](Target%20Architecture%20Definition.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Host Definition](GDB%20Internals.md#apple-krhugnrq)

With the advent of Autoconf, it's rarely necessary to have host
definition machinery anymore. The following information is provided,
mainly, as an historical reference.

## [Adding a New Host](GDB%20Internals.md#apple-krhugnrr)

GDB's host configuration support normally happens via Autoconf.
New host-specific definitions should not be needed. Older hosts
GDB still use the host-specific definitions and files listed
below, but these mostly exist for historical reasons, and will
eventually disappear.

**`gdb/config/arch/xyz.mh'**
: This file once contained both host and native configuration information
(see section [Native Debugging](Native%20Debugging.md#apple-kncugojr)) for the machine xyz. The host
configuration information is now handed by Autoconf.
Host configuration information included a definition of
`XM_FILE=xm-xyz.h` and possibly definitions for `CC`,
`SYSV_DEFINE`, `XM_CFLAGS`, `XM_ADD_FILES`,
`XM_CLIBS`, `XM_CDEPS`, etc.; see `Makefile.in'.
New host only configurations do not need this file.

**`gdb/config/arch/xm-xyz.h'**
: This file once contained definitions and includes required when hosting
gdb on machine xyz. Those definitions and includes are now
handled by Autoconf.
New host and native configurations do not need this file.
_Maintainer's note: Some hosts continue to use the `xm-xyz.h'
file to define the macros HOST_FLOAT_FORMAT,
HOST_DOUBLE_FORMAT and HOST_LONG_DOUBLE_FORMAT. That code
also needs to be replaced with either an Autoconf or run-time test._

### Generic Host Support Files

There are some "generic" versions of routines that can be used by
various systems. These can be customized in various ways by macros
defined in your `xm-xyz.h' file. If these routines work for
the xyz host, you can just include the generic file's name (with
`` `.o' ``, not `` `.c' ``) in `XDEPFILES`.

Otherwise, if your machine needs custom support routines, you will need
to write routines that perform the same functions as the generic file.
Put them into `xyz-xdep.c`, and put `xyz-xdep.o`
into `XDEPFILES`.

**`ser-unix.c'**
: 

This contains serial line support for Unix systems. This is always
included, via the makefile variable `SER_HARDWIRE`; override this
variable in the `.mh' file to avoid it.

**`ser-go32.c'**
: This contains serial line support for 32-bit programs running under DOS,
using the DJGPP (a.k.a. GO32) execution environment.

**`ser-tcp.c'**
: This contains generic TCP support using sockets.

## [Host Conditionals](GDB%20Internals.md#apple-krhugnrs)

When GDB is configured and compiled, various macros are
defined or left undefined, to control compilation based on the
attributes of the host system. These macros and their meanings (or if
the meaning is not documented here, then one of the source files where
they are used is indicated) are:

**`GDBINIT_FILENAME`**
: 
The default name of GDB's initialization file (normally
`.gdbinit').

**`NO_STD_REGS`**
: 
This macro is deprecated.

**`SIGWINCH_HANDLER`**
: 
If your host defines `SIGWINCH`, you can define this to be the name
of a function to be called if `SIGWINCH` is received.

**`SIGWINCH_HANDLER_BODY`**
: 
Define this to expand into code that will define the function named by
the expansion of `SIGWINCH_HANDLER`.

**`ALIGN_STACK_ON_STARTUP`**
: 

Define this if your system is of a sort that will crash in
`tgetent` if the stack happens not to be longword-aligned when
`main` is called. This is a rare situation, but is known to occur
on several different types of systems.

**`CRLF_SOURCE_FILES`**
: 

Define this if host files use `\r\n` rather than `\n` as a
line terminator. This will cause source file listings to omit `\r`
characters when printing and it will allow `\r\n` line endings of files
which are "sourced" by gdb. It must be possible to open files in binary
mode using `O_BINARY` or, for fopen, `"rb"`.

**`DEFAULT_PROMPT`**
: 

The default value of the prompt string (normally `"(gdb) "`).

**`DEV_TTY`**
: 

The name of the generic TTY device, defaults to `"/dev/tty"`.

**`FOPEN_RB`**
: 
Define this if binary files are opened the same way as text files.

**`HAVE_MMAP`**
: 

In some cases, use the system call `mmap` for reading symbol
tables. For some machines this allows for sharing and quick updates.

**`HAVE_TERMIO`**
: 
Define this if the host system has `termio.h`.

**`INT_MAX`**
: 

**`INT_MIN`**
: 

**`LONG_MAX`**
: 

**`UINT_MAX`**
: 

**`ULONG_MAX`**
: 
Values for host-side constants.

**`ISATTY`**
: 
Substitute for isatty, if not available.

**`LONGEST`**
: 
This is the longest integer type available on the host. If not defined,
it will default to `long long` or `long`, depending on
`CC_HAS_LONG_LONG`.

**`CC_HAS_LONG_LONG`**
: 

Define this if the host C compiler supports `long long`. This is set
by the `configure` script.

**`PRINTF_HAS_LONG_LONG`**
: 
Define this if the host can handle printing of long long integers via
the printf format conversion specifier `ll`. This is set by the
`configure` script.

**`HAVE_LONG_DOUBLE`**
: 
Define this if the host C compiler supports `long double`. This is
set by the `configure` script.

**`PRINTF_HAS_LONG_DOUBLE`**
: 
Define this if the host can handle printing of long double float-point
numbers via the printf format conversion specifier `Lg`. This is
set by the `configure` script.

**`SCANF_HAS_LONG_DOUBLE`**
: 
Define this if the host can handle the parsing of long double
float-point numbers via the scanf format conversion specifier
`Lg`. This is set by the `configure` script.

**`LSEEK_NOT_LINEAR`**
: 
Define this if `lseek (n)` does not necessarily move to byte number
`n` in the file. This is only used when reading source files. It
is normally faster to define `CRLF_SOURCE_FILES` when possible.

**`L_SET`**
: 
This macro is used as the argument to `lseek` (or, most commonly,
`bfd_seek`). FIXME, should be replaced by SEEK_SET instead,
which is the POSIX equivalent.

**`NORETURN`**
: 
If defined, this should be one or more tokens, such as `volatile`,
that can be used in both the declaration and definition of functions to
indicate that they never return. The default is already set correctly
if compiling with GCC. This will almost never need to be defined.

**`ATTR_NORETURN`**
: 
If defined, this should be one or more tokens, such as
`__attribute__ ((noreturn))`, that can be used in the declarations
of functions to indicate that they never return. The default is already
set correctly if compiling with GCC. This will almost never need to be
defined.

**`SEEK_CUR`**
: 

**`SEEK_SET`**
: 
Define these to appropriate value for the system `lseek`, if not already
defined.

**`STOP_SIGNAL`**
: 
This is the signal for stopping GDB. Defaults to
`SIGTSTP`. (Only redefined for the Convex.)

**`USG`**
: 
Means that System V (prior to SVR4) include files are in use. (FIXME:
This symbol is abused in `infrun.c', `regex.c', and
`utils.c' for other things, at the moment.)

**`lint`**
: 
Define this to help placate `lint` in some situations.

**`volatile`**
: 
Define this to override the defaults of `__volatile__` or
`/**/`.

---

Go to the [first](Requirements.md), [previous](Language%20Support.md), [next](Target%20Architecture%20Definition.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
