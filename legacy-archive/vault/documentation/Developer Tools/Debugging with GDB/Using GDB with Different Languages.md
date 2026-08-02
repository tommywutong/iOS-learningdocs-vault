---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_13.html
archived_at: '2026-07-15T07:31:03.208439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Debugging%20Programs%20That%20Use%20Overlays.md), [next](Examining%20the%20Symbol%20Table.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Using GDB with Different Languages](Debugging%20with%20GDB.md#apple-krhugojy)

Although programming languages generally have common aspects, they are
rarely expressed in the same manner. For instance, in ANSI C,
dereferencing a pointer `p` is accomplished by `*p`, but in
Modula-2, it is accomplished by `p^`. Values can also be
represented (and displayed) differently. Hex numbers in C appear as
`` `0x1ae' ``, while in Modula-2 they appear as `` `1AEH' ``.

Language-specific information is built into GDB for some languages,
allowing you to express operations like the above in your program's
native language, and allowing GDB to output values in a manner
consistent with the syntax of your program's native language. The
language you use to build expressions is called the __working
language__.

## [Switching between source languages](Debugging%20with%20GDB.md#apple-krhugojz)

There are two ways to control the working language--either have GDB
set it automatically, or select it manually yourself. You can use the
`set language` command for either purpose. On startup, GDB
defaults to setting the language automatically. The working language is
used to determine how expressions you type are interpreted, how values
are printed, etc.

In addition to the working language, every source file that
GDB knows about has its own working language. For some object
file formats, the compiler might indicate which language a particular
source file is in. However, most of the time GDB infers the
language from the name of the file. The language of a source file
controls whether C++ names are demangled--this way `backtrace` can
show each frame appropriately for its own language. There is no way to
set the language of a source file from within GDB, but you can
set the language associated with a filename extension. See section [Displaying the language](#apple-kncugmjqgm).

This is most commonly a problem when you use a program, such
as `cfront` or `f2c`, that generates C but is written in
another language. In that case, make the
program use `#line` directives in its C output; that way
GDB will know the correct language of the source code of the original
program, and will display that source code, not the generated C code.

### [List of filename extensions and languages](Debugging%20with%20GDB.md#apple-krhugmjqga)

If a source file name ends in one of the following extensions, then
GDB infers that its language is the one indicated.

**`.ada'**
:

**`.ads'**
:

**`.adb'**
:

**`.a'**
: Ada source file.

**`.c'**
: C source file

**`.C'**
:

**`.cc'**
:

**`.cp'**
:

**`.cpp'**
:

**`.cxx'**
:

**`.c++'**
: C++ source file

**`.m'**
: Objective-C source file

**`.M'**
: Objective-C++ source file

**`.f'**
:

**`.F'**
: Fortran source file

**`.mod'**
: Modula-2 source file

**`.s'**
:

**`.S'**
: Assembler source file. This actually behaves almost like C, but
GDB does not skip over function prologues when stepping.

In addition, you may set the language associated with a filename
extension. See section [Displaying the language](#apple-kncugmjqgm).

### [Setting the working language](Debugging%20with%20GDB.md#apple-krhugmjqge)

If you allow GDB to set the language automatically,
expressions are interpreted the same way in your debugging session and
your program.

If you wish, you may set the language manually. To do this, issue the
command `` `set language lang' ``, where lang is the name of
a language, such as
`c` or `modula-2`.
For a list of the supported languages, type `` `set language' ``.

Setting the language manually prevents GDB from updating the working
language automatically. This can lead to confusion if you try
to debug a program when the working language is not the same as the
source language, when an expression is acceptable to both
languages--but means different things. For instance, if the current
source file were written in C, and GDB was parsing Modula-2, a
command such as:

```
print a = b + c
```

might not have the effect you intended. In C, this means to add
`b` and `c` and place the result in `a`. The result
printed would be the value of `a`. In Modula-2, this means to compare
`a` to the result of `b+c`, yielding a `BOOLEAN` value.

### [Having GDB infer the source language](Debugging%20with%20GDB.md#apple-krhugmjqgi)

To have GDB set the working language automatically, use
`` `set language local' `` or `` `set language auto' ``. GDB
then infers the working language. That is, when your program stops in a
frame (usually by encountering a breakpoint), GDB sets the
working language to the language recorded for the function in that
frame. If the language for a frame is unknown (that is, if the function
or block corresponding to the frame was defined in a source file that
does not have a recognized extension), the current working language is
not changed, and GDB issues a warning.

This may not seem necessary for most programs, which are written
entirely in one source language. However, program modules and libraries
written in one source language can be used by a main program written in
a different source language. Using `` `set language auto' `` in this
case frees you from having to set the working language manually.

## [Displaying the language](Debugging%20with%20GDB.md#apple-krhugmjqgm)

The following commands help you find out which language is the
working language, and also what language source files were written in.

**`show language`**
: 
Display the current working language. This is the
language you can use with commands such as `print` to
build and compute expressions that may involve variables in your program.

**`info frame`**
: 
Display the source language for this frame. This language becomes the
working language if you use an identifier from this frame.
See section [Information about a frame](Examining%20the%20Stack.md#apple-kncugnby), to identify the other
information listed here.

**`info source`**
: 
Display the source language of this source file.
See section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha), to identify the other
information listed here.

In unusual circumstances, you may have source files with extensions
not in the standard list. You can then set the extension associated
with a language explicitly:

**`set extension-language ext language`**
: 
Tell GDB that source files with extension ext are to be
assumed as written in the source language language.

**`info extensions`**
: 
List all the filename extensions and the associated languages.

## [Type and range checking](Debugging%20with%20GDB.md#apple-krhugmjqgq)

> _Warning:_ In this release, the GDB commands for type and range
> checking are included, but they do not yet have any effect. This
> section documents the intended facilities.

Some languages are designed to guard you against making seemingly common
errors through a series of compile- and run-time checks. These include
checking the type of arguments to functions and operators, and making
sure mathematical overflows are caught at run time. Checks such as
these help to ensure a program's correctness once it has been compiled
by eliminating type mismatches, and providing active checks for range
errors when your program is running.

GDB can check for conditions like the above if you wish.
Although GDB does not check the statements in your program,
it can check expressions entered directly into GDB for
evaluation via the `print` command, for example. As with the
working language, GDB can also decide whether or not to check
automatically based on your program's source language.
See section [Supported languages](#apple-kncugmjqg4), for the default
settings of supported languages.

### [An overview of type checking](Debugging%20with%20GDB.md#apple-krhugmjqgu)

Some languages, such as Modula-2, are strongly typed, meaning that the
arguments to operators and functions have to be of the correct type,
otherwise an error occurs. These checks prevent type mismatch
errors from ever causing any run-time problems. For example,

```swift
1 + 2 => 3
but
error--> 1 + 2.3
```

The second example fails because the `CARDINAL` 1 is not
type-compatible with the `REAL` 2.3.

For the expressions you use in GDB commands, you can tell the
GDB type checker to skip checking;
to treat any mismatches as errors and abandon the expression;
or to only issue warnings when type mismatches occur,
but evaluate the expression anyway. When you choose the last of
these, GDB evaluates expressions like the second example above, but
also issues a warning.

Even if you turn type checking off, there may be other reasons
related to type that prevent GDB from evaluating an expression.
For instance, GDB does not know how to add an `int` and
a `struct foo`. These particular type errors have nothing to do
with the language in use, and usually arise from expressions, such as
the one described above, which make little sense to evaluate anyway.

Each language defines to what degree it is strict about type. For
instance, both Modula-2 and C require the arguments to arithmetical
operators to be numbers. In C, enumerated types and pointers can be
represented as numbers, so that they are valid arguments to mathematical
operators. See section [Supported languages](#apple-kncugmjqg4), for further
details on specific languages.

GDB provides some additional commands for controlling the type checker:

**`set check type auto`**
: Set type checking on or off based on the current working language.
See section [Supported languages](#apple-kncugmjqg4), for the default settings for
each language.

**`set check type on`**
:

**`set check type off`**
: Set type checking on or off, overriding the default setting for the
current working language. Issue a warning if the setting does not
match the language default. If any type mismatches occur in
evaluating an expression while type checking is on, GDB prints a
message and aborts evaluation of the expression.

**`set check type warn`**
: Cause the type checker to issue warnings, but to always attempt to
evaluate the expression. Evaluating the expression may still
be impossible for other reasons. For example, GDB cannot add
numbers and structures.

**`show type`**
: Show the current setting of the type checker, and whether or not GDB
is setting it automatically.

### [An overview of range checking](Debugging%20with%20GDB.md#apple-krhugmjqgy)

In some languages (such as Modula-2), it is an error to exceed the
bounds of a type; this is enforced with run-time checks. Such range
checking is meant to ensure program correctness by making sure
computations do not overflow, or indices on an array element access do
not exceed the bounds of the array.

For expressions you use in GDB commands, you can tell
GDB to treat range errors in one of three ways: ignore them,
always treat them as errors and abandon the expression, or issue
warnings but evaluate the expression anyway.

A range error can result from numerical overflow, from exceeding an
array index bound, or when you type a constant that is not a member
of any type. Some languages, however, do not treat overflows as an
error. In many implementations of C, mathematical overflow causes the
result to "wrap around" to lower values--for example, if m is
the largest integer value, and s is the smallest, then

```
m + 1 => s
```

This, too, is specific to individual languages, and in some cases
specific to individual compilers or machines. See section [Supported languages](#apple-kncugmjqg4), for further details on specific languages.

GDB provides some additional commands for controlling the range checker:

**`set check range auto`**
: Set range checking on or off based on the current working language.
See section [Supported languages](#apple-kncugmjqg4), for the default settings for
each language.

**`set check range on`**
:

**`set check range off`**
: Set range checking on or off, overriding the default setting for the
current working language. A warning is issued if the setting does not
match the language default. If a range error occurs and range checking is on,
then a message is printed and evaluation of the expression is aborted.

**`set check range warn`**
: Output messages when the GDB range checker detects a range error,
but attempt to evaluate the expression anyway. Evaluating the
expression may still be impossible for other reasons, such as accessing
memory that the process does not own (a typical example from many Unix
systems).

**`show range`**
: Show the current setting of the range checker, and whether or not it is
being set automatically by GDB.

## [Supported languages](Debugging%20with%20GDB.md#apple-krhugmjqg4)

GDB supports C, C++, Objective-C, Objective-C++, Fortran, Java, Pascal,
assembly, Modula-2, and Ada.
Some GDB features may be used in expressions regardless of the
language you use: the GDB `@` and `::` operators,
and the `` `{type}addr' `` construct (see section [Expressions](Examining%20Data.md#apple-kncugnjx)) can be used with the constructs of any supported
language.

The following sections detail to what degree each source language is
supported by GDB. These sections are not meant to be language
tutorials or references, but serve only as a reference guide to what the
GDB expression parser accepts, and what input and output
formats should look like for different languages. There are many good
books written on each of these languages; please look to these for a
language reference or tutorial.

### [C and C++](Debugging%20with%20GDB.md#apple-krhugmjqha)

Since C and C++ are so closely related, many features of GDB apply
to both languages. Whenever this is the case, we discuss those languages
together.

The C++ debugging facilities are jointly implemented by the C++
compiler and GDB. Therefore, to debug your C++ code
effectively, you must compile your C++ programs with a supported
C++ compiler, such as GNU `g++`, or the HP ANSI C++
compiler (`aCC`).

For best results when using GNU C++, use the DWARF 2 debugging
format; if it doesn't work on your system, try the stabs+ debugging
format. You can select those formats explicitly with the `g++`
command-line options @option{-gdwarf-2} and @option{-gstabs+}.
See section `Options for Debugging Your Program or GNU CC' in Using GNU CC.

#### [C and C++ operators](Debugging%20with%20GDB.md#apple-krhugmjqhe)

Operators must be defined on values of specific types. For instance,
`+` is defined on numbers, but not on structures. Operators are
often defined on groups of types.

For the purposes of C and C++, the following definitions hold:

- _Integral types_ include `int` with any of its storage-class
  specifiers; `char`; `enum`; and, for C++, `bool`.
- _Floating-point types_ include `float`, `double`, and
  `long double` (if supported by the target platform).
- _Pointer types_ include all types defined as `(type *)`.
- _Scalar types_ include all of the above.

The following operators are supported. They are listed here
in order of increasing precedence:

**`,`**
: The comma or sequencing operator. Expressions in a comma-separated list
are evaluated from left to right, with the result of the entire
expression being the last expression evaluated.

**`=`**
: Assignment. The value of an assignment expression is the value
assigned. Defined on scalar types.

**`op=`**
: Used in an expression of the form `a op= b`,
and translated to `a = a op b`.
`op=` and `=` have the same precedence.
op is any one of the operators `|`, `^`, `&`,
`<<`, `>>`, `+`, `-`, `*`, `/`, `%`.

**`?:`**
: The ternary operator. `a ? b : c` can be thought
of as: if a then b else c. a should be of an
integral type.

**`||`**
: Logical OR. Defined on integral types.

**`&&`**
: Logical AND. Defined on integral types.

**`|`**
: Bitwise OR. Defined on integral types.

**`^`**
: Bitwise exclusive-OR. Defined on integral types.

**`&`**
: Bitwise AND. Defined on integral types.

**`==, !=`**
: Equality and inequality. Defined on scalar types. The value of these
expressions is 0 for false and non-zero for true.

**`<, >, <=, >=`**
: Less than, greater than, less than or equal, greater than or equal.
Defined on scalar types. The value of these expressions is 0 for false
and non-zero for true.

**`<<, >>`**
: left shift, and right shift. Defined on integral types.

**`@`**
: The GDB "artificial array" operator (see section [Expressions](Examining%20Data.md#apple-kncugnjx)).

**`+, -`**
: Addition and subtraction. Defined on integral types, floating-point types and
pointer types.

**`*, /, %`**
: Multiplication, division, and modulus. Multiplication and division are
defined on integral and floating-point types. Modulus is defined on
integral types.

**`++, --`**
: Increment and decrement. When appearing before a variable, the
operation is performed before the variable is used in an expression;
when appearing after it, the variable's value is used before the
operation takes place.

**`*`**
: Pointer dereferencing. Defined on pointer types. Same precedence as
`++`.

**`&`**
: Address operator. Defined on variables. Same precedence as `++`.
For debugging C++, GDB implements a use of `` `&' `` beyond what is
allowed in the C++ language itself: you can use `` `&(&ref)' ``
(or, if you prefer, simply `` `&&ref' ``) to examine the address
where a C++ reference variable (declared with `` `&ref' ``) is
stored.

**`-`**
: Negative. Defined on integral and floating-point types. Same
precedence as `++`.

**`!`**
: Logical negation. Defined on integral types. Same precedence as
`++`.

**`~`**
: Bitwise complement operator. Defined on integral types. Same precedence as
`++`.

**`., ->`**
: Structure member, and pointer-to-structure member. For convenience,
GDB regards the two as equivalent, choosing whether to dereference a
pointer based on the stored type information.
Defined on `struct` and `union` data.

**`.*, ->*`**
: Dereferences of pointers to members.

**`[]`**
: Array indexing. `a[i]` is defined as
`*(a+i)`. Same precedence as `->`.

**`()`**
: Function parameter list. Same precedence as `->`.

**`::`**
: C++ scope resolution operator. Defined on `struct`, `union`,
and `class` types.

**`::`**
: Doubled colons also represent the GDB scope operator
(see section [Expressions](Examining%20Data.md#apple-kncugnjx)). Same precedence as `::`,
above.

If an operator is redefined in the user code, GDB usually
attempts to invoke the redefined version instead of using the operator's
predefined meaning.

#### [C and C++ constants](Debugging%20with%20GDB.md#apple-krhugmjrga)

GDB allows you to express the constants of C and C++ in the
following ways:

- Integer constants are a sequence of digits. Octal constants are
  specified by a leading `` `0' `` (i.e. zero), and hexadecimal constants
  by a leading `` `0x' `` or `` `0X' ``. Constants may also end with a letter
  `` `l' ``, specifying that the constant should be treated as a
  `long` value.
- Floating point constants are a sequence of digits, followed by a decimal
  point, followed by a sequence of digits, and optionally followed by an
  exponent. An exponent is of the form:
  `` `e[[+]|-]nnn' ``, where nnn is another
  sequence of digits. The `` `+' `` is optional for positive exponents.
  A floating-point constant may also end with a letter `` `f' `` or
  `` `F' ``, specifying that the constant should be treated as being of
  the `float` (as opposed to the default `double`) type; or with
  a letter `` `l' `` or `` `L' ``, which specifies a `long double`
  constant.
- Enumerated constants consist of enumerated identifiers, or their
  integral equivalents.
- Character constants are a single character surrounded by single quotes
  (`'`), or a number--the ordinal value of the corresponding character
  (usually its ASCII value). Within quotes, the single character may
  be represented by a letter or by __escape sequences__, which are of
  the form `` `\nnn' ``, where nnn is the octal representation
  of the character's ordinal value; or of the form `` `\x' ``, where
  `` `x' `` is a predefined special character--for example,
  `` `\n' `` for newline.
- String constants are a sequence of character constants surrounded by
  double quotes (`"`). Any valid character constant (as described
  above) may appear. Double quotes within the string must be preceded by
  a backslash, so for instance `` `"a\"b'c"' `` is a string of five
  characters.
- Pointer constants are an integral value. You can also write pointers
  to constants using the C operator `` `&' ``.
- Array constants are comma-separated lists surrounded by braces `` `{' ``
  and `` `}' ``; for example, `` `{1,2,3}' `` is a three-element array of
  integers, `` `{{1,2}, {3,4}, {5,6}}' `` is a three-by-two array,
  and `` `{&"hi", &"there", &"fred"}' `` is a three-element array of pointers.

#### [C++ expressions](Debugging%20with%20GDB.md#apple-krhugmjrge)

GDB expression handling can interpret most C++ expressions.

> _Warning:_ GDB can only debug C++ code if you use the
> proper compiler and the proper debug format. Currently, GDB
> works best when debugging C++ code that is compiled with
> GCC 2.95.3 or with GCC 3.1 or newer, using the options
> @option{-gdwarf-2} or @option{-gstabs+}. DWARF 2 is preferred over
> stabs+. Most configurations of GCC emit either DWARF 2 or
> stabs+ as their default debug format, so you usually don't need to
> specify a debug format explicitly. Other compilers and/or debug formats
> are likely to work badly or not at all when using GDB to debug
> C++ code.

1. 
   Member function calls are allowed; you can use expressions like

   ```
   count = aml->GetOriginal(x, y)
   ```

2. While a member function is active (in the selected stack frame), your
   expressions have the same namespace available as the member function;
   that is, GDB allows implicit references to the class instance
   pointer `this` following the same rules as C++.

3. You can call overloaded functions; GDB resolves the function
   call to the right definition, with some restrictions. GDB does not
   perform overload resolution involving user-defined type conversions,
   calls to constructors, or instantiations of templates that do not exist
   in the program. It also cannot handle ellipsis argument lists or
   default arguments.
   It does perform integral conversions and promotions, floating-point
   promotions, arithmetic conversions, pointer conversions, conversions of
   class objects to base classes, and standard conversions such as those of
   functions or arrays to pointers; it requires an exact match on the
   number of function arguments.
   Overload resolution is always performed, unless you have specified
   `set overload-resolution off`. See section [GDB features for C++](#apple-kncugmjrgu).
   You must specify `set overload-resolution off` in order to use an
   explicit function signature to call an overloaded function, as in

   ```
   p 'foo(char,int)'('x', 13)
   ```

   The GDB command-completion facility can simplify this;
   see section [Command completion](GDB%20Commands.md#apple-kncugmjw).
   
4. GDB understands variables declared as C++ references; you can use
   them in expressions just as you do in C++ source--they are automatically
   dereferenced.
   In the parameter list shown when GDB displays a frame, the values of
   reference variables are not displayed (unlike other variables); this
   avoids clutter, since references are often used for large structures.
   The _address_ of a reference variable is always shown, unless
   you have specified `` `set print address off' ``.
5. GDB supports the C++ name resolution operator `::`---your
   expressions can use it just as expressions in your program do. Since
   one scope may be defined in another, you can use `::` repeatedly if
   necessary, for example in an expression like
   `` `scope1::scope2::name' ``. GDB also allows
   resolving name scope by reference to source files, in both C and C++
   debugging (see section [Program variables](Examining%20Data.md#apple-kncugnjy)).

In addition, when used with HP's C++ compiler, GDB supports
calling virtual functions correctly, printing out virtual bases of
objects, calling functions in a base subobject, casting objects, and
invoking user-defined operators.

#### [C and C++ defaults](Debugging%20with%20GDB.md#apple-krhugmjrgi)

If you allow GDB to set type and range checking automatically, they
both default to `off` whenever the working language changes to
C or C++. This happens regardless of whether you or GDB
selects the working language.

If you allow GDB to set the language automatically, it
recognizes source files whose names end with `.c', `.C', or
`.cc', etc, and when GDB enters code compiled from one of
these files, it sets the working language to C or C++.
See section [Having GDB infer the source language](#apple-kncugmjqgi),
for further details.

#### [C and C++ type and range checks](Debugging%20with%20GDB.md#apple-krhugmjrgm)

By default, when GDB parses C or C++ expressions, type checking
is not used. However, if you turn type checking on, GDB
considers two variables type equivalent if:

- The two variables are structured and have the same structure, union, or
  enumerated tag.
- The two variables have the same type name, or types that have been
  declared equivalent through `typedef`.

Range checking, if turned on, is done on mathematical operations. Array
indices are not checked, since they are often used to index a pointer
that is not itself an array.

#### [GDB and C](Debugging%20with%20GDB.md#apple-krhugmjrgq)

The `set print union` and `show print union` commands apply to
the `union` type. When set to `` `on' ``, any `union` that is
inside a `struct` or `class` is also printed. Otherwise, it
appears as `` `{...}' ``.

The `@` operator aids in the debugging of dynamic arrays, formed
with pointers and a memory allocation function. See section [Expressions](Examining%20Data.md#apple-kncugnjx).

#### [GDB features for C++](Debugging%20with%20GDB.md#apple-krhugmjrgu)

Some GDB commands are particularly useful with C++, and some are
designed specifically for use with C++. Here is a summary:

**`breakpoint menus`**
: 
When you want a breakpoint in a function whose name is overloaded,
GDB breakpoint menus help you specify which function definition
you want. See section [Breakpoint menus](Stopping%20and%20Continuing.md#apple-kncugmzy).

**`rbreak regex`**
: Setting breakpoints using regular expressions is helpful for setting
breakpoints on overloaded functions that are not members of any special
classes.
See section [Setting breakpoints](Stopping%20and%20Continuing.md#apple-kncugmzr).

**`catch throw`**
:

**`catch catch`**
: Debug C++ exception handling using these commands. See section [Setting catchpoints](Stopping%20and%20Continuing.md#apple-kncugmzt).

**`ptype typename`**
: Print inheritance relationships as well as other information for type
typename.
See section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha).

**`set print demangle`**
:

**`show print demangle`**
:

**`set print asm-demangle`**
:

**`show print asm-demangle`**
: Control whether C++ symbols display in their source form, both when
displaying code as C++ source and when displaying disassemblies.
See section [Print settings](Examining%20Data.md#apple-kncugnrt).

**`set print object`**
:

**`show print object`**
: Choose whether to print derived (actual) or declared types of objects.
See section [Print settings](Examining%20Data.md#apple-kncugnrt).

**`set print vtbl`**
:

**`show print vtbl`**
: Control the format for printing virtual function tables.
See section [Print settings](Examining%20Data.md#apple-kncugnrt).
(The `vtbl` commands do not work on programs compiled with the HP
ANSI C++ compiler (`aCC`).)

**`set overload-resolution on`**
: Enable overload resolution for C++ expression evaluation. The default
is on. For overloaded functions, GDB evaluates the arguments
and searches for a function whose signature matches the argument types,
using the standard C++ conversion rules (see section [C++ expressions](#apple-kncugmjrge), for details). If it cannot find a match, it emits a
message.

**`set overload-resolution off`**
: Disable overload resolution for C++ expression evaluation. For
overloaded functions that are not class member functions, GDB
chooses the first function of the specified name that it finds in the
symbol table, whether or not its arguments are of the correct type. For
overloaded functions that are class member functions, GDB
searches for a function whose signature _exactly_ matches the
argument types.

**`show overload-resolution`**
: Show the current setting of overload resolution.

**`Overloaded symbol names`**
: You can specify a particular definition of an overloaded symbol, using
the same notation that is used to declare such symbols in C++: type
`symbol(types)` rather than just symbol. You can
also use the GDB command-line word completion facilities to list the
available choices, or to finish the type list for you.
See section [Command completion](GDB%20Commands.md#apple-kncugmjw), for details on how to do this.

### [Objective-C/C++](Debugging%20with%20GDB.md#apple-krhugmjrgy)

This section provides information about some commands and command
options that are useful for debugging Objective-C and Objective-C++ code. See also
section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha), and section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha), for a
few more commands specific to Objective-C support.

#### [Method Names in Commands](Debugging%20with%20GDB.md#apple-krhugmjrg4)

The following commands have been extended to accept Objective-C method
names as line specifications:

- `clear`
- `break`
- `info line`
- `jump`
- `list`

A fully qualified Objective-C method name is specified as

```
-[Class methodName]
```

where the minus sign is used to indicate an instance method and a
plus sign (not shown) is used to indicate a class method. The class
name Class and method name methoName are enclosed in
brackets, similar to the way messages are specified in Objective-C
source code. For example, to set a breakpoint at the `create`
instance method of class `Fruit` in the program currently being
debugged, enter:

```
break -[Fruit create]
```

To list ten program lines around the `initialize` class method,
enter:

```
list +[NSText initialize]
```

In the current version of GDB, the plus or minus sign is
required. In future versions of GDB, the plus or minus
sign will be optional, but you can use it to narrow the search. It
is also possible to specify just a method name:

```
break create
```

You must specify the complete method name, including any colons. If
your program's source files contain more than one `create` method,
you'll be presented with a numbered list of classes that implement that
method. Indicate your choice by number, or type `` `0' `` to exit if
none apply.

As another example, to clear a breakpoint established at the
`makeKeyAndOrderFront:` method of the `NSWindow` class, enter:

```
clear -[NSWindow makeKeyAndOrderFront:]
```

#### [The Print Command With Objective-C](Debugging%20with%20GDB.md#apple-krhugmjrha)

The print command has also been extended to accept methods. For example:

```
print -[object hash]
```


will tell GDB to send the `hash` message to object
and print the result. Also, an additional command has been added,
`print-object` or `po` for short, which is meant to print
the description of an object. However, this command may only work
with certain Objective-C libraries that have a particular hook
function, `_NSPrintForDebugger`, defined.

#### [Command Descriptions](Debugging%20with%20GDB.md#apple-krhugmjrhe)

This section describes commands and options that are useful in debugging
Objective-C/C++ code. Some of these are commands added specifically to
upport Objective-C/C++; others are previously existing GDB commands
that have been extended to support Objective-C/C++.

**`info classes`**
:

**`info selectors`**
:

### [Fortran](Debugging%20with%20GDB.md#apple-krhugmjsga)

**`info common [common-name]`**
: 

This command prints the values contained in the Fortran `COMMON`
block whose name is common-name. With no argument, the names of
all `COMMON` blocks visible at current program location are
printed.

Fortran symbols are usually case-insensitive, so GDB by
default uses case-insensitive matches for Fortran symbols. You can
change that with the `` `set case-insensitive' `` command, see
section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha), for the details.

### [Pascal](Debugging%20with%20GDB.md#apple-krhugmjsge)

Debugging Pascal programs which use sets, subranges, file variables, or
nested functions does not currently work. GDB does not support
entering expressions, printing values, or similar features using Pascal
syntax.

The Pascal-specific command `set print pascal_static-members`
controls whether static members of Pascal objects are displayed.
See section [Print settings](Examining%20Data.md#apple-kncugnrt).

### [Modula-2](Debugging%20with%20GDB.md#apple-krhugmjsgi)

The extensions made to GDB to support Modula-2 only support
output from the GNU Modula-2 compiler (which is currently being
developed). Other Modula-2 compilers are not currently supported, and
attempting to debug executables produced by them is most likely
to give an error as GDB reads in the executable's symbol
table.

#### [Operators](Debugging%20with%20GDB.md#apple-krhugmjsgm)

Operators must be defined on values of specific types. For instance,
`+` is defined on numbers, but not on structures. Operators are
often defined on groups of types. For the purposes of Modula-2, the
following definitions hold:

- _Integral types_ consist of `INTEGER`, `CARDINAL`, and
  their subranges.
- _Character types_ consist of `CHAR` and its subranges.
- _Floating-point types_ consist of `REAL`.
- _Pointer types_ consist of anything declared as `POINTER TO
  type`.
- _Scalar types_ consist of all of the above.
- _Set types_ consist of `SET` and `BITSET` types.
- _Boolean types_ consist of `BOOLEAN`.

The following operators are supported, and appear in order of
increasing precedence:

**`,`**
: Function argument or array index separator.

**`:=`**
: Assignment. The value of var `:=` value is
value.

**`<, >`**
: Less than, greater than on integral, floating-point, or enumerated
types.

**`<=, >=`**
: Less than or equal to, greater than or equal to
on integral, floating-point and enumerated types, or set inclusion on
set types. Same precedence as `<`.

**`=, <>, #`**
: Equality and two ways of expressing inequality, valid on scalar types.
Same precedence as `<`. In GDB scripts, only `<>` is
available for inequality, since `#` conflicts with the script
comment character.

**`IN`**
: Set membership. Defined on set types and the types of their members.
Same precedence as `<`.

**`OR`**
: Boolean disjunction. Defined on boolean types.

**`AND, &`**
: Boolean conjunction. Defined on boolean types.

**`@`**
: The GDB "artificial array" operator (see section [Expressions](Examining%20Data.md#apple-kncugnjx)).

**`+, -`**
: Addition and subtraction on integral and floating-point types, or union
and difference on set types.

**`*`**
: Multiplication on integral and floating-point types, or set intersection
on set types.

**`/`**
: Division on floating-point types, or symmetric set difference on set
types. Same precedence as `*`.

**`DIV, MOD`**
: Integer division and remainder. Defined on integral types. Same
precedence as `*`.

**`-`**
: Negative. Defined on `INTEGER` and `REAL` data.

**`^`**
: Pointer dereferencing. Defined on pointer types.

**`NOT`**
: Boolean negation. Defined on boolean types. Same precedence as
`^`.

**`.`**
: `RECORD` field selector. Defined on `RECORD` data. Same
precedence as `^`.

**`[]`**
: Array indexing. Defined on `ARRAY` data. Same precedence as `^`.

**`()`**
: Procedure argument list. Defined on `PROCEDURE` objects. Same precedence
as `^`.

**`::, .`**
: GDB and Modula-2 scope operators.

> _Warning:_ Sets and their operations are not yet supported, so GDB
> treats the use of the operator `IN`, or the use of operators
> `+`, `-`, `*`, `/`, `=`, , `<>`, `#`,
> `<=`, and `>=` on sets as an error.

#### [Built-in functions and procedures](Debugging%20with%20GDB.md#apple-krhugmjsgq)

Modula-2 also makes available several built-in procedures and functions.
In describing these, the following metavariables are used:

**a**
: represents an `ARRAY` variable.

**c**
: represents a `CHAR` constant or variable.

**i**
: represents a variable or constant of integral type.

**m**
: represents an identifier that belongs to a set. Generally used in the
same function with the metavariable s. The type of s should
be `SET OF mtype` (where mtype is the type of m).

**n**
: represents a variable or constant of integral or floating-point type.

**r**
: represents a variable or constant of floating-point type.

**t**
: represents a type.

**v**
: represents a variable.

**x**
: represents a variable or constant of one of many types. See the
explanation of the function for details.

All Modula-2 built-in procedures also return a result, described below.

**`ABS(n)`**
: Returns the absolute value of n.

**`CAP(c)`**
: If c is a lower case letter, it returns its upper case
equivalent, otherwise it returns its argument.

**`CHR(i)`**
: Returns the character whose ordinal value is i.

**`DEC(v)`**
: Decrements the value in the variable v by one. Returns the new value.

**`DEC(v,i)`**
: Decrements the value in the variable v by i. Returns the
new value.

**`EXCL(m,s)`**
: Removes the element m from the set s. Returns the new
set.

**`FLOAT(i)`**
: Returns the floating point equivalent of the integer i.

**`HIGH(a)`**
: Returns the index of the last member of a.

**`INC(v)`**
: Increments the value in the variable v by one. Returns the new value.

**`INC(v,i)`**
: Increments the value in the variable v by i. Returns the
new value.

**`INCL(m,s)`**
: Adds the element m to the set s if it is not already
there. Returns the new set.

**`MAX(t)`**
: Returns the maximum value of the type t.

**`MIN(t)`**
: Returns the minimum value of the type t.

**`ODD(i)`**
: Returns boolean TRUE if i is an odd number.

**`ORD(x)`**
: Returns the ordinal value of its argument. For example, the ordinal
value of a character is its ASCII value (on machines supporting the
ASCII character set). x must be of an ordered type, which include
integral, character and enumerated types.

**`SIZE(x)`**
: Returns the size of its argument. x can be a variable or a type.

**`TRUNC(r)`**
: Returns the integral part of r.

**`VAL(t,i)`**
: Returns the member of the type t whose ordinal value is i.

> _Warning:_ Sets and their operations are not yet supported, so
> GDB treats the use of procedures `INCL` and `EXCL` as
> an error.

#### [Constants](Debugging%20with%20GDB.md#apple-krhugmjsgu)

GDB allows you to express the constants of Modula-2 in the following
ways:

- Integer constants are simply a sequence of digits. When used in an
  expression, a constant is interpreted to be type-compatible with the
  rest of the expression. Hexadecimal integers are specified by a
  trailing `` `H' ``, and octal integers by a trailing `` `B' ``.
- Floating point constants appear as a sequence of digits, followed by a
  decimal point and another sequence of digits. An optional exponent can
  then be specified, in the form `` `E[+|-]nnn' ``, where
  `` `[+|-]nnn' `` is the desired exponent. All of the
  digits of the floating point constant must be valid decimal (base 10)
  digits.
- Character constants consist of a single character enclosed by a pair of
  like quotes, either single (`'`) or double (`"`). They may
  also be expressed by their ordinal value (their ASCII value, usually)
  followed by a `` `C' ``.
- String constants consist of a sequence of characters enclosed by a
  pair of like quotes, either single (`'`) or double (`"`).
  Escape sequences in the style of C are also allowed. See section [C and C++ constants](#apple-kncugmjrga), for a brief explanation of escape
  sequences.
- Enumerated constants consist of an enumerated identifier.
- Boolean constants consist of the identifiers `TRUE` and
  `FALSE`.
- Pointer constants consist of integral values only.
- Set constants are not yet supported.

#### [Modula-2 defaults](Debugging%20with%20GDB.md#apple-krhugmjsgy)

If type and range checking are set automatically by GDB, they
both default to `on` whenever the working language changes to
Modula-2. This happens regardless of whether you or GDB
selected the working language.

If you allow GDB to set the language automatically, then entering
code compiled from a file whose name ends with `.mod' sets the
working language to Modula-2. See section [Having GDB infer the source language](#apple-kncugmjqgi), for further details.

#### [Deviations from standard Modula-2](Debugging%20with%20GDB.md#apple-krhugmjsg4)

A few changes have been made to make Modula-2 programs easier to debug.
This is done primarily via loosening its type strictness:

- Unlike in standard Modula-2, pointer constants can be formed by
  integers. This allows you to modify pointer variables during
  debugging. (In standard Modula-2, the actual address contained in a
  pointer variable is hidden from you; it can only be modified
  through direct assignment to another pointer variable or expression that
  returned a pointer.)
- C escape sequences can be used in strings and characters to represent
  non-printable characters. GDB prints out strings with these
  escape sequences embedded. Single non-printable characters are
  printed using the `` `CHR(nnn)' `` format.
- The assignment operator (`:=`) returns the value of its right-hand
  argument.
- All built-in procedures both modify _and_ return their argument.

#### [Modula-2 type and range checks](Debugging%20with%20GDB.md#apple-krhugmjsha)

> _Warning:_ in this release, GDB does not yet perform type or
> range checking.

GDB considers two Modula-2 variables type equivalent if:

- They are of types that have been declared equivalent via a `TYPE
  t1 = t2` statement
- They have been declared on the same line. (Note: This is true of the
  GNU Modula-2 compiler, but it may not be true of other compilers.)

As long as type checking is enabled, any attempt to combine variables
whose types are not equivalent is an error.

Range checking is done on all mathematical operations, assignment, array
index bounds, and all built-in functions and procedures.

#### [The scope operators `::` and `.`](gdb_toc.md#apple-krhugmjshe)

There are a few subtle differences between the Modula-2 scope operator
(`.`) and the GDB scope operator (`::`). The two have
similar syntax:

```
module . id
scope :: id
```

where scope is the name of a module or a procedure,
module the name of a module, and id is any declared
identifier within your program, except another module.

Using the `::` operator makes GDB search the scope
specified by scope for the identifier id. If it is not
found in the specified scope, then GDB searches all scopes
enclosing the one specified by scope.

Using the `.` operator makes GDB search the current scope for
the identifier specified by id that was imported from the
definition module specified by module. With this operator, it is
an error if the identifier id was not imported from definition
module module, or if id is not an identifier in
module.

#### [GDB and Modula-2](Debugging%20with%20GDB.md#apple-krhugmjtga)

Some GDB commands have little use when debugging Modula-2 programs.
Five subcommands of `set print` and `show print` apply
specifically to C and C++: `` `vtbl' ``, `` `demangle' ``,
`` `asm-demangle' ``, `` `object' ``, and `` `union' ``. The first four
apply to C++, and the last to the C `union` type, which has no direct
analogue in Modula-2.

The `@` operator (see section [Expressions](Examining%20Data.md#apple-kncugnjx)), while available
with any language, is not useful with Modula-2. Its
intent is to aid the debugging of __dynamic arrays__, which cannot be
created in Modula-2 as they can in C or C++. However, because an
address can be specified by an integral constant, the construct
`` `{type}adrexp' `` is still useful.

In GDB scripts, the Modula-2 inequality operator `#` is
interpreted as the beginning of a comment. Use `<>` instead.

### [Ada](Debugging%20with%20GDB.md#apple-krhugmjtge)

The extensions made to GDB for Ada only support
output from the GNU Ada (GNAT) compiler.
Other Ada compilers are not currently supported, and
attempting to debug executables produced by them is most likely
to be difficult.

#### [Introduction](Debugging%20with%20GDB.md#apple-krhugmjtgi)

The Ada mode of GDB supports a fairly large subset of Ada expression
syntax, with some extensions.
The philosophy behind the design of this subset is

- That GDB should provide basic literals and access to operations for
  arithmetic, dereferencing, field selection, indexing, and subprogram calls,
  leaving more sophisticated computations to subprograms written into the
  program (which therefore may be called from GDB).
- That type safety and strict adherence to Ada language restrictions
  are not particularly important to the GDB user.
- That brevity is important to the GDB user.

Thus, for brevity, the debugger acts as if there were
implicit `with` and `use` clauses in effect for all user-written
packages, making it unnecessary to fully qualify most names with
their packages, regardless of context. Where this causes ambiguity,
GDB asks the user's intent.

The debugger will start in Ada mode if it detects an Ada main program.
As for other languages, it will enter Ada mode when stopped in a program that
was translated from an Ada source file.

While in Ada mode, you may use `--' for comments. This is useful
mostly for documenting command files. The standard GDB comment
(`` `#' ``) still works at the beginning of a line in Ada mode, but not in the
middle (to allow based literals).

The debugger supports limited overloading. Given a subprogram call in which
the function symbol has multiple definitions, it will use the number of
actual parameters and some information about their types to attempt to narrow
the set of definitions. It also makes very limited use of context, preferring
procedures to functions in the context of the `call` command, and
functions to procedures elsewhere.

#### [Omissions from Ada](Debugging%20with%20GDB.md#apple-krhugmjtgm)

Here are the notable omissions from the subset:

- Only a subset of the attributes are supported:
  - 'First, 'Last, and 'Length
    on array objects (not on types and subtypes).
  - 'Min and 'Max.
  - 'Pos and 'Val.
  - 'Tag.
  - 'Range on array objects (not subtypes), but only as the right
    operand of the membership (`in`) operator.
  - 'Access, 'Unchecked_Access, and
    'Unrestricted_Access (a GNAT extension).
  - 'Address.
- The names in
  `Characters.Latin_1` are not available and
  concatenation is not implemented. Thus, escape characters in strings are
  not currently available.
- Equality tests (`` `=' `` and `` `/=' ``) on arrays test for bitwise
  equality of representations. They will generally work correctly
  for strings and arrays whose elements have integer or enumeration types.
  They may not work correctly for arrays whose element
  types have user-defined equality, for arrays of real values
  (in particular, IEEE-conformant floating point, because of negative
  zeroes and NaNs), and for arrays whose elements contain unused bits with
  indeterminate values.
- The other component-by-component array operations (`and`, `or`,
  `xor`, `not`, and relational tests other than equality)
  are not implemented.
- There are no record or array aggregates.
- Calls to dispatching subprograms are not implemented.
- The overloading algorithm is much more limited (i.e., less selective)
  than that of real Ada. It makes only limited use of the context in which a subexpression
  appears to resolve its meaning, and it is much looser in its rules for allowing
  type matches. As a result, some function calls will be ambiguous, and the user
  will be asked to choose the proper resolution.
- The `new` operator is not implemented.
- Entry calls are not implemented.
- Aside from printing, arithmetic operations on the native VAX floating-point
  formats are not supported.
- It is not possible to slice a packed array.

#### [Additions to Ada](Debugging%20with%20GDB.md#apple-krhugmjtgq)

As it does for other languages, GDB makes certain generic
extensions to Ada (see section [Expressions](Examining%20Data.md#apple-kncugnjx)):

- If the expression E is a variable residing in memory
  (typically a local variable or array element) and N is
  a positive integer, then `E@N` displays the values of
  E and the N-1 adjacent variables following it in memory as an array.
  In Ada, this operator is generally not necessary, since its prime use
  is in displaying parts of an array, and slicing will usually do this in Ada.
  However, there are occasional uses when debugging programs
  in which certain debugging information has been optimized away.
- `B::var` means "the variable named var that appears
  in function or file B." When B is a file name, you must typically
  surround it in single quotes.
- The expression `{type} addr` means "the variable of type
  type that appears at address addr."
- A name starting with `` `$' `` is a convenience variable
  (see section [Convenience variables](Examining%20Data.md#apple-kncugnrv)) or a machine register (see section [Registers](Examining%20Data.md#apple-kncugnrw)).

In addition, GDB provides a few other shortcuts and outright additions specific
to Ada:

- The assignment statement is allowed as an expression, returning
  its right-hand operand as its value. Thus, you may enter

  ```
  set x := y + 3
  print A(tmp := y + 1)
  ```
- The semicolon is allowed as an "operator," returning as its value
  the value of its right-hand operand.
  This allows, for example,
  complex conditional breaks:

  ```
  break f
  condition 1 (report(i); k += 1; A(k) > 100)
  ```
- Rather than use catenation and symbolic character names to introduce special
  characters into strings, one may instead use a special bracket notation,
  which is also used to print strings. A sequence of characters of the form
  `` `["XX"]' `` within a string or character literal denotes the
  (single) character whose numeric encoding is XX in hexadecimal. The
  sequence of characters `` `["""]' `` also denotes a single quotation mark
  in strings. For example,

  ```
     "One line.["0a"]Next line.["0a"]"
  ```

  contains an ASCII newline character (`Ada.Characters.Latin_1.LF`) after each
  period.
- The subtype used as a prefix for the attributes 'Pos, 'Min, and
  'Max is optional (and is ignored in any case). For example, it is valid
  to write

  ```
  print 'max(x, y)
  ```
- When printing arrays, GDB uses positional notation when the
  array has a lower bound of 1, and uses a modified named notation otherwise.
  For example, a one-dimensional array of three integers with a lower bound of 3 might print as

  ```
  (3 => 10, 17, 1)
  ```

  That is, in contrast to valid Ada, only the first component has a `=>`
  clause.
- You may abbreviate attributes in expressions with any unique,
  multi-character subsequence of
  their names (an exact match gets preference).
  For example, you may use a'len, a'gth, or a'lh
  in place of a'length.
- 
  Since Ada is case-insensitive, the debugger normally maps identifiers you type
  to lower case. The GNAT compiler uses upper-case characters for
  some of its internal identifiers, which are normally of no interest to users.
  For the rare occasions when you actually have to look at them,
  enclose them in angle brackets to avoid the lower-case mapping.
  For example,

  ```
  gdb print <JMPBUF_SAVE>[0]
  ```
- Printing an object of class-wide type or dereferencing an
  access-to-class-wide value will display all the components of the object's
  specific type (as indicated by its run-time tag). Likewise, component
  selection on such a value will operate on the specific type of the
  object.

#### [Stopping at the Very Beginning](Debugging%20with%20GDB.md#apple-krhugmjtgu)

It is sometimes necessary to debug the program during elaboration, and
before reaching the main procedure.
As defined in the Ada Reference
Manual, the elaboration code is invoked from a procedure called
`adainit`. To run your program up to the beginning of
elaboration, simply use the following two commands:
`tbreak adainit` and `run`.

#### [Known Peculiarities of Ada Mode](Debugging%20with%20GDB.md#apple-krhugmjtgy)

Besides the omissions listed previously (see section [Omissions from Ada](#apple-kncugmjtgm)),
we know of several problems with and limitations of Ada mode in
GDB,
some of which will be fixed with planned future releases of the debugger
and the GNU Ada compiler.

- Currently, the debugger
  has insufficient information to determine whether certain pointers represent
  pointers to objects or the objects themselves.
  Thus, the user may have to tack an extra `.all` after an expression
  to get it printed properly.
- Static constants that the compiler chooses not to materialize as objects in
  storage are invisible to the debugger.
- Named parameter associations in function argument lists are ignored (the
  argument lists are treated as positional).
- Many useful library packages are currently invisible to the debugger.
- Fixed-point arithmetic, conversions, input, and output is carried out using
  floating-point arithmetic, and may give results that only approximate those on
  the host machine.
- The type of the 'Address attribute may not be `System.Address`.
- The GNAT compiler never generates the prefix `Standard` for any of
  the standard symbols defined by the Ada language. GDB knows about
  this: it will strip the prefix from names when you use it, and will never
  look for a name you have so qualified among local symbols, nor match against
  symbols in other packages or subprograms. If you have
  defined entities anywhere in your program other than parameters and
  local variables whose simple names match names in `Standard`,
  GNAT's lack of qualification here can cause confusion. When this happens,
  you can usually resolve the confusion
  by qualifying the problematic names with package
  `Standard` explicitly.

## [Unsupported languages](Debugging%20with%20GDB.md#apple-krhugmjtg4)

In addition to the other fully-supported programming languages,
GDB also provides a pseudo-language, called `minimal`.
It does not represent a real programming language, but provides a set
of capabilities close to what the C or assembly languages provide.
This should allow most simple operations to be performed while debugging
an application that uses a language currently not supported by GDB.

If the language is set to `auto`, GDB will automatically
select this language if the current frame corresponds to an unsupported
language.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Debugging%20Programs%20That%20Use%20Overlays.md), [next](Examining%20the%20Symbol%20Table.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
