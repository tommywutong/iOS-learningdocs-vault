---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_22.html
archived_at: '2026-07-15T07:31:03.337202Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Canned%20Sequences%20of%20Commands.md), [next](GDB%20Text%20User%20Interface.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Command Interpreters](Debugging%20with%20GDB.md#apple-krhugmrsha)

GDB supports multiple command interpreters, and some command
infrastructure to allow users or user interface writers to switch
between interpreters or run commands in other interpreters.

GDB currently supports two command interpreters, the console
interpreter (sometimes called the command-line interpreter or CLI)
and the machine interface interpreter (or GDB/MI). This manual
describes both of these interfaces in great detail.

By default, GDB will start with the console interpreter.
However, the user may choose to start GDB with another
interpreter by specifying the @option{-i} or @option{--interpreter}
startup options. Defined interpreters include:

**`console`**
: 
The traditional console or command-line interpreter. This is the most often
used interpreter with GDB. With no interpreter specified at runtime,
GDB will use this interpreter.

**`mi`**
: 
The newest GDB/MI interface (currently `mi2`). Used primarily
by programs wishing to use GDB as a backend for a debugger GUI
or an IDE. For more information, see section [The GDB/MI Interface](The%20GDB-MI%20Interface.md#apple-kncugmrtgy).

**`mi2`**
: 
The current GDB/MI interface.

**`mi1`**
: 
The GDB/MI interface included in GDB 5.1, 5.2, and 5.3.

The interpreter being used by GDB may not be dynamically
switched at runtime. Although possible, this could lead to a very
precarious situation. Consider an IDE using GDB/MI. If a user
enters the command "interpreter-set console" in a console view,
GDB would switch to using the console interpreter, rendering
the IDE inoperable!

Although you may only choose a single interpreter at startup, you may execute
commands in any interpreter from the current interpreter using the appropriate
command. If you are running the console interpreter, simply use the
`interpreter-exec` command:

```
interpreter-exec mi "-data-list-register-names"
```

GDB/MI has a similar command, although it is only available in versions of
GDB which support GDB/MI version 2 (or greater).

---

Go to the [first](Summary%20of%20GDB.md), [previous](Canned%20Sequences%20of%20Commands.md), [next](GDB%20Text%20User%20Interface.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
