---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_6.html
archived_at: '2026-07-15T07:31:03.617414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Running%20Programs%20Under%20GDB.md), [next](Examining%20the%20Stack.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Stopping and Continuing](Debugging%20with%20GDB.md#apple-krhugmrz)

The principal purposes of using a debugger are so that you can stop your
program before it terminates; or so that, if your program runs into
trouble, you can investigate and find out why.

Inside GDB, your program may stop for any of several reasons,
such as a signal, a breakpoint, or reaching a new line after a
GDB command such as `step`. You may then examine and
change variables, set new breakpoints or remove old ones, and then
continue execution. Usually, the messages shown by GDB provide
ample explanation of the status of your program--but you can also
explicitly request this information at any time.

**`info program`**
: 
Display information about the status of your program: whether it is
running or not, what process it is, and why it stopped.

## [Breakpoints, watchpoints, and catchpoints](Debugging%20with%20GDB.md#apple-krhugmzq)

A __breakpoint__ makes your program stop whenever a certain point in
the program is reached. For each breakpoint, you can add conditions to
control in finer detail whether your program stops. You can set
breakpoints with the `break` command and its variants (see section [Setting breakpoints](#apple-kncugmzr)), to specify the place where your program
should stop by line number, function name or exact address in the
program.

On some systems, you can set breakpoints in shared libraries before
the executable is run. There is a minor limitation on HP-UX systems:
you must wait until the executable is run in order to set breakpoints
in shared library routines that are not called directly by the program
(for example, routines that are arguments in a `pthread_create`
call).

A __watchpoint__ is a special breakpoint that stops your program
when the value of an expression changes. You must use a different
command to set watchpoints (see section [Setting watchpoints](#apple-kncugmzs)), but aside from that, you can manage a watchpoint like
any other breakpoint: you enable, disable, and delete both breakpoints
and watchpoints using the same commands.

You can arrange to have values from your program displayed automatically
whenever GDB stops at a breakpoint. See section [Automatic display](Examining%20Data.md#apple-kncugnrs).

A __catchpoint__ is another special breakpoint that stops your program
when a certain kind of event occurs, such as the throwing of a C++
exception or the loading of a library. As with watchpoints, you use a
different command to set a catchpoint (see section [Setting catchpoints](#apple-kncugmzt)), but aside from that, you can manage a catchpoint like any
other breakpoint. (To stop when your program receives a signal, use the
`handle` command; see section [Signals](#apple-kncugnbs).)

GDB assigns a number to each breakpoint, watchpoint, or
catchpoint when you create it; these numbers are successive integers
starting with one. In many of the commands for controlling various
features of breakpoints you use the breakpoint number to say which
breakpoint you want to change. Each breakpoint may be __enabled__ or
__disabled__; if disabled, it has no effect on your program until you
enable it again.

Some GDB commands accept a range of breakpoints on which to
operate. A breakpoint range is either a single breakpoint number, like
`` `5' ``, or two such numbers, in increasing order, separated by a
hyphen, like `` `5-7' ``. When a breakpoint range is given to a command,
all breakpoint in that range are operated on.

### [Setting breakpoints](Debugging%20with%20GDB.md#apple-krhugmzr)

Breakpoints are set with the `break` command (abbreviated
`b`). The debugger convenience variable `` `$bpnum' `` records the
number of the breakpoint you've set most recently; see section [Convenience variables](Examining%20Data.md#apple-kncugnrv), for a discussion of what you can do with
convenience variables.

You have several ways to say where the breakpoint should go.

**`break function`**
: Set a breakpoint at entry to function function.
When using source languages that permit overloading of symbols, such as
C++, function may refer to more than one possible place to break.
See section [Breakpoint menus](#apple-kncugmzy), for a discussion of that situation.

**`break +offset`**
:

**`break -offset`**
: Set a breakpoint some number of lines forward or back from the position
at which execution stopped in the currently selected __stack frame__.
(See section [Stack frames](Examining%20the%20Stack.md#apple-kncugnbv), for a description of stack frames.)

**`break linenum`**
: Set a breakpoint at line linenum in the current source file.
The current source file is the last file whose source text was printed.
The breakpoint will stop your program just before it executes any of the
code on that line.

**`break filename:linenum`**
: Set a breakpoint at line linenum in source file filename.

**`break filename:function`**
: Set a breakpoint at entry to function function found in file
filename. Specifying a file name as well as a function name is
superfluous except when multiple files contain similarly named
functions.

**`break *address`**
: Set a breakpoint at address address. You can use this to set
breakpoints in parts of your program which do not have debugging
information or source files.

**`break`**
: When called without any arguments, `break` sets a breakpoint at
the next instruction to be executed in the selected stack frame
(see section [Examining the Stack](Examining%20the%20Stack.md#apple-kncugnbu)). In any selected frame but the
innermost, this makes your program stop as soon as control
returns to that frame. This is similar to the effect of a
`finish` command in the frame inside the selected frame--except
that `finish` does not leave an active breakpoint. If you use
`break` without an argument in the innermost frame, GDB stops
the next time it reaches the current location; this may be useful
inside loops.
GDB normally ignores breakpoints when it resumes execution, until at
least one instruction has been executed. If it did not do this, you
would be unable to proceed past a breakpoint without first disabling the
breakpoint. This rule applies whether or not the breakpoint already
existed when your program stopped.

**`break ... if cond`**
: Set a breakpoint with condition cond; evaluate the expression
cond each time the breakpoint is reached, and stop only if the
value is nonzero--that is, if cond evaluates as true.
`` `...' `` stands for one of the possible arguments described
above (or no argument) specifying where to break. See section [Break conditions](#apple-kncugmzw), for more information on breakpoint conditions.

**`tbreak args`**
: Set a breakpoint enabled only for one stop. args are the
same as for the `break` command, and the breakpoint is set in the same
way, but the breakpoint is automatically deleted after the first time your
program stops there. See section [Disabling breakpoints](#apple-kncugmzv).

**`hbreak args`**
: Set a hardware-assisted breakpoint. args are the same as for the
`break` command and the breakpoint is set in the same way, but the
breakpoint requires hardware support and some target hardware may not
have this support. The main purpose of this is EPROM/ROM code
debugging, so you can set a breakpoint at an instruction without
changing the instruction. This can be used with the new trap-generation
provided by SPARClite DSU and most x86-based targets. These targets
will generate traps when a program accesses some data or instruction
address that is assigned to the debug registers. However the hardware
breakpoint registers can take a limited number of breakpoints. For
example, on the DSU, only two data breakpoints can be set at a time, and
GDB will reject this command if more than two are used. Delete
or disable unused hardware breakpoints before setting new ones
(see section [Disabling breakpoints](#apple-kncugmzv)). See section [Break conditions](#apple-kncugmzw).
For remote targets, you can restrict the number of hardware
breakpoints GDB will use, see @xref{set remote hardware-breakpoint-limit}.

**`thbreak args`**
: Set a hardware-assisted breakpoint enabled only for one stop. args
are the same as for the `hbreak` command and the breakpoint is set in
the same way. However, like the `tbreak` command,
the breakpoint is automatically deleted after the
first time your program stops there. Also, like the `hbreak`
command, the breakpoint requires hardware support and some target hardware
may not have this support. See section [Disabling breakpoints](#apple-kncugmzv).
See also section [Break conditions](#apple-kncugmzw).

**`rbreak regex`**
: Set breakpoints on all functions matching the regular expression
regex. This command sets an unconditional breakpoint on all
matches, printing a list of all breakpoints it set. Once these
breakpoints are set, they are treated just like the breakpoints set with
the `break` command. You can delete them, disable them, or make
them conditional the same way as any other breakpoint.
The syntax of the regular expression is the standard one used with tools
like `grep'. Note that this is different from the syntax used by
shells, so for instance `foo*` matches all functions that include
an `fo` followed by zero or more `o`s. There is an implicit
`.*` leading and trailing the regular expression you supply, so to
match only functions that begin with `foo`, use `^foo`.

When debugging C++ programs, `rbreak` is useful for setting
breakpoints on overloaded functions that are not members of any special
classes.

The `rbreak` command can be used to set breakpoints in
__all__ the functions in a program, like this:

```
(gdb) rbreak .
```


**`info breakpoints [n]`**
:

**`info break [n]`**
:

**`info watchpoints [n]`**
: Print a table of all breakpoints, watchpoints, and catchpoints set and
not deleted, with the following columns for each breakpoint:

**_Breakpoint Numbers_**
:

**_Type_**
: Breakpoint, watchpoint, or catchpoint.

**_Disposition_**
: Whether the breakpoint is marked to be disabled or deleted when hit.

**_Enabled or Disabled_**
: Enabled breakpoints are marked with `` `y' ``. `` `n' `` marks breakpoints
that are not enabled.

**_Address_**
: Where the breakpoint is in your program, as a memory address. If the
breakpoint is pending (see below for details) on a future load of a shared library, the address
will be listed as `` `<PENDING>' ``.

**_What_**
: Where the breakpoint is in the source for your program, as a file and
line number. For a pending breakpoint, the original string passed to
the breakpoint command will be listed as it cannot be resolved until
the appropriate shared library is loaded in the future.

If a breakpoint is conditional, `info break` shows the condition on
the line following the affected breakpoint; breakpoint commands, if any,
are listed after that. A pending breakpoint is allowed to have a condition
specified for it. The condition is not parsed for validity until a shared
library is loaded that allows the pending breakpoint to resolve to a
valid location.
`info break` with a breakpoint
number n as argument lists only that breakpoint. The
convenience variable `$_` and the default examining-address for
the `x` command are set to the address of the last breakpoint
listed (see section [Examining memory](Examining%20Data.md#apple-kncugnrr)).
`info break` displays a count of the number of times the breakpoint
has been hit. This is especially useful in conjunction with the
`ignore` command. You can ignore a large number of breakpoint
hits, look at the breakpoint info to see how many times the breakpoint
was hit, and then run again, ignoring one less than that number. This
will get you quickly to the last hit of that breakpoint.

GDB allows you to set any number of breakpoints at the same place in
your program. There is nothing silly or meaningless about this. When
the breakpoints are conditional, this is even useful
(see section [Break conditions](#apple-kncugmzw)).

If a specified breakpoint location cannot be found, it may be due to the fact
that the location is in a shared library that is yet to be loaded. In such
a case, you may want GDB to create a special breakpoint (known as
a __pending breakpoint__) that
attempts to resolve itself in the future when an appropriate shared library
gets loaded.

Pending breakpoints are useful to set at the start of your
GDB session for locations that you know will be dynamically loaded
later by the program being debugged. When shared libraries are loaded,
a check is made to see if the load resolves any pending breakpoint locations.
If a pending breakpoint location gets resolved,
a regular breakpoint is created and the original pending breakpoint is removed.

GDB provides some additional commands for controlling pending
breakpoint support:

**`set breakpoint pending auto`**
: This is the default behavior. When GDB cannot find the breakpoint
location, it queries you whether a pending breakpoint should be created.

**`set breakpoint pending on`**
: This indicates that an unrecognized breakpoint location should automatically
result in a pending breakpoint being created.

**`set breakpoint pending off`**
: This indicates that pending breakpoints are not to be created. Any
unrecognized breakpoint location results in an error. This setting does
not affect any pending breakpoints previously created.

**`show breakpoint pending`**
: Show the current behavior setting for creating pending breakpoints.

Normal breakpoint operations apply to pending breakpoints as well. You may
specify a condition for a pending breakpoint and/or commands to run when the
breakpoint is reached. You can also enable or disable
the pending breakpoint. When you specify a condition for a pending breakpoint,
the parsing of the condition will be deferred until the point where the
pending breakpoint location is resolved. Disabling a pending breakpoint
tells GDB to not attempt to resolve the breakpoint on any subsequent
shared library load. When a pending breakpoint is re-enabled,
GDB checks to see if the location is already resolved.
This is done because any number of shared library loads could have
occurred since the time the breakpoint was disabled and one or more
of these loads could resolve the location.

GDB itself sometimes sets breakpoints in your program for
special purposes, such as proper handling of `longjmp` (in C
programs). These internal breakpoints are assigned negative numbers,
starting with `-1`; `` `info breakpoints' `` does not display them.
You can see these breakpoints with the GDB maintenance command
`` `maint info breakpoints' `` (@xref{maint info breakpoints}).

### [Setting watchpoints](Debugging%20with%20GDB.md#apple-krhugmzs)

You can use a watchpoint to stop execution whenever the value of an
expression changes, without having to predict a particular place where
this may happen.

Depending on your system, watchpoints may be implemented in software or
hardware. GDB does software watchpointing by single-stepping your
program and testing the variable's value each time, which is hundreds of
times slower than normal execution. (But this may still be worth it, to
catch errors where you have no clue what part of your program is the
culprit.)

On some systems, such as HP-UX, GNU/Linux and most other
x86-based targets, GDB includes support for hardware
watchpoints, which do not slow down the running of your program.

**`watch expr`**
: 
Set a watchpoint for an expression. GDB will break when expr
is written into by the program and its value changes.

**`rwatch expr`**
: Set a watchpoint that will break when the value of expr is read
by the program.

**`awatch expr`**
: Set a watchpoint that will break when expr is either read from
or written into by the program.

**`info watchpoints`**
: This command prints a list of watchpoints, breakpoints, and catchpoints;
it is the same as `info break` (see section [Setting breakpoints](#apple-kncugmzr)).

GDB sets a __hardware watchpoint__ if possible. Hardware
watchpoints execute very quickly, and the debugger reports a change in
value at the exact instruction where the change occurs. If GDB
cannot set a hardware watchpoint, it sets a software watchpoint, which
executes more slowly and reports the change in value at the next
_statement_, not the instruction, after the change occurs.

You can force GDB to use only software watchpoints with the
`set can-use-hw-watchpoints 0` command. With this variable set to
zero, GDB will never try to use hardware watchpoints, even if
the underlying system supports them. (Note that hardware-assisted
watchpoints that were set _before_ setting
`can-use-hw-watchpoints` to zero will still use the hardware
mechanism of watching expressiion values.)

**`set can-use-hw-watchpoints`**
: 
Set whether or not to use hardware watchpoints.

**`show can-use-hw-watchpoints`**
: 
Show the current mode of using hardware watchpoints.

For remote targets, you can restrict the number of hardware
watchpoints GDB will use, see @xref{set remote hardware-breakpoint-limit}.

When you issue the `watch` command, GDB reports

```
Hardware watchpoint num: expr
```

if it was able to set a hardware watchpoint.

Currently, the `awatch` and `rwatch` commands can only set
hardware watchpoints, because accesses to data that don't change the
value of the watched expression cannot be detected without examining
every instruction as it is being executed, and GDB does not do
that currently. If GDB finds that it is unable to set a
hardware breakpoint with the `awatch` or `rwatch` command, it
will print a message like this:

```
Expression cannot be implemented with read/access watchpoint.
```

Sometimes, GDB cannot set a hardware watchpoint because the
data type of the watched expression is wider than what a hardware
watchpoint on the target machine can handle. For example, some systems
can only watch regions that are up to 4 bytes wide; on such systems you
cannot set hardware watchpoints for an expression that yields a
double-precision floating-point number (which is typically 8 bytes
wide). As a work-around, it might be possible to break the large region
into a series of smaller ones and watch them with separate watchpoints.

If you set too many hardware watchpoints, GDB might be unable
to insert all of them when you resume the execution of your program.
Since the precise number of active watchpoints is unknown until such
time as the program is about to be resumed, GDB might not be
able to warn you about this when you set the watchpoints, and the
warning will be printed only when the program is resumed:

```
Hardware watchpoint num: Could not insert watchpoint
```

If this happens, delete or disable some of the watchpoints.

The SPARClite DSU will generate traps when a program accesses some data
or instruction address that is assigned to the debug registers. For the
data addresses, DSU facilitates the `watch` command. However the
hardware breakpoint registers can only take two data watchpoints, and
both watchpoints must be the same kind. For example, you can set two
watchpoints with `watch` commands, two with `rwatch` commands,
__or__ two with `awatch` commands, but you cannot set one
watchpoint with one command and the other with a different command.
GDB will reject the command if you try to mix watchpoints.
Delete or disable unused watchpoint commands before setting new ones.

If you call a function interactively using `print` or `call`,
any watchpoints you have set will be inactive until GDB reaches another
kind of breakpoint or the call completes.

GDB automatically deletes watchpoints that watch local
(automatic) variables, or expressions that involve such variables, when
they go out of scope, that is, when the execution leaves the block in
which these variables were defined. In particular, when the program
being debugged terminates, _all_ local variables go out of scope,
and so only watchpoints that watch global variables remain set. If you
rerun the program, you will need to set all such watchpoints again. One
way of doing that would be to set a code breakpoint at the entry to the
`main` function and when it breaks, set all the watchpoints.

> 
> 
>
> _Warning:_ In multi-thread programs, watchpoints have only limited
> usefulness. With the current watchpoint implementation, GDB
> can only watch the value of an expression _in a single thread_. If
> you are confident that the expression can only change due to the current
> thread's activity (and if you are also confident that no other thread
> can become current), then you can use watchpoints as usual. However,
> GDB may not notice when a non-current thread's activity changes
> the expression.
>
> _HP-UX Warning:_ In multi-thread programs, software watchpoints
> have only limited usefulness. If GDB creates a software
> watchpoint, it can only watch the value of an expression _in a
> single thread_. If you are confident that the expression can only
> change due to the current thread's activity (and if you are also
> confident that no other thread can become current), then you can use
> software watchpoints as usual. However, GDB may not notice
> when a non-current thread's activity changes the expression. (Hardware
> watchpoints, in contrast, watch an expression in all threads.)

@xref{set remote hardware-watchpoint-limit}.

### [Setting catchpoints](Debugging%20with%20GDB.md#apple-krhugmzt)

You can use __catchpoints__ to cause the debugger to stop for certain
kinds of program events, such as C++ exceptions or the loading of a
shared library. Use the `catch` command to set a catchpoint.

**`catch event`**
: 
Stop when event occurs. event can be any of the following:

**`throw`**
: 
The throwing of a C++ exception.

**`catch`**
: The catching of a C++ exception.

**`exec`**
: 
A call to `exec`. This is currently only available for HP-UX.

**`fork`**
: A call to `fork`. This is currently only available for HP-UX.

**`vfork`**
: A call to `vfork`. This is currently only available for HP-UX.

**`load`**
:

**`load libname`**
: 
The dynamic loading of any shared library, or the loading of the library
libname. This is currently only available for HP-UX.

**`unload`**
:

**`unload libname`**
: The unloading of any dynamically loaded shared library, or the unloading
of the library libname. This is currently only available for HP-UX.

**`tcatch event`**
: Set a catchpoint that is enabled only for one stop. The catchpoint is
automatically deleted after the first time the event is caught.

Use the `info break` command to list the current catchpoints.

There are currently some limitations to C++ exception handling
(`catch throw` and `catch catch`) in GDB:

- If you call a function interactively, GDB normally returns
  control to you when the function has finished executing. If the call
  raises an exception, however, the call may bypass the mechanism that
  returns control to you and cause your program either to abort or to
  simply continue running until it hits a breakpoint, catches a signal
  that GDB is listening for, or exits. This is the case even if
  you set a catchpoint for the exception; catchpoints on exceptions are
  disabled within interactive calls.
- You cannot raise an exception interactively.
- You cannot install an exception handler interactively.

Sometimes `catch` is not the best way to debug exception handling:
if you need to know exactly where an exception is raised, it is better to
stop _before_ the exception handler is called, since that way you
can see the stack before any unwinding takes place. If you set a
breakpoint in an exception handler instead, it may not be easy to find
out where the exception was raised.

To stop just before an exception handler is called, you need some
knowledge of the implementation. In the case of GNU C++, exceptions are
raised by calling a library function named `__raise_exception`
which has the following ANSI C interface:

```
    /* addr is where the exception identifier is stored.
       id is the exception identifier.  */
    void __raise_exception (void **addr, void *id);
```

To make the debugger catch all exceptions before any stack
unwinding takes place, set a breakpoint on `__raise_exception`
(see section [Breakpoints, watchpoints, and catchpoints](#apple-kncugmzq)).

With a conditional breakpoint (see section [Break conditions](#apple-kncugmzw))
that depends on the value of id, you can stop your program when
a specific exception is raised. You can use multiple conditional
breakpoints to stop your program when any of a number of exceptions are
raised.

### [Deleting breakpoints](Debugging%20with%20GDB.md#apple-krhugmzu)

It is often necessary to eliminate a breakpoint, watchpoint, or
catchpoint once it has done its job and you no longer want your program
to stop there. This is called __deleting__ the breakpoint. A
breakpoint that has been deleted no longer exists; it is forgotten.

With the `clear` command you can delete breakpoints according to
where they are in your program. With the `delete` command you can
delete individual breakpoints, watchpoints, or catchpoints by specifying
their breakpoint numbers.

It is not necessary to delete a breakpoint to proceed past it. GDB
automatically ignores breakpoints on the first instruction to be executed
when you continue execution without changing the execution address.

**`clear`**
: 
Delete any breakpoints at the next instruction to be executed in the
selected stack frame (see section [Selecting a frame](Examining%20the%20Stack.md#apple-kncugnbx)). When
the innermost frame is selected, this is a good way to delete a
breakpoint where your program just stopped.

**`clear function`**
:

**`clear filename:function`**
: Delete any breakpoints set at entry to the named function.

**`clear linenum`**
:

**`clear filename:linenum`**
: Delete any breakpoints set at or within the code of the specified
linenum of the specified filename.

**`delete [breakpoints] [range...]`**
: Delete the breakpoints, watchpoints, or catchpoints of the breakpoint
ranges specified as arguments. If no argument is specified, delete all
breakpoints (GDB asks confirmation, unless you have `set
confirm off`). You can abbreviate this command as `d`.

### [Disabling breakpoints](Debugging%20with%20GDB.md#apple-krhugmzv)

Rather than deleting a breakpoint, watchpoint, or catchpoint, you might
prefer to __disable__ it. This makes the breakpoint inoperative as if
it had been deleted, but remembers the information on the breakpoint so
that you can __enable__ it again later.

You disable and enable breakpoints, watchpoints, and catchpoints with
the `enable` and `disable` commands, optionally specifying one
or more breakpoint numbers as arguments. Use `info break` or
`info watch` to print a list of breakpoints, watchpoints, and
catchpoints if you do not know which numbers to use.

A breakpoint, watchpoint, or catchpoint can have any of four different
states of enablement:

- Enabled. The breakpoint stops your program. A breakpoint set
  with the `break` command starts out in this state.
- Disabled. The breakpoint has no effect on your program.
- Enabled once. The breakpoint stops your program, but then becomes
  disabled.
- Enabled for deletion. The breakpoint stops your program, but
  immediately after it does so it is deleted permanently. A breakpoint
  set with the `tbreak` command starts out in this state.

You can use the following commands to enable or disable breakpoints,
watchpoints, and catchpoints:

**`disable [breakpoints] [range...]`**
: 

Disable the specified breakpoints--or all breakpoints, if none are
listed. A disabled breakpoint has no effect but is not forgotten. All
options such as ignore-counts, conditions and commands are remembered in
case the breakpoint is enabled again later. You may abbreviate
`disable` as `dis`.

**`enable [breakpoints] [range...]`**
: Enable the specified breakpoints (or all defined breakpoints). They
become effective once again in stopping your program.

**`enable [breakpoints] once range...`**
: Enable the specified breakpoints temporarily. GDB disables any
of these breakpoints immediately after stopping your program.

**`enable [breakpoints] delete range...`**
: Enable the specified breakpoints to work once, then die. GDB
deletes any of these breakpoints as soon as your program stops there.
Breakpoints set by the `tbreak` command start out in this state.

Except for a breakpoint set with `tbreak` (see section [Setting breakpoints](#apple-kncugmzr)), breakpoints that you set are initially enabled;
subsequently, they become disabled or enabled only when you use one of
the commands above. (The command `until` can set and delete a
breakpoint of its own, but it does not change the state of your other
breakpoints; see section [Continuing and stepping](#apple-kncugnbr).)

### [Break conditions](Debugging%20with%20GDB.md#apple-krhugmzw)

The simplest sort of breakpoint breaks every time your program reaches a
specified place. You can also specify a __condition__ for a
breakpoint. A condition is just a Boolean expression in your
programming language (see section [Expressions](Examining%20Data.md#apple-kncugnjx)). A breakpoint with
a condition evaluates the expression each time your program reaches it,
and your program stops only if the condition is _true_.

This is the converse of using assertions for program validation; in that
situation, you want to stop when the assertion is violated--that is,
when the condition is false. In C, if you want to test an assertion expressed
by the condition assert, you should set the condition
`` `! assert' `` on the appropriate breakpoint.

Conditions are also accepted for watchpoints; you may not need them,
since a watchpoint is inspecting the value of an expression anyhow--but
it might be simpler, say, to just set a watchpoint on a variable name,
and specify a condition that tests whether the new value is an interesting
one.

Break conditions can have side effects, and may even call functions in
your program. This can be useful, for example, to activate functions
that log program progress, or to use your own print functions to
format special data structures. The effects are completely predictable
unless there is another enabled breakpoint at the same address. (In
that case, GDB might see the other breakpoint first and stop your
program without checking the condition of this one.) Note that
breakpoint commands are usually more convenient and flexible than break
conditions for the
purpose of performing side effects when a breakpoint is reached
(see section [Breakpoint command lists](#apple-kncugmzx)).

Break conditions can be specified when a breakpoint is set, by using
`` `if' `` in the arguments to the `break` command. See section [Setting breakpoints](#apple-kncugmzr). They can also be changed at any time
with the `condition` command.

You can also use the `if` keyword with the `watch` command.
The `catch` command does not recognize the `if` keyword;
`condition` is the only way to impose a further condition on a
catchpoint.

**`condition bnum expression`**
: 
Specify expression as the break condition for breakpoint,
watchpoint, or catchpoint number bnum. After you set a condition,
breakpoint bnum stops your program only if the value of
expression is true (nonzero, in C). When you use
`condition`, GDB checks expression immediately for
syntactic correctness, and to determine whether symbols in it have
referents in the context of your breakpoint. If expression uses
symbols not referenced in the context of the breakpoint, GDB
prints an error message:

```
No symbol "foo" in current context.
```

GDB does
not actually evaluate expression at the time the `condition`
command (or a command that sets a breakpoint with a condition, like
`break if ...`) is given, however. See section [Expressions](Examining%20Data.md#apple-kncugnjx).

**`condition bnum`**
: Remove the condition from breakpoint number bnum. It becomes
an ordinary unconditional breakpoint.

A special case of a breakpoint condition is to stop only when the
breakpoint has been reached a certain number of times. This is so
useful that there is a special way to do it, using the __ignore
count__ of the breakpoint. Every breakpoint has an ignore count, which
is an integer. Most of the time, the ignore count is zero, and
therefore has no effect. But if your program reaches a breakpoint whose
ignore count is positive, then instead of stopping, it just decrements
the ignore count by one and continues. As a result, if the ignore count
value is n, the breakpoint does not stop the next n times
your program reaches it.

**`ignore bnum count`**
: 
Set the ignore count of breakpoint number bnum to count.
The next count times the breakpoint is reached, your program's
execution does not stop; other than to decrement the ignore count, GDB
takes no action.
To make the breakpoint stop the next time it is reached, specify
a count of zero.
When you use `continue` to resume execution of your program from a
breakpoint, you can specify an ignore count directly as an argument to
`continue`, rather than using `ignore`. See section [Continuing and stepping](#apple-kncugnbr).
If a breakpoint has a positive ignore count and a condition, the
condition is not checked. Once the ignore count reaches zero,
GDB resumes checking the condition.
You could achieve the effect of the ignore count with a condition such
as `` `$foo-- <= 0' `` using a debugger convenience variable that
is decremented each time. See section [Convenience variables](Examining%20Data.md#apple-kncugnrv).

Ignore counts apply to breakpoints, watchpoints, and catchpoints.

### [Breakpoint command lists](Debugging%20with%20GDB.md#apple-krhugmzx)

You can give any breakpoint (or watchpoint or catchpoint) a series of
commands to execute when your program stops due to that breakpoint. For
example, you might want to print the values of certain expressions, or
enable other breakpoints.

**`commands [bnum]`**
: 

**`... command-list ...`**
:

**`end`**
: Specify a list of commands for breakpoint number bnum. The commands
themselves appear on the following lines. Type a line containing just
`end` to terminate the commands.
To remove all commands from a breakpoint, type `commands` and
follow it immediately with `end`; that is, give no commands.
With no bnum argument, `commands` refers to the last
breakpoint, watchpoint, or catchpoint set (not to the breakpoint most
recently encountered).

Pressing `RET` as a means of repeating the last GDB command is
disabled within a command-list.

You can use breakpoint commands to start your program up again. Simply
use the `continue` command, or `step`, or any other command
that resumes execution.

Any other commands in the command list, after a command that resumes
execution, are ignored. This is because any time you resume execution
(even with a simple `next` or `step`), you may encounter
another breakpoint--which could have its own command list, leading to
ambiguities about which list to execute.

If the first command you specify in a command list is `silent`, the
usual message about stopping at a breakpoint is not printed. This may
be desirable for breakpoints that are to print a specific message and
then continue. If none of the remaining commands print anything, you
see no sign that the breakpoint was reached. `silent` is
meaningful only at the beginning of a breakpoint command list.

The commands `echo`, `output`, and `printf` allow you to
print precisely controlled output, and are often useful in silent
breakpoints. See section [Commands for controlled output](Canned%20Sequences%20of%20Commands.md#apple-kncugmrsg4).

For example, here is how you could use breakpoint commands to print the
value of `x` at entry to `foo` whenever `x` is positive.

```
break foo if x>0
commands
silent
printf "x is %d\n",x
cont
end
```

One application for breakpoint commands is to compensate for one bug so
you can test for another. Put a breakpoint just after the erroneous line
of code, give it a condition to detect the case in which something
erroneous has been done, and give it commands to assign correct values
to any variables that need them. End with the `continue` command
so that your program does not stop, and start with the `silent`
command so that no output is produced. Here is an example:

```
break 403
commands
silent
set x = y + 4
cont
end
```

### [Breakpoint menus](Debugging%20with%20GDB.md#apple-krhugmzy)

Some programming languages (notably C++ and Objective-C/C++) permit a
single function name
to be defined several times, for application in different contexts.
This is called __overloading__. When a function name is overloaded,
`` `break function' `` is not enough to tell GDB where you want
a breakpoint. If you realize this is a problem, you can use
something like `` `break function(types)' `` to specify which
particular version of the function you want. Otherwise, GDB offers
you a menu of numbered choices for different possible breakpoints, and
waits for your selection with the prompt `` `>' ``. The first two
options are always `` `[0] cancel' `` and `` `[1] all' ``. Typing `1`
sets a breakpoint at each definition of function, and typing
`0` aborts the `break` command without setting any new
breakpoints.

For example, the following session excerpt shows an attempt to set a
breakpoint at the overloaded symbol `String::after`.
We choose three particular definitions of that function name:

```
(gdb) b String::after
[0] cancel
[1] all
[2] file:String.cc; line number:867
[3] file:String.cc; line number:860
[4] file:String.cc; line number:875
[5] file:String.cc; line number:853
[6] file:String.cc; line number:846
[7] file:String.cc; line number:735
> 2 4 6
Breakpoint 1 at 0xb26c: file String.cc, line 867.
Breakpoint 2 at 0xb344: file String.cc, line 875.
Breakpoint 3 at 0xafcc: file String.cc, line 846.
Multiple breakpoints were set.
Use the "delete" command to delete unwanted
 breakpoints.
(gdb)
```

### ["Cannot insert breakpoints"](Debugging%20with%20GDB.md#apple-krhugmzz)

Under some operating systems, breakpoints cannot be used in a program if
any other process is running that program. In this situation,
attempting to run or continue a program with a breakpoint causes
GDB to print an error message:

```
Cannot insert breakpoints.
The same program may be running in another process.
```

When this happens, you have three ways to proceed:

1. Remove or disable the breakpoints, then continue.
2. Suspend GDB, and copy the file containing your program to a new
   name. Resume GDB and use the `exec-file` command to specify
   that GDB should run your program under that name.
   Then start your program again.
3. Relink your program so that the text segment is nonsharable, using the
   linker option `` `-N' ``. The operating system limitation may not apply
   to nonsharable executables.

A similar message can be printed if you request too many active
hardware-assisted breakpoints and watchpoints:

```
Stopped; cannot insert breakpoints.
You may have requested too many hardware breakpoints and watchpoints.
```

This message is printed when you attempt to resume the program, since
only then GDB knows exactly how many hardware breakpoints and
watchpoints it needs to insert.

When this message is printed, you need to disable or remove some of the
hardware-assisted breakpoints and watchpoints, and then continue.

### ["Breakpoint address adjusted..."](Debugging%20with%20GDB.md#apple-krhugnbq)

Some processor architectures place constraints on the addresses at
which breakpoints may be placed. For architectures thus constrained,
GDB will attempt to adjust the breakpoint's address to comply
with the constraints dictated by the architecture.

One example of such an architecture is the Fujitsu FR-V. The FR-V is
a VLIW architecture in which a number of RISC-like instructions may be
bundled together for parallel execution. The FR-V architecture
constrains the location of a breakpoint instruction within such a
bundle to the instruction with the lowest address. GDB
honors this constraint by adjusting a breakpoint's address to the
first in the bundle.

It is not uncommon for optimized code to have bundles which contain
instructions from different source statements, thus it may happen that
a breakpoint's address will be adjusted from one source statement to
another. Since this adjustment may significantly alter GDB's
breakpoint related behavior from what the user expects, a warning is
printed when the breakpoint is first set and also when the breakpoint
is hit.

A warning like the one below is printed when setting a breakpoint
that's been subject to address adjustment:

```
warning: Breakpoint address adjusted from 0x00010414 to 0x00010410.
```

Such warnings are printed both for user settable and GDB's
internal breakpoints. If you see one of these warnings, you should
verify that a breakpoint set at the adjusted address will have the
desired affect. If not, the breakpoint in question may be removed and
other breakpoints may be set which will have the desired behavior.
E.g., it may be sufficient to place the breakpoint at a later
instruction. A conditional breakpoint may also be useful in some
cases to prevent the breakpoint from triggering too often.

GDB will also issue a warning when stopping at one of these
adjusted breakpoints:

```
warning: Breakpoint 1 address previously adjusted from 0x00010414
to 0x00010410.
```

When this warning is encountered, it may be too late to take remedial
action except in cases where the breakpoint is hit earlier or more
frequently than expected.

## [Continuing and stepping](Debugging%20with%20GDB.md#apple-krhugnbr)

__Continuing__ means resuming program execution until your program
completes normally. In contrast, __stepping__ means executing just
one more "step" of your program, where "step" may mean either one
line of source code, or one machine instruction (depending on what
particular command you use). Either when continuing or when stepping,
your program may stop even sooner, due to a breakpoint or a signal. (If
it stops due to a signal, you may want to use `handle`, or use
`` `signal 0' `` to resume execution. See section [Signals](#apple-kncugnbs).)

**`continue [ignore-count]`**
: 

**`c [ignore-count]`**
:

**`fg [ignore-count]`**
: Resume program execution, at the address where your program last stopped;
any breakpoints set at that address are bypassed. The optional argument
ignore-count allows you to specify a further number of times to
ignore a breakpoint at this location; its effect is like that of
`ignore` (see section [Break conditions](#apple-kncugmzw)).
The argument ignore-count is meaningful only when your program
stopped due to a breakpoint. At other times, the argument to
`continue` is ignored.
The synonyms `c` and `fg` (for __foreground__, as the
debugged program is deemed to be the foreground program) are provided
purely for convenience, and have exactly the same behavior as
`continue`.

To resume execution at a different place, you can use `return`
(see section [Returning from a function](Altering%20Execution.md#apple-kncugmjugm)) to go back to the
calling function; or `jump` (see section [Continuing at a different address](Altering%20Execution.md#apple-kncugmjuge)) to go to an arbitrary location in your program.

A typical technique for using stepping is to set a breakpoint
(see section [Breakpoints, watchpoints, and catchpoints](#apple-kncugmzq)) at the
beginning of the function or the section of your program where a problem
is believed to lie, run your program until it stops at that breakpoint,
and then step through the suspect area, examining the variables that are
interesting, until you see the problem happen.

**`step`**
: 

Continue running your program until control reaches a different source
line, then stop it and return control to GDB. This command is
abbreviated `s`.
> _Warning:_ If you use the `step` command while control is
> within a function that was compiled without debugging information,
> execution proceeds until control reaches a function that does have
> debugging information. Likewise, it will not step into a function which
> is compiled without debugging information. To step through functions
> without debugging information, use the `stepi` command, described
> below.

The `step` command only stops at the first instruction of a source
line. This prevents the multiple stops that could otherwise occur in
`switch` statements, `for` loops, etc. `step` continues
to stop if a function that has debugging information is called within
the line. In other words, `step` _steps inside_ any functions
called within the line.
Also, the `step` command only enters a function if there is line
number information for the function. Otherwise it acts like the
`next` command. This avoids problems when using `cc -gl`
on MIPS machines. Previously, `step` entered subroutines if there
was any debugging information about the routine.

**`step count`**
: Continue running as in `step`, but do so count times. If a
breakpoint is reached, or a signal not related to stepping occurs before
count steps, stepping stops right away.

**`next [count]`**
: Continue to the next source line in the current (innermost) stack frame.
This is similar to `step`, but function calls that appear within
the line of code are executed without stopping. Execution stops when
control reaches a different line of code at the original stack level
that was executing when you gave the `next` command. This command
is abbreviated `n`.
An argument count is a repeat count, as for `step`.
The `next` command only stops at the first instruction of a
source line. This prevents multiple stops that could otherwise occur in
`switch` statements, `for` loops, etc.

**`set step-mode`**
: 

**`set step-mode on`**
: The `set step-mode on` command causes the `step` command to
stop at the first instruction of a function which contains no debug line
information rather than stepping over it.
This is useful in cases where you may be interested in inspecting the
machine instructions of a function which has no symbolic info and do not
want GDB to automatically skip over this function.

**`set step-mode off`**
: Causes the `step` command to step over any functions which contains no
debug information. This is the default.

**`show step-mode`**
: Show whether GDB will stop in or step over functions without
source line debug information.

**`finish`**
: Continue running until just after function in the selected stack frame
returns. Print the returned value (if any).
Contrast this with the `return` command (see section [Returning from a function](Altering%20Execution.md#apple-kncugmjugm)).

**`until`**
:

**`u`**
: Continue running until a source line past the current line, in the
current stack frame, is reached. This command is used to avoid single
stepping through a loop more than once. It is like the `next`
command, except that when `until` encounters a jump, it
automatically continues execution until the program counter is greater
than the address of the jump.
This means that when you reach the end of a loop after single stepping
though it, `until` makes your program continue execution until it
exits the loop. In contrast, a `next` command at the end of a loop
simply steps back to the beginning of the loop, which forces you to step
through the next iteration.
`until` always stops your program if it attempts to exit the current
stack frame.
`until` may produce somewhat counterintuitive results if the order
of machine code does not match the order of the source lines. For
example, in the following excerpt from a debugging session, the `f`
(`frame`) command shows that execution is stopped at line
`206`; yet when we use `until`, we get to line `195`:

```
(gdb) f
#0  main (argc=4, argv=0xf7fffae8) at m4.c:206
206                 expand_input();
(gdb) until
195             for ( ; argc > 0; NEXTARG) {
```

This happened because, for execution efficiency, the compiler had
generated code for the loop closure test at the end, rather than the
start, of the loop--even though the test in a C `for`-loop is
written before the body of the loop. The `until` command appeared
to step back to the beginning of the loop when it advanced to this
expression; however, it has not really gone to an earlier
statement--not in terms of the actual machine code.
`until` with no argument works by means of single
instruction stepping, and hence is slower than `until` with an
argument.

**`until location`**
:

**`u location`**
: Continue running your program until either the specified location is
reached, or the current stack frame returns. location is any of
the forms of argument acceptable to `break` (see section [Setting breakpoints](#apple-kncugmzr)). This form of the command uses breakpoints, and
hence is quicker than `until` without an argument. The specified
location is actually reached only if it is in the current frame. This
implies that `until` can be used to skip over recursive function
invocations. For instance in the code below, if the current location is
line `96`, issuing `until 99` will execute the program up to
line `99` in the same invocation of factorial, i.e. after the inner
invocations have returned.

```
94	int factorial (int value)
95	{
96	    if (value > 1) {
97            value *= factorial (value - 1);
98	    }
99	    return (value);
100     }
```


**`advance location`**
: Continue running the program up to the given location. An argument is
required, which should be of the same form as arguments for the `break`
command. Execution will also stop upon exit from the current stack
frame. This command is similar to `until`, but `advance` will
not skip over recursive function calls, and the target location doesn't
have to be in the same frame as the current one.

**`stepi`**
:

**`stepi arg`**
:

**`si`**
: Execute one machine instruction, then stop and return to the debugger.
It is often useful to do `` `display/i $pc' `` when stepping by machine
instructions. This makes GDB automatically display the next
instruction to be executed, each time your program stops. See section [Automatic display](Examining%20Data.md#apple-kncugnrs).
An argument is a repeat count, as in `step`.

**`nexti`**
:

**`nexti arg`**
:

**`ni`**
: Execute one machine instruction, but if it is a function call,
proceed until the function returns.
An argument is a repeat count, as in `next`.

## [Signals](Debugging%20with%20GDB.md#apple-krhugnbs)

A signal is an asynchronous event that can happen in a program. The
operating system defines the possible kinds of signals, and gives each
kind a name and a number. For example, in Unix `SIGINT` is the
signal a program gets when you type an interrupt character (often `C-c`);
`SIGSEGV` is the signal a program gets from referencing a place in
memory far away from all the areas in use; `SIGALRM` occurs when
the alarm clock timer goes off (which happens only if your program has
requested an alarm).

Some signals, including `SIGALRM`, are a normal part of the
functioning of your program. Others, such as `SIGSEGV`, indicate
errors; these signals are __fatal__ (they kill your program immediately) if the
program has not specified in advance some other way to handle the signal.
`SIGINT` does not indicate an error in your program, but it is normally
fatal so it can carry out the purpose of the interrupt: to kill the program.

GDB has the ability to detect any occurrence of a signal in your
program. You can tell GDB in advance what to do for each kind of
signal.

Normally, GDB is set up to let the non-erroneous signals like
`SIGALRM` be silently passed to your program
(so as not to interfere with their role in the program's functioning)
but to stop your program immediately whenever an error signal happens.
You can change these settings with the `handle` command.

**`info signals`**
: 

**`info handle`**
: Print a table of all the kinds of signals and how GDB has been told to
handle each one. You can use this to see the signal numbers of all
the defined types of signals.
`info handle` is an alias for `info signals`.

**`handle signal keywords...`**
: Change the way GDB handles signal signal. signal
can be the number of a signal or its name (with or without the
`` `SIG' `` at the beginning); a list of signal numbers of the form
`` `low-high' ``; or the word `` `all' ``, meaning all the
known signals. The keywords say what change to make.

The keywords allowed by the `handle` command can be abbreviated.
Their full names are:

**`nostop`**
: GDB should not stop your program when this signal happens. It may
still print a message telling you that the signal has come in.

**`stop`**
: GDB should stop your program when this signal happens. This implies
the `print` keyword as well.

**`print`**
: GDB should print a message when this signal happens.

**`noprint`**
: GDB should not mention the occurrence of the signal at all. This
implies the `nostop` keyword as well.

**`pass`**
:

**`noignore`**
: GDB should allow your program to see this signal; your program
can handle the signal, or else it may terminate if the signal is fatal
and not handled. `pass` and `noignore` are synonyms.

**`nopass`**
:

**`ignore`**
: GDB should not allow your program to see this signal.
`nopass` and `ignore` are synonyms.

When a signal stops your program, the signal is not visible to the
program until you
continue. Your program sees the signal then, if `pass` is in
effect for the signal in question _at that time_. In other words,
after GDB reports a signal, you can use the `handle`
command with `pass` or `nopass` to control whether your
program sees that signal when you continue.

The default is set to `nostop`, `noprint`, `pass` for
non-erroneous signals such as `SIGALRM`, `SIGWINCH` and
`SIGCHLD`, and to `stop`, `print`, `pass` for the
erroneous signals.

You can also use the `signal` command to prevent your program from
seeing a signal, or cause it to see a signal it normally would not see,
or to give it any signal at any time. For example, if your program stopped
due to some sort of memory reference error, you might store correct
values into the erroneous variables and continue, hoping to see more
execution; but your program would probably terminate immediately as
a result of the fatal signal once it saw the signal. To prevent this,
you can continue with `` `signal 0' ``. See section [Giving your program a signal](Altering%20Execution.md#apple-kncugmjugi).

## [Stopping and starting multi-thread programs](Debugging%20with%20GDB.md#apple-krhugnbt)

When your program has multiple threads (see section [Debugging programs with multiple threads](Running%20Programs%20Under%20GDB.md#apple-kncugmrx)), you can choose whether to set
breakpoints on all threads, or on a particular thread.

**`break linespec thread threadno`**
: 

**`break linespec thread threadno if ...`**
: linespec specifies source lines; there are several ways of
writing them, but the effect is always to specify some source line.
Use the qualifier `` `thread threadno' `` with a breakpoint command
to specify that you only want GDB to stop the program when a
particular thread reaches this breakpoint. threadno is one of the
numeric thread identifiers assigned by GDB, shown in the first
column of the `` `info threads' `` display.
If you do not specify `` `thread threadno' `` when you set a
breakpoint, the breakpoint applies to _all_ threads of your
program.
You can use the `thread` qualifier on conditional breakpoints as
well; in this case, place `` `thread threadno' `` before the
breakpoint condition, like this:

```
(gdb) break frik.c:13 thread 28 if bartab > lim
```


Whenever your program stops under GDB for any reason,
_all_ threads of execution stop, not just the current thread. This
allows you to examine the overall state of the program, including
switching between threads, without worrying that things may change
underfoot.

There is an unfortunate side effect. If one thread stops for a
breakpoint, or for some other reason, and another thread is blocked in a
system call, then the system call may return prematurely. This is a
consequence of the interaction between multiple threads and the signals
that GDB uses to implement breakpoints and other events that
stop execution.

To handle this problem, your program should check the return value of
each system call and react appropriately. This is good programming
style anyways.

For example, do not write code like this:

```
  sleep (10);
```

The call to `sleep` will return early if a different thread stops
at a breakpoint or for some other reason.

Instead, write this:

```
  int unslept = 10;
  while (unslept > 0)
    unslept = sleep (unslept);
```

A system call is allowed to return early, so the system is still
conforming to its specification. But GDB does cause your
multi-threaded program to behave differently than it would without
GDB.

Also, GDB uses internal breakpoints in the thread library to
monitor certain events such as thread creation and thread destruction.
When such an event happens, a system call in another thread may return
prematurely, even though your program does not appear to stop.

Conversely, whenever you restart the program, _all_ threads start
executing. _This is true even when single-stepping_ with commands
like `step` or `next`.

In particular, GDB cannot single-step all threads in lockstep.
Since thread scheduling is up to your debugging target's operating
system (not controlled by GDB), other threads may
execute more than one statement while the current thread completes a
single step. Moreover, in general other threads stop in the middle of a
statement, rather than at a clean statement boundary, when the program
stops.

You might even find your program stopped in another thread after
continuing or even single-stepping. This happens whenever some other
thread runs into a breakpoint, a signal, or an exception before the
first thread completes whatever you requested.

On some OSes, you can lock the OS scheduler and thus allow only a single
thread to run.

**`set scheduler-locking mode`**
: 

Set the scheduler locking mode. If it is `off`, then there is no
locking and any thread may run at any time. If `on`, then only the
current thread may run when the inferior is resumed. The `step`
mode optimizes for single-stepping. It stops other threads from
"seizing the prompt" by preempting the current thread while you are
stepping. Other threads will only rarely (or never) get a chance to run
when you step. They are more likely to run when you `` `next' `` over a
function call, and they are completely free to run when you use commands
like `` `continue' ``, `` `until' ``, or `` `finish' ``. However, unless another
thread hits a breakpoint during its timeslice, they will never steal the
GDB prompt away from the thread that you are debugging.

**`show scheduler-locking`**
: Display the current scheduler locking mode.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Running%20Programs%20Under%20GDB.md), [next](Examining%20the%20Stack.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
