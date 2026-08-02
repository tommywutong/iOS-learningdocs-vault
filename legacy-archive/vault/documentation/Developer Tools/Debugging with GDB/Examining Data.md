---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_9.html
archived_at: '2026-07-15T07:31:03.654428Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Examining%20Source%20Files.md), [next](C%20Preprocessor%20Macros.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Examining Data](Debugging%20with%20GDB.md#apple-krhugnjw)

The usual way to examine data in your program is with the `print`
command (abbreviated `p`), or its synonym `inspect`. It
evaluates and prints the value of an expression of the language your
program is written in (see section [Using GDB with Different Languages](Using%20GDB%20with%20Different%20Languages.md#apple-kncugojy)).

**`print expr`**
:

**`print /f expr`**
: expr is an expression (in the source language). By default the
value of expr is printed in a format appropriate to its data type;
you can choose a different format by specifying `` `/f' ``, where
f is a letter specifying the format; see section [Output formats](#apple-kncugnrq).

**`print`**
:

**`print /f`**
: 
If you omit expr, GDB displays the last value again (from the
__value history__; see section [Value history](#apple-kncugnru)). This allows you to
conveniently inspect the same value in an alternative format.

A more low-level way of examining data is with the `x` command.
It examines data in memory at a specified address and prints it in a
specified format. See section [Examining memory](#apple-kncugnrr).

If you are interested in information about types, or about how the
fields of a struct or a class are declared, use the `ptype exp`
command rather than `print`. See section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha).

## [Expressions](Debugging%20with%20GDB.md#apple-krhugnjx)

`print` and many other GDB commands accept an expression and
compute its value. Any kind of constant, variable or operator defined
by the programming language you are using is valid in an expression in
GDB. This includes conditional expressions, function calls,
casts, and string constants. It also includes preprocessor macros, if
you compiled your program to include this information; see
section [Compiling for debugging](Running%20Programs%20Under%20GDB.md#apple-kncugmjz).

GDB supports array constants in expressions input by
the user. The syntax is {element, element...}. For example,
you can use the command `print {1, 2, 3}` to build up an array in
memory that is `malloc`ed in the target program.

Because C is so widespread, most of the expressions shown in examples in
this manual are in C. See section [Using GDB with Different Languages](Using%20GDB%20with%20Different%20Languages.md#apple-kncugojy), for information on how to use expressions in other
languages.

In this section, we discuss operators that you can use in GDB
expressions regardless of your programming language.

Casts are supported in all languages, not just in C, because it is so
useful to cast a number into a pointer in order to examine a structure
at that address in memory.

GDB supports these operators, in addition to those common
to programming languages:

**`@`**
: `` `@' `` is a binary operator for treating parts of memory as arrays.
See section [Artificial arrays](#apple-kncugnjz), for more information.

**`::`**
: `` `::' `` allows you to specify a variable in terms of the file or
function where it is defined. See section [Program variables](#apple-kncugnjy).

**`{type} addr`**
: Refers to an object of type type stored at address addr in
memory. addr may be any expression whose value is an integer or
pointer (but parentheses are required around binary operators, just as in
a cast). This construct is allowed regardless of what kind of data is
normally supposed to reside at addr.

## [Program variables](Debugging%20with%20GDB.md#apple-krhugnjy)

The most common kind of expression to use is the name of a variable
in your program.

Variables in expressions are understood in the selected stack frame
(see section [Selecting a frame](Examining%20the%20Stack.md#apple-kncugnbx)); they must be either:

- global (or file-static)

or

- visible according to the scope rules of the
  programming language from the point of execution in that frame

This means that in the function

```
foo (a)
     int a;
{
  bar (a);
  {
    int b = test ();
    bar (b);
  }
}
```

you can examine and use the variable `a` whenever your program is
executing within the function `foo`, but you can only use or
examine the variable `b` while your program is executing inside
the block where `b` is declared.

There is an exception: you can refer to a variable or function whose
scope is a single source file even if the current execution point is not
in this file. But it is possible to have more than one such variable or
function with the same name (in different source files). If that
happens, referring to that name has unpredictable effects. If you wish,
you can specify a static variable in a particular function or file,
using the colon-colon (`::`) notation:


```
file::variable
function::variable
```

Here file or function is the name of the context for the
static variable. In the case of file names, you can use quotes to
make sure GDB parses the file name as a single word--for example,
to print a global value of `x` defined in `f2.c':

```
(gdb) p 'f2.c'::x
```


This use of `` `::' `` is very rarely in conflict with the very similar
use of the same notation in C++. GDB also supports use of the C++
scope resolution operator in GDB expressions.

> _Warning:_ Occasionally, a local variable may appear to have the
> wrong value at certain points in a function--just after entry to a new
> scope, and just before exit.

You may see this problem when you are stepping by machine instructions.
This is because, on most machines, it takes more than one instruction to
set up a stack frame (including local variable definitions); if you are
stepping by machine instructions, variables may appear to have the wrong
values until the stack frame is completely built. On exit, it usually
also takes more than one machine instruction to destroy a stack frame;
after you begin stepping through that group of instructions, local
variable definitions may be gone.

This may also happen when the compiler does significant optimizations.
To be sure of always seeing accurate values, turn off all optimization
when compiling.

Another possible effect of compiler optimizations is to optimize
unused variables out of existence, or assign variables to registers (as
opposed to memory addresses). Depending on the support for such cases
offered by the debug info format used by the compiler, GDB
might not be able to display values for such local variables. If that
happens, GDB will print a message like this:

```
No symbol "foo" in current context.
```

To solve such problems, either recompile without optimizations, or use a
different debug info format, if the compiler supports several such
formats. For example, GCC, the GNU C/C++ compiler,
usually supports the @option{-gstabs+} option. @option{-gstabs+}
produces debug info in a format that is superior to formats such as
COFF. You may be able to use DWARF 2 (@option{-gdwarf-2}), which is also
an effective form for debug info. See section `Options for Debugging Your Program or GNU CC' in Using GNU CC.

See section [C and C++](Using%20GDB%20with%20Different%20Languages.md#apple-kncugmjqha), for more info about debug info formats
that are best suited to C++ programs.

## [Artificial arrays](Debugging%20with%20GDB.md#apple-krhugnjz)

It is often useful to print out several successive objects of the
same type in memory; a section of an array, or an array of
dynamically determined size for which only a pointer exists in the
program.

You can do this by referring to a contiguous span of memory as an
__artificial array__, using the binary operator `` `@' ``. The left
operand of `` `@' `` should be the first element of the desired array
and be an individual object. The right operand should be the desired length
of the array. The result is an array value whose elements are all of
the type of the left argument. The first element is actually the left
argument; the second element comes from bytes of memory immediately
following those that hold the first element, and so on. Here is an
example. If a program says

```
int *array = (int *) malloc (len * sizeof (int));
```

you can print the contents of `array` with

```
p *array@len
```

The left operand of `` `@' `` must reside in memory. Array values made
with `` `@' `` in this way behave just like other arrays in terms of
subscripting, and are coerced to pointers when used in expressions.
Artificial arrays most often appear in expressions via the value history
(see section [Value history](#apple-kncugnru)), after printing one out.

Another way to create an artificial array is to use a cast.
This re-interprets a value as if it were an array.
The value need not be in memory:

```
(gdb) p/x (short[2])0x12345678
$1 = {0x1234, 0x5678}
```

As a convenience, if you leave the array length out (as in
`` `(type[])value' ``) GDB calculates the size to fill
the value (as `` `sizeof(value)/sizeof(type)' ``:

```
(gdb) p/x (short[])0x12345678
$2 = {0x1234, 0x5678}
```

Sometimes the artificial array mechanism is not quite enough; in
moderately complex data structures, the elements of interest may not
actually be adjacent--for example, if you are interested in the values
of pointers in an array. One useful work-around in this situation is
to use a convenience variable (see section [Convenience variables](#apple-kncugnrv)) as a counter in an expression that prints the first
interesting value, and then repeat that expression via `RET`. For
instance, suppose you have an array `dtab` of pointers to
structures, and you are interested in the values of a field `fv`
in each structure. Here is an example of what you might type:

```swift
set $i = 0
p dtab[$i++]->fv
RET
RET
...
```

## [Output formats](Debugging%20with%20GDB.md#apple-krhugnrq)

By default, GDB prints a value according to its data type. Sometimes
this is not what you want. For example, you might want to print a number
in hex, or a pointer in decimal. Or you might want to view data in memory
at a certain address as a character string or as an instruction. To do
these things, specify an __output format__ when you print a value.

The simplest use of output formats is to say how to print a value
already computed. This is done by starting the arguments of the
`print` command with a slash and a format letter. The format
letters supported are:

**`x`**
: Regard the bits of the value as an integer, and print the integer in
hexadecimal.

**`d`**
: Print as integer in signed decimal.

**`u`**
: Print as integer in unsigned decimal.

**`o`**
: Print as integer in octal.

**`t`**
: Print as integer in binary. The letter `` `t' `` stands for "two".
[(4)](Debugging%20with%20GDB-2.md#apple-izhu6vbu)

**`a`**
: 

Print as an address, both absolute in hexadecimal and as an offset from
the nearest preceding symbol. You can use this format used to discover
where (in what function) an unknown address is located:

```
(gdb) p/a 0x54320
$3 = 0x54320 <_initialize_vx+396>
```

The command `info symbol 0x54320` yields similar results.
See section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha).

**`c`**
: Regard as an integer and print it as a character constant. This
prints both the numerical value and its character representation. The
character representation is replaced with the octal escape `` `\nnn' ``
for characters outside the 7-bit ASCII range.

**`f`**
: Regard the bits of the value as a floating point number and print
using typical floating point syntax.

For example, to print the program counter in hex (see section [Registers](#apple-kncugnrw)), type

```
p/x $pc
```

Note that no space is required before the slash; this is because command
names in GDB cannot contain a slash.

To reprint the last value in the value history with a different format,
you can use the `print` command with just a format and no
expression. For example, `` `p/x' `` reprints the last value in hex.

## [Examining memory](Debugging%20with%20GDB.md#apple-krhugnrr)

You can use the command `x` (for "examine") to examine memory in
any of several formats, independently of your program's data types.

**`x/nfu addr`**
: 

**`x addr`**
:

**`x`**
: Use the `x` command to examine memory.

n, f, and u are all optional parameters that specify how
much memory to display and how to format it; addr is an
expression giving the address where you want to start displaying memory.
If you use defaults for nfu, you need not type the slash `` `/' ``.
Several commands set convenient defaults for addr.

**n, the repeat count**
: The repeat count is a decimal integer; the default is 1. It specifies
how much memory (counting by units u) to display.

**f, the display format**
: The display format is one of the formats used by `print`
(`` `x' ``, `` `d' ``, `` `u' ``, `` `o' ``, `` `t' ``, `` `a' ``, `` `c' ``,
`` `f' ``), and in addition `` `s' `` (for null-terminated strings) and
`` `i' `` (for machine instructions). The default is `` `x' ``
(hexadecimal) initially. The default changes each time you use either
`x` or `print`.

**u, the unit size**
: The unit size is any of

**`b`**
: Bytes.

**`h`**
: Halfwords (two bytes).

**`w`**
: Words (four bytes). This is the initial default.

**`g`**
: Giant words (eight bytes).

Each time you specify a unit size with `x`, that size becomes the
default unit the next time you use `x`. (For the `` `s' `` and
`` `i' `` formats, the unit size is ignored and is normally not written.)

**addr, starting display address**
: addr is the address where you want GDB to begin displaying
memory. The expression need not have a pointer value (though it may);
it is always interpreted as an integer address of a byte of memory.
See section [Expressions](#apple-kncugnjx), for more information on expressions. The default for
addr is usually just after the last address examined--but several
other commands also set the default address: `info breakpoints` (to
the address of the last breakpoint listed), `info line` (to the
starting address of a line), and `print` (if you use it to display
a value from memory).

For example, `` `x/3uh 0x54320' `` is a request to display three halfwords
(`h`) of memory, formatted as unsigned decimal integers (`` `u' ``),
starting at address `0x54320`. `` `x/4xw $sp' `` prints the four
words (`` `w' ``) of memory above the stack pointer (here, `` `$sp' ``;
see section [Registers](#apple-kncugnrw)) in hexadecimal (`` `x' ``).

Since the letters indicating unit sizes are all distinct from the
letters specifying output formats, you do not have to remember whether
unit size or format comes first; either order works. The output
specifications `` `4xw' `` and `` `4wx' `` mean exactly the same thing.
(However, the count n must come first; `` `wx4' `` does not work.)

Even though the unit size u is ignored for the formats `` `s' ``
and `` `i' ``, you might still want to use a count n; for example,
`` `3i' `` specifies that you want to see three machine instructions,
including any operands. The command `disassemble` gives an
alternative way of inspecting machine instructions; see section [Source and machine code](Examining%20Source%20Files.md#apple-kncugnjv).

All the defaults for the arguments to `x` are designed to make it
easy to continue scanning memory with minimal specifications each time
you use `x`. For example, after you have inspected three machine
instructions with `` `x/3i addr' ``, you can inspect the next seven
with just `` `x/7' ``. If you use `RET` to repeat the `x` command,
the repeat count n is used again; the other arguments default as
for successive uses of `x`.

The addresses and contents printed by the `x` command are not saved
in the value history because there is often too much of them and they
would get in the way. Instead, GDB makes these values available for
subsequent use in expressions as values of the convenience variables
`$_` and `$__`. After an `x` command, the last address
examined is available for use in expressions in the convenience variable
`$_`. The contents of that address, as examined, are available in
the convenience variable `$__`.

If the `x` command has a repeat count, the address and contents saved
are from the last memory unit printed; this is not the same as the last
address printed if several units were printed on the last line of output.

When you are debugging a program running on a remote target machine
(see section [Remote debugging](Specifying%20a%20Debugging%20Target.md#apple-kncugmjvgq)), you may wish to verify the program's image in the
remote machine's memory against the executable file you downloaded to
the target. The `compare-sections` command is provided for such
situations.

**`compare-sections [section-name]`**
: 
Compare the data of a loadable section section-name in the
executable file of the program being debugged with the same section in
the remote machine's memory, and report any mismatches. With no
arguments, compares all loadable sections. This command's
availability depends on the target's support for the `"qCRC"`
remote request.

## [Automatic display](Debugging%20with%20GDB.md#apple-krhugnrs)

If you find that you want to print the value of an expression frequently
(to see how it changes), you might want to add it to the __automatic
display list__ so that GDB prints its value each time your program stops.
Each expression added to the list is given a number to identify it;
to remove an expression from the list, you specify that number.
The automatic display looks like this:

```
2: foo = 38
3: bar[5] = (struct hack *) 0x3804
```

This display shows item numbers, expressions and their current values. As with
displays you request manually using `x` or `print`, you can
specify the output format you prefer; in fact, `display` decides
whether to use `print` or `x` depending on how elaborate your
format specification is--it uses `x` if you specify a unit size,
or one of the two formats (`` `i' `` and `` `s' ``) that are only
supported by `x`; otherwise it uses `print`.

**`display expr`**
: 
Add the expression expr to the list of expressions to display
each time your program stops. See section [Expressions](#apple-kncugnjx).
`display` does not repeat if you press `RET` again after using it.

**`display/fmt expr`**
: For fmt specifying only a display format and not a size or
count, add the expression expr to the auto-display list but
arrange to display it each time in the specified format fmt.
See section [Output formats](#apple-kncugnrq).

**`display/fmt addr`**
: For fmt `` `i' `` or `` `s' ``, or including a unit-size or a
number of units, add the expression addr as a memory address to
be examined each time your program stops. Examining means in effect
doing `` `x/fmt addr' ``. See section [Examining memory](#apple-kncugnrr).

For example, `` `display/i $pc' `` can be helpful, to see the machine
instruction about to be executed each time execution stops (`` `$pc' ``
is a common name for the program counter; see section [Registers](#apple-kncugnrw)).

**`undisplay dnums...`**
: 

**`delete display dnums...`**
: Remove item numbers dnums from the list of expressions to display.
`undisplay` does not repeat if you press `RET` after using it.
(Otherwise you would just get the error `` `No display number ...' ``.)

**`disable display dnums...`**
: Disable the display of item numbers dnums. A disabled display
item is not printed automatically, but is not forgotten. It may be
enabled again later.

**`enable display dnums...`**
: Enable display of item numbers dnums. It becomes effective once
again in auto display of its expression, until you specify otherwise.

**`display`**
: Display the current values of the expressions on the list, just as is
done when your program stops.

**`info display`**
: Print the list of expressions previously set up to display
automatically, each one with its item number, but without showing the
values. This includes disabled expressions, which are marked as such.
It also includes expressions which would not be displayed right now
because they refer to automatic variables not currently available.

If a display expression refers to local variables, then it does not make
sense outside the lexical context for which it was set up. Such an
expression is disabled when execution enters a context where one of its
variables is not defined. For example, if you give the command
`display last_char` while inside a function with an argument
`last_char`, GDB displays this argument while your program
continues to stop inside that function. When it stops elsewhere--where
there is no variable `last_char`---the display is disabled
automatically. The next time your program stops where `last_char`
is meaningful, you can enable the display expression once again.

## [Print settings](Debugging%20with%20GDB.md#apple-krhugnrt)

GDB provides the following ways to control how arrays, structures,
and symbols are printed.

These settings are useful for debugging programs in any language:

**`set print address`**
: 

**`set print address on`**
: 
GDB prints memory addresses showing the location of stack
traces, structure values, pointer values, breakpoints, and so forth,
even when it also displays the contents of those addresses. The default
is `on`. For example, this is what a stack frame display looks like with
`set print address on`:

```
(gdb) f
#0  set_quotes (lq=0x34c78 "<<", rq=0x34c88 ">>")
    at input.c:530
530         if (lquote != def_lquote)
```

**`set print address off`**
: Do not print addresses when displaying their contents. For example,
this is the same stack frame displayed with `set print address off`:

```
(gdb) set print addr off
(gdb) f
#0  set_quotes (lq="<<", rq=">>") at input.c:530
530         if (lquote != def_lquote)
```

You can use `` `set print address off' `` to eliminate all machine
dependent displays from the GDB interface. For example, with
`print address off`, you should get the same text for backtraces on
all machines--whether or not they involve pointer arguments.

**`show print address`**
: Show whether or not addresses are to be printed.

When GDB prints a symbolic address, it normally prints the
closest earlier symbol plus an offset. If that symbol does not uniquely
identify the address (for example, it is a name whose scope is a single
source file), you may need to clarify. One way to do this is with
`info line`, for example `` `info line *0x4537' ``. Alternately,
you can set GDB to print the source file and line number when
it prints a symbolic address:

**`set print symbol-filename on`**
: 

Tell GDB to print the source file name and line number of a
symbol in the symbolic form of an address.

**`set print symbol-filename off`**
: Do not print source file name and line number of a symbol. This is the
default.

**`show print symbol-filename`**
: Show whether or not GDB will print the source file name and
line number of a symbol in the symbolic form of an address.

Another situation where it is helpful to show symbol filenames and line
numbers is when disassembling code; GDB shows you the line
number and source file that corresponds to each instruction.

Also, you may wish to see the symbolic form only if the address being
printed is reasonably close to the closest earlier symbol:

**`set print max-symbolic-offset max-offset`**
: 
Tell GDB to only display the symbolic form of an address if the
offset between the closest earlier symbol and the address is less than
max-offset. The default is 0, which tells GDB
to always print the symbolic form of an address if any symbol precedes it.

**`show print max-symbolic-offset`**
: Ask how large the maximum offset is that GDB prints in a
symbolic address.

If you have a pointer and you are not sure where it points, try
`` `set print symbol-filename on' ``. Then you can determine the name
and source file location of the variable where it points, using
`` `p/a pointer' ``. This interprets the address in symbolic form.
For example, here GDB shows that a variable `ptt` points
at another variable `t`, defined in `hi2.c':

```
(gdb) set print symbol-filename on
(gdb) p/a ptt
$4 = 0xe008 <t in hi2.c>
```

> _Warning:_ For pointers that point to a local variable, `` `p/a' ``
> does not show the symbol name and filename of the referent, even with
> the appropriate `set print` options turned on.

Other settings control how different kinds of objects are printed:

**`set print array`**
:

**`set print array on`**
: 
Pretty print arrays. This format is more convenient to read,
but uses more space. The default is off.

**`set print array off`**
: Return to compressed format for arrays.

**`show print array`**
: Show whether compressed or pretty format is selected for displaying
arrays.

**`set print elements number-of-elements`**
: 

Set a limit on how many elements of an array GDB will print.
If GDB is printing a large array, it stops printing after it has
printed the number of elements set by the `set print elements` command.
This limit also applies to the display of strings.
When GDB starts, this limit is set to 200.
Setting number-of-elements to zero means that the printing is unlimited.

**`show print elements`**
: Display the number of elements of a large array that GDB will print.
If the number is 0, then the printing is unlimited.

**`set print repeats`**
: 
Set the threshold for suppressing display of repeated array
elelments. When the number of consecutive identical elements of an
array exceeds the threshold, GDB prints the string
`"<repeats n times>"`, where n is the number of
identical repetitions, instead of displaying the identical elements
themselves. Setting the threshold to zero will cause all elements to
be individually printed. The default threshold is 10.

**`show print repeats`**
: Display the current threshold for printing repeated identical
elements.

**`set print null-stop`**
: 
Cause GDB to stop printing the characters of an array when the first
NULL is encountered. This is useful when large arrays actually
contain only short strings.
The default is off.

**`show print null-stop`**
: Show whether GDB stops printing an array on the first
NULL character.

**`set print pretty on`**
: 

Cause GDB to print structures in an indented format with one member
per line, like this:

```
$1 = {
  next = 0x0,
  flags = {
    sweet = 1,
    sour = 1
  },
  meat = 0x54 "Pork"
}
```

**`set print pretty off`**
: Cause GDB to print structures in a compact format, like this:

```
$1 = {next = 0x0, flags = {sweet = 1, sour = 1}, \
meat = 0x54 "Pork"}
```

This is the default format.

**`show print pretty`**
: Show which format GDB is using to print structures.

**`set print sevenbit-strings on`**
: 

Print using only seven-bit characters; if this option is set,
GDB displays any eight-bit characters (in strings or
character values) using the notation `\`nnn. This setting is
best if you are working in English (ASCII) and you use the
high-order bit of characters as a marker or "meta" bit.

**`set print sevenbit-strings off`**
: Print full eight-bit characters. This allows the use of more
international character sets, and is the default.

**`show print sevenbit-strings`**
: Show whether or not GDB is printing only seven-bit characters.

**`set print union on`**
: 
Tell GDB to print unions which are contained in structures
and other unions. This is the default setting.

**`set print union off`**
: Tell GDB not to print unions which are contained in
structures and other unions. GDB will print `"{...}"`
instead.

**`show print union`**
: Ask GDB whether or not it will print unions which are contained in
structures and other unions.
For example, given the declarations

```
typedef enum {Tree, Bug} Species;
typedef enum {Big_tree, Acorn, Seedling} Tree_forms;
typedef enum {Caterpillar, Cocoon, Butterfly}
              Bug_forms;

struct thing {
  Species it;
  union {
    Tree_forms tree;
    Bug_forms bug;
  } form;
};

struct thing foo = {Tree, {Acorn}};
```

with `set print union on` in effect `` `p foo' `` would print

```
$1 = {it = Tree, form = {tree = Acorn, bug = Cocoon}}
```

and with `set print union off` in effect it would print

```
$1 = {it = Tree, form = {...}}
```

`set print union` affects programs written in C-like languages
and in Pascal.

These settings are of interest when debugging C++ programs:

**`set print demangle`**
: 

**`set print demangle on`**
: Print C++ names in their source form rather than in the encoded
("mangled") form passed to the assembler and linker for type-safe
linkage. The default is on.

**`show print demangle`**
: Show whether C++ names are printed in mangled or demangled form.

**`set print asm-demangle`**
:

**`set print asm-demangle on`**
: Print C++ names in their source form rather than their mangled form, even
in assembler code printouts such as instruction disassemblies.
The default is off.

**`show print asm-demangle`**
: Show whether C++ names in assembly listings are printed in mangled
or demangled form.

**`set demangle-style style`**
: Choose among several encoding schemes used by different compilers to
represent C++ names. The choices for style are currently:

**`auto`**
: Allow GDB to choose a decoding style by inspecting your program.

**`gnu`**
: Decode based on the GNU C++ compiler (`g++`) encoding algorithm.
This is the default.

**`hp`**
: Decode based on the HP ANSI C++ (`aCC`) encoding algorithm.

**`lucid`**
: Decode based on the Lucid C++ compiler (`lcc`) encoding algorithm.

**`arm`**
: Decode using the algorithm in the C++ Annotated Reference Manual.
__Warning:__ this setting alone is not sufficient to allow
debugging `cfront`-generated executables. GDB would
require further enhancement to permit that.

If you omit style, you will see a list of possible formats.

**`show demangle-style`**
: Display the encoding style currently in use for decoding C++ symbols.

**`set print object`**
:

**`set print object on`**
: 

When displaying a pointer to an object, identify the _actual_
(derived) type of the object rather than the _declared_ type, using
the virtual function table.

**`set print object off`**
: Display only the declared type of objects, without reference to the
virtual function table. This is the default setting.

**`show print object`**
: Show whether actual, or declared, object types are displayed.

**`set print static-members`**
:

**`set print static-members on`**
: 
Print static members when displaying a C++ object. The default is on.

**`set print static-members off`**
: Do not print static members when displaying a C++ object.

**`show print static-members`**
: Show whether C++ static members are printed or not.

**`set print pascal_static-members`**
:

**`set print pascal_static-members on`**
: 

Print static members when displaying a Pascal object. The default is on.

**`set print pascal_static-members off`**
: Do not print static members when displaying a Pascal object.

**`show print pascal_static-members`**
: Show whether Pascal static members are printed or not.

**`set print vtbl`**
:

**`set print vtbl on`**
: 

Pretty print C++ virtual function tables. The default is off.
(The `vtbl` commands do not work on programs compiled with the HP
ANSI C++ compiler (`aCC`).)

**`set print vtbl off`**
: Do not pretty print C++ virtual function tables.

**`show print vtbl`**
: Show whether C++ virtual function tables are pretty printed, or not.

## [Value history](Debugging%20with%20GDB.md#apple-krhugnru)

Values printed by the `print` command are saved in the GDB
__value history__. This allows you to refer to them in other expressions.
Values are kept until the symbol table is re-read or discarded
(for example with the `file` or `symbol-file` commands).
When the symbol table changes, the value history is discarded,
since the values may contain pointers back to the types defined in the
symbol table.

The values printed are given __history numbers__ by which you can
refer to them. These are successive integers starting with one.
`print` shows you the history number assigned to a value by
printing `` `$num = ' `` before the value; here num is the
history number.

To refer to any previous value, use `` `$' `` followed by the value's
history number. The way `print` labels its output is designed to
remind you of this. Just `$` refers to the most recent value in
the history, and `$$` refers to the value before that.
`$$n` refers to the nth value from the end; `$$2`
is the value just prior to `$$`, `$$1` is equivalent to
`$$`, and `$$0` is equivalent to `$`.

For example, suppose you have just printed a pointer to a structure and
want to see the contents of the structure. It suffices to type

```
p *$
```

If you have a chain of structures where the component `next` points
to the next one, you can print the contents of the next one with this:

```
p *$.next
```

You can print successive links in the chain by repeating this
command--which you can do by just typing `RET`.

Note that the history records values, not expressions. If the value of
`x` is 4 and you type these commands:

```
print x
set x=5
```

then the value recorded in the value history by the `print` command
remains 4 even though the value of `x` has changed.

**`show values`**
: 
Print the last ten values in the value history, with their item numbers.
This is like `` `p $$9' `` repeated ten times, except that `show
values` does not change the history.

**`show values n`**
: Print ten history values centered on history item number n.

**`show values +`**
: Print ten history values just after the values last printed. If no more
values are available, `show values +` produces no display.

Pressing `RET` to repeat `show values n` has exactly the
same effect as `` `show values +' ``.

## [Convenience variables](Debugging%20with%20GDB.md#apple-krhugnrv)

GDB provides __convenience variables__ that you can use within
GDB to hold on to a value and refer to it later. These variables
exist entirely within GDB; they are not part of your program, and
setting a convenience variable has no direct effect on further execution
of your program. That is why you can use them freely.

Convenience variables are prefixed with `` `$' ``. Any name preceded by
`` `$' `` can be used for a convenience variable, unless it is one of
the predefined machine-specific register names (see section [Registers](#apple-kncugnrw)).
(Value history references, in contrast, are _numbers_ preceded
by `` `$' ``. See section [Value history](#apple-kncugnru).)

You can save a value in a convenience variable with an assignment
expression, just as you would set a variable in your program.
For example:

```
set $foo = *object_ptr
```

would save in `$foo` the value contained in the object pointed to by
`object_ptr`.

Using a convenience variable for the first time creates it, but its
value is `void` until you assign a new value. You can alter the
value with another assignment at any time.

Convenience variables have no fixed types. You can assign a convenience
variable any type of value, including structures and arrays, even if
that variable already has a value of a different type. The convenience
variable, when used as an expression, has the type of its current value.

**`show convenience`**
: 

Print a list of convenience variables used so far, and their values.
Abbreviated `show conv`.

One of the ways to use a convenience variable is as a counter to be
incremented or a pointer to be advanced. For example, to print
a field from successive elements of an array of structures:

```swift
set $i = 0
print bar[$i++]->contents
```

Repeat that command by typing `RET`.

Some convenience variables are created automatically by GDB and given
values likely to be useful.

**`$_`**
: 
The variable `$_` is automatically set by the `x` command to
the last address examined (see section [Examining memory](#apple-kncugnrr)). Other
commands which provide a default address for `x` to examine also
set `$_` to that address; these commands include `info line`
and `info breakpoint`. The type of `$_` is `void *`
except when set by the `x` command, in which case it is a pointer
to the type of `$__`.

**`$__`**
: The variable `$__` is automatically set by the `x` command
to the value found in the last address examined. Its type is chosen
to match the format in which the data was printed.

**`$_exitcode`**
: 
The variable `$_exitcode` is automatically set to the exit code when
the program being debugged terminates.

On HP-UX systems, if you refer to a function or variable name that
begins with a dollar sign, GDB searches for a user or system
name first, before it searches for a convenience variable.

## [Registers](Debugging%20with%20GDB.md#apple-krhugnrw)

You can refer to machine register contents, in expressions, as variables
with names starting with `` `$' ``. The names of registers are different
for each machine; use `info registers` to see the names used on
your machine.

**`info registers`**
: 
Print the names and values of all registers except floating-point
and vector registers (in the selected stack frame).

**`info all-registers`**
: Print the names and values of all registers, including floating-point
and vector registers (in the selected stack frame).

**`info registers regname ...`**
: Print the __relativized__ value of each specified register regname.
As discussed in detail below, register values are normally relative to
the selected stack frame. regname may be any register name valid on
the machine you are using, with or without the initial `` `$' ``.

GDB has four "standard" register names that are available (in
expressions) on most machines--whenever they do not conflict with an
architecture's canonical mnemonics for registers. The register names
`$pc` and `$sp` are used for the program counter register and
the stack pointer. `$fp` is used for a register that contains a
pointer to the current stack frame, and `$ps` is used for a
register that contains the processor status. For example,
you could print the program counter in hex with

```
p/x $pc
```

or print the instruction to be executed next with

```
x/i $pc
```

or add four to the stack pointer[(5)](Debugging%20with%20GDB-2.md#apple-izhu6vbv) with

```
set $sp += 4
```

Whenever possible, these four standard register names are available on
your machine even though the machine has different canonical mnemonics,
so long as there is no conflict. The `info registers` command
shows the canonical names. For example, on the SPARC, `info
registers` displays the processor status register as `$psr` but you
can also refer to it as `$ps`; and on x86-based machines `$ps`
is an alias for the EFLAGS register.

GDB always considers the contents of an ordinary register as an
integer when the register is examined in this way. Some machines have
special registers which can hold nothing but floating point; these
registers are considered to have floating point values. There is no way
to refer to the contents of an ordinary register as floating point value
(although you can _print_ it as a floating point value with
`` `print/f $regname' ``).

Some registers have distinct "raw" and "virtual" data formats. This
means that the data format in which the register contents are saved by
the operating system is not the same one that your program normally
sees. For example, the registers of the 68881 floating point
coprocessor are always saved in "extended" (raw) format, but all C
programs expect to work with "double" (virtual) format. In such
cases, GDB normally works with the virtual format only (the format
that makes sense for your program), but the `info registers` command
prints the data in both formats.

Normally, register values are relative to the selected stack frame
(see section [Selecting a frame](Examining%20the%20Stack.md#apple-kncugnbx)). This means that you get the
value that the register would contain if all stack frames farther in
were exited and their saved registers restored. In order to see the
true contents of hardware registers, you must select the innermost
frame (with `` `frame 0' ``).

However, GDB must deduce where registers are saved, from the machine
code generated by your compiler. If some registers are not saved, or if
GDB is unable to locate the saved registers, the selected stack
frame makes no difference.

## [Floating point hardware](Debugging%20with%20GDB.md#apple-krhugnrx)

Depending on the configuration, GDB may be able to give
you more information about the status of the floating point hardware.

**`info float`**
: 
Display hardware-dependent information about the floating
point unit. The exact contents and layout vary depending on the
floating point chip. Currently, `` `info float' `` is supported on
the ARM and x86 machines.

## [Vector Unit](Debugging%20with%20GDB.md#apple-krhugnry)

Depending on the configuration, GDB may be able to give you
more information about the status of the vector unit.

**`info vector`**
: 
Display information about the vector unit. The exact contents and
layout vary depending on the hardware.

## [Operating system auxiliary information](Debugging%20with%20GDB.md#apple-krhugnrz)

GDB provides interfaces to useful OS facilities that can help
you debug your program.

When GDB runs on a __Posix system__ (such as GNU or Unix
machines), it interfaces with the inferior via the `ptrace`
system call. The operating system creates a special sata structure,
called `struct user`, for this interface. You can use the
command `info udot` to display the contents of this data
structure.

**`info udot`**
: 
Display the contents of the `struct user` maintained by the OS
kernel for the program being debugged. GDB displays the
contents of `struct user` as a list of hex numbers, similar to
the `examine` command.

Some operating systems supply an __auxiliary vector__ to programs at
startup. This is akin to the arguments and environment that you
specify for a program, but contains a system-dependent variety of
binary values that tell system libraries important details about the
hardware, operating system, and process. Each value's purpose is
identified by an integer tag; the meanings are well-known but system-specific.
Depending on the configuration and operating system facilities,
GDB may be able to show you this information. For remote
targets, this functionality may further depend on the remote stub's
support of the `` `qPart:auxv:read' `` packet, see section [Remote configuration](Debugging%20remote%20programs.md#apple-kncugmjwga).

**`info auxv`**
: 
Display the auxiliary vector of the inferior, which can be either a
live process or a core dump file. GDB prints each tag value
numerically, and also shows names and text descriptions for recognized
tags. Some values in the vector are numbers, some bit masks, and some
pointers to strings or other data. GDB displays each value in the
most appropriate form for a recognized tag, and in hexadecimal for
an unrecognized tag.

## [Memory region attributes](Debugging%20with%20GDB.md#apple-krhugnzq)

__Memory region attributes__ allow you to describe special handling
required by regions of your target's memory. GDB uses attributes
to determine whether to allow certain types of memory accesses; whether to
use specific width accesses; and whether to cache target memory.

Defined memory regions can be individually enabled and disabled. When a
memory region is disabled, GDB uses the default attributes when
accessing memory in that region. Similarly, if no memory regions have
been defined, GDB uses the default attributes when accessing
all memory.

When a memory region is defined, it is given a number to identify it;
to enable, disable, or remove a memory region, you specify that number.

**`mem lower upper attributes...`**
: 
Define a memory region bounded by lower and upper with
attributes attributes..., and add it to the list of regions
monitored by GDB. Note that upper == 0 is a special
case: it is treated as the the target's maximum memory address.
(0xffff on 16 bit targets, 0xffffffff on 32 bit targets, etc.)

**`delete mem nums...`**
: Remove memory regions nums... from the list of regions
monitored by GDB.

**`disable mem nums...`**
: Disable monitoring of memory regions nums....
A disabled memory region is not forgotten.
It may be enabled again later.

**`enable mem nums...`**
: Enable monitoring of memory regions nums....

**`info mem`**
: Print a table of all defined memory regions, with the following columns
for each region:

**_Memory Region Number_**
:

**_Enabled or Disabled._**
: Enabled memory regions are marked with `` `y' ``.
Disabled memory regions are marked with `` `n' ``.

**_Lo Address_**
: The address defining the inclusive lower bound of the memory region.

**_Hi Address_**
: The address defining the exclusive upper bound of the memory region.

**_Attributes_**
: The list of attributes set for this memory region.

### [Attributes](Debugging%20with%20GDB.md#apple-krhugnzr)

#### [Memory Access Mode](Debugging%20with%20GDB.md#apple-krhugnzs)

The access mode attributes set whether GDB may make read or
write accesses to a memory region.

While these attributes prevent GDB from performing invalid
memory accesses, they do nothing to prevent the target system, I/O DMA,
etc. from accessing memory.

**`ro`**
: Memory is read only.

**`wo`**
: Memory is write only.

**`rw`**
: Memory is read/write. This is the default.

#### [Memory Access Size](Debugging%20with%20GDB.md#apple-krhugnzt)

The acccess size attributes tells GDB to use specific sized
accesses in the memory region. Often memory mapped device registers
require specific sized accesses. If no access size attribute is
specified, GDB may use accesses of any size.

**`8`**
: Use 8 bit memory accesses.

**`16`**
: Use 16 bit memory accesses.

**`32`**
: Use 32 bit memory accesses.

**`64`**
: Use 64 bit memory accesses.

#### [Data Cache](Debugging%20with%20GDB.md#apple-krhugnzu)

The data cache attributes set whether GDB will cache target
memory. While this generally improves performance by reducing debug
protocol overhead, it can lead to incorrect results because GDB
does not know about volatile variables or memory mapped device
registers.

**`cache`**
: Enable GDB to cache target memory.

**`nocache`**
: Disable GDB from caching target memory. This is the default.

## [Copy between memory and a file](Debugging%20with%20GDB.md#apple-krhugnzv)

You can use the commands `dump`, `append`, and
`restore` to copy data between target memory and a file. The
`dump` and `append` commands write data to a file, and the
`restore` command reads data from a file back into the inferior's
memory. Files may be in binary, Motorola S-record, Intel hex, or
Tektronix Hex format; however, GDB can only append to binary
files.

**`dump [format] memory filename start_addr end_addr`**
: 

**`dump [format] value filename expr`**
: Dump the contents of memory from start_addr to end_addr,
or the value of expr, to filename in the given format.
The format parameter may be any one of:

**`binary`**
: Raw binary form.

**`ihex`**
: Intel hex format.

**`srec`**
: Motorola S-record format.

**`tekhex`**
: Tektronix Hex format.

GDB uses the same definitions of these formats as the
GNU binary utilities, like `` `objdump' `` and `` `objcopy' ``. If
format is omitted, GDB dumps the data in raw binary
form.

**`append [binary] memory filename start_addr end_addr`**
:

**`append [binary] value filename expr`**
: Append the contents of memory from start_addr to end_addr,
or the value of expr, to the file filename, in raw binary form.
(GDB can only append data to files in raw binary form.)

**`restore filename [binary] bias start end`**
: Restore the contents of file filename into memory. The
`restore` command can automatically recognize any known BFD
file format, except for raw binary. To restore a raw binary file you
must specify the optional keyword `binary` after the filename.
If bias is non-zero, its value will be added to the addresses
contained in the file. Binary files always start at address zero, so
they will be restored at address bias. Other bfd files have
a built-in location; they will be restored at offset bias
from that location.
If start and/or end are non-zero, then only data between
file offset start and file offset end will be restored.
These offsets are relative to the addresses in the file, before
the bias argument is applied.

## [How to Produce a Core File from Your Program](Debugging%20with%20GDB.md#apple-krhugnzw)

A __core file__ or __core dump__ is a file that records the memory
image of a running process and its process status (register values
etc.). Its primary use is post-mortem debugging of a program that
crashed while it ran outside a debugger. A program that crashes
automatically produces a core file, unless this feature is disabled by
the user. See section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4), for information on invoking GDB in
the post-mortem debugging mode.

Occasionally, you may wish to produce a core file of the program you
are debugging in order to preserve a snapshot of its state.
GDB has a special command for that.

**`generate-core-file [file]`**
: 

**`gcore [file]`**
: Produce a core dump of the inferior process. The optional argument
file specifies the file name where to put the core dump. If not
specified, the file name defaults to `core.pid', where
pid is the inferior process ID.
Note that this command is implemented only for some systems (as of
this writing, GNU/Linux, FreeBSD, Solaris, Unixware, and S390).

## [Character Sets](Debugging%20with%20GDB.md#apple-krhugnzx)

If the program you are debugging uses a different character set to
represent characters and strings than the one GDB uses itself,
GDB can automatically translate between the character sets for
you. The character set GDB uses we call the __host
character set__; the one the inferior program uses we call the
__target character set__.

For example, if you are running GDB on a GNU/Linux system, which
uses the ISO Latin 1 character set, but you are using GDB's
remote protocol (see section [Remote debugging](Specifying%20a%20Debugging%20Target.md#apple-kncugmjvgq)) to debug a program
running on an IBM mainframe, which uses the EBCDIC character set,
then the host character set is Latin-1, and the target character set is
EBCDIC. If you give GDB the command `set
target-charset EBCDIC-US`, then GDB translates between
EBCDIC and Latin 1 as you print character or string values, or use
character and string literals in expressions.

GDB has no way to automatically recognize which character set
the inferior program uses; you must tell it, using the `set
target-charset` command, described below.

Here are the commands for controlling GDB's character set
support:

**`set target-charset charset`**
: 
Set the current target character set to charset. We list the
character set names GDB recognizes below, but if you type
`set target-charset` followed by `TAB``TAB`, GDB will
list the target character sets it supports.

**`set host-charset charset`**
: 
Set the current host character set to charset.
By default, GDB uses a host character set appropriate to the
system it is running on; you can override that default using the
`set host-charset` command.
GDB can only use certain character sets as its host character
set. We list the character set names GDB recognizes below, and
indicate which can be host character sets, but if you type
`set target-charset` followed by `TAB``TAB`, GDB will
list the host character sets it supports.

**`set charset charset`**
: 
Set the current host and target character sets to charset. As
above, if you type `set charset` followed by `TAB``TAB`,
GDB will list the name of the character sets that can be used
for both host and target.

**`show charset`**
: 
Show the names of the current host and target charsets.

**`show host-charset`**
: 
Show the name of the current host charset.

**`show target-charset`**
: 
Show the name of the current target charset.

GDB currently includes support for the following character
sets:

**`ASCII`**
: 
Seven-bit U.S. ASCII. GDB can use this as its host
character set.

**`ISO-8859-1`**
: 

The ISO Latin 1 character set. This extends ASCII with accented
characters needed for French, German, and Spanish. GDB can use
this as its host character set.

**`EBCDIC-US`**
:

**`IBM1047`**
: 

Variants of the EBCDIC character set, used on some of IBM's
mainframe operating systems. (GNU/Linux on the S/390 uses U.S. ASCII.)
GDB cannot use these as its host character set.

Note that these are all single-byte character sets. More work inside
GDB is needed to support multi-byte or variable-width character
encodings, like the UTF-8 and UCS-2 encodings of Unicode.

Here is an example of GDB's character set support in action.
Assume that the following source code has been placed in the file
`charset-test.c':

```c
#include <stdio.h>

char ascii_hello[]
  = {72, 101, 108, 108, 111, 44, 32, 119,
     111, 114, 108, 100, 33, 10, 0};
char ibm1047_hello[]
  = {200, 133, 147, 147, 150, 107, 64, 166,
     150, 153, 147, 132, 90, 37, 0};

main ()
{
  printf ("Hello, world!\n");
}
```

In this program, `ascii_hello` and `ibm1047_hello` are arrays
containing the string `` `Hello, world!' `` followed by a newline,
encoded in the ASCII and IBM1047 character sets.

We compile the program, and invoke the debugger on it:

```shell
$ gcc -g charset-test.c -o charset-test
$ gdb -nw charset-test
GNU gdb 2001-12-19-cvs
Copyright 2001 Free Software Foundation, Inc.
...
(gdb)
```

We can use the `show charset` command to see what character sets
GDB is currently using to interpret and display characters and
strings:

```
(gdb) show charset
The current host and target character set is `ISO-8859-1'.
(gdb)
```

For the sake of printing this manual, let's use ASCII as our
initial character set:

```
(gdb) set charset ASCII
(gdb) show charset
The current host and target character set is `ASCII'.
(gdb)
```

Let's assume that ASCII is indeed the correct character set for our
host system -- in other words, let's assume that if GDB prints
characters using the ASCII character set, our terminal will display
them properly. Since our current target character set is also
ASCII, the contents of `ascii_hello` print legibly:

```
(gdb) print ascii_hello
$1 = 0x401698 "Hello, world!\n"
(gdb) print ascii_hello[0]
$2 = 72 'H'
(gdb)
```

GDB uses the target character set for character and string
literals you use in expressions:

```
(gdb) print '+'
$3 = 43 '+'
(gdb)
```

The ASCII character set uses the number 43 to encode the `` `+' ``
character.

GDB relies on the user to tell it which character set the
target program uses. If we print `ibm1047_hello` while our target
character set is still ASCII, we get jibberish:

```
(gdb) print ibm1047_hello
$4 = 0x4016a8 "\310\205\223\223\226k@\246\226\231\223\204Z%"
(gdb) print ibm1047_hello[0]
$5 = 200 '\310'
(gdb)
```

If we invoke the `set target-charset` followed by `TAB``TAB`,
GDB tells us the character sets it supports:

```
(gdb) set target-charset
ASCII       EBCDIC-US   IBM1047     ISO-8859-1
(gdb) set target-charset
```

We can select IBM1047 as our target character set, and examine the
program's strings again. Now the ASCII string is wrong, but
GDB translates the contents of `ibm1047_hello` from the
target character set, IBM1047, to the host character set,
ASCII, and they display correctly:

```
(gdb) set target-charset IBM1047
(gdb) show charset
The current host character set is `ASCII'.
The current target character set is `IBM1047'.
(gdb) print ascii_hello
$6 = 0x401698 "\110\145%%?\054\040\167?\162%\144\041\012"
(gdb) print ascii_hello[0]
$7 = 72 '\110'
(gdb) print ibm1047_hello
$8 = 0x4016a8 "Hello, world!\n"
(gdb) print ibm1047_hello[0]
$9 = 200 'H'
(gdb)
```

As above, GDB uses the target character set for character and
string literals you use in expressions:

```
(gdb) print '+'
$10 = 78 '+'
(gdb)
```

The IBM1047 character set uses the number 78 to encode the `` `+' ``
character.

## [Caching Data of Remote Targets](Debugging%20with%20GDB.md#apple-krhugnzy)

GDB can cache data exchanged between the debugger and a
remote target (see section [Remote debugging](Specifying%20a%20Debugging%20Target.md#apple-kncugmjvgq)). Such caching generally improves
performance, because it reduces the overhead of the remote protocol by
bundling memory reads and writes into large chunks. Unfortunately,
GDB does not currently know anything about volatile
registers, and thus data caching will produce incorrect results when
volatile registers are in use.

**`set remotecache on`**
: 

**`set remotecache off`**
: Set caching state for remote targets. When `ON`, use data
caching. By default, this option is `OFF`.

**`show remotecache`**
: Show the current state of data caching for remote targets.

**`info dcache`**
: Print the information about the data cache performance. The
information displayed includes: the dcache width and depth; and for
each cache line, how many times it was referenced, and its data and
state (dirty, bad, ok, etc.). This command is useful for debugging
the data cache operation.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Examining%20Source%20Files.md), [next](C%20Preprocessor%20Macros.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
