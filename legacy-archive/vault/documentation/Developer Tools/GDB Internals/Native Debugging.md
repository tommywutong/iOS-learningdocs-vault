---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_11.html
archived_at: '2026-07-15T07:31:03.709684Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Target%20Vector%20Definition.md), [next](Support%20Libraries.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Native Debugging](GDB%20Internals.md#apple-krhugojr)

Several files control GDB's configuration for native support:

**`gdb/config/arch/xyz.mh'**
: 
Specifies Makefile fragments needed by a _native_ configuration on
machine xyz. In particular, this lists the required
native-dependent object files, by defining `` `NATDEPFILES=...' ``.
Also specifies the header file which describes native support on
xyz, by defining `` `NAT_FILE= nm-xyz.h' ``. You can also
define `` `NAT_CFLAGS' ``, `` `NAT_ADD_FILES' ``, `` `NAT_CLIBS' ``,
`` `NAT_CDEPS' ``, etc.; see `Makefile.in'.
_Maintainer's note: The `.mh' suffix is because this file
originally contained `Makefile' fragments for hosting GDB
on machine xyz. While the file is no longer used for this
purpose, the `.mh' suffix remains. Perhaps someone will
eventually rename these fragments so that they have a `.mn'
suffix._

**`gdb/config/arch/nm-xyz.h'**
: (`nm.h' is a link to this file, created by `configure`). Contains C
macro definitions describing the native system environment, such as
child process control and core file support.

**`gdb/xyz-nat.c'**
: Contains any miscellaneous C code required for this native support of
this machine. On some machines it doesn't exist at all.

There are some "generic" versions of routines that can be used by
various systems. These can be customized in various ways by macros
defined in your `nm-xyz.h' file. If these routines work for
the xyz host, you can just include the generic file's name (with
`` `.o' ``, not `` `.c' ``) in `NATDEPFILES`.

Otherwise, if your machine needs custom support routines, you will need
to write routines that perform the same functions as the generic file.
Put them into `xyz-nat.c', and put `xyz-nat.o'
into `NATDEPFILES`.

**`inftarg.c'**
: This contains the _target_ops vector_ that supports Unix child
processes on systems which use ptrace and wait to control the child.

**`procfs.c'**
: This contains the _target_ops vector_ that supports Unix child
processes on systems which use /proc to control the child.

**`fork-child.c'**
: This does the low-level grunge that uses Unix system calls to do a "fork
and exec" to start up a child process.

**`infptrace.c'**
: This is the low level interface to inferior processes for systems using
the Unix `ptrace` call in a vanilla way.

## [Native core file Support](GDB%20Internals.md#apple-krhugojs)

**`core-aout.c::fetch_core_registers()'**
: 
Support for reading registers out of a core file. This routine calls
`register_addr()`, see below. Now that BFD is used to read core
files, virtually all machines should use `core-aout.c`, and should
just provide `fetch_core_registers` in `xyz-nat.c` (or
`REGISTER_U_ADDR` in `nm-xyz.h`).

**`core-aout.c::register_addr()'**
: If your `nm-xyz.h` file defines the macro
`REGISTER_U_ADDR(addr, blockend, regno)`, it should be defined to
set `addr` to the offset within the `` `user' `` struct of GDB
register number `regno`. `blockend` is the offset within the
"upage" of `u.u_ar0`. If `REGISTER_U_ADDR` is defined,
`core-aout.c' will define the `register_addr()` function and
use the macro in it. If you do not define `REGISTER_U_ADDR`, but
you are using the standard `fetch_core_registers()`, you will need
to define your own version of `register_addr()`, put it into your
`xyz-nat.c` file, and be sure `xyz-nat.o` is in
the `NATDEPFILES` list. If you have your own
`fetch_core_registers()`, you may not need a separate
`register_addr()`. Many custom `fetch_core_registers()`
implementations simply locate the registers themselves.

When making GDB run native on a new operating system, to make it
possible to debug core files, you will need to either write specific
code for parsing your OS's core files, or customize
`bfd/trad-core.c'. First, use whatever `#include` files your
machine uses to define the struct of registers that is accessible
(possibly in the u-area) in a core file (rather than
`machine/reg.h'), and an include file that defines whatever header
exists on a core file (e.g. the u-area or a `struct core`). Then
modify `trad_unix_core_file_p` to use these values to set up the
section information for the data segment, stack segment, any other
segments in the core file (perhaps shared library contents or control
information), "registers" segment, and if there are two discontiguous
sets of registers (e.g. integer and float), the "reg2" segment. This
section information basically delimits areas in the core file in a
standard way, which the section-reading routines in BFD know how to seek
around in.

Then back in GDB, you need a matching routine called
`fetch_core_registers`. If you can use the generic one, it's in
`core-aout.c'; if not, it's in your `xyz-nat.c' file.
It will be passed a char pointer to the entire "registers" segment,
its length, and a zero; or a char pointer to the entire "regs2"
segment, its length, and a 2. The routine should suck out the supplied
register values and install them into GDB's "registers" array.

If your system uses `/proc' to control processes, and uses ELF
format core files, then you may be able to use the same routines for
reading the registers out of processes and out of core files.

## [ptrace](GDB%20Internals.md#apple-krhugojt)

## [/proc](GDB%20Internals.md#apple-krhugoju)

## [win32](GDB%20Internals.md#apple-krhugojv)

## [shared libraries](GDB%20Internals.md#apple-krhugojw)

## [Native Conditionals](GDB%20Internals.md#apple-krhugojx)

When GDB is configured and compiled, various macros are
defined or left undefined, to control compilation when the host and
target systems are the same. These macros should be defined (or left
undefined) in `nm-system.h'.

**`CHILD_PREPARE_TO_STORE`**
: 
If the machine stores all registers at once in the child process, then
define this to ensure that all values are correct. This usually entails
a read from the child.
[Note that this is incorrectly defined in `xm-system.h' files
currently.]

**`FETCH_INFERIOR_REGISTERS`**
: 
Define this if the native-dependent code will provide its own routines
`fetch_inferior_registers` and `store_inferior_registers` in
`host-nat.c'. If this symbol is _not_ defined, and
`infptrace.c' is included in this configuration, the default
routines in `infptrace.c' are used for these functions.

**`FP0_REGNUM`**
: 
This macro is normally defined to be the number of the first floating
point register, if the machine has such registers. As such, it would
appear only in target-specific code. However, `/proc' support uses this
to decide whether floats are in use on this target.

**`GET_LONGJMP_TARGET`**
: 
For most machines, this is a target-dependent parameter. On the
DECstation and the Iris, this is a native-dependent parameter, since
`setjmp.h' is needed to define it.
This macro determines the target PC address that `longjmp` will jump to,
assuming that we have just stopped at a longjmp breakpoint. It takes a
`CORE_ADDR *` as argument, and stores the target PC value through this
pointer. It examines the current state of the machine as needed.

**`I386_USE_GENERIC_WATCHPOINTS`**
: An x86-based machine can define this to use the generic x86 watchpoint
support; see section [Algorithms](Algorithms.md#apple-kncugnq).

**`KERNEL_U_ADDR`**
: 
Define this to the address of the `u` structure (the "user
struct", also known as the "u-page") in kernel virtual memory. GDB
needs to know this so that it can subtract this address from absolute
addresses in the upage, that are obtained via ptrace or from core files.
On systems that don't need this value, set it to zero.

**`KERNEL_U_ADDR_HPUX`**
: 
Define this to cause GDB to determine the address of `u` at
runtime, by using HP-style `nlist` on the kernel's image in the
root directory.

**`ONE_PROCESS_WRITETEXT`**
: 
Define this to be able to, when a breakpoint insertion fails, warn the
user that another process may be running with the same executable.

**`PROC_NAME_FMT`**
: 
Defines the format for the name of a `/proc' device. Should be
defined in `nm.h' _only_ in order to override the default
definition in `procfs.c'.

**`PTRACE_ARG3_TYPE`**
: 
The type of the third argument to the `ptrace` system call, if it
exists and is different from `int`.

**`REGISTER_U_ADDR`**
: 
Defines the offset of the registers in the "u area".

**`SHELL_COMMAND_CONCAT`**
: 
If defined, is a string to prefix on the shell command used to start the
inferior.

**`SHELL_FILE`**
: 
If defined, this is the name of the shell to use to run the inferior.
Defaults to `"/bin/sh"`.

**`SOLIB_ADD (filename, from_tty, targ, readsyms)`**
: 
Define this to expand into an expression that will cause the symbols in
filename to be added to GDB's symbol table. If
readsyms is zero symbols are not read but any necessary low level
processing for filename is still done.

**`SOLIB_CREATE_INFERIOR_HOOK`**
: 
Define this to expand into any shared-library-relocation code that you
want to be run just after the child process has been forked.

**`START_INFERIOR_TRAPS_EXPECTED`**
: 
When starting an inferior, GDB normally expects to trap
twice; once when
the shell execs, and once when the program itself execs. If the actual
number of traps is something other than 2, then define this macro to
expand into the number expected.

**`USE_PROC_FS`**
: 
This determines whether small routines in `\*-tdep.c', which
translate register values between GDB's internal
representation and the `/proc' representation, are compiled.

**`U_REGS_OFFSET`**
: 
This is the offset of the registers in the upage. It need only be
defined if the generic ptrace register access routines in
`infptrace.c' are being used (that is, `infptrace.c' is
configured in, and `FETCH_INFERIOR_REGISTERS` is not defined). If
the default value from `infptrace.c' is good enough, leave it
undefined.
The default value means that u.u_ar0 _points to_ the location of
the registers. I'm guessing that `#define U_REGS_OFFSET 0` means
that `u.u_ar0` _is_ the location of the registers.

**`CLEAR_SOLIB`**
: 
See `objfiles.c'.

**`DEBUG_PTRACE`**
: 
Define this to debug `ptrace` calls.

---

Go to the [first](Requirements.md), [previous](Target%20Vector%20Definition.md), [next](Support%20Libraries.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
