---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_17.html
archived_at: '2026-07-15T07:31:03.259923Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Files.md), [next](Debugging%20remote%20programs.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Specifying a Debugging Target](Debugging%20with%20GDB.md#apple-krhugmjvga)

A __target__ is the execution environment occupied by your program.

Often, GDB runs in the same host environment as your program;
in that case, the debugging target is specified as a side effect when
you use the `file` or `core` commands. When you need more
flexibility--for example, running GDB on a physically separate
host, or controlling a standalone system over a serial port or a
realtime system over a TCP/IP connection--you can use the `target`
command to specify one of the target types configured for GDB
(see section [Commands for managing targets](#apple-kncugmjvgi)).

It is possible to build GDB for several different __target
architectures__. When GDB is built like that, you can choose
one of the available architectures with the `set architecture`
command.

**`set architecture arch`**
: 

This command sets the current target architecture to arch. The
value of arch can be `"auto"`, in addition to one of the
supported architectures.

**`show architecture`**
: Show the current target architecture.

**`set processor`**
:

**`processor`**
: 

These are alias commands for, respectively, `set architecture`
and `show architecture`.

## [Active targets](Debugging%20with%20GDB.md#apple-krhugmjvge)

There are three classes of targets: processes, core files, and
executable files. GDB can work concurrently on up to three
active targets, one in each class. This allows you to (for example)
start a process and inspect its activity without abandoning your work on
a core file.

For example, if you execute `` `gdb a.out' ``, then the executable file
`a.out` is the only active target. If you designate a core file as
well--presumably from a prior run that crashed and coredumped--then
GDB has two active targets and uses them in tandem, looking
first in the corefile target, then in the executable file, to satisfy
requests for memory addresses. (Typically, these two classes of target
are complementary, since core files contain only a program's
read-write memory--variables and so on--plus machine status, while
executable files contain only the program text and initialized data.)

When you type `run`, your executable file becomes an active process
target as well. When a process target is active, all GDB
commands requesting memory addresses refer to that target; addresses in
an active core file or executable file target are obscured while the
process target is active.

Use the `core-file` and `exec-file` commands to select a new
core file or executable target (see section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4)). To specify as a target a process that is already running, use
the `attach` command (see section [Debugging an already-running process](Running%20Programs%20Under%20GDB.md#apple-kncugmrv)).

## [Commands for managing targets](Debugging%20with%20GDB.md#apple-krhugmjvgi)

**`target type parameters`**
: Connects the GDB host environment to a target machine or
process. A target is typically a protocol for talking to debugging
facilities. You use the argument type to specify the type or
protocol of the target machine.
Further parameters are interpreted by the target protocol, but
typically include things like device names or host names to connect
with, process numbers, and baud rates.
The `target` command does not repeat if you press `RET` again
after executing the command.

**`help target`**
: Displays the names of all targets available. To display targets
currently selected, use either `info target` or `info files`
(see section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4)).

**`help target name`**
: Describe a particular target, including any parameters necessary to
select it.

**`set gnutarget args`**
: GDB uses its own library BFD to read your files. GDB
knows whether it is reading an __executable__,
a __core__, or a __.o__ file; however, you can specify the file format
with the `set gnutarget` command. Unlike most `target` commands,
with `gnutarget` the `target` refers to a program, not a machine.
> _Warning:_ To specify a file format with `set gnutarget`,
> you must know the actual BFD name.

See section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4).

**`show gnutarget`**
: Use the `show gnutarget` command to display what file format
`gnutarget` is set to read. If you have not set `gnutarget`,
GDB will determine the file format for each file automatically,
and `show gnutarget` displays `` `The current BDF target is "auto"' ``.

Here are some common targets (available, or not, depending on the GDB
configuration):

**`target exec program`**
: 

An executable file. `` `target exec program' `` is the same as
`` `exec-file program' ``.

**`target core filename`**
: 
A core dump file. `` `target core filename' `` is the same as
`` `core-file filename' ``.

**`target remote dev`**
: 
Remote serial target in GDB-specific protocol. The argument dev
specifies what serial device to use for the connection (e.g.
`/dev/ttya'). See section [Remote debugging](#apple-kncugmjvgq). `target remote`
supports the `load` command. This is only useful if you have
some other way of getting the stub to the target system, and you can put
it somewhere in memory where it won't get clobbered by the download.

**`target sim`**
: 
Builtin CPU simulator. GDB includes simulators for most architectures.
In general,

```
        target sim
        load
        run
```

works; however, you cannot assume that a specific memory map, device
drivers, or even basic I/O is available, although some simulators do
provide these. For info about any processor-specific simulator details,
see the appropriate section in section [Embedded Processors](Configuration-Specific%20Information.md#apple-kncugmjygi).

Some configurations may include these targets as well:

**`target nrom dev`**
: 
NetROM ROM emulator. This target only supports downloading.

Different targets are available on different configurations of GDB;
your configuration may have more or fewer targets.

Many remote targets require you to download the executable's code once
you've successfully established a connection. You may wish to control
various aspects of this process, such as the size of the data chunks
used by GDB to download program parts to the remote target.

**`set download-write-size size`**
: 
Set the write size used when downloading a program. Only used when
downloading a program onto a remote target. Specify zero or a
negative value to disable blocked writes. The actual size of each
transfer is also limited by the size of the target packet and the
memory cache.

**`show download-write-size`**
: 
Show the current value of the write size.

**`set hash`**
: 

This command controls whether a hash mark `` `#' `` is displayed while
downloading a file to the remote monitor. If on, a hash mark is
displayed after each S-record is successfully downloaded to the
monitor.

**`show hash`**
: 
Show the current status of displaying the hash mark.

**`set debug monitor`**
: 

Enable or disable display of communications messages between
GDB and the remote monitor.

**`show debug monitor`**
: 
Show the current status of displaying communications between
GDB and the remote monitor.

**`load filename`**
: 
Depending on what remote debugging facilities are configured into
GDB, the `load` command may be available. Where it exists, it
is meant to make filename (an executable) available for debugging
on the remote system--by downloading, or dynamic linking, for example.
`load` also records the filename symbol table in GDB, like
the `add-symbol-file` command.
If your GDB does not have a `load` command, attempting to
execute it gets the error message "`You can't do that when your
target is ...`"
The file is loaded at whatever address is specified in the executable.
For some object file formats, you can specify the load address when you
link the program; for other formats, like a.out, the object file format
specifies a fixed address.
`load` does not repeat if you press `RET` again after using it.

## [Choosing target byte order](Debugging%20with%20GDB.md#apple-krhugmjvgm)

Some types of processors, such as the MIPS, PowerPC, and Renesas SH,
offer the ability to run either big-endian or little-endian byte
orders. Usually the executable or symbol will include a bit to
designate the endian-ness, and you will not need to worry about
which to use. However, you may still find it useful to adjust
GDB's idea of processor endian-ness manually.

**`set endian big`**
: 
Instruct GDB to assume the target is big-endian.

**`set endian little`**
: Instruct GDB to assume the target is little-endian.

**`set endian auto`**
: Instruct GDB to use the byte order associated with the
executable.

**`show endian`**
: Display GDB's current idea of the target byte order.

Note that these commands merely adjust interpretation of symbolic
data on the host, and that they have absolutely no effect on the
target system.

## [Remote debugging](Debugging%20with%20GDB.md#apple-krhugmjvgq)

If you are trying to debug a program running on a machine that cannot run
GDB in the usual way, it is often useful to use remote debugging.
For example, you might use remote debugging on an operating system kernel,
or on a small system which does not have a general purpose operating system
powerful enough to run a full-featured debugger.

Some configurations of GDB have special serial or TCP/IP interfaces
to make this work with particular debugging targets. In addition,
GDB comes with a generic serial protocol (specific to GDB,
but not specific to any particular target system) which you can use if you
write the remote stubs--the code that runs on the remote system to
communicate with GDB.

Other remote targets may be available in your
configuration of GDB; use `help target` to list them.

Once you've connected to the remote target, GDB allows you to
send arbitrary commands to the remote monitor:

**`remote command`**
: 

Send an arbitrary command string to the remote monitor.

## [Kernel Object Display](Debugging%20with%20GDB.md#apple-krhugmjvgu)

Some targets support kernel object display. Using this facility,
GDB communicates specially with the underlying operating system
and can display information about operating system-level objects such as
mutexes and other synchronization objects. Exactly which objects can be
displayed is determined on a per-OS basis.

Use the `set os` command to set the operating system. This tells
GDB which kernel object display module to initialize:

```
(gdb) set os cisco
```


The associated command `show os` displays the operating system
set with the `set os` command; if no operating system has been
set, `show os` will display an empty string `` `""' ``.

If `set os` succeeds, GDB will display some information
about the operating system, and will create a new `info` command
which can be used to query the target. The `info` command is named
after the operating system:


```
(gdb) info cisco
List of Cisco Kernel Objects
Object     Description
any        Any and all objects
```

Further subcommands can be used to query about particular objects known
by the kernel.

There is currently no way to determine whether a given operating
system is supported other than to try setting it with `set os
name`, where name is the name of the operating system you
want to try.

---

Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Files.md), [next](Debugging%20remote%20programs.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
