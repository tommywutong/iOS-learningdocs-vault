---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_26.html
archived_at: '2026-07-15T07:31:03.400109Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](The%20GDB-MI%20Interface.md), [next](Reporting%20Bugs%20in%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [GDB Annotations](Debugging%20with%20GDB.md#apple-krhugmrvhe)

This chapter describes annotations in GDB. Annotations were
designed to interface GDB to graphical user interfaces or other
similar programs which want to interact with GDB at a
relatively high level.

The annotation mechanism has largely been superseeded by GDB/MI
(see section [The GDB/MI Interface](The%20GDB-MI%20Interface.md#apple-kncugmrtgy)).

## [What is an Annotation?](Debugging%20with%20GDB.md#apple-krhugmrwga)

Annotations start with a newline character, two `` `control-z' ``
characters, and the name of the annotation. If there is no additional
information associated with this annotation, the name of the annotation
is followed immediately by a newline. If there is additional
information, the name of the annotation is followed by a space, the
additional information, and a newline. The additional information
cannot contain newline characters.

Any output not beginning with a newline and two `` `control-z' ``
characters denotes literal output from GDB. Currently there is
no need for GDB to output a newline followed by two
`` `control-z' `` characters, but if there was such a need, the
annotations could be extended with an `` `escape' `` annotation which
means those three characters as output.

The annotation level, which is specified using the
@option{--annotate} command line option (see section [Choosing modes](Getting%20In%20and%20Out%20of%20GDB.md#apple-kncugoi)), controls
how much information GDB prints together with its prompt,
values of expressions, source lines, and other types of output. Level 0
is for no anntations, level 1 is for use when GDB is run as a
subprocess of GNU Emacs, level 3 is the maximum annotation suitable
for programs that control GDB, and level 2 annotations have
been made obsolete (see section `Limitations of the Annotation Interface' in GDB's Obsolete Annotations).

**`set annotate level`**
: 
The GDB command `set annotate` sets the level of
annotations to the specified level.

**`show annotate`**
: 
Show the current annotation level.

This chapter describes level 3 annotations.

A simple example of starting up GDB with annotations is:

```
$ gdb --annotate=3
GNU gdb 6.0
Copyright 2003 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License,
and you are welcome to change it and/or distribute copies of it
under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty"
for details.
This GDB was configured as "i386-pc-linux-gnu"

^Z^Zpre-prompt
(gdb)
^Z^Zprompt
quit

^Z^Zpost-prompt
$
```

Here `` `quit' `` is input to GDB; the rest is output from
GDB. The three lines beginning `` `^Z^Z' `` (where `` `^Z' ``
denotes a `` `control-z' `` character) are annotations; the rest is
output from GDB.

## [Annotation for GDB Input](Debugging%20with%20GDB.md#apple-krhugmrwge)

When GDB prompts for input, it annotates this fact so it is possible
to know when to send output, when the output from a given command is
over, etc.

Different kinds of input each have a different __input type__. Each
input type has three annotations: a `pre-` annotation, which
denotes the beginning of any prompt which is being output, a plain
annotation, which denotes the end of the prompt, and then a `post-`
annotation which denotes the end of any echo which may (or may not) be
associated with the input. For example, the `prompt` input type
features the following annotations:

```
^Z^Zpre-prompt
^Z^Zprompt
^Z^Zpost-prompt
```

The input types are

**`prompt`**
: 

When GDB is prompting for a command (the main GDB prompt).

**`commands`**
: When GDB prompts for a set of commands, like in the `commands`
command. The annotations are repeated for each command which is input.

**`overload-choice`**
: When GDB wants the user to select between various overloaded functions.

**`query`**
: When GDB wants the user to confirm a potentially dangerous operation.

**`prompt-for-continue`**
: When GDB is asking the user to press return to continue. Note: Don't
expect this to work well; instead use `set height 0` to disable
prompting. This is because the counting of lines is buggy in the
presence of annotations.

## [Errors](Debugging%20with%20GDB.md#apple-krhugmrwgi)


```
^Z^Zquit
```

This annotation occurs right before GDB responds to an interrupt.


```
^Z^Zerror
```

This annotation occurs right before GDB responds to an error.

Quit and error annotations indicate that any annotations which GDB was
in the middle of may end abruptly. For example, if a
`value-history-begin` annotation is followed by a `error`, one
cannot expect to receive the matching `value-history-end`. One
cannot expect not to receive it either, however; an error annotation
does not necessarily mean that GDB is immediately returning all the way
to the top level.

A quit or error annotation may be preceded by

```
^Z^Zerror-begin
```

Any output between that and the quit or error annotation is the error
message.

Warning messages are not yet annotated.

## [Invalidation Notices](Debugging%20with%20GDB.md#apple-krhugmrwgm)

The following annotations say that certain pieces of state may have
changed.

**`^Z^Zframes-invalid`**
: 
The frames (for example, output from the `backtrace` command) may
have changed.

**`^Z^Zbreakpoints-invalid`**
: The breakpoints may have changed. For example, the user just added or
deleted a breakpoint.

## [Running the Program](Debugging%20with%20GDB.md#apple-krhugmrwgq)

When the program starts executing due to a GDB command such as
`step` or `continue`,

```
^Z^Zstarting
```

is output. When the program stops,

```
^Z^Zstopped
```

is output. Before the `stopped` annotation, a variety of
annotations describe how the program stopped.

**`^Z^Zexited exit-status`**
: 
The program exited, and exit-status is the exit status (zero for
successful exit, otherwise nonzero).

**`^Z^Zsignalled`**
: The program exited with a signal. After the `^Z^Zsignalled`, the
annotation continues:

```
intro-text
^Z^Zsignal-name
name
^Z^Zsignal-name-end
middle-text
^Z^Zsignal-string
string
^Z^Zsignal-string-end
end-text
```

where name is the name of the signal, such as `SIGILL` or
`SIGSEGV`, and string is the explanation of the signal, such
as `Illegal Instruction` or `Segmentation fault`.
intro-text, middle-text, and end-text are for the
user's benefit and have no particular format.

**`^Z^Zsignal`**
: The syntax of this annotation is just like `signalled`, but GDB is
just saying that the program received the signal, not that it was
terminated with it.

**`^Z^Zbreakpoint number`**
: The program hit breakpoint number number.

**`^Z^Zwatchpoint number`**
: The program hit watchpoint number number.

## [Displaying Source](Debugging%20with%20GDB.md#apple-krhugmrwgu)

The following annotation is used instead of displaying source code:

```
^Z^Zsource filename:line:character:middle:addr
```

where filename is an absolute file name indicating which source
file, line is the line number within that file (where 1 is the
first line in the file), character is the character position
within the file (where 0 is the first character in the file) (for most
debug formats this will necessarily point to the beginning of a line),
middle is `` `middle' `` if addr is in the middle of the
line, or `` `beg' `` if addr is at the beginning of the line, and
addr is the address in the target program associated with the
source which is being displayed. addr is in the form `` `0x' ``
followed by one or more lowercase hex digits (note that this does not
depend on the language).

---

Go to the [first](Summary%20of%20GDB.md), [previous](The%20GDB-MI%20Interface.md), [next](Reporting%20Bugs%20in%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
