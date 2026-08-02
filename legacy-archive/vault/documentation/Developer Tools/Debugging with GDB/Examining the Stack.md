---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_7.html
archived_at: '2026-07-15T07:31:03.636704Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Stopping%20and%20Continuing.md), [next](Examining%20Source%20Files.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Examining the Stack](Debugging%20with%20GDB.md#apple-krhugnbu)

When your program has stopped, the first thing you need to know is where it
stopped and how it got there.

Each time your program performs a function call, information about the call
is generated.
That information includes the location of the call in your program,
the arguments of the call,
and the local variables of the function being called.
The information is saved in a block of data called a __stack frame__.
The stack frames are allocated in a region of memory called the __call
stack__.

When your program stops, the GDB commands for examining the
stack allow you to see all of this information.

One of the stack frames is __selected__ by GDB and many
GDB commands refer implicitly to the selected frame. In
particular, whenever you ask GDB for the value of a variable in
your program, the value is found in the selected frame. There are
special GDB commands to select whichever frame you are
interested in. See section [Selecting a frame](#apple-kncugnbx).

When your program stops, GDB automatically selects the
currently executing frame and describes it briefly, similar to the
`frame` command (see section [Information about a frame](#apple-kncugnby)).

## [Stack frames](Debugging%20with%20GDB.md#apple-krhugnbv)

The call stack is divided up into contiguous pieces called __stack
frames__, or __frames__ for short; each frame is the data associated
with one call to one function. The frame contains the arguments given
to the function, the function's local variables, and the address at
which the function is executing.

When your program is started, the stack has only one frame, that of the
function `main`. This is called the __initial__ frame or the
__outermost__ frame. Each time a function is called, a new frame is
made. Each time a function returns, the frame for that function invocation
is eliminated. If a function is recursive, there can be many frames for
the same function. The frame for the function in which execution is
actually occurring is called the __innermost__ frame. This is the most
recently created of all the stack frames that still exist.

Inside your program, stack frames are identified by their addresses. A
stack frame consists of many bytes, each of which has its own address; each
kind of computer has a convention for choosing one byte whose
address serves as the address of the frame. Usually this address is kept
in a register called the __frame pointer register__
(see section [Registers](Examining%20Data.md#apple-kncugnrw)) while execution is going on in that frame.

GDB assigns numbers to all existing stack frames, starting with
zero for the innermost frame, one for the frame that called it,
and so on upward. These numbers do not really exist in your program;
they are assigned by GDB to give you a way of designating stack
frames in GDB commands.

Some compilers provide a way to compile functions so that they operate
without stack frames. (For example, the gcc option

```
`-fomit-frame-pointer'
```

generates functions without a frame.)
This is occasionally done with heavily used library functions to save
the frame setup time. GDB has limited facilities for dealing
with these function invocations. If the innermost function invocation
has no stack frame, GDB nevertheless regards it as though
it had a separate frame, which is numbered zero as usual, allowing
correct tracing of the function call chain. However, GDB has
no provision for frameless functions elsewhere in the stack.

**`frame args`**
: 

The `frame` command allows you to move from one stack frame to another,
and to print the stack frame you select. args may be either the
address of the frame or the stack frame number. Without an argument,
`frame` prints the current stack frame.

**`select-frame`**
: The `select-frame` command allows you to move from one stack frame
to another without printing the frame. This is the silent version of
`frame`.

## [Backtraces](Debugging%20with%20GDB.md#apple-krhugnbw)

A backtrace is a summary of how your program got where it is. It shows one
line per frame, for many frames, starting with the currently executing
frame (frame zero), followed by its caller (frame one), and on up the
stack.

**`backtrace`**
: 

**`bt`**
: Print a backtrace of the entire stack: one line per frame for all
frames in the stack.
You can stop the backtrace at any time by typing the system interrupt
character, normally `C-c`.

**`backtrace n`**
:

**`bt n`**
: Similar, but print only the innermost n frames.

**`backtrace -n`**
:

**`bt -n`**
: Similar, but print only the outermost n frames.

**`backtrace full`**
: Print the values of the local variables also.

**`bt full`**
:

The names `where` and `info stack` (abbreviated `info s`)
are additional aliases for `backtrace`.

Each line in the backtrace shows the frame number and the function name.
The program counter value is also shown--unless you use `set
print address off`. The backtrace also shows the source file name and
line number, as well as the arguments to the function. The program
counter value is omitted if it is at the beginning of the code for that
line number.

Here is an example of a backtrace. It was made with the command
`` `bt 3' ``, so it shows the innermost three frames.

```
#0  m4_traceon (obs=0x24eb0, argc=1, argv=0x2b8c8)
    at builtin.c:993
#1  0x6e38 in expand_macro (sym=0x2b600) at macro.c:242
#2  0x6840 in expand_token (obs=0x0, t=177664, td=0xf7fffb08)
    at macro.c:71
(More stack frames follow...)
```

The display for frame zero does not begin with a program counter
value, indicating that your program has stopped at the beginning of the
code for line `993` of `builtin.c`.

If your program was compiled with optimizations, some compilers will
optimize away arguments passed to functions if those arguments are
never used after the call. Such optimizations generate code that
passes arguments through registers, but doesn't store those arguments
in the stack frame. GDB has no way of displaying such
arguments in stack frames other than the innermost one. Here's what
such a backtrace might look like:

```
#0  m4_traceon (obs=0x24eb0, argc=1, argv=0x2b8c8)
    at builtin.c:993
#1  0x6e38 in expand_macro (sym=<value optimized out>) at macro.c:242
#2  0x6840 in expand_token (obs=0x0, t=<value optimized out>, td=0xf7fffb08)
    at macro.c:71
(More stack frames follow...)
```

The values of arguments that were not saved in their stack frames are
shown as `` `<value optimized out>' ``.

If you need to display the values of such optimized-out arguments,
either deduce that from other variables whose values depend on the one
you are interested in, or recompile without optimizations.

Most programs have a standard user entry point--a place where system
libraries and startup code transition into user code. For C this is
`main`[(2)](Debugging%20with%20GDB-2.md#apple-izhu6vbs).
When GDB finds the entry function in a backtrace
it will terminate the backtrace, to avoid tracing into highly
system-specific (and generally uninteresting) code.

If you need to examine the startup code, or limit the number of levels
in a backtrace, you can change this behavior:

**`set backtrace past-main`**
:

**`set backtrace past-main on`**
: 
Backtraces will continue past the user entry point.

**`set backtrace past-main off`**
: Backtraces will stop when they encounter the user entry point. This is the
default.

**`show backtrace past-main`**
: 
Display the current user entry point backtrace policy.

**`set backtrace past-entry`**
:

**`set backtrace past-entry on`**
: Backtraces will continue past the internal entry point of an application.
This entry point is encoded by the linker when the application is built,
and is likely before the user entry point `main` (or equivalent) is called.

**`set backtrace past-entry off`**
: Backtraces will stop when they encouter the internal entry point of an
application. This is the default.

**`show backtrace past-entry`**
: Display the current internal entry point backtrace policy.

**`set backtrace limit n`**
:

**`set backtrace limit 0`**
: 
Limit the backtrace to n levels. A value of zero means
unlimited.

**`show backtrace limit`**
: Display the current limit on backtrace levels.

## [Selecting a frame](Debugging%20with%20GDB.md#apple-krhugnbx)

Most commands for examining the stack and other data in your program work on
whichever stack frame is selected at the moment. Here are the commands for
selecting a stack frame; all of them finish by printing a brief description
of the stack frame just selected.

**`frame n`**
: 

**`f n`**
: Select frame number n. Recall that frame zero is the innermost
(currently executing) frame, frame one is the frame that called the
innermost one, and so on. The highest-numbered frame is the one for
`main`.

**`frame addr`**
:

**`f addr`**
: Select the frame at address addr. This is useful mainly if the
chaining of stack frames has been damaged by a bug, making it
impossible for GDB to assign numbers properly to all frames. In
addition, this can be useful when your program has multiple stacks and
switches between them.
On the SPARC architecture, `frame` needs two addresses to
select an arbitrary frame: a frame pointer and a stack pointer.
On the MIPS and Alpha architecture, it needs two addresses: a stack
pointer and a program counter.
On the 29k architecture, it needs three addresses: a register stack
pointer, a program counter, and a memory stack pointer.

**`up n`**
: Move n frames up the stack. For positive numbers n, this
advances toward the outermost frame, to higher frame numbers, to frames
that have existed longer. n defaults to one.

**`down n`**
: Move n frames down the stack. For positive numbers n, this
advances toward the innermost frame, to lower frame numbers, to frames
that were created more recently. n defaults to one. You may
abbreviate `down` as `do`.

All of these commands end by printing two lines of output describing the
frame. The first line shows the frame number, the function name, the
arguments, and the source file and line number of execution in that
frame. The second line shows the text of that source line.

For example:

```
(gdb) up
#1  0x22f0 in main (argc=1, argv=0xf7fffbf4, env=0xf7fffbfc)
    at env.c:10
10              read_input_file (argv[i]);
```

After such a printout, the `list` command with no arguments
prints ten lines centered on the point of execution in the frame.
You can also edit the program at the point of execution with your favorite
editing program by typing `edit`.
See section [Printing source lines](Examining%20Source%20Files.md#apple-kncugnjq),
for details.

**`up-silently n`**
: 

**`down-silently n`**
: These two commands are variants of `up` and `down`,
respectively; they differ in that they do their work silently, without
causing display of the new frame. They are intended primarily for use
in GDB command scripts, where the output might be unnecessary and
distracting.

## [Information about a frame](Debugging%20with%20GDB.md#apple-krhugnby)

There are several other commands to print information about the selected
stack frame.

**`frame`**
:

**`f`**
: When used without any argument, this command does not change which
frame is selected, but prints a brief description of the currently
selected stack frame. It can be abbreviated `f`. With an
argument, this command is used to select a stack frame.
See section [Selecting a frame](#apple-kncugnbx).

**`info frame`**
:

**`info f`**
: This command prints a verbose description of the selected stack frame,
including:

- the address of the frame
- the address of the next frame down (called by this frame)
- the address of the next frame up (caller of this frame)
- the language in which the source code corresponding to this frame is written
- the address of the frame's arguments
- the address of the frame's local variables
- the program counter saved in it (the address of execution in the caller frame)
- which registers were saved in the frame

The verbose description is useful when
something has gone wrong that has made the stack format fail to fit
the usual conventions.

**`info frame addr`**
:

**`info f addr`**
: Print a verbose description of the frame at address addr, without
selecting that frame. The selected frame remains unchanged by this
command. This requires the same kind of address (more than one for some
architectures) that you specify in the `frame` command.
See section [Selecting a frame](#apple-kncugnbx).

**`info args`**
: Print the arguments of the selected frame, each on a separate line.

**`info locals`**
: 
Print the local variables of the selected frame, each on a separate
line. These are all variables (declared either static or automatic)
accessible at the point of execution of the selected frame.

**`info catch`**
: Print a list of all the exception handlers that are active in the
current stack frame at the current point of execution. To see other
exception handlers, visit the associated frame (using the `up`,
`down`, or `frame` commands); then type `info catch`.
See section [Setting catchpoints](Stopping%20and%20Continuing.md#apple-kncugmzt).

---

Go to the [first](Summary%20of%20GDB.md), [previous](Stopping%20and%20Continuing.md), [next](Examining%20Source%20Files.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
