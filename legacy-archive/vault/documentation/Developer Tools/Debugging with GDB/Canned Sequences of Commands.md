---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_21.html
archived_at: '2026-07-15T07:31:03.329911Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Controlling%20GDB.md), [next](Command%20Interpreters.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Canned Sequences of Commands](Debugging%20with%20GDB.md#apple-krhugmrsgm)

Aside from breakpoint commands (see section [Breakpoint command lists](Stopping%20and%20Continuing.md#apple-kncugmzx)), GDB provides two ways to store sequences of
commands for execution as a unit: user-defined commands and command
files.

## [User-defined commands](Debugging%20with%20GDB.md#apple-krhugmrsgq)

A __user-defined command__ is a sequence of GDB commands to
which you assign a new name as a command. This is done with the
`define` command. User commands may accept up to 10 arguments
separated by whitespace. Arguments are accessed within the user command
via $arg0...$arg9. A trivial example:

```
define adder
  print $arg0 + $arg1 + $arg2
```

To execute the command use:

```
adder 1 2 3
```

This defines the command `adder`, which prints the sum of
its three arguments. Note the arguments are text substitutions, so they may
reference variables, use complex expressions, or even perform inferior
functions calls.

**`define commandname`**
: 
Define a command named commandname. If there is already a command
by that name, you are asked to confirm that you want to redefine it.
The definition of the command is made up of other GDB command lines,
which are given following the `define` command. The end of these
commands is marked by a line containing `end`.

**`if`**
:

**`else`**
: Takes a single argument, which is an expression to evaluate.
It is followed by a series of commands that are executed
only if the expression is true (nonzero).
There can then optionally be a line `else`, followed
by a series of commands that are only executed if the expression
was false. The end of the list is marked by a line containing `end`.

**`while`**
: The syntax is similar to `if`: the command takes a single argument,
which is an expression to evaluate, and must be followed by the commands to
execute, one per line, terminated by an `end`.
The commands are executed repeatedly as long as the expression
evaluates to true.

**`document commandname`**
: Document the user-defined command commandname, so that it can be
accessed by `help`. The command commandname must already be
defined. This command reads lines of documentation just as `define`
reads the lines of the command definition, ending with `end`.
After the `document` command is finished, `help` on command
commandname displays the documentation you have written.
You may use the `document` command again to change the
documentation of a command. Redefining the command with `define`
does not change the documentation.

**`dont-repeat`**
: Used inside a user-defined command, this tells GDB that this
command should not be repeated when the user hits `RET`
(see section [Command syntax](GDB%20Commands.md#apple-kncugmjv)).

**`help user-defined`**
: List all user-defined commands, with the first line of the documentation
(if any) for each.

**`show user`**
:

**`show user commandname`**
: Display the GDB commands used to define commandname (but
not its documentation). If no commandname is given, display the
definitions for all user-defined commands.

**`show max-user-call-depth`**
:

**`set max-user-call-depth`**
: The value of `max-user-call-depth` controls how many recursion
levels are allowed in user-defined commands before GDB suspects an
infinite recursion and aborts the command.

When user-defined commands are executed, the
commands of the definition are not printed. An error in any command
stops execution of the user-defined command.

If used interactively, commands that would ask for confirmation proceed
without asking when used inside a user-defined command. Many GDB
commands that normally print messages to say what they are doing omit the
messages when used in a user-defined command.

## [User-defined command hooks](Debugging%20with%20GDB.md#apple-krhugmrsgu)

You may define __hooks__, which are a special kind of user-defined
command. Whenever you run the command `` `foo' ``, if the user-defined
command `` `hook-foo' `` exists, it is executed (with no arguments)
before that command.

A hook may also be defined which is run after the command you executed.
Whenever you run the command `` `foo' ``, if the user-defined command
`` `hookpost-foo' `` exists, it is executed (with no arguments) after
that command. Post-execution hooks may exist simultaneously with
pre-execution hooks, for the same command.

It is valid for a hook to call the command which it hooks. If this
occurs, the hook is not re-executed, thereby avoiding infinite recursion.

In addition, a pseudo-command, `` `stop' `` exists. Defining
(`` `hook-stop' ``) makes the associated commands execute every time
execution stops in your program: before breakpoint commands are run,
displays are printed, or the stack frame is printed.

For example, to ignore `SIGALRM` signals while
single-stepping, but treat them normally during normal execution,
you could define:

```
define hook-stop
handle SIGALRM nopass
end

define hook-run
handle SIGALRM pass
end

define hook-continue
handle SIGLARM pass
end
```

As a further example, to hook at the begining and end of the `echo`
command, and to add extra text to the beginning and end of the message,
you could define:

```
define hook-echo
echo <<<---
end

define hookpost-echo
echo --->>>\n
end

(gdb) echo Hello World
<<<---Hello World--->>>
(gdb)
```

You can define a hook for any single-word command in GDB, but
not for command aliases; you should define a hook for the basic command
name, e.g. `backtrace` rather than `bt`.
If an error occurs during the execution of your hook, execution of
GDB commands stops and GDB issues a prompt
(before the command that you actually typed had a chance to run).

If you try to define a hook which does not match any known command, you
get a warning from the `define` command.

## [Command files](Debugging%20with%20GDB.md#apple-krhugmrsgy)

A command file for GDB is a text file made of lines that are
GDB commands. Comments (lines starting with `#`) may
also be included. An empty line in a command file does nothing; it
does not mean to repeat the last command, as it would from the
terminal.

You can request the execution of a command file with the `source`
command:

**`source filename`**
: 
Execute the command file filename.

The lines in a command file are executed sequentially. They are not
printed as they are executed. An error in any command terminates
execution of the command file and control is returned to the console.

Commands that would ask for confirmation if used interactively proceed
without asking when used in a command file. Many GDB commands that
normally print messages to say what they are doing omit the messages
when called from command files.

GDB also accepts command input from standard input. In this
mode, normal output goes to standard output and error output goes to
standard error. Errors in a command file supplied on standard input do
not terminate execution of the command file--execution continues with
the next command.

```
gdb < cmds > log 2>&1
```

(The syntax above will vary depending on the shell used.) This example
will execute commands from the file `cmds'. All output and errors
would be directed to `log'.

## [Commands for controlled output](Debugging%20with%20GDB.md#apple-krhugmrsg4)

During the execution of a command file or a user-defined command, normal
GDB output is suppressed; the only output that appears is what is
explicitly printed by the commands in the definition. This section
describes three commands useful for generating exactly the output you
want.

**`echo text`**
: 
Print text. Nonprinting characters can be included in
text using C escape sequences, such as `` `\n' `` to print a
newline. __No newline is printed unless you specify one.__
In addition to the standard C escape sequences, a backslash followed
by a space stands for a space. This is useful for displaying a
string with spaces at the beginning or the end, since leading and
trailing spaces are otherwise trimmed from all arguments.
To print `` ` and foo = ' ``, use the command
`` `echo \ and foo = \ ' ``.
A backslash at the end of text can be used, as in C, to continue
the command onto subsequent lines. For example,

```
echo This is some text\n\
which is continued\n\
onto several lines.\n
```

produces the same output as

```
echo This is some text\n
echo which is continued\n
echo onto several lines.\n
```


**`output expression`**
: Print the value of expression and nothing but that value: no
newlines, no `` `$nn = ' ``. The value is not entered in the
value history either. See section [Expressions](Examining%20Data.md#apple-kncugnjx), for more information
on expressions.

**`output/fmt expression`**
: Print the value of expression in format fmt. You can use
the same formats as for `print`. See section [Output formats](Examining%20Data.md#apple-kncugnrq), for more information.

**`printf string, expressions...`**
: Print the values of the expressions under the control of
string. The expressions are separated by commas and may be
either numbers or pointers. Their values are printed as specified by
string, exactly as if your program were to execute the C
subroutine

```
printf (string, expressions...);
```

For example, you can print two values in hex like this:

```
printf "foo, bar-foo = 0x%x, 0x%x\n", foo, bar-foo
```

The only backslash-escape sequences that you can use in the format
string are the simple ones that consist of backslash followed by a
letter.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Controlling%20GDB.md), [next](Command%20Interpreters.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
