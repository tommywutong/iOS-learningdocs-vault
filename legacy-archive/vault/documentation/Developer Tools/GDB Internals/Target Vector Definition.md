---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_10.html
archived_at: '2026-07-15T07:31:03.704147Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Target%20Architecture%20Definition.md), [next](Native%20Debugging.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Target Vector Definition](GDB%20Internals.md#apple-krhugobu)

The target vector defines the interface between GDB's
abstract handling of target systems, and the nitty-gritty code that
actually exercises control over a process or a serial port.
GDB includes some 30-40 different target vectors; however,
each configuration of GDB includes only a few of them.

## [File Targets](GDB%20Internals.md#apple-krhugobv)

Both executables and core files have target vectors.

## [Standard Protocol and Remote Stubs](GDB%20Internals.md#apple-krhugobw)

GDB's file `remote.c' talks a serial protocol to code
that runs in the target system. GDB provides several sample
__stubs__ that can be integrated into target programs or operating
systems for this purpose; they are named `\*-stub.c'.

The GDB user's manual describes how to put such a stub into
your target code. What follows is a discussion of integrating the
SPARC stub into a complicated operating system (rather than a simple
program), by Stu Grossman, the author of this stub.

The trap handling code in the stub assumes the following upon entry to
`trap_low`:

1. %l1 and %l2 contain pc and npc respectively at the time of the trap;
2. traps are disabled;
3. you are in the correct trap window.

As long as your trap handler can guarantee those conditions, then there
is no reason why you shouldn't be able to "share" traps with the stub.
The stub has no requirement that it be jumped to directly from the
hardware trap vector. That is why it calls `exceptionHandler()`,
which is provided by the external environment. For instance, this could
set up the hardware traps to actually execute code which calls the stub
first, and then transfers to its own trap handler.

For the most point, there probably won't be much of an issue with
"sharing" traps, as the traps we use are usually not used by the kernel,
and often indicate unrecoverable error conditions. Anyway, this is all
controlled by a table, and is trivial to modify. The most important
trap for us is for `ta 1`. Without that, we can't single step or
do breakpoints. Everything else is unnecessary for the proper operation
of the debugger/stub.

From reading the stub, it's probably not obvious how breakpoints work.
They are simply done by deposit/examine operations from GDB.

## [ROM Monitor Interface](GDB%20Internals.md#apple-krhugobx)

## [Custom Protocols](GDB%20Internals.md#apple-krhugoby)

## [Transport Layer](GDB%20Internals.md#apple-krhugobz)

## [Builtin Simulator](GDB%20Internals.md#apple-krhugojq)

---

Go to the [first](Requirements.md), [previous](Target%20Architecture%20Definition.md), [next](Native%20Debugging.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
