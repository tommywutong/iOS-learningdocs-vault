---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_14.html
archived_at: '2026-07-15T07:31:03.232140Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Using%20GDB%20with%20Different%20Languages.md), [next](Altering%20Execution.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Examining the Symbol Table](Debugging%20with%20GDB.md#apple-krhugmjtha)

The commands described in this chapter allow you to inquire about the
symbols (names of variables, functions and types) defined in your
program. This information is inherent in the text of your program and
does not change as your program executes. GDB finds it in your
program's symbol table, in the file indicated when you started GDB
(see section [Choosing files](Getting%20In%20and%20Out%20of%20GDB.md#apple-kncugoa)), or by one of the
file-management commands (see section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4)).

Occasionally, you may need to refer to symbols that contain unusual
characters, which GDB ordinarily treats as word delimiters. The
most frequent case is in referring to static variables in other
source files (see section [Program variables](Examining%20Data.md#apple-kncugnjy)). File names
are recorded in object files as debugging symbols, but GDB would
ordinarily parse a typical file name, like `foo.c', as the three words
`` `foo' `` `` `.' `` `` `c' ``. To allow GDB to recognize
`` `foo.c' `` as a single symbol, enclose it in single quotes; for example,

```
p 'foo.c'::x
```

looks up the value of `x` in the scope of the file `foo.c'.

**`set case-sensitive on`**
: 

**`set case-sensitive off`**
:

**`set case-sensitive auto`**
: Normally, when GDB looks up symbols, it matches their names
with case sensitivity determined by the current source language.
Occasionally, you may wish to control that. The command `set
case-sensitive` lets you do that by specifying `on` for
case-sensitive matches or `off` for case-insensitive ones. If
you specify `auto`, case sensitivity is reset to the default
suitable for the source language. The default is case-sensitive
matches for all languages except for Fortran, for which the default is
case-insensitive matches.

**`show case-sensitive`**
: This command shows the current setting of case sensitivity for symbols
lookups.

**`info address symbol`**
: Describe where the data for symbol is stored. For a register
variable, this says which register it is kept in. For a non-register
local variable, this prints the stack-frame offset at which the variable
is always stored.
Note the contrast with `` `print &symbol' ``, which does not work
at all for a register variable, and for a stack local variable prints
the exact address of the current instantiation of the variable.

**`info symbol addr`**
: Print the name of a symbol which is stored at the address addr.
If no symbol is stored exactly at addr, GDB prints the
nearest symbol and an offset from it:

```
(gdb) info symbol 0x54320
_initialize_vx + 396 in section .text
```

This is the opposite of the `info address` command. You can use
it to find out the name of a variable or a function given its address.

**`whatis expr`**
: Print the data type of expression expr. expr is not
actually evaluated, and any side-effecting operations (such as
assignments or function calls) inside it do not take place.
See section [Expressions](Examining%20Data.md#apple-kncugnjx).

**`whatis`**
: Print the data type of `$`, the last value in the value history.

**`ptype typename`**
: Print a description of data type typename. typename may be
the name of a type, or for C code it may have the form `` `class
class-name' ``, `` `struct struct-tag' ``, `` `union
union-tag' `` or `` `enum enum-tag' ``.

**`ptype expr`**
:

**`ptype`**
: Print a description of the type of expression expr. `ptype`
differs from `whatis` by printing a detailed description, instead
of just the name of the type.
For example, for this variable declaration:

```
struct complex {double real; double imag;} v;
```

the two commands give this output:

```
(gdb) whatis v
type = struct complex
(gdb) ptype v
type = struct complex {
    double real;
    double imag;
}
```

As with `whatis`, using `ptype` without an argument refers to
the type of `$`, the last value in the value history.

**`info types regexp`**
:

**`info types`**
: Print a brief description of all types whose names match the regular
expression regexp (or all types in your program, if you supply
no argument). Each complete typename is matched as though it were a
complete line; thus, `` `i type value' `` gives information on all
types in your program whose names include the string `value`, but
`` `i type ^value$' `` gives information only on types whose complete
name is `value`.
This command differs from `ptype` in two ways: first, like
`whatis`, it does not print a detailed description; second, it
lists all source files where a type is defined.

**`info scope location`**
: List all the variables local to a particular scope. This command
accepts a location argument--a function name, a source line, or
an address preceded by a `` `*' ``, and prints all the variables local
to the scope defined by that location. For example:

```
(gdb) info scope command_line_handler
Scope for command_line_handler:
Symbol rl is an argument at stack/frame offset 8, length 4.
Symbol linebuffer is in static storage at address 0x150a18, length 4.
Symbol linelength is in static storage at address 0x150a1c, length 4.
Symbol p is a local variable in register $esi, length 4.
Symbol p1 is a local variable in register $ebx, length 4.
Symbol nline is a local variable in register $edx, length 4.
Symbol repeat is a local variable at frame offset -8, length 4.
```

This command is especially useful for determining what data to collect
during a __trace experiment__, see section [Tracepoint Action Lists](Tracepoints.md#apple-kncugobv).

**`info source`**
: Show information about the current source file--that is, the source file for
the function containing the current point of execution:

- the name of the source file, and the directory containing it,
- the directory it was compiled in,
- its length, in lines,
- which programming language it is written in,
- whether the executable includes debugging information for that file, and
  if so, what format the information is in (e.g., STABS, Dwarf 2, etc.), and
- whether the debugging information includes information about
  preprocessor macros.

**`info sources`**
: Print the names of all source files in your program for which there is
debugging information, organized into two lists: files whose symbols
have already been read, and files whose symbols will be read when needed.

**`info functions`**
: Print the names and data types of all defined functions.

**`info functions regexp`**
: Print the names and data types of all defined functions
whose names contain a match for regular expression regexp.
Thus, `` `info fun step' `` finds all functions whose names
include `step`; `` `info fun ^step' `` finds those whose names
start with `step`. If a function name contains characters
that conflict with the regular expression language (eg.
`` `operator*()' ``), they may be quoted with a backslash.

**`info variables`**
: Print the names and data types of all variables that are declared
outside of functions (i.e. excluding local variables).

**`info variables regexp`**
: Print the names and data types of all variables (except for local
variables) whose names contain a match for regular expression
regexp.

**`info classes`**
:

**`info classes regexp`**
: Display all Objective-C or Objective-C++ classes in your program, or
(with the regexp argument) all those matching a particular regular
expression.

**`info selectors`**
:

**`info selectors regexp`**
: Display all Objective-C selectors in your program, or
(with the regexp argument) all those matching a particular regular

Some systems allow individual object files that make up your program to
be replaced without stopping and restarting your program. For example,
in VxWorks you can simply recompile a defective object file and keep on
running. If you are running on one of these systems, you can allow
GDB to reload the symbols for automatically relinked modules:

**`set symbol-reloading on`**
: 
Replace symbol definitions for the corresponding source file when an
object file with a particular name is seen again.

**`set symbol-reloading off`**
: Do not replace symbol definitions when encountering object files of the
same name more than once. This is the default state; if you are not
running on a system that permits automatic relinking of modules, you
should leave `symbol-reloading` off, since otherwise GDB
may discard symbols when linking large programs, that may contain
several modules (from different directories or libraries) with the same
name.

**`show symbol-reloading`**
: Show the current `on` or `off` setting.

**`set opaque-type-resolution on`**
: Tell GDB to resolve opaque types. An opaque type is a type
declared as a pointer to a `struct`, `class`, or
`union`---for example, `struct MyType *`---that is used in one
source file although the full declaration of `struct MyType` is in
another source file. The default is on.
A change in the setting of this subcommand will not take effect until
the next time symbols for a file are loaded.

**`set opaque-type-resolution off`**
: Tell GDB not to resolve opaque types. In this case, the type
is printed as follows:

```
{<no data fields>}
```


**`show opaque-type-resolution`**
: Show whether opaque types are resolved or not.

**`maint print symbols filename`**
:

**`maint print psymbols filename`**
:

**`maint print msymbols filename`**
: Write a dump of debugging symbol data into the file filename.
These commands are used to debug the GDB symbol-reading code. Only
symbols with debugging data are included. If you use `` `maint print
symbols' ``, GDB includes all the symbols for which it has already
collected full details: that is, filename reflects symbols for
only those files whose symbols GDB has read. You can use the
command `info sources` to find out which files these are. If you
use `` `maint print psymbols' `` instead, the dump shows information about
symbols that GDB only knows partially--that is, symbols defined in
files that GDB has skimmed, but not yet read completely. Finally,
`` `maint print msymbols' `` dumps just the minimal symbol information
required for each object file from which GDB has read some symbols.
See section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4), for a discussion of how
GDB reads symbols (in the description of `symbol-file`).

**`maint info symtabs [ regexp ]`**
:

**`maint info psymtabs [ regexp ]`**
: List the `struct symtab` or `struct partial_symtab`
structures whose names match regexp. If regexp is not
given, list them all. The output includes expressions which you can
copy into a GDB debugging this one to examine a particular
structure in more detail. For example:

```
(gdb) maint info psymtabs dwarf2read
{ objfile /home/gnu/build/gdb/gdb
  ((struct objfile *) 0x82e69d0)
  { psymtab /home/gnu/src/gdb/dwarf2read.c
    ((struct partial_symtab *) 0x8474b10)
    readin no
    fullname (null)
    text addresses 0x814d3c8 -- 0x8158074
    globals (* (struct partial_symbol **) 0x8507a08 @ 9)
    statics (* (struct partial_symbol **) 0x40e95b78 @ 2882)
    dependencies (none)
  }
}
(gdb) maint info symtabs
(gdb)
```

We see that there is one partial symbol table whose filename contains
the string `` `dwarf2read' ``, belonging to the `` `gdb' `` executable;
and we see that GDB has not read in any symtabs yet at all.
If we set a breakpoint on a function, that will cause GDB to
read the symtab for the compilation unit containing that function:

```
(gdb) break dwarf2_psymtab_to_symtab
Breakpoint 1 at 0x814e5da: file /home/gnu/src/gdb/dwarf2read.c,
line 1574.
(gdb) maint info symtabs
{ objfile /home/gnu/build/gdb/gdb
  ((struct objfile *) 0x82e69d0)
  { symtab /home/gnu/src/gdb/dwarf2read.c
    ((struct symtab *) 0x86c1f38)
    dirname (null)
    fullname (null)
    blockvector ((struct blockvector *) 0x86c1bd0) (primary)
    debugformat DWARF 2
  }
}
(gdb)
```

---

Go to the [first](Summary%20of%20GDB.md), [previous](Using%20GDB%20with%20Different%20Languages.md), [next](Altering%20Execution.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
