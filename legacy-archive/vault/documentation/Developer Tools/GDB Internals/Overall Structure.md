---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_2.html
archived_at: '2026-07-15T07:31:03.779760Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Requirements.md), [next](Algorithms.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Overall Structure](GDB%20Internals.md#apple-krhugmq)

GDB consists of three major subsystems: user interface,
symbol handling (the __symbol side__), and target system handling (the
__target side__).

The user interface consists of several actual interfaces, plus
supporting code.

The symbol side consists of object file readers, debugging info
interpreters, symbol table management, source language expression
parsing, type and value printing.

The target side consists of execution control, stack frame analysis, and
physical target manipulation.

The target side/symbol side division is not formal, and there are a
number of exceptions. For instance, core file support involves symbolic
elements (the basic core file reader is in BFD) and target elements (it
supplies the contents of memory and the values of registers). Instead,
this division is useful for understanding how the minor subsystems
should fit together.

## [The Symbol Side](GDB%20Internals.md#apple-krhugmy)

The symbolic side of GDB can be thought of as "everything
you can do in GDB without having a live program running".
For instance, you can look at the types of variables, and evaluate
many kinds of expressions.

## [The Target Side](GDB%20Internals.md#apple-krhugna)

The target side of GDB is the "bits and bytes manipulator".
Although it may make reference to symbolic info here and there, most
of the target side will run with only a stripped executable
available--or even no executable at all, in remote debugging cases.

Operations such as disassembly, stack frame crawls, and register
display, are able to work with no symbolic info at all. In some cases,
such as disassembly, GDB will use symbolic info to present addresses
relative to symbols rather than as raw numbers, but it will work either
way.

## [Configurations](GDB%20Internals.md#apple-krhugni)

__Host__ refers to attributes of the system where GDB runs.
__Target__ refers to the system where the program being debugged
executes. In most cases they are the same machine, in which case a
third type of __Native__ attributes come into play.

Defines and include files needed to build on the host are host support.
Examples are tty support, system defined types, host byte order, host
float format.

Defines and information needed to handle the target format are target
dependent. Examples are the stack frame format, instruction set,
breakpoint instruction, registers, and how to set up and tear down the stack
to call a function.

Information that is only needed when the host and target are the same,
is native dependent. One example is Unix child process support; if the
host and target are not the same, doing a fork to start the target
process is a bad idea. The various macros needed for finding the
registers in the `upage`, running `ptrace`, and such are all
in the native-dependent files.

Another example of native-dependent code is support for features that
are really part of the target environment, but which require
`#include` files that are only available on the host system. Core
file handling and `setjmp` handling are two common cases.

When you want to make GDB work "native" on a particular machine, you
have to include all three kinds of information.

---

Go to the [first](Requirements.md), [previous](Requirements.md), [next](Algorithms.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
