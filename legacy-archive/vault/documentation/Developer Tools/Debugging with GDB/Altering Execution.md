---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_15.html
archived_at: '2026-07-15T07:31:03.240452Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Examining%20the%20Symbol%20Table.md), [next](GDB%20Files.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Altering Execution](Debugging%20with%20GDB.md#apple-krhugmjthe)

Once you think you have found an error in your program, you might want to
find out for certain whether correcting the apparent error would lead to
correct results in the rest of the run. You can find the answer by
experiment, using the GDB features for altering execution of the
program.

For example, you can store new values into variables or memory
locations, give your program a signal, restart it at a different
address, or even return prematurely from a function.

## [Assignment to variables](Debugging%20with%20GDB.md#apple-krhugmjuga)

To alter the value of a variable, evaluate an assignment expression.
See section [Expressions](Examining%20Data.md#apple-kncugnjx). For example,

```
print x=4
```

stores the value 4 into the variable `x`, and then prints the
value of the assignment expression (which is 4).
See section [Using GDB with Different Languages](Using%20GDB%20with%20Different%20Languages.md#apple-kncugojy), for more
information on operators in supported languages.

If you are not interested in seeing the value of the assignment, use the
`set` command instead of the `print` command. `set` is
really the same as `print` except that the expression's value is
not printed and is not put in the value history (see section [Value history](Examining%20Data.md#apple-kncugnru)). The expression is evaluated only for its effects.

If the beginning of the argument string of the `set` command
appears identical to a `set` subcommand, use the `set
variable` command instead of just `set`. This command is identical
to `set` except for its lack of subcommands. For example, if your
program has a variable `width`, you get an error if you try to set
a new value with just `` `set width=13' ``, because GDB has the
command `set width`:

```
(gdb) whatis width
type = double
(gdb) p width
$4 = 13
(gdb) set width=47
Invalid syntax in expression.
```

The invalid expression, of course, is `` `=47' ``. In
order to actually set the program's variable `width`, use

```
(gdb) set var width=47
```

Because the `set` command has many subcommands that can conflict
with the names of program variables, it is a good idea to use the
`set variable` command instead of just `set`. For example, if
your program has a variable `g`, you run into problems if you try
to set a new value with just `` `set g=4' ``, because GDB has
the command `set gnutarget`, abbreviated `set g`:

```
(gdb) whatis g
type = double
(gdb) p g
$1 = 1
(gdb) set g=4
(gdb) p g
$2 = 1
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/smith/cc_progs/a.out
"/home/smith/cc_progs/a.out": can't open to read symbols:
                                 Invalid bfd target.
(gdb) show g
The current BFD target is "=4".
```

The program variable `g` did not change, and you silently set the
`gnutarget` to an invalid value. In order to set the variable
`g`, use

```
(gdb) set var g=4
```

GDB allows more implicit conversions in assignments than C; you can
freely store an integer value into a pointer variable or vice versa,
and you can convert any structure to any other structure that is the
same length or shorter.

To store values into arbitrary places in memory, use the `` `{...}' ``
construct to generate a value of specified type at a specified address
(see section [Expressions](Examining%20Data.md#apple-kncugnjx)). For example, `{int}0x83040` refers
to memory location `0x83040` as an integer (which implies a certain size
and representation in memory), and

```
set {int}0x83040 = 4
```

stores the value 4 into that memory location.

## [Continuing at a different address](Debugging%20with%20GDB.md#apple-krhugmjuge)

Ordinarily, when you continue your program, you do so at the place where
it stopped, with the `continue` command. You can instead continue at
an address of your own choosing, with the following commands:

**`jump linespec`**
: 
Resume execution at line linespec. Execution stops again
immediately if there is a breakpoint there. See section [Printing source lines](Examining%20Source%20Files.md#apple-kncugnjq), for a description of the different forms of
linespec. It is common practice to use the `tbreak` command
in conjunction with `jump`. See section [Setting breakpoints](Stopping%20and%20Continuing.md#apple-kncugmzr).
The `jump` command does not change the current stack frame, or
the stack pointer, or the contents of any memory location or any
register other than the program counter. If line linespec is in
a different function from the one currently executing, the results may
be bizarre if the two functions expect different patterns of arguments or
of local variables. For this reason, the `jump` command requests
confirmation if the specified line is not in the function currently
executing. However, even bizarre results are predictable if you are
well acquainted with the machine-language code of your program.

**`jump *address`**
: Resume execution at the instruction at address address.

On many systems, you can get much the same effect as the `jump`
command by storing a new value into the register `$pc`. The
difference is that this does not start your program running; it only
changes the address of where it _will_ run when you continue. For
example,

```
set $pc = 0x485
```

makes the next `continue` command or stepping command execute at
address `0x485`, rather than at the address where your program stopped.
See section [Continuing and stepping](Stopping%20and%20Continuing.md#apple-kncugnbr).

The most common occasion to use the `jump` command is to back
up--perhaps with more breakpoints set--over a portion of a program
that has already executed, in order to examine its execution in more
detail.

## [Giving your program a signal](Debugging%20with%20GDB.md#apple-krhugmjugi)

**`signal signal`**
: 
Resume execution where your program stopped, but immediately give it the
signal signal. signal can be the name or the number of a
signal. For example, on many systems `signal 2` and `signal
SIGINT` are both ways of sending an interrupt signal.
Alternatively, if signal is zero, continue execution without
giving a signal. This is useful when your program stopped on account of
a signal and would ordinary see the signal when resumed with the
`continue` command; `` `signal 0' `` causes it to resume without a
signal.
`signal` does not repeat when you press `RET` a second time
after executing the command.

Invoking the `signal` command is not the same as invoking the
`kill` utility from the shell. Sending a signal with `kill`
causes GDB to decide what to do with the signal depending on
the signal handling tables (see section [Signals](Stopping%20and%20Continuing.md#apple-kncugnbs)). The `signal` command
passes the signal directly to your program.

## [Returning from a function](Debugging%20with%20GDB.md#apple-krhugmjugm)

**`return`**
: 

**`return expression`**
: You can cancel execution of a function call with the `return`
command. If you give an
expression argument, its value is used as the function's return
value.

When you use `return`, GDB discards the selected stack frame
(and all frames within it). You can think of this as making the
discarded frame return prematurely. If you wish to specify a value to
be returned, give that value as the argument to `return`.

This pops the selected stack frame (see section [Selecting a frame](Examining%20the%20Stack.md#apple-kncugnbx)), and any other frames inside of it, leaving its caller as the
innermost remaining frame. That frame becomes selected. The
specified value is stored in the registers used for returning values
of functions.

The `return` command does not resume execution; it leaves the
program stopped in the state that would exist if the function had just
returned. In contrast, the `finish` command (see section [Continuing and stepping](Stopping%20and%20Continuing.md#apple-kncugnbr)) resumes execution until the
selected stack frame returns naturally.

## [Calling program functions](Debugging%20with%20GDB.md#apple-krhugmjugq)

**`print expr`**
: 

Evaluate the expression expr and display the resuling value.
expr may include calls to functions in the program being
debugged.

**`call expr`**
: Evaluate the expression expr without displaying `void`
returned values.
You can use this variant of the `print` command if you want to
execute a function from your program that does not return anything
(a.k.a. __a void function__), but without cluttering the output
with `void` returned values that GDB will otherwise
print. If the result is not void, it is printed and saved in the
value history.

It is possible for the function you call via the `print` or
`call` command to generate a signal (e.g., if there's a bug in
the function, or if you passed it incorrect arguments). What happens
in that case is controlled by the `set unwindonsignal` command.

**`set unwindonsignal`**
: 

Set unwinding of the stack if a signal is received while in a function
that GDB called in the program being debugged. If set to on,
GDB unwinds the stack it created for the call and restores
the context to what it was before the call. If set to off (the
default), GDB stops in the frame where the signal was
received.

**`show unwindonsignal`**
: 
Show the current setting of stack unwinding in the functions called by
GDB.

Sometimes, a function you wish to call is actually a __weak alias__
for another function. In such case, GDB might not pick up
the type information, including the types of the function arguments,
which causes GDB to call the inferior function incorrectly.
As a result, the called function will function erroneously and may
even crash. A solution to that is to use the name of the aliased
function instead.

## [Patching programs](Debugging%20with%20GDB.md#apple-krhugmjugu)

By default, GDB opens the file containing your program's
executable code (or the corefile) read-only. This prevents accidental
alterations to machine code; but it also prevents you from intentionally
patching your program's binary.

If you'd like to be able to patch the binary, you can specify that
explicitly with the `set write` command. For example, you might
want to turn on internal debugging flags, or even to make emergency
repairs.

**`set write on`**
: 

**`set write off`**
: If you specify `` `set write on' ``, GDB opens executable and
core files for both reading and writing; if you specify `` `set write
off' `` (the default), GDB opens them read-only.
If you have already loaded a file, you must load it again (using the
`exec-file` or `core-file` command) after changing `set
write`, for your new setting to take effect.

**`show write`**
: 
Display whether executable files and core files are opened for writing
as well as reading.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Examining%20the%20Symbol%20Table.md), [next](GDB%20Files.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
