---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_3.html
archived_at: '2026-07-15T07:31:03.441789Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](A%20Sample%20GDB%20Session.md), [next](GDB%20Commands.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Getting In and Out of GDB](Debugging%20with%20GDB.md#apple-krhugnq)

This chapter discusses how to start GDB, and how to get out of it.
The essentials are:

- type `` `gdb' `` to start GDB.
- type `quit` or `C-d` to exit.

## [Invoking GDB](Debugging%20with%20GDB.md#apple-krhugny)

Invoke GDB by running the program `gdb`. Once started,
GDB reads commands from the terminal until you tell it to exit.

You can also run `gdb` with a variety of arguments and options,
to specify more of your debugging environment at the outset.

The command-line options described here are designed
to cover a variety of situations; in some environments, some of these
options may effectively be unavailable.

The most usual way to start GDB is with one argument,
specifying an executable program:

```
gdb program
```

You can also start with both an executable program and a core file
specified:

```
gdb program core
```

You can, instead, specify a process ID as a second argument, if you want
to debug a running process:

```
gdb program 1234
```

would attach GDB to process `1234` (unless you also have a file
named `1234'; GDB does check for a core file first).

Taking advantage of the second command-line argument requires a fairly
complete operating system; when you use GDB as a remote
debugger attached to a bare board, there may not be any notion of
"process", and there is often no way to get a core dump. GDB
will warn you if it is unable to attach or to read core dumps.

You can optionally have `gdb` pass any arguments after the
executable file to the inferior using `--args`. This option stops
option processing.

```
gdb --args gcc -O2 -c foo.c
```

This will cause `gdb` to debug `gcc`, and to set
`gcc`'s command-line arguments (see section [Your program's arguments](Running%20Programs%20Under%20GDB.md#apple-kncugmrr)) to `` `-O2 -c foo.c' ``.

You can run `gdb` without printing the front material, which describes
GDB's non-warranty, by specifying `-silent`:

```
gdb -silent
```

You can further control how GDB starts up by using command-line
options. GDB itself can remind you of the options available.

Type

```
gdb -help
```

to display all available options and briefly describe their use
(`` `gdb -h' `` is a shorter equivalent).

All options and command line arguments you give are processed
in sequential order. The order makes a difference when the
`` `-x' `` option is used.

### [Choosing files](Debugging%20with%20GDB.md#apple-krhugoa)

When GDB starts, it reads any arguments other than options as
specifying an executable file and core file (or process ID). This is
the same as if the arguments were specified by the `` `-se' `` and
`` `-c' `` (or `` `-p' `` options respectively. (GDB reads the
first argument that does not have an associated option flag as
equivalent to the `` `-se' `` option followed by that argument; and the
second argument that does not have an associated option flag, if any, as
equivalent to the `` `-c' ``/`` `-p' `` option followed by that argument.)
If the second argument begins with a decimal digit, GDB will
first attempt to attach to it as a process, and if that fails, attempt
to open it as a corefile. If you have a corefile whose name begins with
a digit, you can prevent GDB from treating it as a pid by
prefixing it with `./', eg. `./12345'.

If GDB has not been configured to included core file support,
such as for most embedded targets, then it will complain about a second
argument and ignore it.

Many options have both long and short forms; both are shown in the
following list. GDB also recognizes the long forms if you truncate
them, so long as enough of the option is present to be unambiguous.
(If you prefer, you can flag option arguments with `` `--' `` rather
than `` `-' ``, though we illustrate the more usual convention.)

**`-symbols file`**
:

**`-s file`**
: 

Read symbol table from file file.

**`-exec file`**
:

**`-e file`**
: 

Use file file as the executable file to execute when appropriate,
and for examining pure data in conjunction with a core dump.

**`-se file`**
: 
Read symbol table from file file and use it as the executable
file.

**`-core file`**
:

**`-c file`**
: 

Use file file as a core dump to examine.

**`-c number`**
:

**`-pid number`**
:

**`-p number`**
: 

Connect to process ID number, as with the `attach` command.
If there is no such process, GDB will attempt to open a core
file named number.

**`-command file`**
:

**`-x file`**
: 

Execute GDB commands from file file. See section [Command files](Canned%20Sequences%20of%20Commands.md#apple-kncugmrsgy).

**`-directory directory`**
:

**`-d directory`**
: 

Add directory to the path to search for source files.

**`-m`**
:

**`-mapped`**
: 

_Warning: this option depends on operating system facilities that are not
supported on all systems._
If memory-mapped files are available on your system through the `mmap`
system call, you can use this option
to have GDB write the symbols from your
program into a reusable file in the current directory. If the program you are debugging is
called `/tmp/fred', the mapped symbol file is `/tmp/fred.syms'.
Future GDB debugging sessions notice the presence of this file,
and can quickly map in symbol information from it, rather than reading
the symbol table from the executable program.
The `.syms' file is specific to the host machine where GDB
is run. It holds an exact image of the internal GDB symbol
table. It cannot be shared across multiple host platforms.

**`-r`**
:

**`-readnow`**
: 

Read each symbol file's entire symbol table immediately, rather than
the default, which is to read it incrementally as it is needed.
This makes startup slower, but makes future operations faster.

You typically combine the `-mapped` and `-readnow` options in
order to build a `.syms' file that contains complete symbol
information. (See section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4), for information
on `.syms' files.) A simple GDB invocation to do nothing
but build a `.syms' file for future use is:

```
gdb -batch -nx -mapped -readnow programname
```

### [Choosing modes](Debugging%20with%20GDB.md#apple-krhugoi)

You can run GDB in various alternative modes--for example, in
batch mode or quiet mode.

**`-nx`**
:

**`-n`**
: 

Do not execute commands found in any initialization files. Normally,
GDB executes the commands in these files after all the command
options and arguments have been processed. See section [Command files](Canned%20Sequences%20of%20Commands.md#apple-kncugmrsgy).

**`-quiet`**
:

**`-silent`**
:

**`-q`**
: 

"Quiet". Do not print the introductory and copyright messages. These
messages are also suppressed in batch mode.

**`-batch`**
: 
Run in batch mode. Exit with status `0` after processing all the
command files specified with `` `-x' `` (and all commands from
initialization files, if not inhibited with `` `-n' ``). Exit with
nonzero status if an error occurs in executing the GDB commands
in the command files.
Batch mode may be useful for running GDB as a filter, for
example to download and run a program on another computer; in order to
make this more useful, the message

```
Program exited normally.
```

(which is ordinarily issued whenever a program running under
GDB control terminates) is not issued when running in batch
mode.

**`-nowindows`**
:

**`-nw`**
: 

"No windows". If GDB comes with a graphical user interface
(GUI) built in, then this option tells GDB to only use the command-line
interface. If no GUI is available, this option has no effect.

**`-windows`**
:

**`-w`**
: 

If GDB includes a GUI, then this option requires it to be
used if possible.

**`-cd directory`**
: 
Run GDB using directory as its working directory,
instead of the current directory.

**`-fullname`**
:

**`-f`**
: 

GNU Emacs sets this option when it runs GDB as a
subprocess. It tells GDB to output the full file name and line
number in a standard, recognizable fashion each time a stack frame is
displayed (which includes each time your program stops). This
recognizable format looks like two `` `\032' `` characters, followed by
the file name, line number and character position separated by colons,
and a newline. The Emacs-to-GDB interface program uses the two
`` `\032' `` characters as a signal to display the source code for the
frame.

**`-epoch`**
: 
The Epoch Emacs-GDB interface sets this option when it runs
GDB as a subprocess. It tells GDB to modify its print
routines so as to allow Epoch to display values of expressions in a
separate window.

**`-annotate level`**
: 
This option sets the __annotation level__ inside GDB. Its
effect is identical to using `` `set annotate level' ``
(see section [GDB Annotations](GDB%20Annotations.md#apple-kncugmrvhe)). The annotation level controls how much
information GDB prints together with its prompt, values of
expressions, source lines, and other types of output. Level 0 is the
normal, level 1 is for use when GDB is run as a subprocess of
GNU Emacs, level 3 is the maximum annotation suitable for programs
that control GDB, and level 2 has been deprecated.
The annotation mechanism has largely been superseded by GDB/MI
(see section [The GDB/MI Interface](The%20GDB-MI%20Interface.md#apple-kncugmrtgy)).

**`--args`**
: 
Change interpretation of command line so that arguments following the
executable file are passed as command line arguments to the inferior.
This option stops option processing.

**`-baud bps`**
:

**`-b bps`**
: 

Set the line speed (baud rate or bits per second) of any serial
interface used by GDB for remote debugging.

**`-l timeout`**
: 
Set the timeout (in seconds) of any communication used by GDB
for remote debugging.

**`-tty device`**
:

**`-t device`**
: 

Run using device for your program's standard input and output.

**`-tui`**
: 
Activate the __Text User Interface__ when starting. The Text User
Interface manages several text windows on the terminal, showing
source, assembly, registers and GDB command outputs
(see section [GDB Text User Interface](GDB%20Text%20User%20Interface.md#apple-kncugmrshe)). Alternatively, the
Text User Interface can be enabled by invoking the program
`` `gdbtui' ``. Do not use this option if you run GDB from
Emacs (see section [Using GDB under GNU Emacs](Using%20GDB%20under%20GNU%20Emacs.md#apple-kncugmrtgu)).

**`-interpreter interp`**
: 
Use the interpreter interp for interface with the controlling
program or device. This option is meant to be set by programs which
communicate with GDB using it as a back end.
See section [Command Interpreters](Command%20Interpreters.md#apple-kncugmrsha).
`` `--interpreter=mi' `` (or `` `--interpreter=mi2' ``) causes
GDB to use the __GDB/MI interface__ (see section [The GDB/MI Interface](The%20GDB-MI%20Interface.md#apple-kncugmrtgy)) included since GDB version 6.0. The
previous GDB/MI interface, included in GDB version 5.3 and
selected with `` `--interpreter=mi1' ``, is deprecated. Earlier
GDB/MI interfaces are no longer supported.

**`-write`**
: 
Open the executable and core files for both reading and writing. This
is equivalent to the `` `set write on' `` command inside GDB
(see section [Patching programs](Altering%20Execution.md#apple-kncugmjugu)).

**`-statistics`**
: 
This option causes GDB to print statistics about time and
memory usage after it completes each command and returns to the prompt.

**`-version`**
: 
This option causes GDB to print its version number and
no-warranty blurb, and exit.

### [What GDB does during startup](Debugging%20with%20GDB.md#apple-krhugmjq)

Here's the description of what GDB does during session startup:

1. Sets up the command interpreter as specified by the command line
   (see section [Choosing modes](#apple-kncugoi)).
2. 
   Reads the __init file__ (if any) in your home directory[(1)](Debugging%20with%20GDB-2.md#apple-izhu6vbr) and executes all the commands in
   that file.
3. Processes command line options and operands.
4. Reads and executes the commands from init file (if any) in the current
   working directory. This is only done if the current directory is
   different from your home directory. Thus, you can have more than one
   init file, one generic in your home directory, and another, specific
   to the program you are debugging, in the directory where you invoke
   GDB.
5. Reads command files specified by the `` `-x' `` option. See section [Command files](Canned%20Sequences%20of%20Commands.md#apple-kncugmrsgy), for more details about GDB command files.
6. Reads the command history recorded in the __history file__.
   See section [Command history](Controlling%20GDB.md#apple-kncugmrrg4), for more details about the command history and the
   files where GDB records it.

Init files use the same syntax as __command files__ (see section [Command files](Canned%20Sequences%20of%20Commands.md#apple-kncugmrsgy)) and are processed by GDB in the same way. The init
file in your home directory can set options (such as `` `set
complaints' ``) that affect subsequent processing of command line options
and operands. Init files are not executed if you use the `` `-nx' ``
option (see section [Choosing modes](#apple-kncugoi)).

The GDB init files are normally called `.gdbinit'.
On some configurations of GDB, the init file is known by a
different name (these are typically environments where a specialized
form of GDB may need to coexist with other forms, hence a
different name for the specialized version's init file). These are the
environments with special init file names:

- 
  The DJGPP port of GDB uses the name `gdb.ini', due to
  the limitations of file names imposed by DOS filesystems. The Windows
  ports of GDB use the standard name, but if they find a
  `gdb.ini' file, they warn you about that and suggest to rename
  the file to the standard name.
  
- VxWorks (Wind River Systems real-time OS): `.vxgdbinit'
  
- OS68K (Enea Data Systems real-time OS): `.os68gdbinit'
  
- ES-1800 (Ericsson Telecom AB M68000 emulator): `.esgdbinit'
- CISCO 68k: `.cisco-gdbinit'

## [Quitting GDB](Debugging%20with%20GDB.md#apple-krhugmjr)

**`quit [expression]`**
: 

**`q`**
: To exit GDB, use the `quit` command (abbreviated
`q`), or type an end-of-file character (usually `C-d`). If you
do not supply expression, GDB will terminate normally;
otherwise it will terminate using the result of expression as the
error code.

An interrupt (often `C-c`) does not exit from GDB, but rather
terminates the action of any GDB command that is in progress and
returns to GDB command level. It is safe to type the interrupt
character at any time because GDB does not allow it to take effect
until a time when it is safe.

If you have been using GDB to control an attached process or
device, you can release it with the `detach` command
(see section [Debugging an already-running process](Running%20Programs%20Under%20GDB.md#apple-kncugmrv)).

## [Shell commands](Debugging%20with%20GDB.md#apple-krhugmjs)

If you need to execute occasional shell commands during your
debugging session, there is no need to leave or suspend GDB; you can
just use the `shell` command.

**`shell command string`**
: 

Invoke a standard shell to execute command string.
If it exists, the environment variable `SHELL` determines which
shell to run. Otherwise GDB uses the default shell
(`/bin/sh' on Unix systems, `COMMAND.COM' on MS-DOS, etc.).

The utility `make` is often needed in development environments.
You do not have to use the `shell` command for this purpose in
GDB:

**`make make-args`**
: 

Execute the `make` program with the specified
arguments. This is equivalent to `` `shell make make-args' ``.

## [Logging output](Debugging%20with%20GDB.md#apple-krhugmjt)

You may want to save the output of GDB commands to a file.
There are several commands to control GDB's logging.

**`set logging on`**
: 
Enable logging.

**`set logging off`**
: Disable logging.

**`set logging file file`**
: Change the name of the current logfile. The default logfile is `gdb.txt'.

**`set logging overwrite [on|off]`**
: By default, GDB will append to the logfile. Set `overwrite` if
you want `set logging on` to overwrite the logfile instead.

**`set logging redirect [on|off]`**
: By default, GDB output will go to both the terminal and the logfile.
Set `redirect` if you want output to go only to the log file.

**`show logging`**
: Show the current values of the logging settings.

---

Go to the [first](Summary%20of%20GDB.md), [previous](A%20Sample%20GDB%20Session.md), [next](GDB%20Commands.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
