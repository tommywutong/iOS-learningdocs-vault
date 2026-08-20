---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_8.html
archived_at: '2026-07-15T07:31:03.645008Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Examining%20the%20Stack.md), [next](Examining%20Data.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Examining Source Files](Debugging%20with%20GDB.md#apple-krhugnbz)

GDB can print parts of your program's source, since the debugging
information recorded in the program tells GDB what source files were
used to build it. When your program stops, GDB spontaneously prints
the line where it stopped. Likewise, when you select a stack frame
(see section [Selecting a frame](Examining%20the%20Stack.md#apple-kncugnbx)), GDB prints the line where
execution in that frame has stopped. You can print other portions of
source files by explicit command.

If you use GDB through its GNU Emacs interface, you may
prefer to use Emacs facilities to view source; see section [Using GDB under GNU Emacs](Using%20GDB%20under%20GNU%20Emacs.md#apple-kncugmrtgu).

## [Printing source lines](Debugging%20with%20GDB.md#apple-krhugnjq)

To print lines from a source file, use the `list` command
(abbreviated `l`). By default, ten lines are printed.
There are several ways to specify what part of the file you want to print.

Here are the forms of the `list` command most commonly used:

**`list linenum`**
: Print lines centered around line number linenum in the
current source file.

**`list function`**
: Print lines centered around the beginning of function
function.

**`list`**
: Print more lines. If the last lines printed were printed with a
`list` command, this prints lines following the last lines
printed; however, if the last line printed was a solitary line printed
as part of displaying a stack frame (see section [Examining the Stack](Examining%20the%20Stack.md#apple-kncugnbu)), this prints lines centered around that line.

**`list -`**
: Print lines just before the lines last printed.

By default, GDB prints ten source lines with any of these forms of
the `list` command. You can change this using `set listsize`:

**`set listsize count`**
: 
Make the `list` command display count source lines (unless
the `list` argument explicitly specifies some other number).

**`show listsize`**
: Display the number of lines that `list` prints.

Repeating a `list` command with `RET` discards the argument,
so it is equivalent to typing just `list`. This is more useful
than listing the same lines again. An exception is made for an
argument of `` `-' ``; that argument is preserved in repetition so that
each repetition moves up in the source file.

In general, the `list` command expects you to supply zero, one or two
__linespecs__. Linespecs specify source lines; there are several ways
of writing them, but the effect is always to specify some source line.
Here is a complete description of the possible arguments for `list`:

**`list linespec`**
: Print lines centered around the line specified by linespec.

**`list first,last`**
: Print lines from first to last. Both arguments are
linespecs.

**`list ,last`**
: Print lines ending with last.

**`list first,`**
: Print lines starting with first.

**`list +`**
: Print lines just after the lines last printed.

**`list -`**
: Print lines just before the lines last printed.

**`list`**
: As described in the preceding table.

Here are the ways of specifying a single source line--all the
kinds of linespec.

**`number`**
: Specifies line number of the current source file.
When a `list` command has two linespecs, this refers to
the same source file as the first linespec.

**`+offset`**
: Specifies the line offset lines after the last line printed.
When used as the second linespec in a `list` command that has
two, this specifies the line offset lines down from the
first linespec.

**`-offset`**
: Specifies the line offset lines before the last line printed.

**`filename:number`**
: Specifies line number in the source file filename.

**`function`**
: Specifies the line that begins the body of the function function.
For example: in C, this is the line with the open brace.

**`filename:function`**
: Specifies the line of the open-brace that begins the body of the
function function in the file filename. You only need the
file name with a function name to avoid ambiguity when there are
identically named functions in different source files.

**`*address`**
: Specifies the line containing the program address address.
address may be any expression.

## [Editing source files](Debugging%20with%20GDB.md#apple-krhugnjr)

To edit the lines in a source file, use the `edit` command.
The editing program of your choice
is invoked with the current line set to
the active line in the program.
Alternatively, there are several ways to specify what part of the file you
want to print if you want to see other parts of the program.

Here are the forms of the `edit` command most commonly used:

**`edit`**
: Edit the current source file at the active line number in the program.

**`edit number`**
: Edit the current source file with number as the active line number.

**`edit function`**
: Edit the file containing function at the beginning of its definition.

**`edit filename:number`**
: Specifies line number in the source file filename.

**`edit filename:function`**
: Specifies the line that begins the body of the
function function in the file filename. You only need the
file name with a function name to avoid ambiguity when there are
identically named functions in different source files.

**`edit *address`**
: Specifies the line containing the program address address.
address may be any expression.

### [Choosing your editor](Debugging%20with%20GDB.md#apple-krhugnjs)

You can customize GDB to use any editor you want
[(3)](Debugging%20with%20GDB-2.md#apple-izhu6vbt).
By default, it is `/bin/ex', but you can change this
by setting the environment variable `EDITOR` before using
GDB. For example, to configure GDB to use the
`vi` editor, you could use these commands with the `sh` shell:

```
EDITOR=/usr/bin/vi
export EDITOR
gdb ...
```

or in the `csh` shell,

```
setenv EDITOR /usr/bin/vi
gdb ...
```

## [Searching source files](Debugging%20with%20GDB.md#apple-krhugnjt)

There are two commands for searching through the current source file for a
regular expression.

**`forward-search regexp`**
: 

**`search regexp`**
: The command `` `forward-search regexp' `` checks each line,
starting with the one following the last line listed, for a match for
regexp. It lists the line that is found. You can use the
synonym `` `search regexp' `` or abbreviate the command name as
`fo`.

**`reverse-search regexp`**
: The command `` `reverse-search regexp' `` checks each line, starting
with the one before the last line listed and going backward, for a match
for regexp. It lists the line that is found. You can abbreviate
this command as `rev`.

## [Specifying source directories](Debugging%20with%20GDB.md#apple-krhugnju)

Executable programs sometimes do not record the directories of the source
files from which they were compiled, just the names. Even when they do,
the directories could be moved between the compilation and your debugging
session. GDB has a list of directories to search for source files;
this is called the __source path__. Each time GDB wants a source file,
it tries all the directories in the list, in the order they are present
in the list, until it finds a file with the desired name.

For example, suppose an executable references the file
`/usr/src/foo-1.0/lib/foo.c', and our source path is
`/mnt/cross'. The file is first looked up literally; if this
fails, `/mnt/cross/usr/src/foo-1.0/lib/foo.c' is tried; if this
fails, `/mnt/cross/foo.c' is opened; if this fails, an error
message is printed. GDB does not look up the parts of the
source file name, such as `/mnt/cross/src/foo-1.0/lib/foo.c'.
Likewise, the subdirectories of the source path are not searched: if
the source path is `/mnt/cross', and the binary refers to
`foo.c', GDB would not find it under
`/mnt/cross/usr/src/foo-1.0/lib'.

Plain file names, relative file names with leading directories, file
names containing dots, etc. are all treated as described above; for
instance, if the source path is `/mnt/cross', and the source file
is recorded as `../lib/foo.c', GDB would first try
`../lib/foo.c', then `/mnt/cross/../lib/foo.c', and after
that---`/mnt/cross/foo.c'.

Note that the executable search path is _not_ used to locate the
source files. Neither is the current working directory, unless it
happens to be in the source path.

Whenever you reset or rearrange the source path, GDB clears out
any information it has cached about where source files are found and where
each line is in the file.

When you start GDB, its source path includes only `` `cdir' ``
and `` `cwd' ``, in that order.
To add other directories, use the `directory` command.

**`directory dirname ...`**
:

**`dir dirname ...`**
: Add directory dirname to the front of the source path. Several
directory names may be given to this command, separated by `` `:' ``
(`` `;' `` on MS-DOS and MS-Windows, where `` `:' `` usually appears as
part of absolute file names) or
whitespace. You may specify a directory that is already in the source
path; this moves it forward, so GDB searches it sooner.

You can use the string `` `$cdir' `` to refer to the compilation
directory (if one is recorded), and `` `$cwd' `` to refer to the current
working directory. `` `$cwd' `` is not the same as `` `.' ``---the former
tracks the current working directory as it changes during your GDB
session, while the latter is immediately expanded to the current
directory at the time you add an entry to the source path.

**`directory`**
: Reset the source path to empty again. This requires confirmation.

**`show directories`**
: 
Print the source path: show which directories it contains.

If your source path is cluttered with directories that are no longer of
interest, GDB may sometimes cause confusion by finding the wrong
versions of source. You can correct the situation as follows:

1. Use `directory` with no argument to reset the source path to empty.
2. Use `directory` with suitable arguments to reinstall the
   directories you want in the source path. You can add all the
   directories in one command.

## [Source and machine code](Debugging%20with%20GDB.md#apple-krhugnjv)

You can use the command `info line` to map source lines to program
addresses (and vice versa), and the command `disassemble` to display
a range of addresses as machine instructions. When run under GNU Emacs
mode, the `info line` command causes the arrow to point to the
line specified. Also, `info line` prints addresses in symbolic form as
well as hex.

**`info line linespec`**
: 
Print the starting and ending addresses of the compiled code for
source line linespec. You can specify source lines in any of
the ways understood by the `list` command (see section [Printing source lines](#apple-kncugnjq)).

For example, we can use `info line` to discover the location of
the object code for the first line of function
`m4_changequote`:

```
(gdb) info line m4_changequote
Line 895 of "builtin.c" starts at pc 0x634c and ends at 0x6350.
```


We can also inquire (using `*addr` as the form for
linespec) what source line covers a particular address:

```
(gdb) info line *0x63ff
Line 926 of "builtin.c" starts at pc 0x63e4 and ends at 0x6404.
```


After `info line`, the default address for the `x` command
is changed to the starting address of the line, so that `` `x/i' `` is
sufficient to begin examining the machine code (see section [Examining memory](Examining%20Data.md#apple-kncugnrr)). Also, this address is saved as the value of the
convenience variable `$_` (see section [Convenience variables](Examining%20Data.md#apple-kncugnrv)).

**`disassemble`**
: 

This specialized command dumps a range of memory as machine
instructions. The default memory range is the function surrounding the
program counter of the selected frame. A single argument to this
command is a program counter value; GDB dumps the function
surrounding this value. Two arguments specify a range of addresses
(first inclusive, second exclusive) to dump.

The following example shows the disassembly of a range of addresses of
HP PA-RISC 2.0 code:

```
(gdb) disas 0x32c4 0x32e4
Dump of assembler code from 0x32c4 to 0x32e4:
0x32c4 <main+204>:      addil 0,dp
0x32c8 <main+208>:      ldw 0x22c(sr0,r1),r26
0x32cc <main+212>:      ldil 0x3000,r31
0x32d0 <main+216>:      ble 0x3f8(sr4,r31)
0x32d4 <main+220>:      ldo 0(r31),rp
0x32d8 <main+224>:      addil -0x800,dp
0x32dc <main+228>:      ldo 0x588(r1),r26
0x32e0 <main+232>:      ldil 0x3000,r31
End of assembler dump.
```

Some architectures have more than one commonly-used set of instruction
mnemonics or other syntax.

For programs that were dynamically linked and use shared libraries,
instructions that call functions or branch to locations in the shared
libraries might show a seemingly bogus location--it's actually a
location of the relocation table. On some architectures, GDB
might be able to resolve these to actual function names.

**`set disassembly-flavor instruction-set`**
: 

Select the instruction set to use when disassembling the
program via the `disassemble` or `x/i` commands.
Currently this command is only defined for the Intel x86 family. You
can set instruction-set to either `intel` or `att`.
The default is `att`, the AT&T flavor used by default by Unix
assemblers for x86-based targets.

**`show disassembly-flavor`**
: Show the current setting of the disassembly flavor.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Examining%20the%20Stack.md), [next](Examining%20Data.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
