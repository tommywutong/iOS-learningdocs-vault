---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_20.html
archived_at: '2026-07-15T07:31:03.318623Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Configuration-Specific%20Information.md), [next](Canned%20Sequences%20of%20Commands.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Controlling GDB](Debugging%20with%20GDB.md#apple-krhugmrrgq)

You can alter the way GDB interacts with you by using the
`set` command. For commands controlling how GDB displays
data, see section [Print settings](Examining%20Data.md#apple-kncugnrt). Other settings are
described here.

## [Prompt](Debugging%20with%20GDB.md#apple-krhugmrrgu)

GDB indicates its readiness to read a command by printing a string
called the __prompt__. This string is normally `` `(gdb)' ``. You
can change the prompt string with the `set prompt` command. For
instance, when debugging GDB with GDB, it is useful to change
the prompt in one of the GDB sessions so that you can always tell
which one you are talking to.

_Note:_ `set prompt` does not add a space for you after the
prompt you set. This allows you to set a prompt which ends in a space
or a prompt that does not.

**`set prompt newprompt`**
: 
Directs GDB to use newprompt as its prompt string henceforth.

**`show prompt`**
: Prints a line of the form: `` `Gdb's prompt is: your-prompt' ``

## [Command editing](Debugging%20with%20GDB.md#apple-krhugmrrgy)

GDB reads its input commands via the __Readline__ interface. This
GNU library provides consistent behavior for programs which provide a
command line interface to the user. Advantages are GNU Emacs-style
or __vi__-style inline editing of commands, `csh`-like history
substitution, and a storage and recall of command history across
debugging sessions.

You may control the behavior of command line editing in GDB with the
command `set`.

**`set editing`**
: 

**`set editing on`**
: Enable command line editing (enabled by default).

**`set editing off`**
: Disable command line editing.

**`show editing`**
: Show whether command line editing is enabled.

See section [Command Line Editing](Command%20Line%20Editing.md#apple-kncugmrwhe), for more details about the Readline
interface. Users unfamiliar with GNU Emacs or `vi` are
encouraged to read that chapter.

## [Command history](Debugging%20with%20GDB.md#apple-krhugmrrg4)

GDB can keep track of the commands you type during your
debugging sessions, so that you can be certain of precisely what
happened. Use these commands to manage the GDB command
history facility.

GDB uses the GNU History library, a part of the Readline
package, to provide the history facility. See section [Using History Interactively](Using%20History%20Interactively.md#apple-kncugmrzge), for the detailed description of the History library.

To issue a command to GDB without affecting certain aspects of
the state which is seen by users, prefix it with `` `server ' ``. This
means that this command will not affect the command history, nor will it
affect GDB's notion of which command to repeat if `RET` is
pressed on a line by itself.

The server prefix does not affect the recording of values into the value
history; to print a value without recording it into the value history,
use the `output` command instead of the `print` command.

Here is the description of GDB commands related to command
history.

**`set history filename fname`**
: 

Set the name of the GDB command history file to fname.
This is the file where GDB reads an initial command history
list, and where it writes the command history from this session when it
exits. You can access this list through history expansion or through
the history command editing characters listed below. This file defaults
to the value of the environment variable `GDBHISTFILE`, or to
`./.gdb_history' (`./_gdb_history' on MS-DOS) if this variable
is not set.

**`set history save`**
:

**`set history save on`**
: Record command history in a file, whose name may be specified with the
`set history filename` command. By default, this option is disabled.

**`set history save off`**
: Stop recording command history in a file.

**`set history size size`**
: Set the number of commands which GDB keeps in its history list.
This defaults to the value of the environment variable
`HISTSIZE`, or to 256 if this variable is not set.

History expansion assigns special meaning to the character `!`.
See section [Event Designators](Using%20History%20Interactively.md#apple-kncugmrzgm), for more details.

Since `!` is also the logical not operator in C, history expansion
is off by default. If you decide to enable history expansion with the
`set history expansion on` command, you may sometimes need to
follow `!` (when it is used as logical not, in an expression) with
a space or a tab to prevent it from being expanded. The readline
history facilities do not attempt substitution on the strings
`!=` and `!(`, even when history expansion is enabled.

The commands to control history expansion are:

**`set history expansion on`**
:

**`set history expansion`**
: 
Enable history expansion. History expansion is off by default.

**`set history expansion off`**
: Disable history expansion.

**`show history`**
:

**`show history filename`**
:

**`show history save`**
:

**`show history size`**
:

**`show history expansion`**
: These commands display the state of the GDB history parameters.
`show history` by itself displays all four states.

**`show commands`**
: 

Display the last ten commands in the command history.

**`show commands n`**
: Print ten commands centered on command number n.

**`show commands +`**
: Print ten commands just after the commands last printed.

## [Screen size](Debugging%20with%20GDB.md#apple-krhugmrrha)

Certain commands to GDB may produce large amounts of
information output to the screen. To help you read all of it,
GDB pauses and asks you for input at the end of each page of
output. Type `RET` when you want to continue the output, or `q`
to discard the remaining output. Also, the screen width setting
determines when to wrap lines of output. Depending on what is being
printed, GDB tries to break the line at a readable place,
rather than simply letting it overflow onto the following line.

Normally GDB knows the size of the screen from the terminal
driver software. For example, on Unix GDB uses the termcap data base
together with the value of the `TERM` environment variable and the
`stty rows` and `stty cols` settings. If this is not correct,
you can override it with the `set height` and `set
width` commands:

**`set height lpp`**
: 

**`show height`**
:

**`set width cpl`**
:

**`show width`**
: These `set` commands specify a screen height of lpp lines and
a screen width of cpl characters. The associated `show`
commands display the current settings.
If you specify a height of zero lines, GDB does not pause during
output no matter how long the output is. This is useful if output is to a
file or to an editor buffer.
Likewise, you can specify `` `set width 0' `` to prevent GDB
from wrapping its output.

**`set pagination on`**
:

**`set pagination off`**
: 
Turn the output pagination on or off; the default is on. Turning
pagination off is the alternative to `set height 0`.

**`show pagination`**
: 
Show the current pagination mode.

## [Numbers](Debugging%20with%20GDB.md#apple-krhugmrrhe)

You can always enter numbers in octal, decimal, or hexadecimal in
GDB by the usual conventions: octal numbers begin with
`` `0' ``, decimal numbers end with `` `.' ``, and hexadecimal numbers
begin with `` `0x' ``. Numbers that neither begin with `` `0' `` or
`` `0x' ``, nor end with a `` `.' `` are, by default, entered in base
10; likewise, the default display for numbers--when no particular
format is specified--is base 10. You can change the default base for
both input and output with the commands described below.

**`set input-radix base`**
: 
Set the default base for numeric input. Supported choices
for base are decimal 8, 10, or 16. base must itself be
specified either unambiguously or using the current input radix; for
example, any of

```
set input-radix 012
set input-radix 10.
set input-radix 0xa
```

sets the input base to decimal. On the other hand, `` `set input-radix 10' ``
leaves the input radix unchanged, no matter what it was, since
`` `10' ``, being without any leading or trailing signs of its base, is
interpreted in the current radix. Thus, if the current radix is 16,
`` `10' `` is interpreted in hex, i.e. as 16 decimal, which doesn't
change the radix.

**`set output-radix base`**
: Set the default base for numeric display. Supported choices
for base are decimal 8, 10, or 16. base must itself be
specified either unambiguously or using the current input radix.

**`show input-radix`**
: Display the current default base for numeric input.

**`show output-radix`**
: Display the current default base for numeric display.

**`set radix [base]`**
:

**`show radix`**
: 

These commands set and show the default base for both input and output
of numbers. `set radix` sets the radix of input and output to
the same base; without an argument, it resets the radix back to its
default value of 10.

## [Configuring the current ABI](Debugging%20with%20GDB.md#apple-krhugmrsga)

GDB can determine the __ABI__ (Application Binary Interface) of your
application automatically. However, sometimes you need to override its
conclusions. Use these commands to manage GDB's view of the
current ABI.

One GDB configuration can debug binaries for multiple operating
system targets, either via remote debugging or native emulation.
GDB will autodetect the __OS ABI__ (Operating System ABI) in use,
but you can override its conclusion using the `set osabi` command.
One example where this is useful is in debugging of binaries which use
an alternate C library (e.g. UCLIBC for GNU/Linux) which does
not have the same identifying marks that the standard C library for your
platform provides.

**`show osabi`**
: Show the OS ABI currently in use.

**`set osabi`**
: With no argument, show the list of registered available OS ABI's.

**`set osabi abi`**
: Set the current OS ABI to abi.

Generally, the way that an argument of type `float` is passed to a
function depends on whether the function is prototyped. For a prototyped
(i.e. ANSI/ISO style) function, `float` arguments are passed unchanged,
according to the architecture's convention for `float`. For unprototyped
(i.e. K&R style) functions, `float` arguments are first promoted to type
`double` and then passed.

Unfortunately, some forms of debug information do not reliably indicate whether
a function is prototyped. If GDB calls a function that is not marked
as prototyped, it consults `set coerce-float-to-double`.

**`set coerce-float-to-double`**
: 

**`set coerce-float-to-double on`**
: Arguments of type `float` will be promoted to `double` when passed
to an unprototyped function. This is the default setting.

**`set coerce-float-to-double off`**
: Arguments of type `float` will be passed directly to unprototyped
functions.

**`show coerce-float-to-double`**
: Show the current setting of promoting `float` to `double`.

GDB needs to know the ABI used for your program's C++
objects. The correct C++ ABI depends on which C++ compiler was
used to build your application. GDB only fully supports
programs with a single C++ ABI; if your program contains code using
multiple C++ ABI's or if GDB can not identify your
program's ABI correctly, you can tell GDB which ABI to use.
Currently supported ABI's include "gnu-v2", for `g++` versions
before 3.0, "gnu-v3", for `g++` versions 3.0 and later, and
"hpaCC" for the HP ANSI C++ compiler. Other C++ compilers may
use the "gnu-v2" or "gnu-v3" ABI's as well. The default setting is
"auto".

**`show cp-abi`**
: Show the C++ ABI currently in use.

**`set cp-abi`**
: With no argument, show the list of supported C++ ABI's.

**`set cp-abi abi`**
:

**`set cp-abi auto`**
: Set the current C++ ABI to abi, or return to automatic detection.

## [Optional warnings and messages](Debugging%20with%20GDB.md#apple-krhugmrsge)

By default, GDB is silent about its inner workings. If you are
running on a slow machine, you may want to use the `set verbose`
command. This makes GDB tell you when it does a lengthy
internal operation, so you will not think it has crashed.

Currently, the messages controlled by `set verbose` are those
which announce that the symbol table for a source file is being read;
see `symbol-file` in section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4).

**`set verbose on`**
: 
Enables GDB output of certain informational messages.

**`set verbose off`**
: Disables GDB output of certain informational messages.

**`show verbose`**
: Displays whether `set verbose` is on or off.

By default, if GDB encounters bugs in the symbol table of an
object file, it is silent; but if you are debugging a compiler, you may
find this information useful (see section [Errors reading symbol files](GDB%20Files.md#apple-kncugmjuhe)).

**`set complaints limit`**
: 
Permits GDB to output limit complaints about each type of
unusual symbols before becoming silent about the problem. Set
limit to zero to suppress all complaints; set it to a large number
to prevent complaints from being suppressed.

**`show complaints`**
: Displays how many symbol complaints GDB is permitted to produce.

By default, GDB is cautious, and asks what sometimes seems to be a
lot of stupid questions to confirm certain commands. For example, if
you try to run a program which is already running:

```
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n)
```

If you are willing to unflinchingly face the consequences of your own
commands, you can disable this "feature":

**`set confirm off`**
: 

Disables confirmation requests.

**`set confirm on`**
: Enables confirmation requests (the default).

**`show confirm`**
: Displays state of confirmation requests.

## [Optional messages about internal happenings](Debugging%20with%20GDB.md#apple-krhugmrsgi)

GDB has commands that enable optional debugging messages from
various GDB subsystems; normally these commands are of
interest to GDB maintainers, or when reporting a bug. This
section documents those commands.

**`set exec-done-display`**
: 
Turns on or off the notification of asynchronous commands'
completion. When on, GDB will print a message when an
asynchronous command finishes its execution. The default is off.

**`show exec-done-display`**
: Displays the current setting of asynchronous command completion
notification.

**`set debug arch`**
: Turns on or off display of gdbarch debugging info. The default is off

**`show debug arch`**
: Displays the current state of displaying gdbarch debugging info.

**`set debug aix-thread`**
: 
Display debugging messages about inner workings of the AIX thread
module.

**`show debug aix-thread`**
: Show the current state of AIX thread debugging info display.

**`set debug event`**
: 
Turns on or off display of GDB event debugging info. The
default is off.

**`show debug event`**
: Displays the current state of displaying GDB event debugging
info.

**`set debug expression`**
: 
Turns on or off display of debugging info about GDB
expression parsing. The default is off.

**`show debug expression`**
: Displays the current state of displaying debugging info about
GDB expression parsing.

**`set debug frame`**
: 
Turns on or off display of GDB frame debugging info. The
default is off.

**`show debug frame`**
: Displays the current state of displaying GDB frame debugging
info.

**`set debug infrun`**
: 
Turns on or off display of GDB debugging info for running the inferior.
The default is off. `infrun.c' contains GDB's runtime state machine used
for implementing operations such as single-stepping the inferior.

**`show debug infrun`**
: Displays the current state of GDB inferior debugging.

**`set debug lin-lwp`**
: 

Turns on or off debugging messages from the Linux LWP debug support.

**`show debug lin-lwp`**
: Show the current state of Linux LWP debugging messages.

**`set debug observer`**
: 
Turns on or off display of GDB observer debugging. This
includes info such as the notification of observable events.

**`show debug observer`**
: Displays the current state of observer debugging.

**`set debug overload`**
: 
Turns on or off display of GDB C++ overload debugging
info. This includes info such as ranking of functions, etc. The default
is off.

**`show debug overload`**
: Displays the current state of displaying GDB C++ overload
debugging info.

**`set debug remote`**
: Turns on or off display of reports on all packets sent back and forth across
the serial line to the remote machine. The info is printed on the
GDB standard output stream. The default is off.

**`show debug remote`**
: Displays the state of display of remote packets.

**`set debug serial`**
: Turns on or off display of GDB serial debugging info. The
default is off.

**`show debug serial`**
: Displays the current state of displaying GDB serial debugging
info.

**`set debug solib-frv`**
: 
Turns on or off debugging messages for FR-V shared-library code.

**`show debug solib-frv`**
: Display the current state of FR-V shared-library code debugging
messages.

**`set debug target`**
: 
Turns on or off display of GDB target debugging info. This info
includes what is going on at the target level of GDB, as it happens. The
default is 0. Set it to 1 to track events, and to 2 to also track the
value of large memory transfers. Changes to this flag do not take effect
until the next time you connect to a target or use the `run` command.

**`show debug target`**
: Displays the current state of displaying GDB target debugging
info.

**`set debugvarobj`**
: 
Turns on or off display of GDB variable object debugging
info. The default is off.

**`show debugvarobj`**
: Displays the current state of displaying GDB variable object
debugging info.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Configuration-Specific%20Information.md), [next](Canned%20Sequences%20of%20Commands.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
