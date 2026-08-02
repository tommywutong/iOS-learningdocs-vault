---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_1.html
archived_at: '2026-07-15T07:31:03.699160Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the first, previous, [next](Overall%20Structure.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Requirements](GDB%20Internals.md#apple-krhugmi)

Before diving into the internals, you should understand the formal
requirements and other expectations for GDB. Although some
of these may seem obvious, there have been proposals for GDB
that have run counter to these requirements.

First of all, GDB is a debugger. It's not designed to be a
front panel for embedded systems. It's not a text editor. It's not a
shell. It's not a programming environment.

GDB is an interactive tool. Although a batch mode is
available, GDB's primary role is to interact with a human
programmer.

GDB should be responsive to the user. A programmer hot on
the trail of a nasty bug, and operating under a looming deadline, is
going to be very impatient of everything, including the response time
to debugger commands.

GDB should be relatively permissive, such as for expressions.
While the compiler should be picky (or have the option to be made
picky), since source code lives for a long time usually, the
programmer doing debugging shouldn't be spending time figuring out to
mollify the debugger.

GDB will be called upon to deal with really large programs.
Executable sizes of 50 to 100 megabytes occur regularly, and we've
heard reports of programs approaching 1 gigabyte in size.

GDB should be able to run everywhere. No other debugger is
available for even half as many configurations as GDB
supports.

---

Go to the first, previous, [next](Overall%20Structure.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
