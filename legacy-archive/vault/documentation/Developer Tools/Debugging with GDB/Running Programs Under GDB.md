---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_5.html
archived_at: '2026-07-15T07:31:03.604780Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Commands.md), [next](Stopping%20and%20Continuing.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Running Programs Under GDB](Debugging%20with%20GDB.md#apple-krhugmjy)

When you run a program under GDB, you must first generate
debugging information when you compile it.

You may start GDB with its arguments, if any, in an environment
of your choice. If you are doing native debugging, you may redirect
your program's input and output, debug an already running process, or
kill a child process.

## [Compiling for debugging](Debugging%20with%20GDB.md#apple-krhugmjz)

In order to debug a program effectively, you need to generate
debugging information when you compile it. This debugging information
is stored in the object file; it describes the data type of each
variable or function and the correspondence between source line numbers
and addresses in the executable code.

To request debugging information, specify the `` `-g' `` option when you run
the compiler.

Most compilers do not include information about preprocessor macros in
the debugging information if you specify the @option{-g} flag alone,
because this information is rather large. Version 3.1 of GCC,
the GNU C compiler, provides macro information if you specify the
options @option{-gdwarf-2} and @option{-g3}; the former option requests
debugging information in the Dwarf 2 format, and the latter requests
"extra information". In the future, we hope to find more compact ways
to represent macro information, so that it can be included with
@option{-g} alone.

Programs that are to be shipped to your customers are compiled with
optimizations, using the `` `-O' `` compiler option. However, many
compilers are unable to handle the `` `-g' `` and `` `-O' `` options
together. Using those compilers, you cannot generate optimized
executables containing debugging information.

GCC, the GNU C/C++ compiler, supports `` `-g' `` with or
without `` `-O' ``, making it possible to debug optimized code. We
recommend that you _always_ use `` `-g' `` whenever you compile a
program. You may think your program is correct, but there is no sense
in pushing your luck.

When you debug a program compiled with `` `-g -O' ``, remember that the
optimizer is rearranging your code; the debugger shows you what is
really there. Do not be too surprised when the execution path does not
exactly match your source file! An extreme example: if you define a
variable, but never use it, GDB never sees that
variable--because the compiler optimizes it out of existence.

Some things do not work as well with `` `-g -O' `` as with just
`` `-g' ``, particularly on machines with instruction scheduling. If in
doubt, recompile with `` `-g' `` alone, and if this fixes the problem,
please report it to us as a bug (including a test case!).
See section [Program variables](Examining%20Data.md#apple-kncugnjy), for more information about debugging optimized code.

Older versions of the GNU C compiler permitted a variant option
`` `-gg' `` for debugging information. GDB no longer supports this
format; if your GNU C compiler has this option, do not use it.

GDB knows about preprocessor macros and can show you their
expansion (see section [C Preprocessor Macros](C%20Preprocessor%20Macros.md#apple-kncugnzz)). Most compilers do not include information
about preprocessor macros in the debugging information if you specify
the @option{-g} flag alone, because this information is rather large.
Version 3.1 and later of GCC, the GNU C compiler,
provides macro information if you specify the options
@option{-gdwarf-2} and @option{-g3}; the former option requests
debugging information in the Dwarf 2 format, and the latter requests
"extra information". In the future, we hope to find more compact
ways to represent macro information, so that it can be included with
@option{-g} alone.

## [Starting your program](Debugging%20with%20GDB.md#apple-krhugmrq)

**`run`**
: 

**`r`**
: Use the `run` command to start your program under GDB.
You must first specify the program name (except on VxWorks) with an
argument to GDB (see section [Getting In and Out of GDB](Getting%20In%20and%20Out%20of%20GDB.md#apple-kncugnq)), or by using the `file` or `exec-file` command
(see section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4)).

If you are running your program in an execution environment that
supports processes, `run` creates an inferior process and makes
that process run your program. (In environments without processes,
`run` jumps to the start of your program.)

The execution of a program is affected by certain information it
receives from its superior. GDB provides ways to specify this
information, which you must do _before_ starting your program. (You
can change it after starting your program, but such changes only affect
your program the next time you start it.) This information may be
divided into four categories:

**The _arguments._**
: Specify the arguments to give your program as the arguments of the
`run` command. If a shell is available on your target, the shell
is used to pass the arguments, so that you may use normal conventions
(such as wildcard expansion or variable substitution) in describing
the arguments.
In Unix systems, you can control which shell is used with the
`SHELL` environment variable.
See section [Your program's arguments](#apple-kncugmrr).

**The _environment._**
: Your program normally inherits its environment from GDB, but you can
use the GDB commands `set environment` and `unset
environment` to change parts of the environment that affect
your program. See section [Your program's environment](#apple-kncugmrs).

**The _working directory._**
: Your program inherits its working directory from GDB. You can set
the GDB working directory with the `cd` command in GDB.
See section [Your program's working directory](#apple-kncugmrt).

**The _standard input and output._**
: Your program normally uses the same device for standard input and
standard output as GDB is using. You can redirect input and output
in the `run` command line, or you can use the `tty` command to
set a different device for your program.
See section [Your program's input and output](#apple-kncugmru).

_Warning:_ While input and output redirection work, you cannot use
pipes to pass the output of the program you are debugging to another
program; if you attempt this, GDB is likely to wind up debugging the
wrong program.

When you issue the `run` command, your program begins to execute
immediately. See section [Stopping and Continuing](Stopping%20and%20Continuing.md#apple-kncugmrz), for discussion
of how to arrange for your program to stop. Once your program has
stopped, you may call functions in your program, using the `print`
or `call` commands. See section [Examining Data](Examining%20Data.md#apple-kncugnjw).

If the modification time of your symbol file has changed since the last
time GDB read its symbols, GDB discards its symbol
table, and reads it again. When it does this, GDB tries to retain
your current breakpoints.

**`start`**
: 

The name of the main procedure can vary from language to language.
With C or C++, the main procedure name is always `main`, but
other languages such as Ada do not require a specific name for their
main procedure. The debugger provides a convenient way to start the
execution of the program and to stop at the beginning of the main
procedure, depending on the language used.
The `` `start' `` command does the equivalent of setting a temporary
breakpoint at the beginning of the main procedure and then invoking
the `` `run' `` command.

Some programs contain an __elaboration__ phase where some startup code is
executed before the main procedure is called. This depends on the
languages used to write your program. In C++, for instance,
constructors for static and global objects are executed before
`main` is called. It is therefore possible that the debugger stops
before reaching the main procedure. However, the temporary breakpoint
will remain to halt execution.
Specify the arguments to give to your program as arguments to the
`` `start' `` command. These arguments will be given verbatim to the
underlying `` `run' `` command. Note that the same arguments will be
reused if no argument is provided during subsequent calls to
`` `start' `` or `` `run' ``.
It is sometimes necessary to debug the program during elaboration. In
these cases, using the `start` command would stop the execution of
your program too late, as the program would have already completed the
elaboration phase. Under these circumstances, insert breakpoints in your
elaboration code before running your program.

## [Your program's arguments](Debugging%20with%20GDB.md#apple-krhugmrr)

The arguments to your program can be specified by the arguments of the
`run` command.
They are passed to a shell, which expands wildcard characters and
performs redirection of I/O, and thence to your program. Your
`SHELL` environment variable (if it exists) specifies what shell
GDB uses. If you do not define `SHELL`, GDB uses
the default shell (`/bin/sh' on Unix).

On non-Unix systems, the program is usually invoked directly by
GDB, which emulates I/O redirection via the appropriate system
calls, and the wildcard characters are expanded by the startup code of
the program, not by the shell.

`run` with no arguments uses the same arguments used by the previous
`run`, or those set by the `set args` command.

**`set args`**
: 
Specify the arguments to be used the next time your program is run. If
`set args` has no arguments, `run` executes your program
with no arguments. Once you have run your program with arguments,
using `set args` before the next `run` is the only way to run
it again without arguments.

**`show args`**
: Show the arguments to give your program when it is started.

## [Your program's environment](Debugging%20with%20GDB.md#apple-krhugmrs)

The __environment__ consists of a set of environment variables and
their values. Environment variables conventionally record such things as
your user name, your home directory, your terminal type, and your search
path for programs to run. Usually you set up environment variables with
the shell and they are inherited by all the other programs you run. When
debugging, it can be useful to try running your program with a modified
environment without having to start GDB over again.

**`path directory`**
: 
Add directory to the front of the `PATH` environment variable
(the search path for executables) that will be passed to your program.
The value of `PATH` used by GDB does not change.
You may specify several directory names, separated by whitespace or by a
system-dependent separator character (`` `:' `` on Unix, `` `;' `` on
MS-DOS and MS-Windows). If directory is already in the path, it
is moved to the front, so it is searched sooner.
You can use the string `` `$cwd' `` to refer to whatever is the current
working directory at the time GDB searches the path. If you
use `` `.' `` instead, it refers to the directory where you executed the
`path` command. GDB replaces `` `.' `` in the
directory argument (with the current path) before adding
directory to the search path.

**`show paths`**
: Display the list of search paths for executables (the `PATH`
environment variable).

**`show environment [varname]`**
: Print the value of environment variable varname to be given to
your program when it starts. If you do not supply varname,
print the names and values of all environment variables to be given to
your program. You can abbreviate `environment` as `env`.

**`set environment varname [=value]`**
: Set environment variable varname to value. The value
changes for your program only, not for GDB itself. value may
be any string; the values of environment variables are just strings, and
any interpretation is supplied by your program itself. The value
parameter is optional; if it is eliminated, the variable is set to a
null value.
For example, this command:

```
set env USER = foo
```

tells the debugged program, when subsequently run, that its user is named
`` `foo' ``. (The spaces around `` `=' `` are used for clarity here; they
are not actually required.)

**`unset environment varname`**
: Remove variable varname from the environment to be passed to your
program. This is different from `` `set env varname =' ``;
`unset environment` removes the variable from the environment,
rather than assigning it an empty value.

_Warning:_ On Unix systems, GDB runs your program using
the shell indicated
by your `SHELL` environment variable if it exists (or
`/bin/sh` if not). If your `SHELL` variable names a shell
that runs an initialization file--such as `.cshrc' for C-shell, or
`.bashrc' for BASH--any variables you set in that file affect
your program. You may wish to move setting of environment variables to
files that are only run when you sign on, such as `.login' or
`.profile'.

## [Your program's working directory](Debugging%20with%20GDB.md#apple-krhugmrt)

Each time you start your program with `run`, it inherits its
working directory from the current working directory of GDB.
The GDB working directory is initially whatever it inherited
from its parent process (typically the shell), but you can specify a new
working directory in GDB with the `cd` command.

The GDB working directory also serves as a default for the commands
that specify files for GDB to operate on. See section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4).

**`cd directory`**
: 

Set the GDB working directory to directory.

**`pwd`**
: Print the GDB working directory.

It is generally impossible to find the current working directory of
the process being debugged (since a program can change its directory
during its run). If you work on a system where GDB is
configured with the `/proc' support, you can use the `info
proc` command (see section [SVR4 process information](Configuration-Specific%20Information.md#apple-kncugmjwhe)) to find out the
current working directory of the debuggee.

## [Your program's input and output](Debugging%20with%20GDB.md#apple-krhugmru)

By default, the program you run under GDB does input and output to
the same terminal that GDB uses. GDB switches the terminal
to its own terminal modes to interact with you, but it records the terminal
modes your program was using and switches back to them when you continue
running your program.

**`info terminal`**
: 
Displays information recorded by GDB about the terminal modes your
program is using.

You can redirect your program's input and/or output using shell
redirection with the `run` command. For example,

```
run > outfile
```

starts your program, diverting its output to the file `outfile'.

Another way to specify where your program should do input and output is
with the `tty` command. This command accepts a file name as
argument, and causes this file to be the default for future `run`
commands. It also resets the controlling terminal for the child
process, for future `run` commands. For example,

```
tty /dev/ttyb
```

directs that processes started with subsequent `run` commands
default to do input and output on the terminal `/dev/ttyb' and have
that as their controlling terminal.

An explicit redirection in `run` overrides the `tty` command's
effect on the input/output device, but not its effect on the controlling
terminal.

When you use the `tty` command or redirect input in the `run`
command, only the input _for your program_ is affected. The input
for GDB still comes from your terminal. `tty` is an alias
for `set inferior-tty`.

You can use the `show inferior-tty` command to tell GDB to
display the name of the terminal that will be used for future runs of your
program.

**`set inferior-tty /dev/ttyb`**
: 
Set the tty for the program being debugged to /dev/ttyb.

**`show inferior-tty`**
: 
Show the current tty for the program being debugged.

## [Debugging an already-running process](Debugging%20with%20GDB.md#apple-krhugmrv)

**`attach process-id`**
: This command attaches to a running process--one that was started
outside GDB. (`info files` shows your active
targets.) The command takes as argument a process ID. The usual way to
find out the process-id of a Unix process is with the `ps` utility,
or with the `` `jobs -l' `` shell command.
`attach` does not repeat if you press `RET` a second time after
executing the command.

To use `attach`, your program must be running in an environment
which supports processes; for example, `attach` does not work for
programs on bare-board targets that lack an operating system. You must
also have permission to send the process a signal.

When you use `attach`, the debugger finds the program running in
the process first by looking in the current working directory, then (if
the program is not found) by using the source file search path
(see section [Specifying source directories](Examining%20Source%20Files.md#apple-kncugnju)). You can also use
the `file` command to load the program. See section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4).

The first thing GDB does after arranging to debug the specified
process is to stop it. You can examine and modify an attached process
with all the GDB commands that are ordinarily available when
you start processes with `run`. You can insert breakpoints; you
can step and continue; you can modify storage. If you would rather the
process continue running, you may use the `continue` command after
attaching GDB to the process.

**`detach`**
: 
When you have finished debugging the attached process, you can use the
`detach` command to release it from GDB control. Detaching
the process continues its execution. After the `detach` command,
that process and GDB become completely independent once more, and you
are ready to `attach` another process or start one with `run`.
`detach` does not repeat if you press `RET` again after
executing the command.

If you exit GDB or use the `run` command while you have an
attached process, you kill that process. By default, GDB asks
for confirmation if you try to do either of these things; you can
control whether or not you need to confirm by using the `set
confirm` command (see section [Optional warnings and messages](Controlling%20GDB.md#apple-kncugmrsge)).

## [Killing the child process](Debugging%20with%20GDB.md#apple-krhugmrw)

**`kill`**
: 
Kill the child process in which your program is running under GDB.

This command is useful if you wish to debug a core dump instead of a
running process. GDB ignores any core dump file while your program
is running.

On some operating systems, a program cannot be executed outside GDB
while you have breakpoints set on it inside GDB. You can use the
`kill` command in this situation to permit running your program
outside the debugger.

The `kill` command is also useful if you wish to recompile and
relink your program, since on many systems it is impossible to modify an
executable file while it is running in a process. In this case, when you
next type `run`, GDB notices that the file has changed, and
reads the symbol table again (while trying to preserve your current
breakpoint settings).

## [Debugging programs with multiple threads](Debugging%20with%20GDB.md#apple-krhugmrx)

In some operating systems, such as HP-UX and Solaris, a single program
may have more than one __thread__ of execution. The precise semantics
of threads differ from one operating system to another, but in general
the threads of a single program are akin to multiple processes--except
that they share one address space (that is, they can all examine and
modify the same variables). On the other hand, each thread has its own
registers and execution stack, and perhaps private memory.

GDB provides these facilities for debugging multi-thread
programs:

- automatic notification of new threads
- `` `thread threadno' ``, a command to switch among threads
- `` `info threads' ``, a command to inquire about existing threads
- `` `thread apply [threadno] [all] args' ``,
  a command to apply a command to a list of threads
- thread-specific breakpoints

> _Warning:_ These facilities are not yet available on every
> GDB configuration where the operating system supports threads.
> If your GDB does not support threads, these commands have no
> effect. For example, a system without thread support shows no output
> from `` `info threads' ``, and always rejects the `thread` command,
> like this:
>
> ```
> (gdb) info threads
> (gdb) thread 1
> Thread ID 1 not known.  Use the "info threads" command to
> see the IDs of currently known threads.
> ```

The GDB thread debugging facility allows you to observe all
threads while your program runs--but whenever GDB takes
control, one thread in particular is always the focus of debugging.
This thread is called the __current thread__. Debugging commands show
program information from the perspective of the current thread.

Whenever GDB detects a new thread in your program, it displays
the target system's identification for the thread with a message in the
form `` `[New systag]' ``. systag is a thread identifier
whose form varies depending on the particular system. For example, on
LynxOS, you might see

```
[New process 35 thread 27]
```

when GDB notices a new thread. In contrast, on an SGI system,
the systag is simply something like `` `process 368' ``, with no
further qualifier.

For debugging purposes, GDB associates its own thread
number--always a single integer--with each thread in your program.

**`info threads`**
: 
Display a summary of all threads currently in your
program. GDB displays for each thread (in this order):

1. the thread number assigned by GDB
2. the target system's thread identifier (systag)
3. the current stack frame summary for that thread

An asterisk `` `*' `` to the left of the GDB thread number
indicates the current thread.
For example,

```
(gdb) info threads
  3 process 35 thread 27  0x34e5 in sigpause ()
  2 process 35 thread 23  0x34e5 in sigpause ()
* 1 process 35 thread 13  main (argc=1, argv=0x7ffffff8)
    at threadtest.c:68
```

On HP-UX systems:

For debugging purposes, GDB associates its own thread
number--a small integer assigned in thread-creation order--with each
thread in your program.

Whenever GDB detects a new thread in your program, it displays
both GDB's thread number and the target system's identification for the thread with a message in the
form `` `[New systag]' ``. systag is a thread identifier
whose form varies depending on the particular system. For example, on
HP-UX, you see

```
[New thread 2 (system thread 26594)]
```

when GDB notices a new thread.

**`info threads`**
: 
Display a summary of all threads currently in your
program. GDB displays for each thread (in this order):

1. the thread number assigned by GDB
2. the target system's thread identifier (systag)
3. the current stack frame summary for that thread

An asterisk `` `*' `` to the left of the GDB thread number
indicates the current thread.
For example,

```
(gdb) info threads
    * 3 system thread 26607  worker (wptr=0x7b09c318 "@") \
                               at quicksort.c:137
      2 system thread 26606  0x7b0030d8 in __ksleep () \
                               from /usr/lib/libc.2
      1 system thread 27905  0x7b003498 in _brk () \
                               from /usr/lib/libc.2
```

On Solaris, you can display more information about user threads with a
Solaris-specific command:

**`maint info sol-threads`**
: 

Display info on Solaris user threads.

**`thread threadno`**
: 
Make thread number threadno the current thread. The command
argument threadno is the internal GDB thread number, as
shown in the first field of the `` `info threads' `` display.
GDB responds by displaying the system identifier of the thread
you selected, and its current stack frame summary:

```
(gdb) thread 2
[Switching to process 35 thread 23]
0x34e5 in sigpause ()
```

As with the `` `[New ...]' `` message, the form of the text after
`` `Switching to' `` depends on your system's conventions for identifying
threads.

**`thread apply [threadno] [all] args`**
: The `thread apply` command allows you to apply a command to one or
more threads. Specify the numbers of the threads that you want affected
with the command argument threadno. threadno is the internal
GDB thread number, as shown in the first field of the `` `info
threads' `` display. To apply a command to all threads, use
`thread apply all` args.

Whenever GDB stops your program, due to a breakpoint or a
signal, it automatically selects the thread where that breakpoint or
signal happened. GDB alerts you to the context switch with a
message of the form `` `[Switching to systag]' `` to identify the
thread.

See section [Stopping and starting multi-thread programs](Stopping%20and%20Continuing.md#apple-kncugnbt), for
more information about how GDB behaves when you stop and start
programs with multiple threads.

See section [Setting watchpoints](Stopping%20and%20Continuing.md#apple-kncugmzs), for information about
watchpoints in programs with multiple threads.

## [Debugging programs with multiple processes](Debugging%20with%20GDB.md#apple-krhugmry)

On most systems, GDB has no special support for debugging
programs which create additional processes using the `fork`
function. When a program forks, GDB will continue to debug the
parent process and the child process will run unimpeded. If you have
set a breakpoint in any code which the child then executes, the child
will get a `SIGTRAP` signal which (unless it catches the signal)
will cause it to terminate.

However, if you want to debug the child process there is a workaround
which isn't too painful. Put a call to `sleep` in the code which
the child process executes after the fork. It may be useful to sleep
only if a certain environment variable is set, or a certain file exists,
so that the delay need not occur when you don't want to run GDB
on the child. While the child is sleeping, use the `ps` program to
get its process ID. Then tell GDB (a new invocation of
GDB if you are also debugging the parent process) to attach to
the child process (see section [Debugging an already-running process](#apple-kncugmrv)). From that point on you can debug
the child process just like any other process which you attached to.

On some systems, GDB provides support for debugging programs that
create additional processes using the `fork` or `vfork` functions.
Currently, the only platforms with this feature are HP-UX (11.x and later
only?) and GNU/Linux (kernel version 2.5.60 and later).

By default, when a program forks, GDB will continue to debug
the parent process and the child process will run unimpeded.

If you want to follow the child process instead of the parent process,
use the command `set follow-fork-mode`.

**`set follow-fork-mode mode`**
: 
Set the debugger response to a program call of `fork` or
`vfork`. A call to `fork` or `vfork` creates a new
process. The mode argument can be:

**`parent`**
: The original process is debugged after a fork. The child process runs
unimpeded. This is the default.

**`child`**
: The new process is debugged after a fork. The parent process runs
unimpeded.

**`show follow-fork-mode`**
: Display the current debugger response to a `fork` or `vfork` call.

If you ask to debug a child process and a `vfork` is followed by an
`exec`, GDB executes the new target up to the first
breakpoint in the new target. If you have a breakpoint set on
`main` in your original program, the breakpoint will also be set on
the child process's `main`.

When a child process is spawned by `vfork`, you cannot debug the
child or parent until an `exec` call completes.

If you issue a `run` command to GDB after an `exec`
call executes, the new target restarts. To restart the parent process,
use the `file` command with the parent executable name as its
argument.

You can use the `catch` command to make GDB stop whenever
a `fork`, `vfork`, or `exec` call is made. See section [Setting catchpoints](Stopping%20and%20Continuing.md#apple-kncugmzt).

---

Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Commands.md), [next](Stopping%20and%20Continuing.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
