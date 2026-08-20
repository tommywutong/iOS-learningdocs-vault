---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_19.html
archived_at: '2026-07-15T07:31:03.280717Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Debugging%20remote%20programs.md), [next](Controlling%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Configuration-Specific Information](Debugging%20with%20GDB.md#apple-krhugmjwgu)

While nearly all GDB commands are available for all native and
cross versions of the debugger, there are some exceptions. This chapter
describes things that are only available in certain configurations.

There are three major categories of configurations: native
configurations, where the host and target are the same, embedded
operating system configurations, which are usually the same for several
different processor architectures, and bare embedded processors, which
are quite different from each other.

## [Native](Debugging%20with%20GDB.md#apple-krhugmjwgy)

This section describes details specific to particular native
configurations.

### [HP-UX](Debugging%20with%20GDB.md#apple-krhugmjwg4)

On HP-UX systems, if you refer to a function or variable name that
begins with a dollar sign, GDB searches for a user or system
name first, before it searches for a convenience variable.

### [BSD libkvm Interface](Debugging%20with%20GDB.md#apple-krhugmjwha)

BSD-derived systems (FreeBSD/NetBSD/OpenBSD) have a kernel memory
interface that provides a uniform interface for accessing kernel virtual
memory images, including live systems and crash dumps. GDB
uses this interface to allow you to debug live kernels and kernel crash
dumps on many native BSD configurations. This is implemented as a
special `kvm` debugging target. For debugging a live system, load
the currently running kernel into GDB and connect to the
`kvm` target:

```
(gdb) target kvm
```

For debugging crash dumps, provide the file name of the crash dump as an
argument:

```
(gdb) target kvm /var/crash/bsd.0
```

Once connected to the `kvm` target, the following commands are
available:

**`kvm pcb`**
: 
Set current context from the __Process Control Block__ (PCB) address.

**`kvm proc`**
: Set current context from proc address. This command isn't available on
modern FreeBSD systems.

### [SVR4 process information](Debugging%20with%20GDB.md#apple-krhugmjwhe)

Many versions of SVR4 and compatible systems provide a facility called
`` `/proc' `` that can be used to examine the image of a running
process using file-system subroutines. If GDB is configured
for an operating system with this facility, the command `info
proc` is available to report information about the process running
your program, or about any process running on your system. `info
proc` works only on SVR4 systems that include the `procfs` code.
This includes, as of this writing, GNU/Linux, OSF/1 (Digital
Unix), Solaris, Irix, and Unixware, but not HP-UX, for example.

**`info proc`**
: 

**`info proc process-id`**
: Summarize available information about any running process. If a
process ID is specified by process-id, display information about
that process; otherwise display information about the program being
debugged. The summary includes the debugged process ID, the command
line used to invoke it, its current working directory, and its
executable file's absolute file name.
On some systems, process-id can be of the form
`` `[pid]/tid' `` which specifies a certain thread ID
within a process. If the optional pid part is missing, it means
a thread from the process being debugged (the leading `` `/' `` still
needs to be present, or else GDB will interpret the number as
a process ID rather than a thread ID).

**`info proc mappings`**
: 
Report the memory address space ranges accessible in the program, with
information on whether the process has read, write, or execute access
rights to each range. On GNU/Linux systems, each memory range
includes the object file which is mapped to that range, instead of the
memory access rights to that range.

**`info proc stat`**
:

**`info proc status`**
: 
These subcommands are specific to GNU/Linux systems. They show
the process-related information, including the user ID and group ID;
how many threads are there in the process; its virtual memory usage;
the signals that are pending, blocked, and ignored; its TTY; its
consumption of system and user time; its stack size; its `` `nice' ``
value; etc. For more information, see the `` `proc' `` man page
(type `man 5 proc` from your shell prompt).

**`info proc all`**
: Show all the information about the process described under all of the
above `info proc` subcommands.

**`set procfs-trace`**
: 

This command enables and disables tracing of `procfs` API calls.

**`show procfs-trace`**
: 
Show the current state of `procfs` API call tracing.

**`set procfs-file file`**
: 
Tell GDB to write `procfs` API trace to the named
file. GDB appends the trace info to the previous
contents of the file. The default is to display the trace on the
standard output.

**`show procfs-file`**
: 
Show the file to which `procfs` API trace is written.

**`proc-trace-entry`**
:

**`proc-trace-exit`**
:

**`proc-untrace-entry`**
:

**`proc-untrace-exit`**
: 

These commands enable and disable tracing of entries into and exits
from the `syscall` interface.

**`info pidlist`**
: 

For QNX Neutrino only, this command displays the list of all the
processes and all the threads within each process.

**`info meminfo`**
: 

For QNX Neutrino only, this command displays the list of all mapinfos.

### [Features for Debugging DJGPP Programs](Debugging%20with%20GDB.md#apple-krhugmjxga)

DJGPP is a port of the GNU development tools to MS-DOS and
MS-Windows. DJGPP programs are 32-bit protected-mode programs
that use the __DPMI__ (DOS Protected-Mode Interface) API to run on
top of real-mode DOS systems and their emulations.

GDB supports native debugging of DJGPP programs, and
defines a few commands specific to the DJGPP port. This
subsection describes those commands.

**`info dos`**
: 
This is a prefix of DJGPP-specific commands which print
information about the target system and important OS structures.

**`info dos sysinfo`**
: This command displays assorted information about the underlying
platform: the CPU type and features, the OS version and flavor, the
DPMI version, and the available conventional and DPMI memory.

**`info dos gdt`**
:

**`info dos ldt`**
:

**`info dos idt`**
: These 3 commands display entries from, respectively, Global, Local,
and Interrupt Descriptor Tables (GDT, LDT, and IDT). The descriptor
tables are data structures which store a descriptor for each segment
that is currently in use. The segment's selector is an index into a
descriptor table; the table entry for that index holds the
descriptor's base address and limit, and its attributes and access
rights.
A typical DJGPP program uses 3 segments: a code segment, a data
segment (used for both data and the stack), and a DOS segment (which
allows access to DOS/BIOS data structures and absolute addresses in
conventional memory). However, the DPMI host will usually define
additional segments in order to support the DPMI environment.

These commands allow to display entries from the descriptor tables.
Without an argument, all entries from the specified table are
displayed. An argument, which should be an integer expression, means
display a single entry whose index is given by the argument. For
example, here's a convenient way to display information about the
debugged program's data segment:

```
(gdb) info dos ldt $ds
0x13f: base=0x11970000 limit=0x0009ffff 32-Bit Data (Read/Write, Exp-up)
```

This comes in handy when you want to see whether a pointer is outside
the data segment's limit (i.e. __garbled__).

**`info dos pde`**
:

**`info dos pte`**
: These two commands display entries from, respectively, the Page
Directory and the Page Tables. Page Directories and Page Tables are
data structures which control how virtual memory addresses are mapped
into physical addresses. A Page Table includes an entry for every
page of memory that is mapped into the program's address space; there
may be several Page Tables, each one holding up to 4096 entries. A
Page Directory has up to 4096 entries, one each for every Page Table
that is currently in use.
Without an argument, `info dos pde` displays the entire Page
Directory, and `info dos pte` displays all the entries in all of
the Page Tables. An argument, an integer expression, given to the
`info dos pde` command means display only that entry from the Page
Directory table. An argument given to the `info dos pte` command
means display entries from a single Page Table, the one pointed to by
the specified entry in the Page Directory.

These commands are useful when your program uses __DMA__ (Direct
Memory Access), which needs physical addresses to program the DMA
controller.
These commands are supported only with some DPMI servers.

**`info dos address-pte addr`**
: This command displays the Page Table entry for a specified linear
address. The argument addr is a linear address which should
already have the appropriate segment's base address added to it,
because this command accepts addresses which may belong to _any_
segment. For example, here's how to display the Page Table entry for
the page where a variable `i` is stored:

```
(gdb) info dos address-pte __djgpp_base_address + (char *)&i
Page Table entry for address 0x11a00d30:
Base=0x02698000 Dirty Acc. Not-Cached Write-Back Usr Read-Write +0xd30
```

This says that `i` is stored at offset `0xd30` from the page
whose physical base address is `0x02698000`, and shows all the
attributes of that page.
Note that you must cast the addresses of variables to a `char *`,
since otherwise the value of `__djgpp_base_address`, the base
address of all variables and functions in a DJGPP program, will
be added using the rules of C pointer arithmetics: if `i` is
declared an `int`, GDB will add 4 times the value of
`__djgpp_base_address` to the address of `i`.
Here's another example, it displays the Page Table entry for the
transfer buffer:

```
(gdb) info dos address-pte *((unsigned *)&_go32_info_block + 3)
Page Table entry for address 0x29110:
Base=0x00029000 Dirty Acc. Not-Cached Write-Back Usr Read-Write +0x110
```

(The `+ 3` offset is because the transfer buffer's address is the
3rd member of the `_go32_info_block` structure.) The output
clearly shows that this DPMI server maps the addresses in conventional
memory 1:1, i.e. the physical (`0x00029000` + `0x110`) and
linear (`0x29110`) addresses are identical.
This command is supported only with some DPMI servers.

In addition to native debugging, the DJGPP port supports remote
debugging via a serial data link. The following commands are specific
to remote serial debugging in the DJGPP port of GDB.

**`set com1base addr`**
: 

This command sets the base I/O port address of the `COM1' serial
port.

**`set com1irq irq`**
: This command sets the __Interrupt Request__ (`IRQ`) line to use
for the `COM1' serial port.
There are similar commands `` `set com2base' ``, `` `set com3irq' ``,
etc. for setting the port address and the `IRQ` lines for the
other 3 COM ports.

The related commands `` `show com1base' ``, `` `show com1irq' `` etc.
display the current settings of the base address and the `IRQ`
lines used by the COM ports.

**`info serial`**
: 

This command prints the status of the 4 DOS serial ports. For each
port, it prints whether it's active or not, its I/O base address and
IRQ number, whether it uses a 16550-style FIFO, its baudrate, and the
counts of various errors encountered so far.

### [Features for Debugging MS Windows PE executables](Debugging%20with%20GDB.md#apple-krhugmjxge)

GDB supports native debugging of MS Windows programs, including
DLLs with and without symbolic debugging information. There are various
additional Cygwin-specific commands, described in this subsection. The
subsubsection see section [Support for DLLs without debugging symbols](#apple-kncugmjxgi) describes working with DLLs
that have no debugging symbols.

**`info w32`**
: 
This is a prefix of MS Windows specific commands which print
information about the target system and important OS structures.

**`info w32 selector`**
: This command displays information returned by
the Win32 API `GetThreadSelectorEntry` function.
It takes an optional argument that is evaluated to
a long value to give the information about this given selector.
Without argument, this command displays information
about the the six segment registers.

**`info dll`**
: This is a Cygwin specific alias of info shared.

**`dll-symbols`**
: This command loads symbols from a dll similarly to
add-sym command but without the need to specify a base address.

**`set new-console mode`**
: If mode is `on` the debuggee will
be started in a new console on next start.
If mode is `off`i, the debuggee will
be started in the same console as the debugger.

**`show new-console`**
: Displays whether a new console is used
when the debuggee is started.

**`set new-group mode`**
: This boolean value controls whether the debuggee should
start a new group or stay in the same group as the debugger.
This affects the way the Windows OS handles
Ctrl-C.

**`show new-group`**
: Displays current value of new-group boolean.

**`set debugevents`**
: This boolean value adds debug output concerning events seen by the debugger.

**`set debugexec`**
: This boolean value adds debug output concerning execute events
seen by the debugger.

**`set debugexceptions`**
: This boolean value adds debug ouptut concerning exception events
seen by the debugger.

**`set debugmemory`**
: This boolean value adds debug ouptut concerning memory events
seen by the debugger.

**`set shell`**
: This boolean values specifies whether the debuggee is called
via a shell or directly (default value is on).

**`show shell`**
: Displays if the debuggee will be started with a shell.

#### [Support for DLLs without debugging symbols](Debugging%20with%20GDB.md#apple-krhugmjxgi)

Very often on windows, some of the DLLs that your program relies on do
not include symbolic debugging information (for example,
`kernel32.dll'). When GDB doesn't recognize any debugging
symbols in a DLL, it relies on the minimal amount of symbolic
information contained in the DLL's export table. This subsubsection
describes working with such symbols, known internally to GDB as
"minimal symbols".

Note that before the debugged program has started execution, no DLLs
will have been loaded. The easiest way around this problem is simply to
start the program -- either by setting a breakpoint or letting the
program run once to completion. It is also possible to force
GDB to load a particular DLL before starting the executable ---
see the shared library information in see section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4) or the
`dll-symbols` command in see section [Features for Debugging MS Windows PE executables](#apple-kncugmjxge). Currently,
explicitly loading symbols from a DLL with no debugging information will
cause the symbol names to be duplicated in GDB's lookup table,
which may adversely affect symbol lookup performance.

#### [DLL name prefixes](Debugging%20with%20GDB.md#apple-krhugmjxgm)

In keeping with the naming conventions used by the Microsoft debugging
tools, DLL export symbols are made available with a prefix based on the
DLL name, for instance `KERNEL32!CreateFileA`. The plain name is
also entered into the symbol table, so `CreateFileA` is often
sufficient. In some cases there will be name clashes within a program
(particularly if the executable itself includes full debugging symbols)
necessitating the use of the fully qualified name when referring to the
contents of the DLL. Use single-quotes around the name to avoid the
exclamation mark ("!") being interpreted as a language operator.

Note that the internal name of the DLL may be all upper-case, even
though the file name of the DLL is lower-case, or vice-versa. Since
symbols within GDB are _case-sensitive_ this may cause
some confusion. If in doubt, try the `info functions` and
`info variables` commands or even `maint print msymbols` (see
see section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha)). Here's an example:

```
(gdb) info function CreateFileA
All functions matching regular expression "CreateFileA":

Non-debugging symbols:
0x77e885f4  CreateFileA
0x77e885f4  KERNEL32!CreateFileA
```

```
(gdb) info function !
All functions matching regular expression "!":

Non-debugging symbols:
0x6100114c  cygwin1!__assert
0x61004034  cygwin1!_dll_crt0@0
0x61004240  cygwin1!dll_crt0(per_process *)
[etc...]
```

#### [Working with minimal symbols](Debugging%20with%20GDB.md#apple-krhugmjxgq)

Symbols extracted from a DLL's export table do not contain very much
type information. All that GDB can do is guess whether a symbol
refers to a function or variable depending on the linker section that
contains the symbol. Also note that the actual contents of the memory
contained in a DLL are not available unless the program is running. This
means that you cannot examine the contents of a variable or disassemble
a function within a DLL without a running program.

Variables are generally treated as pointers and dereferenced
automatically. For this reason, it is often necessary to prefix a
variable name with the address-of operator ("&") and provide explicit
type information in the command. Here's an example of the type of
problem:

```
(gdb) print 'cygwin1!__argv'
$1 = 268572168
```

```
(gdb) x 'cygwin1!__argv'
0x10021610:      "\230y\""
```

And two possible solutions:

```
(gdb) print ((char **)'cygwin1!__argv')[0]
$2 = 0x22fd98 "/cygdrive/c/mydirectory/myprogram"
```

```
(gdb) x/2x &'cygwin1!__argv'
0x610c0aa8 <cygwin1!__argv>:    0x10021608      0x00000000
(gdb) x/x 0x10021608
0x10021608:     0x0022fd98
(gdb) x/s 0x0022fd98
0x22fd98:        "/cygdrive/c/mydirectory/myprogram"
```

Setting a break point within a DLL is possible even before the program
starts execution. However, under these circumstances, GDB can't
examine the initial instructions of the function in order to skip the
function's frame set-up code. You can work around this by using "\*&"
to set the breakpoint at a raw memory address:

```
(gdb) break *&'python22!PyOS_Readline'
Breakpoint 1 at 0x1e04eff0
```

The author of these extensions is not entirely convinced that setting a
break point within a shared DLL like `kernel32.dll' is completely
safe.

### [Commands specific to GNU Hurd systems](Debugging%20with%20GDB.md#apple-krhugmjxgu)

This subsection describes GDB commands specific to the
GNU Hurd native debugging.

**`set signals`**
:

**`set sigs`**
: 

This command toggles the state of inferior signal interception by
GDB. Mach exceptions, such as breakpoint traps, are not
affected by this command. `sigs` is a shorthand alias for
`signals`.

**`show signals`**
:

**`show sigs`**
: 

Show the current state of intercepting inferior's signals.

**`set signal-thread`**
:

**`set sigthread`**
: 

This command tells GDB which thread is the `libc` signal
thread. That thread is run when a signal is delivered to a running
process. `set sigthread` is the shorthand alias of `set
signal-thread`.

**`show signal-thread`**
:

**`show sigthread`**
: 

These two commands show which thread will run when the inferior is
delivered a signal.

**`set stopped`**
: 
This commands tells GDB that the inferior process is stopped,
as with the `SIGSTOP` signal. The stopped process can be
continued by delivering a signal to it.

**`show stopped`**
: 
This command shows whether GDB thinks the debuggee is
stopped.

**`set exceptions`**
: 
Use this command to turn off trapping of exceptions in the inferior.
When exception trapping is off, neither breakpoints nor
single-stepping will work. To restore the default, set exception
trapping on.

**`show exceptions`**
: 
Show the current state of trapping exceptions in the inferior.

**`set task pause`**
: 

This command toggles task suspension when GDB has control.
Setting it to on takes effect immediately, and the task is suspended
whenever GDB gets control. Setting it to off will take
effect the next time the inferior is continued. If this option is set
to off, you can use `set thread default pause on` or `set
thread pause on` (see below) to pause individual threads.

**`show task pause`**
: 
Show the current state of task suspension.

**`set task detach-suspend-count`**
: 

This command sets the suspend count the task will be left with when
GDB detaches from it.

**`show task detach-suspend-count`**
: Show the suspend count the task will be left with when detaching.

**`set task exception-port`**
:

**`set task excp`**
: 
This command sets the task exception port to which GDB will
forward exceptions. The argument should be the value of the __send
rights__ of the task. `set task excp` is a shorthand alias.

**`set noninvasive`**
: 
This command switches GDB to a mode that is the least
invasive as far as interfering with the inferior is concerned. This
is the same as using `set task pause`, `set exceptions`, and
`set signals` to values opposite to the defaults.

**`info send-rights`**
:

**`info receive-rights`**
:

**`info port-rights`**
:

**`info port-sets`**
:

**`info dead-names`**
:

**`info ports`**
:

**`info psets`**
: 

These commands display information about, respectively, send rights,
receive rights, port rights, port sets, and dead names of a task.
There are also shorthand aliases: `info ports` for `info
port-rights` and `info psets` for `info port-sets`.

**`set thread pause`**
: 

This command toggles current thread suspension when GDB has
control. Setting it to on takes effect immediately, and the current
thread is suspended whenever GDB gets control. Setting it to
off will take effect the next time the inferior is continued.
Normally, this command has no effect, since when GDB has
control, the whole task is suspended. However, if you used `set
task pause off` (see above), this command comes in handy to suspend
only the current thread.

**`show thread pause`**
: 
This command shows the state of current thread suspension.

**`set thread run`**
: This comamnd sets whether the current thread is allowed to run.

**`show thread run`**
: Show whether the current thread is allowed to run.

**`set thread detach-suspend-count`**
: 

This command sets the suspend count GDB will leave on a
thread when detaching. This number is relative to the suspend count
found by GDB when it notices the thread; use `set thread
takeover-suspend-count` to force it to an absolute value.

**`show thread detach-suspend-count`**
: Show the suspend count GDB will leave on the thread when
detaching.

**`set thread exception-port`**
:

**`set thread excp`**
: Set the thread exception port to which to forward exceptions. This
overrides the port set by `set task exception-port` (see above).
`set thread excp` is the shorthand alias.

**`set thread takeover-suspend-count`**
: Normally, GDB's thread suspend counts are relative to the
value GDB finds when it notices each thread. This command
changes the suspend counts to be absolute instead.

**`set thread default`**
:

**`show thread default`**
: 
Each of the above `set thread` commands has a `set thread
default` counterpart (e.g., `set thread default pause`, `set
thread default exception-port`, etc.). The `thread default`
variety of commands sets the default thread properties for all
threads; you can then change the properties of individual threads with
the non-default commands.

### [QNX Neutrino](Debugging%20with%20GDB.md#apple-krhugmjxgy)

GDB provides the following commands specific to the QNX
Neutrino target:

**`set debug nto-debug`**
: 
When set to on, enables debugging messages specific to the QNX
Neutrino support.

**`show debug nto-debug`**
: 
Show the current state of QNX Neutrino messages.

## [Embedded Operating Systems](Debugging%20with%20GDB.md#apple-krhugmjxg4)

This section describes configurations involving the debugging of
embedded operating systems that are available for several different
architectures.

GDB includes the ability to debug programs running on
various real-time operating systems.

### [Using GDB with VxWorks](Debugging%20with%20GDB.md#apple-krhugmjxha)

**`target vxworks machinename`**
: 
A VxWorks system, attached via TCP/IP. The argument machinename
is the target system's machine name or IP address.

On VxWorks, `load` links filename dynamically on the
current target system as well as adding its symbols in GDB.

GDB enables developers to spawn and debug tasks running on networked
VxWorks targets from a Unix host. Already-running tasks spawned from
the VxWorks shell can also be debugged. GDB uses code that runs on
both the Unix host and on the VxWorks target. The program
`gdb` is installed and executed on the Unix host. (It may be
installed with the name `vxgdb`, to distinguish it from a
GDB for debugging programs on the host itself.)

**`VxWorks-timeout args`**
: 
All VxWorks-based targets now support the option `vxworks-timeout`.
This option is set by the user, and args represents the number of
seconds GDB waits for responses to rpc's. You might use this if
your VxWorks target is a slow software simulator or is on the far side
of a thin network line.

The following information on connecting to VxWorks was current when
this manual was produced; newer releases of VxWorks may use revised
procedures.

To use GDB with VxWorks, you must rebuild your VxWorks kernel
to include the remote debugging interface routines in the VxWorks
library `rdb.a'. To do this, define `INCLUDE_RDB` in the
VxWorks configuration file `configAll.h' and rebuild your VxWorks
kernel. The resulting kernel contains `rdb.a', and spawns the
source debugging task `tRdbTask` when VxWorks is booted. For more
information on configuring and remaking VxWorks, see the manufacturer's
manual.

Once you have included `rdb.a' in your VxWorks system image and set
your Unix execution search path to find GDB, you are ready to
run GDB. From your Unix host, run `gdb` (or
`vxgdb`, depending on your installation).

GDB comes up showing the prompt:

```
(vxgdb)
```

#### [Connecting to VxWorks](Debugging%20with%20GDB.md#apple-krhugmjxhe)

The GDB command `target` lets you connect to a VxWorks target on the
network. To connect to a target whose host name is "`tt`", type:

```
(vxgdb) target vxworks tt
```

GDB displays messages like these:

```
Attaching remote machine across net...
Connected to tt.
```

GDB then attempts to read the symbol tables of any object modules
loaded into the VxWorks target since it was last booted. GDB locates
these files by searching the directories listed in the command search
path (see section [Your program's environment](Running%20Programs%20Under%20GDB.md#apple-kncugmrs)); if it fails
to find an object file, it displays a message such as:

```
prog.o: No such file or directory.
```

When this happens, add the appropriate directory to the search path with
the GDB command `path`, and execute the `target`
command again.

#### [VxWorks download](Debugging%20with%20GDB.md#apple-krhugmjyga)

If you have connected to the VxWorks target and you want to debug an
object that has not yet been loaded, you can use the GDB
`load` command to download a file from Unix to VxWorks
incrementally. The object file given as an argument to the `load`
command is actually opened twice: first by the VxWorks target in order
to download the code, then by GDB in order to read the symbol
table. This can lead to problems if the current working directories on
the two systems differ. If both systems have NFS mounted the same
filesystems, you can avoid these problems by using absolute paths.
Otherwise, it is simplest to set the working directory on both systems
to the directory in which the object file resides, and then to reference
the file by its name, without any path. For instance, a program
`prog.o' may reside in `vxpath/vw/demo/rdb' in VxWorks
and in `hostpath/vw/demo/rdb' on the host. To load this
program, type this on VxWorks:

```swift
-> cd "vxpath/vw/demo/rdb"
```

Then, in GDB, type:

```
(vxgdb) cd hostpath/vw/demo/rdb
(vxgdb) load prog.o
```

GDB displays a response similar to this:

```
Reading symbol data from wherever/vw/demo/rdb/prog.o... done.
```

You can also use the `load` command to reload an object module
after editing and recompiling the corresponding source file. Note that
this makes GDB delete all currently-defined breakpoints,
auto-displays, and convenience variables, and to clear the value
history. (This is necessary in order to preserve the integrity of
debugger's data structures that reference the target system's symbol
table.)

#### [Running tasks](Debugging%20with%20GDB.md#apple-krhugmjyge)

You can also attach to an existing task using the `attach` command as
follows:

```
(vxgdb) attach task
```

where task is the VxWorks hexadecimal task ID. The task can be running
or suspended when you attach to it. Running tasks are suspended at
the time of attachment.

## [Embedded Processors](Debugging%20with%20GDB.md#apple-krhugmjygi)

This section goes into details specific to particular embedded
configurations.

Whenever a specific embedded processor has a simulator, GDB
allows to send an arbitrary command to the simulator.

**`sim command`**
: 
Send an arbitrary command string to the simulator. Consult the
documentation for the specific simulator in use for information about
acceptable commands.

### [ARM](Debugging%20with%20GDB.md#apple-krhugmjygm)

**`target rdi dev`**
: 
ARM Angel monitor, via RDI library interface to ADP protocol. You may
use this target to communicate with both boards running the Angel
monitor, or with the EmbeddedICE JTAG debug device.

**`target rdp dev`**
: ARM Demon monitor.

GDB provides the following ARM-specific commands:

**`set arm disassembler`**
: 
This commands selects from a list of disassembly styles. The
`"std"` style is the standard style.

**`show arm disassembler`**
: 
Show the current disassembly style.

**`set arm apcs32`**
: 
This command toggles ARM operation mode between 32-bit and 26-bit.

**`show arm apcs32`**
: Display the current usage of the ARM 32-bit mode.

**`set arm fpu fputype`**
: This command sets the ARM floating-point unit (FPU) type. The
argument fputype can be one of these:

**`auto`**
: Determine the FPU type by querying the OS ABI.

**`softfpa`**
: Software FPU, with mixed-endian doubles on little-endian ARM
processors.

**`fpa`**
: GCC-compiled FPA co-processor.

**`softvfp`**
: Software FPU with pure-endian doubles.

**`vfp`**
: VFP co-processor.

**`show arm fpu`**
: Show the current type of the FPU.

**`set arm abi`**
: This command forces GDB to use the specified ABI.

**`show arm abi`**
: Show the currently used ABI.

**`set debug arm`**
: Toggle whether to display ARM-specific debugging messages from the ARM
target support subsystem.

**`show debug arm`**
: Show whether ARM-specific debugging messages are enabled.

The following commands are available when an ARM target is debugged
using the RDI interface:

**`rdilogfile [file]`**
: 

Set the filename for the ADP (Angel Debugger Protocol) packet log.
With an argument, sets the log file to the specified file. With
no argument, show the current log file name. The default log file is
`rdi.log'.

**`rdilogenable [arg]`**
: 
Control logging of ADP packets. With an argument of 1 or `"yes"`
enables logging, with an argument 0 or `"no"` disables it. With
no arguments displays the current setting. When logging is enabled,
ADP packets exchanged between GDB and the RDI target device
are logged to a file.

**`set rdiromatzero`**
: 

Tell GDB whether the target has ROM at address 0. If on,
vector catching is disabled, so that zero address can be used. If off
(the default), vector catching is enabled. For this command to take
effect, it needs to be invoked prior to the `target rdi` command.

**`show rdiromatzero`**
: 
Show the current setting of ROM at zero address.

**`set rdiheartbeat`**
: 

Enable or disable RDI heartbeat packets. It is not recommended to
turn on this option, since it confuses ARM and EPI JTAG interface, as
well as the Angel monitor.

**`show rdiheartbeat`**
: 
Show the setting of RDI heartbeat packets.

### [Renesas H8/300](Debugging%20with%20GDB.md#apple-krhugmjygq)

**`target hms dev`**
: 
A Renesas SH, H8/300, or H8/500 board, attached via serial line to your host.
Use special commands `device` and `speed` to control the serial
line and the communications speed used.

**`target e7000 dev`**
: E7000 emulator for Renesas H8 and SH.

**`target sh3 dev`**
:

**`target sh3e dev`**
: Renesas SH-3 and SH-3E target systems.

When you select remote debugging to a Renesas SH, H8/300, or H8/500
board, the `load` command downloads your program to the Renesas
board and also opens it as the current executable target for
GDB on your host (like the `file` command).

GDB needs to know these things to talk to your
Renesas SH, H8/300, or H8/500:

1. that you want to use `` `target hms' ``, the remote debugging interface
   for Renesas microprocessors, or `` `target e7000' ``, the in-circuit
   emulator for the Renesas SH and the Renesas 300H. (`` `target hms' `` is
   the default when GDB is configured specifically for the Renesas SH,
   H8/300, or H8/500.)
2. what serial device connects your host to your Renesas board (the first
   serial device available on your host is the default).
3. what speed to use over the serial device.

#### [Connecting to Renesas boards](Debugging%20with%20GDB.md#apple-krhugmjygu)

Use the special `GDB` command `` `device port' `` if you
need to explicitly set the serial device. The default port is the
first available port on your host. This is only necessary on Unix
hosts, where it is typically something like `/dev/ttya'.

`GDB` has another special command to set the communications
speed: `` `speed bps' ``. This command also is only used from Unix
hosts; on DOS hosts, set the line speed as usual from outside GDB with
the DOS `mode` command (for instance,
`mode com2:9600,n,8,1,p` for a 9600bps connection).

The `` `device' `` and `` `speed' `` commands are available only when you
use a Unix host to debug your Renesas microprocessor programs. If you
use a DOS host,
GDB depends on an auxiliary terminate-and-stay-resident program
called `asynctsr` to communicate with the development board
through a PC serial port. You must also use the DOS `mode` command
to set up the serial port on the DOS side.

The following sample session illustrates the steps needed to start a
program under GDB control on an H8/300. The example uses a
sample H8/300 program called `t.x'. The procedure is the same for
the Renesas SH and the H8/500.

First hook up your development board. In this example, we use a
board attached to serial port `COM2`; if you use a different serial
port, substitute its name in the argument of the `mode` command.
When you call `asynctsr`, the auxiliary comms program used by the
debugger, you give it just the numeric part of the serial port's name;
for example, `` `asyncstr 2' `` below runs `asyncstr` on
`COM2`.

```
C:\H8300\TEST> asynctsr 2
C:\H8300\TEST> mode com2:9600,n,8,1,p

Resident portion of MODE loaded

COM2: 9600, n, 8, 1, p
```

> _Warning:_ We have noticed a bug in PC-NFS that conflicts with
> `asynctsr`. If you also run PC-NFS on your DOS host, you may need to
> disable it, or even boot without it, to use `asynctsr` to control
> your development board.

Now that serial communications are set up, and the development board is
connected, you can start up GDB. Call `GDB` with
the name of your program as the argument. `GDB` prompts
you, as usual, with the prompt `` `(gdb)' ``. Use two special
commands to begin your debugging session: `` `target hms' `` to specify
cross-debugging to the Renesas board, and the `load` command to
download your program to the board. `load` displays the names of
the program's sections, and a `` `*' `` for each 2K of data downloaded.
(If you want to refresh GDB data on symbols or on the
executable file without downloading, use the GDB commands
`file` or `symbol-file`. These commands, and `load`
itself, are described in section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4).)

```
(eg-C:\H8300\TEST) gdb t.x
GDB is free software and you are welcome to distribute copies
 of it under certain conditions; type "show copying" to see
 the conditions.
There is absolutely no warranty for GDB; type "show warranty"
for details.
GDB 6.3.50.20050815-cvs, Copyright 1992 Free Software Foundation, Inc...
(gdb) target hms
Connected to remote H8/300 HMS system.
(gdb) load t.x
.text   : 0x8000 .. 0xabde ***********
.data   : 0xabde .. 0xad30 *
.stack  : 0xf000 .. 0xf014 *
```

At this point, you're ready to run or debug your program. From here on,
you can use all the usual GDB commands. The `break` command
sets breakpoints; the `run` command starts your program;
`print` or `x` display data; the `continue` command
resumes execution after stopping at a breakpoint. You can use the
`help` command at any time to find out more about GDB commands.

Remember, however, that _operating system_ facilities aren't
available on your development board; for example, if your program hangs,
you can't send an interrupt--but you can press the RESET switch!

Use the RESET button on the development board

- to interrupt your program (don't use `ctl-C` on the DOS host--it has
  no way to pass an interrupt signal to the development board); and
- to return to the GDB command prompt after your program finishes
  normally. The communications protocol provides no other way for GDB
  to detect program completion.

In either case, GDB sees the effect of a RESET on the
development board as a "normal exit" of your program.

#### [Using the E7000 in-circuit emulator](Debugging%20with%20GDB.md#apple-krhugmjygy)

You can use the E7000 in-circuit emulator to develop code for either the
Renesas SH or the H8/300H. Use one of these forms of the `` `target
e7000' `` command to connect GDB to your E7000:

**`target e7000 port speed`**
: Use this form if your E7000 is connected to a serial port. The
port argument identifies what serial port to use (for example,
`` `com2' ``). The third argument is the line speed in bits per second
(for example, `` `9600' ``).

**`target e7000 hostname`**
: If your E7000 is installed as a host on a TCP/IP network, you can just
specify its hostname; GDB uses `telnet` to connect.

The following special commands are available when debugging with the
Renesas E7000 ICE:

**`e7000 command`**
: 

This sends the specified command to the E7000 monitor.

**`ftplogin machine username password dir`**
: 
This command records information for subsequent interface with the
E7000 monitor via the FTP protocol: GDB will log into the
named machine using specified username and password,
and then chdir to the named directory dir.

**`ftpload file`**
: 
This command uses credentials recorded by `ftplogin` to fetch and
load the named file from the E7000 monitor.

**`drain`**
: 
This command drains any pending text buffers stored on the E7000.

**`set usehardbreakpoints`**
:

**`show usehardbreakpoints`**
: 

These commands set and show the use of hardware breakpoints for all
breakpoints. See section [Setting breakpoints](Stopping%20and%20Continuing.md#apple-kncugmzr), for
more information about using hardware breakpoints selectively.

#### [Special GDB commands for Renesas micros](Debugging%20with%20GDB.md#apple-krhugmjyg4)

Some GDB commands are available only for the H8/300:

**`set machine h8300`**
: 

**`set machine h8300h`**
: Condition GDB for one of the two variants of the H8/300
architecture with `` `set machine' ``. You can use `` `show machine' ``
to check which variant is currently in effect.

### [H8/500](Debugging%20with%20GDB.md#apple-krhugmjyha)

**`set memory mod`**
: 

**`show memory`**
: Specify which H8/500 memory model (mod) you are using with
`` `set memory' ``; check which memory model is in effect with `` `show
memory' ``. The accepted values for mod are `small`,
`big`, `medium`, and `compact`.

### [Renesas M32R/D and M32R/SDI](Debugging%20with%20GDB.md#apple-krhugmjyhe)

**`target m32r dev`**
: 
Renesas M32R/D ROM monitor.

**`target m32rsdi dev`**
: Renesas M32R SDI server, connected via parallel port to the board.

The following GDB commands are specific to the M32R monitor:

**`set download-path path`**
: 

Set the default path for finding donwloadable SREC files.

**`show download-path`**
: 
Show the default path for downloadable SREC files.

**`set board-address addr`**
: 

Set the IP address for the M32R-EVA target board.

**`show board-address`**
: 
Show the current IP address of the target board.

**`set server-address addr`**
: 

Set the IP address for the download server, which is the GDB's
host machine.

**`show server-address`**
: 
Display the IP address of the download server.

**`upload [file]`**
: 
Upload the specified SREC file via the monitor's Ethernet
upload capability. If no file argument is given, the current
executable file is uploaded.

**`tload [file]`**
: 
Test the `upload` command.

The following commands are available for M32R/SDI:

**`sdireset`**
: 

This command resets the SDI connection.

**`sdistatus`**
: 
This command shows the SDI connection status.

**`debug_chaos`**
: 

Instructs the remote that M32R/Chaos debugging is to be used.

**`use_debug_dma`**
: 
Instructs the remote to use the DEBUG_DMA method of accessing memory.

**`use_mon_code`**
: 
Instructs the remote to use the MON_CODE method of accessing memory.

**`use_ib_break`**
: 
Instructs the remote to set breakpoints by IB break.

**`use_dbt_break`**
: 
Instructs the remote to set breakpoints by DBT.

### [M68k](Debugging%20with%20GDB.md#apple-krhugmjzga)

The Motorola m68k configuration includes ColdFire support, and
target command for the following ROM monitors.

**`target abug dev`**
: 
ABug ROM monitor for M68K.

**`target cpu32bug dev`**
: CPU32BUG monitor, running on a CPU32 (M68K) board.

**`target dbug dev`**
: dBUG ROM monitor for Motorola ColdFire.

**`target est dev`**
: EST-300 ICE monitor, running on a CPU32 (M68K) board.

**`target rom68k dev`**
: ROM 68K monitor, running on an M68K IDP board.

**`target rombug dev`**
: 
ROMBUG ROM monitor for OS/9000.

### [MIPS Embedded](Debugging%20with%20GDB.md#apple-krhugmjzge)

GDB can use the MIPS remote debugging protocol to talk to a
MIPS board attached to a serial line. This is available when
you configure GDB with `` `--target=mips-idt-ecoff' ``.

Use these GDB commands to specify the connection to your target board:

**`target mips port`**
: 
To run a program on the board, start up `gdb` with the
name of your program as the argument. To connect to the board, use the
command `` `target mips port' ``, where port is the name of
the serial port connected to the board. If the program has not already
been downloaded to the board, you may use the `load` command to
download it. You can then use all the usual GDB commands.
For example, this sequence connects to the target board through a serial
port, and loads and runs a program called prog through the
debugger:

```
host$ gdb prog
GDB is free software and ...
(gdb) target mips /dev/ttyb
(gdb) load prog
(gdb) run
```

**`target mips hostname:portnumber`**
: On some GDB host configurations, you can specify a TCP
connection (for instance, to a serial line managed by a terminal
concentrator) instead of a serial port, using the syntax
`` `hostname:portnumber' ``.

**`target pmon port`**
: 
PMON ROM monitor.

**`target ddb port`**
: 
NEC's DDB variant of PMON for Vr4300.

**`target lsi port`**
: 
LSI variant of PMON.

**`target r3900 dev`**
: Densan DVE-R3900 ROM monitor for Toshiba R3900 Mips.

**`target array dev`**
: Array Tech LSI33K RAID controller board.

GDB also supports these special commands for MIPS targets:

**`set mipsfpu double`**
:

**`set mipsfpu single`**
:

**`set mipsfpu none`**
:

**`set mipsfpu auto`**
:

**`show mipsfpu`**
: 

If your target board does not support the MIPS floating point
coprocessor, you should use the command `` `set mipsfpu none' `` (if you
need this, you may wish to put the command in your GDB init
file). This tells GDB how to find the return value of
functions which return floating point values. It also allows
GDB to avoid saving the floating point registers when calling
functions on the board. If you are using a floating point coprocessor
with only single precision floating point support, as on the R4650
processor, use the command `` `set mipsfpu single' ``. The default
double precision floating point coprocessor may be selected using
`` `set mipsfpu double' ``.
In previous versions the only choices were double precision or no
floating point, so `` `set mipsfpu on' `` will select double precision
and `` `set mipsfpu off' `` will select no floating point.
As usual, you can inquire about the `mipsfpu` variable with
`` `show mipsfpu' ``.

**`set timeout seconds`**
:

**`set retransmit-timeout seconds`**
:

**`show timeout`**
:

**`show retransmit-timeout`**
: 

You can control the timeout used while waiting for a packet, in the MIPS
remote protocol, with the `set timeout seconds` command. The
default is 5 seconds. Similarly, you can control the timeout used while
waiting for an acknowledgement of a packet with the `set
retransmit-timeout seconds` command. The default is 3 seconds.
You can inspect both values with `show timeout` and `show
retransmit-timeout`. (These commands are _only_ available when
GDB is configured for `` `--target=mips-idt-ecoff' ``.)
The timeout set by `set timeout` does not apply when GDB
is waiting for your program to stop. In that case, GDB waits
forever because it has no way of knowing how long the program is going
to run before stopping.

**`set syn-garbage-limit num`**
: 

Limit the maximum number of characters GDB should ignore when
it tries to synchronize with the remote target. The default is 10
characters. Setting the limit to -1 means there's no limit.

**`show syn-garbage-limit`**
: 
Show the current limit on the number of characters to ignore when
trying to synchronize with the remote system.

**`set monitor-prompt prompt`**
: 

Tell GDB to expect the specified prompt string from the
remote monitor. The default depends on the target:

**pmon target**
: `` `PMON' ``

**ddb target**
: `` `NEC010' ``

**lsi target**
: `` `PMON>' ``

**`show monitor-prompt`**
: 
Show the current strings GDB expects as the prompt from the
remote monitor.

**`set monitor-warnings`**
: 
Enable or disable monitor warnings about hardware breakpoints. This
has effect only for the `lsi` target. When on, GDB will
display warning messages whose codes are returned by the `lsi`
PMON monitor for breakpoint commands.

**`show monitor-warnings`**
: 
Show the current setting of printing monitor warnings.

**`pmon command`**
: 

This command allows sending an arbitrary command string to the
monitor. The monitor must be in debug mode for this to work.

### [OpenRISC 1000](Debugging%20with%20GDB.md#apple-krhugmjzgi)

See OR1k Architecture document (@uref{www.opencores.org}) for more information
about platform and commands.

**`target jtag jtag://host:port`**
: 
Connects to remote JTAG server.
JTAG remote server can be either an or1ksim or JTAG server,
connected via parallel port to the board.
Example: `target jtag jtag://localhost:9999`

**`or1ksim command`**
: If connected to `or1ksim` OpenRISC 1000 Architectural
Simulator, proprietary commands can be executed.

**`info or1k spr`**
: Displays spr groups.

**`info or1k spr group`**
:

**`info or1k spr groupno`**
: Displays register names in selected group.

**`info or1k spr group register`**
:

**`info or1k spr register`**
:

**`info or1k spr groupno registerno`**
:

**`info or1k spr registerno`**
: Shows information about specified spr register.

**`spr group register value`**
:

**`spr register value`**
:

**`spr groupno registerno value`**
:

**`spr registerno value`**
: Writes value to specified spr register.

Some implementations of OpenRISC 1000 Architecture also have hardware trace.
It is very similar to GDB trace, except it does not interfere with normal
program execution and is thus much faster. Hardware breakpoints/watchpoint
triggers can be set using:

**`$LEA/$LDATA`**
: Load effective address/data

**`$SEA/$SDATA`**
: Store effective address/data

**`$AEA/$ADATA`**
: Access effective address ($SEA or $LEA) or data ($SDATA/$LDATA)

**`$FETCH`**
: Fetch data

When triggered, it can capture low level data, like: `PC`, `LSEA`,
`LDATA`, `SDATA`, `READSPR`, `WRITESPR`, `INSTR`.

`htrace` commands:

**`hwatch conditional`**
: 
Set hardware watchpoint on combination of Load/Store Effecive Address(es)
or Data. For example:
`hwatch ($LEA == my_var) && ($LDATA < 50) || ($SEA == my_var) && ($SDATA >= 50)`
`hwatch ($LEA == my_var) && ($LDATA < 50) || ($SEA == my_var) && ($SDATA >= 50)`

**`htrace info`**
: Display information about current HW trace configuration.

**`htrace trigger conditional`**
: Set starting criteria for HW trace.

**`htrace qualifier conditional`**
: Set acquisition qualifier for HW trace.

**`htrace stop conditional`**
: Set HW trace stopping criteria.

**`htrace record [data]*`**
: Selects the data to be recorded, when qualifier is met and HW trace was
triggered.

**`htrace enable`**
:

**`htrace disable`**
: Enables/disables the HW trace.

**`htrace rewind [filename]`**
: Clears currently recorded trace data.
If filename is specified, new trace file is made and any newly collected data
will be written there.

**`htrace print [start [len]]`**
: Prints trace buffer, using current record configuration.

**`htrace mode continuous`**
: Set continuous trace mode.

**`htrace mode suspend`**
: Set suspend trace mode.

### [PowerPC](Debugging%20with%20GDB.md#apple-krhugmjzgm)

**`target dink32 dev`**
: 
DINK32 ROM monitor.

**`target ppcbug dev`**
: 

**`target ppcbug1 dev`**
: PPCBUG ROM monitor for PowerPC.

**`target sds dev`**
: SDS monitor, running on a PowerPC board (such as Motorola's ADS).

The following commands specifi to the SDS protocol are supported
byGDB:

**`set sdstimeout nsec`**
: 
Set the timeout for SDS protocol reads to be nsec seconds. The
default is 2 seconds.

**`show sdstimeout`**
: 
Show the current value of the SDS timeout.

**`sds command`**
: 
Send the specified command string to the SDS monitor.

### [HP PA Embedded](Debugging%20with%20GDB.md#apple-krhugmjzgq)

**`target op50n dev`**
: 
OP50N monitor, running on an OKI HPPA board.

**`target w89k dev`**
: W89K monitor, running on a Winbond HPPA board.

### [Renesas SH](Debugging%20with%20GDB.md#apple-krhugmjzgu)

**`target hms dev`**
: 
A Renesas SH board attached via serial line to your host. Use special
commands `device` and `speed` to control the serial line and
the communications speed used.

**`target e7000 dev`**
: E7000 emulator for Renesas SH.

**`target sh3 dev`**
:

**`target sh3e dev`**
: Renesas SH-3 and SH-3E target systems.

### [Tsqware Sparclet](Debugging%20with%20GDB.md#apple-krhugmjzgy)

GDB enables developers to debug tasks running on
Sparclet targets from a Unix host.
GDB uses code that runs on
both the Unix host and on the Sparclet target. The program
`gdb` is installed and executed on the Unix host.

**`remotetimeout args`**
: 
GDB supports the option `remotetimeout`.
This option is set by the user, and args represents the number of
seconds GDB waits for responses.

When compiling for debugging, include the options `` `-g' `` to get debug
information and `` `-Ttext' `` to relocate the program to where you wish to
load it on the target. You may also want to add the options `` `-n' `` or
`` `-N' `` in order to reduce the size of the sections. Example:

```
sparclet-aout-gcc prog.c -Ttext 0x12010000 -g -o prog -N
```

You can use `objdump` to verify that the addresses are what you intended:

```
sparclet-aout-objdump --headers --syms prog
```


Once you have set
your Unix execution search path to find GDB, you are ready to
run GDB. From your Unix host, run `gdb`
(or `sparclet-aout-gdb`, depending on your installation).

GDB comes up showing the prompt:

```
(gdbslet)
```

#### [Setting file to debug](Debugging%20with%20GDB.md#apple-krhugmjzg4)

The GDB command `file` lets you choose with program to debug.

```
(gdbslet) file prog
```

GDB then attempts to read the symbol table of `prog'.
GDB locates
the file by searching the directories listed in the command search
path.
If the file was compiled with debug information (option "-g"), source
files will be searched as well.
GDB locates
the source files by searching the directories listed in the directory search
path (see section [Your program's environment](Running%20Programs%20Under%20GDB.md#apple-kncugmrs)).
If it fails
to find a file, it displays a message such as:

```
prog: No such file or directory.
```

When this happens, add the appropriate directories to the search paths with
the GDB commands `path` and `dir`, and execute the
`target` command again.

#### [Connecting to Sparclet](Debugging%20with%20GDB.md#apple-krhugmjzha)

The GDB command `target` lets you connect to a Sparclet target.
To connect to a target on serial port "`ttya`", type:

```
(gdbslet) target sparclet /dev/ttya
Remote target sparclet connected to /dev/ttya
main () at ../prog.c:3
```

GDB displays messages like these:

```
Connected to ttya.
```

#### [Sparclet download](Debugging%20with%20GDB.md#apple-krhugmjzhe)

Once connected to the Sparclet target,
you can use the GDB
`load` command to download the file from the host to the target.
The file name and load offset should be given as arguments to the `load`
command.
Since the file format is aout, the program must be loaded to the starting
address. You can use `objdump` to find out what this value is. The load
offset is an offset which is added to the VMA (virtual memory address)
of each of the file's sections.
For instance, if the program
`prog' was linked to text address 0x1201000, with data at 0x12010160
and bss at 0x12010170, in GDB, type:

```
(gdbslet) load prog 0x12010000
Loading section .text, size 0xdb0 vma 0x12010000
```

If the code is loaded at a different address then what the program was linked
to, you may need to use the `section` and `add-symbol-file` commands
to tell GDB where to map the symbol table.

#### [Running and debugging](Debugging%20with%20GDB.md#apple-krhugmrqga)

You can now begin debugging the task using GDB's execution control
commands, `b`, `step`, `run`, etc. See the GDB
manual for the list of commands.

```
(gdbslet) b main
Breakpoint 1 at 0x12010000: file prog.c, line 3.
(gdbslet) run
Starting program: prog
Breakpoint 1, main (argc=1, argv=0xeffff21c) at prog.c:3
3        char *symarg = 0;
(gdbslet) step
4        char *execarg = "hello!";
(gdbslet)
```

### [Fujitsu Sparclite](Debugging%20with%20GDB.md#apple-krhugmrqge)

**`target sparclite dev`**
: 
Fujitsu sparclite boards, used only for the purpose of loading.
You must use an additional command to debug the program.
For example: target remote dev using GDB standard
remote protocol.

### [Tandem ST2000](Debugging%20with%20GDB.md#apple-krhugmrqgi)

GDB may be used with a Tandem ST2000 phone switch, running Tandem's
STDBUG protocol.

To connect your ST2000 to the host system, see the manufacturer's
manual. Once the ST2000 is physically attached, you can run:

```
target st2000 dev speed
```

to establish it as your debugging environment. dev is normally
the name of a serial device, such as `/dev/ttya', connected to the
ST2000 via a serial line. You can instead specify dev as a TCP
connection (for example, to a serial line attached via a terminal
concentrator) using the syntax `hostname:portnumber`.

The `load` and `attach` commands are _not_ defined for
this target; you must load your program into the ST2000 as you normally
would for standalone operation. GDB reads debugging information
(such as symbols) from a separate, debugging version of the program
available on your host computer.

These auxiliary GDB commands are available to help you with the ST2000
environment:

**`st2000 command`**
: 

Send a command to the STDBUG monitor. See the manufacturer's
manual for available commands.

**`connect`**
: 
Connect the controlling terminal to the STDBUG command monitor. When
you are done interacting with STDBUG, typing either of two character
sequences gets you back to the GDB command prompt:
`RET~.` (Return, followed by tilde and period) or
`RET~C-d` (Return, followed by tilde and control-D).

### [Zilog Z8000](Debugging%20with%20GDB.md#apple-krhugmrqgm)

When configured for debugging Zilog Z8000 targets, GDB includes
a Z8000 simulator.

For the Z8000 family, `` `target sim' `` simulates either the Z8002 (the
unsegmented variant of the Z8000 architecture) or the Z8001 (the
segmented variant). The simulator recognizes which architecture is
appropriate by inspecting the object code.

**`target sim args`**
: 

Debug programs on a simulated CPU. If the simulator supports setup
options, specify them via args.

After specifying this target, you can debug programs for the simulated
CPU in the same style as programs for your host computer; use the
`file` command to load a new program image, the `run` command
to run your program, and so on.

As well as making available all the usual machine registers
(see section [Registers](Examining%20Data.md#apple-kncugnrw)), the Z8000 simulator provides three
additional items of information as specially named registers:

**`cycles`**
: Counts clock-ticks in the simulator.

**`insts`**
: Counts instructions run in the simulator.

**`time`**
: Execution time in 60ths of a second.

You can refer to these values in GDB expressions with the usual
conventions; for example, `` `b fputc if $cycles>5000' `` sets a
conditional breakpoint that suspends only after at least 5000
simulated clock ticks.

### [Atmel AVR](Debugging%20with%20GDB.md#apple-krhugmrqgq)

When configured for debugging the Atmel AVR, GDB supports the
following AVR-specific commands:

**`info io_registers`**
: 

This command displays information about the AVR I/O registers. For
each register, GDB prints its number and value.

### [CRIS](Debugging%20with%20GDB.md#apple-krhugmrqgu)

When configured for debugging CRIS, GDB provides the
following CRIS-specific commands:

**`set cris-version ver`**
: 
Set the current CRIS version to ver, either `` `10' `` or `` `32' ``.
The CRIS version affects register names and sizes. This command is useful in
case autodetection of the CRIS version fails.

**`show cris-version`**
: Show the current CRIS version.

**`set cris-dwarf2-cfi`**
: 
Set the usage of DWARF-2 CFI for CRIS debugging. The default is `` `on' ``.
Change to `` `off' `` when using `gcc-cris` whose version is below
`R59`.

**`show cris-dwarf2-cfi`**
: Show the current state of using DWARF-2 CFI.

**`set cris-mode mode`**
: 
Set the current CRIS mode to mode. It should only be changed when
debugging in guru mode, in which case it should be set to
`` `guru' `` (the default is `` `normal' ``).

**`show cris-mode`**
: Show the current CRIS mode.

### [Renesas Super-H](Debugging%20with%20GDB.md#apple-krhugmrqgy)

For the Renesas Super-H processor, GDB provides these
commands:

**`regs`**
: 
Show the values of all Super-H registers.

### [Windows CE](Debugging%20with%20GDB.md#apple-krhugmrqg4)

The following commands are available for Windows CE:

**`set remotedirectory dir`**
: 
Tell GDB to upload files from the named directory dir.
The default is `/gdb', i.e. the root directory on the current
drive.

**`show remotedirectory`**
: 
Show the current value of the upload directory.

**`set remoteupload method`**
: 
Set the method used to upload files to remote device. Valid values
for method are `` `always' ``, `` `newer' ``, and `` `never' ``.
The default is `` `newer' ``.

**`show remoteupload`**
: 
Show the current setting of the upload method.

**`set remoteaddhost`**
: 
Tell GDB whether to add this host to the remote stub's
arguments when you debug over a network.

**`show remoteaddhost`**
: 
Show whether to add this host to remote stub's arguments when
debugging over a network.

## [Architectures](Debugging%20with%20GDB.md#apple-krhugmrqha)

This section describes characteristics of architectures that affect
all uses of GDB with the architecture, both native and cross.

### [x86 Architecture-specific issues.](Debugging%20with%20GDB.md#apple-krhugmrqhe)

**`set struct-convention mode`**
: 

Set the convention used by the inferior to return `struct`s and
`union`s from functions to mode. Possible values of
mode are `"pcc"`, `"reg"`, and `"default"` (the
default). `"default"` or `"pcc"` means that `struct`s
are returned on the stack, while `"reg"` means that a
`struct` or a `union` whose size is 1, 2, 4, or 8 bytes will
be returned in a register.

**`show struct-convention`**
: 
Show the current setting of the convention to return `struct`s
from functions.

### [A29K](Debugging%20with%20GDB.md#apple-krhugmrrga)

**`set rstack_high_address address`**
: 

On AMD 29000 family processors, registers are saved in a separate
__register stack__. There is no way for GDB to determine the
extent of this stack. Normally, GDB just assumes that the
stack is "large enough". This may result in GDB referencing
memory locations that do not exist. If necessary, you can get around
this problem by specifying the ending address of the register stack with
the `set rstack_high_address` command. The argument should be an
address, which you probably want to precede with `` `0x' `` to specify in
hexadecimal.

**`show rstack_high_address`**
: Display the current limit of the register stack, on AMD 29000 family
processors.

### [Alpha](Debugging%20with%20GDB.md#apple-krhugmrrge)

See the following section.

### [MIPS](Debugging%20with%20GDB.md#apple-krhugmrrgi)

Alpha- and MIPS-based computers use an unusual stack frame, which
sometimes requires GDB to search backward in the object code to
find the beginning of a function.

To improve response time (especially for embedded applications, where
GDB may be restricted to a slow serial line for this search)
you may want to limit the size of this search, using one of these
commands:

**`set heuristic-fence-post limit`**
: 
Restrict GDB to examining at most limit bytes in its
search for the beginning of a function. A value of 0 (the
default) means there is no limit. However, except for 0, the
larger the limit the more bytes `heuristic-fence-post` must search
and therefore the longer it takes to run. You should only need to use
this command when debugging a stripped executable.

**`show heuristic-fence-post`**
: Display the current limit.

These commands are available _only_ when GDB is configured
for debugging programs on Alpha or MIPS processors.

Several MIPS-specific commands are available when debugging MIPS
programs:

**`set mips saved-gpreg-size size`**
: 

Set the size of MIPS general-purpose registers saved on the stack.
The argument size can be one of the following:

**`` `32' ``**
: 32-bit GP registers

**`` `64' ``**
: 64-bit GP registers

**`` `auto' ``**
: Use the target's default setting or autodetect the saved size from the
information contained in the executable. This is the default

**`show mips saved-gpreg-size`**
: 
Show the current size of MIPS GP registers on the stack.

**`set mips stack-arg-size size`**
: 

Set the amount of stack space reserved for arguments to functions.
The argument can be one of `"32"`, `"64"` or `"auto"`
(the default).

**`set mips abi arg`**
: 

Tell GDB which MIPS ABI is used by the inferior. Possible
values of arg are:

**`` `auto' ``**
: The default ABI associated with the current binary (this is the
default).

**`` `o32' ``**
:

**`` `o64' ``**
:

**`` `n32' ``**
:

**`` `n64' ``**
:

**`` `eabi32' ``**
:

**`` `eabi64' ``**
:

**`` `auto' ``**
:

**`show mips abi`**
: 
Show the MIPS ABI used by GDB to debug the inferior.

**`set mipsfpu`**
:

**`show mipsfpu`**
: See section [MIPS Embedded](#apple-kncugmjzge).

**`set mips mask-address arg`**
: 

This command determines whether the most-significant 32 bits of 64-bit
MIPS addresses are masked off. The argument arg can be
`` `on' ``, `` `off' ``, or `` `auto' ``. The latter is the default
setting, which lets GDB determine the correct value.

**`show mips mask-address`**
: 
Show whether the upper 32 bits of MIPS addresses are masked off or
not.

**`set remote-mips64-transfers-32bit-regs`**
: 
This command controls compatibility with 64-bit MIPS targets that
transfer data in 32-bit quantities. If you have an old MIPS 64 target
that transfers 32 bits for some registers, like SR and FSR,
and 64 bits for other registers, set this option to `` `on' ``.

**`show remote-mips64-transfers-32bit-regs`**
: 
Show the current setting of compatibility with older MIPS 64 targets.

**`set debug mips`**
: 
This command turns on and off debugging messages for the MIPS-specific
target code in GDB.

**`show debug mips`**
: 
Show the current setting of MIPS debugging messages.

### [HPPA](Debugging%20with%20GDB.md#apple-krhugmrrgm)

When GDB is debugging te HP PA architecture, it provides the
following special commands:

**`set debug hppa`**
: 
THis command determines whether HPPA architecture specific debugging
messages are to be displayed.

**`show debug hppa`**
: Show whether HPPA debugging messages are displayed.

**`maint print unwind address`**
: 
This command displays the contents of the unwind table entry at the
given address.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Debugging%20remote%20programs.md), [next](Controlling%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
