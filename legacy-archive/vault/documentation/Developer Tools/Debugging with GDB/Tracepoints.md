---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_11.html
archived_at: '2026-07-15T07:31:03.189936Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](C%20Preprocessor%20Macros.md), [next](Debugging%20Programs%20That%20Use%20Overlays.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Tracepoints](Debugging%20with%20GDB.md#apple-krhugobq)

In some applications, it is not feasible for the debugger to interrupt
the program's execution long enough for the developer to learn
anything helpful about its behavior. If the program's correctness
depends on its real-time behavior, delays introduced by a debugger
might cause the program to change its behavior drastically, or perhaps
fail, even when the code itself is correct. It is useful to be able
to observe the program's behavior without interrupting it.

Using GDB's `trace` and `collect` commands, you can
specify locations in the program, called __tracepoints__, and
arbitrary expressions to evaluate when those tracepoints are reached.
Later, using the `tfind` command, you can examine the values
those expressions had when the program hit the tracepoints. The
expressions may also denote objects in memory--structures or arrays,
for example--whose values GDB should record; while visiting
a particular tracepoint, you may inspect those objects as if they were
in memory at that moment. However, because GDB records these
values without interacting with you, it can do so quickly and
unobtrusively, hopefully not disturbing the program's behavior.

The tracepoint facility is currently available only for remote
targets. See section [Specifying a Debugging Target](Specifying%20a%20Debugging%20Target.md#apple-kncugmjvga). In addition, your remote target must know how
to collect trace data. This functionality is implemented in the remote
stub; however, none of the stubs distributed with GDB support
tracepoints as of this writing.

This chapter describes the tracepoint commands and features.

## [Commands to Set Tracepoints](Debugging%20with%20GDB.md#apple-krhugobr)

Before running such a __trace experiment__, an arbitrary number of
tracepoints can be set. Like a breakpoint (see section [Setting breakpoints](Stopping%20and%20Continuing.md#apple-kncugmzr)), a
tracepoint has a number assigned to it by GDB. Like with
breakpoints, tracepoint numbers are successive integers starting from
one. Many of the commands associated with tracepoints take the
tracepoint number as their argument, to identify which tracepoint to
work on.

For each tracepoint, you can specify, in advance, some arbitrary set
of data that you want the target to collect in the trace buffer when
it hits that tracepoint. The collected data can include registers,
local variables, or global data. Later, you can use GDB
commands to examine the values these data had at the time the
tracepoint was hit.

This section describes commands to set tracepoints and associated
conditions and actions.

### [Create and Delete Tracepoints](Debugging%20with%20GDB.md#apple-krhugobs)

**`trace`**
: 

The `trace` command is very similar to the `break` command.
Its argument can be a source line, a function name, or an address in
the target program. See section [Setting breakpoints](Stopping%20and%20Continuing.md#apple-kncugmzr). The `trace` command
defines a tracepoint, which is a point in the target program where the
debugger will briefly stop, collect some data, and then allow the
program to continue. Setting a tracepoint or changing its commands
doesn't take effect until the next `tstart` command; thus, you
cannot change the tracepoint attributes once a trace experiment is
running.
Here are some examples of using the `trace` command:

```
(gdb) trace foo.c:121    // a source file and line number

(gdb) trace +2           // 2 lines forward

(gdb) trace my_function  // first source line of function

(gdb) trace *my_function // EXACT start address of function

(gdb) trace *0x2117c4    // an address
```

You can abbreviate `trace` as `tr`.

The convenience variable `$tpnum` records the tracepoint number
of the most recently set tracepoint.

**`delete tracepoint [num]`**
: Permanently delete one or more tracepoints. With no argument, the
default is to delete all tracepoints.
Examples:

```
(gdb) delete trace 1 2 3 // remove three tracepoints

(gdb) delete trace       // remove all tracepoints
```

You can abbreviate this command as `del tr`.

### [Enable and Disable Tracepoints](Debugging%20with%20GDB.md#apple-krhugobt)

**`disable tracepoint [num]`**
: 
Disable tracepoint num, or all tracepoints if no argument
num is given. A disabled tracepoint will have no effect during
the next trace experiment, but it is not forgotten. You can re-enable
a disabled tracepoint using the `enable tracepoint` command.

**`enable tracepoint [num]`**
: Enable tracepoint num, or all tracepoints. The enabled
tracepoints will become effective the next time a trace experiment is
run.

### [Tracepoint Passcounts](Debugging%20with%20GDB.md#apple-krhugobu)

**`passcount [n [num]]`**
: 

Set the __passcount__ of a tracepoint. The passcount is a way to
automatically stop a trace experiment. If a tracepoint's passcount is
n, then the trace experiment will be automatically stopped on
the n'th time that tracepoint is hit. If the tracepoint number
num is not specified, the `passcount` command sets the
passcount of the most recently defined tracepoint. If no passcount is
given, the trace experiment will run until stopped explicitly by the
user.
Examples:

```
(gdb) passcount 5 2 // Stop on the 5th execution of
                                   // tracepoint 2

(gdb) passcount 12  // Stop on the 12th execution of the
                                   // most recently defined tracepoint.
(gdb) trace foo
(gdb) pass 3
(gdb) trace bar
(gdb) pass 2
(gdb) trace baz
(gdb) pass 1        // Stop tracing when foo has been
                                    // executed 3 times OR when bar has
                                    // been executed 2 times
                                    // OR when baz has been executed 1 time.
```

### [Tracepoint Action Lists](Debugging%20with%20GDB.md#apple-krhugobv)

**`actions [num]`**
: 

This command will prompt for a list of actions to be taken when the
tracepoint is hit. If the tracepoint number num is not
specified, this command sets the actions for the one that was most
recently defined (so that you can define a tracepoint and then say
`actions` without bothering about its number). You specify the
actions themselves on the following lines, one action at a time, and
terminate the actions list with a line containing just `end`. So
far, the only defined actions are `collect` and
`while-stepping`.

To remove all actions from a tracepoint, type `` `actions num' ``
and follow it immediately with `` `end' ``.

```
(gdb) collect data // collect some data

(gdb) while-stepping 5 // single-step 5 times, collect data

(gdb) end              // signals the end of actions.
```

In the following example, the action list begins with `collect`
commands indicating the things to be collected when the tracepoint is
hit. Then, in order to single-step and collect additional data
following the tracepoint, a `while-stepping` command is used,
followed by the list of things to be collected while stepping. The
`while-stepping` command is terminated by its own separate
`end` command. Lastly, the action list is terminated by an
`end` command.

```
(gdb) trace foo
(gdb) actions
Enter actions for tracepoint 1, one per line:
> collect bar,baz
> collect $regs
> while-stepping 12
  > collect $fp, $sp
  > end
end
```


**`collect expr1, expr2, ...`**
: Collect values of the given expressions when the tracepoint is hit.
This command accepts a comma-separated list of any valid expressions.
In addition to global, static, or local variables, the following
special arguments are supported:

**`$regs`**
: collect all registers

**`$args`**
: collect all function arguments

**`$locals`**
: collect all local variables.

You can give several consecutive `collect` commands, each one
with a single argument, or one `collect` command with several
arguments separated by commas: the effect is the same.
The command `info scope` (see section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha)) is
particularly useful for figuring out what data to collect.

**`while-stepping n`**
: Perform n single-step traces after the tracepoint, collecting
new data at each step. The `while-stepping` command is
followed by the list of what to collect while stepping (followed by
its own `end` command):

```
> while-stepping 12
  > collect $regs, myglobal
  > end
>
```

You may abbreviate `while-stepping` as `ws` or
`stepping`.

### [Listing Tracepoints](Debugging%20with%20GDB.md#apple-krhugobw)

**`info tracepoints [num]`**
: 

Display information about the tracepoint num. If you don't specify
a tracepoint number, displays information about all the tracepoints
defined so far. For each tracepoint, the following information is
shown:

- its number
- whether it is enabled or disabled
- its address
- its passcount as given by the `passcount n` command
- its step count as given by the `while-stepping n` command
- where in the source files is the tracepoint set
- its action list as given by the `actions` command

```
(gdb) info trace
Num Enb Address    PassC StepC What
1   y   0x002117c4 0     0     <gdb_asm>
2   y   0x0020dc64 0     0     in g_test at g_test.c:1375
3   y   0x0020b1f4 0     0     in get_data at ../foo.c:41
(gdb)
```

This command can be abbreviated `info tp`.

### [Starting and Stopping Trace Experiment](Debugging%20with%20GDB.md#apple-krhugobx)

**`tstart`**
: 

This command takes no arguments. It starts the trace experiment, and
begins collecting data. This has the side effect of discarding all
the data collected in the trace buffer during the previous trace
experiment.

**`tstop`**
: This command takes no arguments. It ends the trace experiment, and
stops collecting data.
__Note__: a trace experiment and data collection may stop
automatically if any tracepoint's passcount is reached
(see section [Tracepoint Passcounts](#apple-kncugobu)), or if the trace buffer becomes full.

**`tstatus`**
: This command displays the status of the current trace data
collection.

Here is an example of the commands we described so far:

```
(gdb) trace gdb_c_test
(gdb) actions
Enter actions for tracepoint #1, one per line.
> collect $regs,$locals,$args
> while-stepping 11
  > collect $regs
  > end
> end
(gdb) tstart
    [time passes ...]
(gdb) tstop
```

## [Using the collected data](Debugging%20with%20GDB.md#apple-krhugoby)

After the tracepoint experiment ends, you use GDB commands
for examining the trace data. The basic idea is that each tracepoint
collects a trace __snapshot__ every time it is hit and another
snapshot every time it single-steps. All these snapshots are
consecutively numbered from zero and go into a buffer, and you can
examine them later. The way you examine them is to __focus__ on a
specific trace snapshot. When the remote stub is focused on a trace
snapshot, it will respond to all GDB requests for memory and
registers by reading from the buffer which belongs to that snapshot,
rather than from _real_ memory or registers of the program being
debugged. This means that __all__ GDB commands
(`print`, `info registers`, `backtrace`, etc.) will
behave as if we were currently debugging the program state as it was
when the tracepoint occurred. Any requests for data that are not in
the buffer will fail.

### [`tfind n`](gdb_toc.md#apple-krhugobz)

The basic command for selecting a trace snapshot from the buffer is
`tfind n`, which finds trace snapshot number n,
counting from zero. If no argument n is given, the next
snapshot is selected.

Here are the various forms of using the `tfind` command.

**`tfind start`**
: Find the first snapshot in the buffer. This is a synonym for
`tfind 0` (since 0 is the number of the first snapshot).

**`tfind none`**
: Stop debugging trace snapshots, resume _live_ debugging.

**`tfind end`**
: Same as `` `tfind none' ``.

**`tfind`**
: No argument means find the next trace snapshot.

**`tfind -`**
: Find the previous trace snapshot before the current one. This permits
retracing earlier steps.

**`tfind tracepoint num`**
: Find the next snapshot associated with tracepoint num. Search
proceeds forward from the last examined trace snapshot. If no
argument num is given, it means find the next snapshot collected
for the same tracepoint as the current snapshot.

**`tfind pc addr`**
: Find the next snapshot associated with the value addr of the
program counter. Search proceeds forward from the last examined trace
snapshot. If no argument addr is given, it means find the next
snapshot with the same value of PC as the current snapshot.

**`tfind outside addr1, addr2`**
: Find the next snapshot whose PC is outside the given range of
addresses.

**`tfind range addr1, addr2`**
: Find the next snapshot whose PC is between addr1 and
addr2.

**`tfind line [file:]n`**
: Find the next snapshot associated with the source line n. If
the optional argument file is given, refer to line n in
that source file. Search proceeds forward from the last examined
trace snapshot. If no argument n is given, it means find the
next line other than the one currently being examined; thus saying
`tfind line` repeatedly can appear to have the same effect as
stepping from line to line in a _live_ debugging session.

The default arguments for the `tfind` commands are specifically
designed to make it easy to scan through the trace buffer. For
instance, `tfind` with no argument selects the next trace
snapshot, and `tfind -` with no argument selects the previous
trace snapshot. So, by giving one `tfind` command, and then
simply hitting `RET` repeatedly you can examine all the trace
snapshots in order. Or, by saying `tfind -` and then hitting
`RET` repeatedly you can examine the snapshots in reverse order.
The `tfind line` command with no argument selects the snapshot
for the next source line executed. The `tfind pc` command with
no argument selects the next snapshot with the same program counter
(PC) as the current frame. The `tfind tracepoint` command with
no argument selects the next trace snapshot collected by the same
tracepoint as the current one.

In addition to letting you scan through the trace buffer manually,
these commands make it easy to construct GDB scripts that
scan through the trace buffer and print out whatever collected data
you are interested in. Thus, if we want to examine the PC, FP, and SP
registers from each trace frame in the buffer, we can say this:

```
(gdb) tfind start
(gdb) while ($trace_frame != -1)
> printf "Frame %d, PC = %08X, SP = %08X, FP = %08X\n", \
          $trace_frame, $pc, $sp, $fp
> tfind
> end

Frame 0, PC = 0020DC64, SP = 0030BF3C, FP = 0030BF44
Frame 1, PC = 0020DC6C, SP = 0030BF38, FP = 0030BF44
Frame 2, PC = 0020DC70, SP = 0030BF34, FP = 0030BF44
Frame 3, PC = 0020DC74, SP = 0030BF30, FP = 0030BF44
Frame 4, PC = 0020DC78, SP = 0030BF2C, FP = 0030BF44
Frame 5, PC = 0020DC7C, SP = 0030BF28, FP = 0030BF44
Frame 6, PC = 0020DC80, SP = 0030BF24, FP = 0030BF44
Frame 7, PC = 0020DC84, SP = 0030BF20, FP = 0030BF44
Frame 8, PC = 0020DC88, SP = 0030BF1C, FP = 0030BF44
Frame 9, PC = 0020DC8E, SP = 0030BF18, FP = 0030BF44
Frame 10, PC = 00203F6C, SP = 0030BE3C, FP = 0030BF14
```

Or, if we want to examine the variable `X` at each source line in
the buffer:

```
(gdb) tfind start
(gdb) while ($trace_frame != -1)
> printf "Frame %d, X == %d\n", $trace_frame, X
> tfind line
> end

Frame 0, X = 1
Frame 7, X = 2
Frame 13, X = 255
```

### [`tdump`](gdb_toc.md#apple-krhugojq)

This command takes no arguments. It prints all the data collected at
the current trace snapshot.

```
(gdb) trace 444
(gdb) actions
Enter actions for tracepoint #2, one per line:
> collect $regs, $locals, $args, gdb_long_test
> end

(gdb) tstart

(gdb) tfind line 444
#0  gdb_test (p1=0x11, p2=0x22, p3=0x33, p4=0x44, p5=0x55, p6=0x66)
at gdb_test.c:444
444        printp( "%s: arguments = 0x%X 0x%X 0x%X 0x%X 0x%X 0x%X\n", )

(gdb) tdump
Data collected at tracepoint 2, trace frame 1:
d0             0xc4aa0085       -995491707
d1             0x18     24
d2             0x80     128
d3             0x33     51
d4             0x71aea3d        119204413
d5             0x22     34
d6             0xe0     224
d7             0x380035 3670069
a0             0x19e24a 1696330
a1             0x3000668        50333288
a2             0x100    256
a3             0x322000 3284992
a4             0x3000698        50333336
a5             0x1ad3cc 1758156
fp             0x30bf3c 0x30bf3c
sp             0x30bf34 0x30bf34
ps             0x0      0
pc             0x20b2c8 0x20b2c8
fpcontrol      0x0      0
fpstatus       0x0      0
fpiaddr        0x0      0
p = 0x20e5b4 "gdb-test"
p1 = (void *) 0x11
p2 = (void *) 0x22
p3 = (void *) 0x33
p4 = (void *) 0x44
p5 = (void *) 0x55
p6 = (void *) 0x66
gdb_long_test = 17 '\021'

(gdb)
```

### [`save-tracepoints filename`](gdb_toc.md#apple-krhugojr)

This command saves all current tracepoint definitions together with
their actions and passcounts, into a file `filename'
suitable for use in a later debugging session. To read the saved
tracepoint definitions, use the `source` command (see section [Command files](Canned%20Sequences%20of%20Commands.md#apple-kncugmrsgy)).

## [Convenience Variables for Tracepoints](Debugging%20with%20GDB.md#apple-krhugojs)

**`(int) $trace_frame`**
: 
The current trace snapshot (a.k.a. __frame__) number, or -1 if no
snapshot is selected.

**`(int) $tracepoint`**
: The tracepoint for the current trace snapshot.

**`(int) $trace_line`**
: The line number for the current trace snapshot.

**`(char []) $trace_file`**
: The source file for the current trace snapshot.

**`(char []) $trace_func`**
: The name of the function containing `$tracepoint`.

Note: `$trace_file` is not suitable for use in `printf`,
use `output` instead.

Here's a simple example of using these convenience variables for
stepping through all the trace snapshots and printing some of their
data.

```
(gdb) tfind start

(gdb) while $trace_frame != -1
> output $trace_file
> printf ", line %d (tracepoint #%d)\n", $trace_line, $tracepoint
> tfind
> end
```

---

Go to the [first](Summary%20of%20GDB.md), [previous](C%20Preprocessor%20Macros.md), [next](Debugging%20Programs%20That%20Use%20Overlays.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
