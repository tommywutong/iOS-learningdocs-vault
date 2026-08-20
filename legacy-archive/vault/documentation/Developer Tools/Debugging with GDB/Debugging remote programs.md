---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_18.html
archived_at: '2026-07-15T07:31:03.268297Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Specifying%20a%20Debugging%20Target.md), [next](Configuration-Specific%20Information.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Debugging remote programs](Debugging%20with%20GDB.md#apple-krhugmjvgy)

## [Connecting to a remote target](Debugging%20with%20GDB.md#apple-krhugmjvg4)

On the GDB host machine, you will need an unstripped copy of
your program, since GDB needs symobl and debugging information.
Start up GDB as usual, using the name of the local copy of your
program as the first argument.

If you're using a serial line, you may want to give GDB the
`` `--baud' `` option, or use the `set remotebaud` command
(see section [Remote configuration](#apple-kncugmjwga)) before the
`target` command.

After that, use `target remote` to establish communications with
the target machine. Its argument specifies how to communicate--either
via a devicename attached to a direct serial line, or a TCP or UDP port
(possibly to a terminal server which in turn has a serial line to the
target). For example, to use a serial line connected to the device
named `/dev/ttyb':

```
target remote /dev/ttyb
```


To use a TCP connection, use an argument of the form
`host:port` or `tcp:host:port`.
For example, to connect to port 2828 on a
terminal server named `manyfarms`:

```
target remote manyfarms:2828
```

If your remote target is actually running on the same machine as
your debugger session (e.g. a simulator of your target running on
the same host), you can omit the hostname. For example, to connect
to port 1234 on your local machine:

```
target remote :1234
```

Note that the colon is still required here.

To use a UDP connection, use an argument of the form
`udp:host:port`. For example, to connect to UDP port 2828
on a terminal server named `manyfarms`:

```
target remote udp:manyfarms:2828
```

When using a UDP connection for remote debugging, you should keep in mind
that the `U' stands for "Unreliable". UDP can silently drop packets on
busy or unreliable networks, which will cause havoc with your debugging
session.

Now you can use all the usual commands to examine and change data and to
step and continue the remote program.

Whenever GDB is waiting for the remote program, if you type the
interrupt character (often `C-C`), GDB attempts to stop the
program. This may or may not succeed, depending in part on the hardware
and the serial drivers the remote system uses. If you type the
interrupt character once again, GDB displays this prompt:

```
Interrupted while waiting for the program.
Give up (and stop debugging it)?  (y or n)
```

If you type `y`, GDB abandons the remote debugging session.
(If you decide you want to try again later, you can use `` `target
remote' `` again to connect once more.) If you type `n`, GDB
goes back to waiting.

**`detach`**
: 
When you have finished debugging the remote program, you can use the
`detach` command to release it from GDB control.
Detaching from the target normally resumes its execution, but the results
will depend on your particular remote stub. After the `detach`
command, GDB is free to connect to another target.

**`disconnect`**
: The `disconnect` command behaves like `detach`, except that
the target is generally not resumed. It will wait for GDB
(this instance or another one) to connect and continue debugging. After
the `disconnect` command, GDB is again free to connect to
another target.

**`monitor cmd`**
: This command allows you to send commands directly to the remote
monitor.

## [Using the `gdbserver` program](gdb_toc.md#apple-krhugmjvha)

`gdbserver` is a control program for Unix-like systems, which
allows you to connect your program with a remote GDB via
`target remote`---but without linking in the usual debugging stub.

`gdbserver` is not a complete replacement for the debugging stubs,
because it requires essentially the same operating-system facilities
that GDB itself does. In fact, a system that can run
`gdbserver` to connect to a remote GDB could also run
GDB locally! `gdbserver` is sometimes useful nevertheless,
because it is a much smaller program than GDB itself. It is
also easier to port than all of GDB, so you may be able to get
started more quickly on a new system by using `gdbserver`.
Finally, if you develop code for real-time systems, you may find that
the tradeoffs involved in real-time operation make it more convenient to
do as much development work as possible on another system, for example
by cross-compiling. You can use `gdbserver` to make a similar
choice for debugging.

GDB and `gdbserver` communicate via either a serial line
or a TCP connection, using the standard GDB remote serial
protocol.

**_On the target machine,_**
: you need to have a copy of the program you want to debug.
`gdbserver` does not need your program's symbol table, so you can
strip the program if necessary to save space. GDB on the host
system does all the symbol handling.
To use the server, you must tell it how to communicate with GDB;
the name of your program; and the arguments for your program. The usual
syntax is:

```
target> gdbserver comm program [ args ... ]
```

comm is either a device name (to use a serial line) or a TCP
hostname and portnumber. For example, to debug Emacs with the argument
`` `foo.txt' `` and communicate with GDB over the serial port
`/dev/com1':

```
target> gdbserver /dev/com1 emacs foo.txt
```

`gdbserver` waits passively for the host GDB to communicate
with it.
To use a TCP connection instead of a serial line:

```
target> gdbserver host:2345 emacs foo.txt
```

The only difference from the previous example is the first argument,
specifying that you are communicating with the host GDB via
TCP. The `` `host:2345' `` argument means that `gdbserver` is to
expect a TCP connection from machine `` `host' `` to local TCP port 2345.
(Currently, the `` `host' `` part is ignored.) You can choose any number
you want for the port number as long as it does not conflict with any
TCP ports already in use on the target system (for example, `23` is
reserved for `telnet`).[(6)](Debugging%20with%20GDB-2.md#apple-izhu6vbw) You must use the same port number with the host GDB
`target remote` command.
On some targets, `gdbserver` can also attach to running programs.
This is accomplished via the `--attach` argument. The syntax is:

```
target> gdbserver comm --attach pid
```

pid is the process ID of a currently running process. It isn't necessary
to point `gdbserver` at a binary for the running process.

You can debug processes by name instead of process ID if your target has the
`pidof` utility:

```
target> gdbserver comm --attach `pidof PROGRAM`
```

In case more than one copy of PROGRAM is running, or PROGRAM
has multiple threads, most versions of `pidof` support the
`-s` option to only return the first process ID.

**_On the host machine,_**
: connect to your target (see section [Connecting to a remote target](#apple-kncugmjvg4)).
For TCP connections, you must start up `gdbserver` prior to using
the `target remote` command. Otherwise you may get an error whose
text depends on the host system, but which usually looks something like
`` `Connection refused' ``. You don't need to use the `load`
command in GDB when using `gdbserver`, since the program is
already on the target. However, if you want to load the symbols (as
you normally would), do that with the `file` command, and issue
it _before_ connecting to the server; otherwise, you will get an
error message saying `"Program is already running"`, since the
program is considered running after the connection.

## [Using the `gdbserve.nlm` program](gdb_toc.md#apple-krhugmjvhe)

`gdbserve.nlm` is a control program for NetWare systems, which
allows you to connect your program with a remote GDB via
`target remote`.

GDB and `gdbserve.nlm` communicate via a serial line,
using the standard GDB remote serial protocol.

**_On the target machine,_**
: you need to have a copy of the program you want to debug.
`gdbserve.nlm` does not need your program's symbol table, so you
can strip the program if necessary to save space. GDB on the
host system does all the symbol handling.
To use the server, you must tell it how to communicate with
GDB; the name of your program; and the arguments for your
program. The syntax is:

```
load gdbserve [ BOARD=board ] [ PORT=port ]
              [ BAUD=baud ] program [ args ... ]
```

board and port specify the serial line; baud specifies
the baud rate used by the connection. port and node default
to 0, baud defaults to 9600bps.
For example, to debug Emacs with the argument `` `foo.txt' ``and
communicate with GDB over serial port number 2 or board 1
using a 19200bps connection:

```
load gdbserve BOARD=1 PORT=2 BAUD=19200 emacs foo.txt
```

****
: On the GDB host machine, connect to your target (see section [Connecting to a remote target](#apple-kncugmjvg4)).

## [Remote configuration](Debugging%20with%20GDB.md#apple-krhugmjwga)

This section documents the configuration options available when
debugging remote programs. For the options related to the File I/O
extensions of the remote protocol, see section [The `` `system' `` function call](gdb_33.md#apple-kncugmzrha).

**`set remoteaddresssize bits`**
: 

Set the maximum size of address in a memory packet to the specified
number of bits. GDB will mask off the address bits above
that number, when it passes addresses to the remote target. The
default value is the number of bits in the target's address.

**`show remoteaddresssize`**
: Show the current value of remote address size in bits.

**`set remotebaud n`**
: 
Set the baud rate for the remote serial I/O to n baud. The
value is used to set the speed of the serial port used for debugging
remote targets.

**`show remotebaud`**
: Show the current speed of the remote connection.

**`set remotebreak`**
: 

If set to on, GDB sends a `BREAK` signal to the remote
when you press the `Ctrl-C` key to interrupt the program running
on the remote. If set to off, GDB sends the `` `Strl-C' ``
character instead. The default is off, since most remote systems
expect to see `` `Ctrl-C' `` as the interrupt signal.

**`show remotebreak`**
: Show whether GDB sends `BREAK` or `` `Ctrl-C' `` to
interrupt the remote program.

**`set remotedebug`**
: 

Control the debugging of the remote protocol. When enabled, each
packet sent to or received from the remote target is displayed. The
defaults is off.

**`show remotedebug`**
: Show the current setting of the remote protocol debugging.

**`set remotedevice device`**
: 
Set the name of the serial port through which to communicate to the
remote target to device. This is the device used by
GDB to open the serial communications line to the remote
target. There's no default, so you must set a valid port name for the
remote serial communications to work. (Some varieties of the
`target` command accept the port name as part of their
arguments.)

**`show remotedevice`**
: Show the current name of the serial port.

**`set remotelogbase base`**
: Set the base (a.k.a. radix) of logging serial protocol
communications to base. Supported values of base are:
`ascii`, `octal`, and `hex`. The default is
`ascii`.

**`show remotelogbase`**
: Show the current setting of the radix for logging remote serial
protocol.

**`set remotelogfile file`**
: 
Record remote serial communications on the named file. The
default is not to record at all.

**`show remotelogfile.`**
: Show the current setting of the file name on which to record the
serial communications.

**`set remotetimeout num`**
: 

Set the timeout limit to wait for the remote target to respond to
num seconds. The default is 2 seconds.

**`show remotetimeout`**
: Show the current number of seconds to wait for the remote target
responses.

@anchor{set remote hardware-watchpoint-limit}
@anchor{set remote hardware-breakpoint-limit}

**`set remote hardware-watchpoint-limit limit`**
:

**`set remote hardware-breakpoint-limit limit`**
: Restrict GDB to using limit remote hardware breakpoint or
watchpoints. A limit of -1, the default, is treated as unlimited.

**`set remote fetch-register-packet`**
:

**`set remote set-register-packet`**
:

**`set remote P-packet`**
:

**`set remote p-packet`**
: 

Determine whether GDB can set and fetch registers from the
remote target using the `` `P' `` packets. The default depends on the
remote stub's support of the `` `P' `` packets (GDB queries
the stub when this packet is first required).

**`show remote fetch-register-packet`**
:

**`show remote set-register-packet`**
:

**`show remote P-packet`**
:

**`show remote p-packet`**
: Show the current setting of using the `` `P' `` packets for setting and
fetching registers from the remote target.

**`set remote binary-download-packet`**
:

**`set remote X-packet`**
: Determine whether GDB sends downloads in binary mode using
the `` `X' `` packets. The default is on.

**`show remote binary-download-packet`**
:

**`show remote X-packet`**
: Show the current setting of using the `` `X' `` packets for binary
downloads.

**`set remote read-aux-vector-packet`**
: 

Set the use of the remote protocol's `` `qPart:auxv:read' `` (target
auxiliary vector read) request. This request is used to fetch the
remote target's __auxiliary vector__, see section [Operating system auxiliary information](Examining%20Data.md#apple-kncugnrz). The default setting depends on the remote stub's
support of this request (GDB queries the stub when this
request is first required). See section [General Query Packets](GDB%20Remote%20Serial%20Protocol.md#apple-kncugmzqgy), for
more information about this request.

**`show remote read-aux-vector-packet`**
: Show the current setting of use of the `` `qPart:auxv:read' `` request.

**`set remote symbol-lookup-packet`**
: 
Set the use of the remote protocol's `` `qSymbol' `` (target symbol
lookup) request. This request is used to communicate symbol
information to the remote target, e.g., whenever a new shared library
is loaded by the remote (see section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4)). The
default setting depends on the remote stub's support of this request
(GDB queries the stub when this request is first required).
See section [General Query Packets](GDB%20Remote%20Serial%20Protocol.md#apple-kncugmzqgy), for more information about this
request.

**`show remote symbol-lookup-packet`**
: Show the current setting of use of the `` `qSymbol' `` request.

**`set remote verbose-resume-packet`**
: 

Set the use of the remote protocol's `` `vCont' `` (descriptive resume)
request. This request is used to resume specific threads in the
remote target, and to single-step or signal them. The default setting
depends on the remote stub's support of this request (GDB
queries the stub when this request is first required). This setting
affects debugging of multithreaded programs: if `` `vCont' `` cannot be
used, GDB might be unable to single-step a specific thread,
especially under `set scheduler-locking off`; it is also
impossible to pause a specific thread. See section [Packets](GDB%20Remote%20Serial%20Protocol.md#apple-kncugmzqgq), for
more details.

**`show remote verbose-resume-packet`**
: Show the current setting of use of the `` `vCont' `` request

**`set remote software-breakpoint-packet`**
:

**`set remote hardware-breakpoint-packet`**
:

**`set remote write-watchpoint-packet`**
:

**`set remote read-watchpoint-packet`**
:

**`set remote access-watchpoint-packet`**
:

**`set remote Z-packet`**
: 

These commands enable or disable the use of `` `Z' `` packets for
setting breakpoints and watchpoints in the remote target. The default
depends on the remote stub's support of the `` `Z' `` packets
(GDB queries the stub when each packet is first required).
The command `set remote Z-packet`, kept for back-compatibility,
turns on or off all the features that require the use of `` `Z' ``
packets.

**`show remote software-breakpoint-packet`**
:

**`show remote hardware-breakpoint-packet`**
:

**`show remote write-watchpoint-packet`**
:

**`show remote read-watchpoint-packet`**
:

**`show remote access-watchpoint-packet`**
:

**`show remote Z-packet`**
: Show the current setting of `` `Z' `` packets usage.

**`set remote get-thread-local-storage-address`**
: 

This command enables or disables the use of the `` `qGetTLSAddr' ``
(Get Thread Local Storage Address) request packet. The default
depends on whether the remote stub supports this request.
See section [General Query Packets](GDB%20Remote%20Serial%20Protocol.md#apple-kncugmzqgy), for more details about this
packet.

**`show remote get-thread-local-storage-address`**
: 
Show the current setting of `` `qGetTLSAddr' `` packet usage.

## [Implementing a remote stub](Debugging%20with%20GDB.md#apple-krhugmjwge)

The stub files provided with GDB implement the target side of the
communication protocol, and the GDB side is implemented in the
GDB source file `remote.c'. Normally, you can simply allow
these subroutines to communicate, and ignore the details. (If you're
implementing your own stub file, you can still ignore the details: start
with one of the existing stub files. `sparc-stub.c' is the best
organized, and therefore the easiest to read.)

To debug a program running on another machine (the debugging
__target__ machine), you must first arrange for all the usual
prerequisites for the program to run by itself. For example, for a C
program, you need:

1. A startup routine to set up the C runtime environment; these usually
   have a name like `crt0'. The startup routine may be supplied by
   your hardware supplier, or you may have to write your own.
2. A C subroutine library to support your program's
   subroutine calls, notably managing input and output.
3. A way of getting your program to the other machine--for example, a
   download program. These are often supplied by the hardware
   manufacturer, but you may have to write your own from hardware
   documentation.

The next step is to arrange for your program to use a serial port to
communicate with the machine where GDB is running (the __host__
machine). In general terms, the scheme looks like this:

**_On the host,_**
: GDB already understands how to use this protocol; when everything
else is set up, you can simply use the `` `target remote' `` command
(see section [Specifying a Debugging Target](Specifying%20a%20Debugging%20Target.md#apple-kncugmjvga)).

**_On the target,_**
: you must link with your program a few special-purpose subroutines that
implement the GDB remote serial protocol. The file containing these
subroutines is called a __debugging stub__.
On certain remote targets, you can use an auxiliary program
`gdbserver` instead of linking a stub into your program.
See section [Using the `gdbserver` program](#apple-kncugmjvha), for details.

The debugging stub is specific to the architecture of the remote
machine; for example, use `sparc-stub.c' to debug programs on
SPARC boards.

These working remote stubs are distributed with GDB:

**`i386-stub.c`**
: 

For Intel 386 and compatible architectures.

**`m68k-stub.c`**
: 

For Motorola 680x0 architectures.

**`sh-stub.c`**
: 

For Renesas SH architectures.

**`sparc-stub.c`**
: 

For SPARC architectures.

**`sparcl-stub.c`**
: 

For Fujitsu SPARCLITE architectures.

The `README' file in the GDB distribution may list other
recently added stubs.

### [What the stub can do for you](Debugging%20with%20GDB.md#apple-krhugmjwgi)

The debugging stub for your architecture supplies these three
subroutines:

**`set_debug_traps`**
: 

This routine arranges for `handle_exception` to run when your
program stops. You must call this subroutine explicitly near the
beginning of your program.

**`handle_exception`**
: 

This is the central workhorse, but your program never calls it
explicitly--the setup code arranges for `handle_exception` to
run when a trap is triggered.
`handle_exception` takes control when your program stops during
execution (for example, on a breakpoint), and mediates communications
with GDB on the host machine. This is where the communications
protocol is implemented; `handle_exception` acts as the GDB
representative on the target machine. It begins by sending summary
information on the state of your program, then continues to execute,
retrieving and transmitting any information GDB needs, until you
execute a GDB command that makes your program resume; at that point,
`handle_exception` returns control to your own code on the target
machine.

**`breakpoint`**
: 
Use this auxiliary subroutine to make your program contain a
breakpoint. Depending on the particular situation, this may be the only
way for GDB to get control. For instance, if your target
machine has some sort of interrupt button, you won't need to call this;
pressing the interrupt button transfers control to
`handle_exception`---in effect, to GDB. On some machines,
simply receiving characters on the serial port may also trigger a trap;
again, in that situation, you don't need to call `breakpoint` from
your own program--simply running `` `target remote' `` from the host
GDB session gets control.
Call `breakpoint` if none of these is true, or if you simply want
to make certain your program stops at a predetermined point for the
start of your debugging session.

### [What you must do for the stub](Debugging%20with%20GDB.md#apple-krhugmjwgm)

The debugging stubs that come with GDB are set up for a particular
chip architecture, but they have no information about the rest of your
debugging target machine.

First of all you need to tell the stub how to communicate with the
serial port.

**`int getDebugChar()`**
: 
Write this subroutine to read a single character from the serial port.
It may be identical to `getchar` for your target system; a
different name is used to allow you to distinguish the two if you wish.

**`void putDebugChar(int)`**
: 
Write this subroutine to write a single character to the serial port.
It may be identical to `putchar` for your target system; a
different name is used to allow you to distinguish the two if you wish.

If you want GDB to be able to stop your program while it is
running, you need to use an interrupt-driven serial driver, and arrange
for it to stop when it receives a `^C` (`` `\003' ``, the control-C
character). That is the character which GDB uses to tell the
remote system to stop.

Getting the debugging target to return the proper status to GDB
probably requires changes to the standard stub; one quick and dirty way
is to just execute a breakpoint instruction (the "dirty" part is that
GDB reports a `SIGTRAP` instead of a `SIGINT`).

Other routines you need to supply are:

**`void exceptionHandler (int exception_number, void *exception_address)`**
: 
Write this function to install exception_address in the exception
handling tables. You need to do this because the stub does not have any
way of knowing what the exception handling tables on your target system
are like (for example, the processor's table might be in ROM,
containing entries which point to a table in RAM).
exception_number is the exception number which should be changed;
its meaning is architecture-dependent (for example, different numbers
might represent divide by zero, misaligned access, etc). When this
exception occurs, control should be transferred directly to
exception_address, and the processor state (stack, registers,
and so on) should be just as it is when a processor exception occurs. So if
you want to use a jump instruction to reach exception_address, it
should be a simple jump, not a jump to subroutine.
For the 386, exception_address should be installed as an interrupt
gate so that interrupts are masked while the handler runs. The gate
should be at privilege level 0 (the most privileged level). The
SPARC and 68k stubs are able to mask interrupts themselves without
help from `exceptionHandler`.

**`void flush_i_cache()`**
: 
On SPARC and SPARCLITE only, write this subroutine to flush the
instruction cache, if any, on your target machine. If there is no
instruction cache, this subroutine may be a no-op.
On target machines that have instruction caches, GDB requires this
function to make certain that the state of your program is stable.

You must also make sure this library routine is available:

**`void *memset(void *, int, int)`**
: 
This is the standard library function `memset` that sets an area of
memory to a known value. If you have one of the free versions of
`libc.a`, `memset` can be found there; otherwise, you must
either obtain it from your hardware manufacturer, or write your own.

If you do not use the GNU C compiler, you may need other standard
library subroutines as well; this varies from one stub to another,
but in general the stubs are likely to use any of the common library
subroutines which `gcc` generates as inline code.

### [Putting it all together](Debugging%20with%20GDB.md#apple-krhugmjwgq)

In summary, when your program is ready to debug, you must follow these
steps.

1. Make sure you have defined the supporting low-level routines
   (see section [What you must do for the stub](#apple-kncugmjwgm)):

   ```
   getDebugChar, putDebugChar,
   flush_i_cache, memset, exceptionHandler.
   ```
2. Insert these lines near the top of your program:

   ```
   set_debug_traps();
   breakpoint();
   ```
3. For the 680x0 stub only, you need to provide a variable called
   `exceptionHook`. Normally you just use:

   ```
   void (*exceptionHook)() = 0;
   ```

   but if before calling `set_debug_traps`, you set it to point to a
   function in your program, that function is called when
   `GDB` continues after stopping on a trap (for example, bus
   error). The function indicated by `exceptionHook` is called with
   one parameter: an `int` which is the exception number.
4. Compile and link together: your program, the GDB debugging stub for
   your target architecture, and the supporting subroutines.
5. Make sure you have a serial connection between your target machine and
   the GDB host, and identify the serial port on the host.
6. Download your program to your target machine (or get it there by
   whatever means the manufacturer provides), and start it.
7. To start remote debugging, run GDB on the host machine, and specify
   as an executable file the program that is running in the remote machine.
   This tells GDB how to find your program's symbols and the contents
   of its pure text.
8. Start GDB on the host, and connect to the target
   (see section [Connecting to a remote target](#apple-kncugmjvg4)).

   ```
   target remote udp:manyfarms:2828
   ```

   When using a UDP connection for remote debugging, you should keep in mind
   that the `U' stands for "Unreliable". UDP can silently drop packets on
   busy or unreliable networks, which will cause havoc with your debugging
   session.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Specifying%20a%20Debugging%20Target.md), [next](Configuration-Specific%20Information.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
