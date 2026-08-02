---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_10.html
archived_at: '2026-07-15T07:31:03.184230Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Examining%20Data.md), [next](Tracepoints.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [C Preprocessor Macros](Debugging%20with%20GDB.md#apple-krhugnzz)

Some languages, such as C and C++, provide a way to define and invoke
"preprocessor macros" which expand into strings of tokens.
GDB can evaluate expressions containing macro invocations, show
the result of macro expansion, and show a macro's definition, including
where it was defined.

You may need to compile your program specially to provide GDB
with information about preprocessor macros. Most compilers do not
include macros in their debugging information, even when you compile
with the @option{-g} flag. See section [Compiling for debugging](Running%20Programs%20Under%20GDB.md#apple-kncugmjz).

A program may define a macro at one point, remove that definition later,
and then provide a different definition after that. Thus, at different
points in the program, a macro may have different definitions, or have
no definition at all. If there is a current stack frame, GDB
uses the macros in scope at that frame's source code line. Otherwise,
GDB uses the macros in scope at the current listing location;
see section [Printing source lines](Examining%20Source%20Files.md#apple-kncugnjq).

At the moment, GDB does not support the `##`
token-splicing operator, the `#` stringification operator, or
variable-arity macros.

Whenever GDB evaluates an expression, it always expands any
macro invocations present in the expression. GDB also provides
the following commands for working with macros explicitly.

**`macro expand expression`**
: 

**`macro exp expression`**
: Show the results of expanding all preprocessor macro invocations in
expression. Since GDB simply expands macros, but does
not parse the result, expression need not be a valid expression;
it can be any string of tokens.

**`macro expand-once expression`**
:

**`macro exp1 expression`**
: 
_(This command is not yet implemented.)_ Show the results of
expanding those preprocessor macro invocations that appear explicitly in
expression. Macro invocations appearing in that expansion are
left unchanged. This command allows you to see the effect of a
particular macro more clearly, without being confused by further
expansions. Since GDB simply expands macros, but does not
parse the result, expression need not be a valid expression; it
can be any string of tokens.

**`info macro macro`**
: Show the definition of the macro named macro, and describe the
source location where that definition was established.

**`macro define macro replacement-list`**
:

**`macro define macro(arglist) replacement-list`**
: _(This command is not yet implemented.)_ Introduce a definition for a
preprocessor macro named macro, invocations of which are replaced
by the tokens given in replacement-list. The first form of this
command defines an "object-like" macro, which takes no arguments; the
second form defines a "function-like" macro, which takes the arguments
given in arglist.
A definition introduced by this command is in scope in every expression
evaluated in GDB, until it is removed with the @command{macro
undef} command, described below. The definition overrides all
definitions for macro present in the program being debugged, as
well as any previous user-supplied definition.

**`macro undef macro`**
: _(This command is not yet implemented.)_ Remove any user-supplied
definition for the macro named macro. This command only affects
definitions provided with the @command{macro define} command, described
above; it cannot remove definitions present in the program being
debugged.

**`macro list`**
: _(This command is not yet implemented.)_ List all the macros
defined using the `macro define` command.

Here is a transcript showing the above commands in action. First, we
show our source files:

```c
$ cat sample.c
#include <stdio.h>
#include "sample.h"

#define M 42
#define ADD(x) (M + x)

main ()
{
#define N 28
  printf ("Hello, world!\n");
#undef N
  printf ("We're so creative.\n");
#define N 1729
  printf ("Goodbye, world!\n");
}
$ cat sample.h
#define Q <
$
```

Now, we compile the program using the GNU C compiler, GCC.
We pass the @option{-gdwarf-2} and @option{-g3} flags to ensure the
compiler includes information about preprocessor macros in the debugging
information.

```
$ gcc -gdwarf-2 -g3 sample.c -o sample
$
```

Now, we start GDB on our sample program:

```
$ gdb -nw sample
GNU gdb 2002-05-06-cvs
Copyright 2002 Free Software Foundation, Inc.
GDB is free software, ...
(gdb)
```

We can expand macros and examine their definitions, even when the
program is not running. GDB uses the current listing position
to decide which macro definitions are in scope:

```
(gdb) list main
3
4       #define M 42
5       #define ADD(x) (M + x)
6
7       main ()
8       {
9       #define N 28
10        printf ("Hello, world!\n");
11      #undef N
12        printf ("We're so creative.\n");
(gdb) info macro ADD
Defined at /home/jimb/gdb/macros/play/sample.c:5
#define ADD(x) (M + x)
(gdb) info macro Q
Defined at /home/jimb/gdb/macros/play/sample.h:1
  included at /home/jimb/gdb/macros/play/sample.c:2
#define Q <
(gdb) macro expand ADD(1)
expands to: (42 + 1)
(gdb) macro expand-once ADD(1)
expands to: once (M + 1)
(gdb)
```

In the example above, note that @command{macro expand-once} expands only
the macro invocation explicit in the original text -- the invocation of
`ADD` -- but does not expand the invocation of the macro `M`,
which was introduced by `ADD`.

Once the program is running, GDB uses the macro definitions in force at
the source line of the current stack frame:

```
(gdb) break main
Breakpoint 1 at 0x8048370: file sample.c, line 10.
(gdb) run
Starting program: /home/jimb/gdb/macros/play/sample

Breakpoint 1, main () at sample.c:10
10        printf ("Hello, world!\n");
(gdb)
```

At line 10, the definition of the macro `N` at line 9 is in force:

```
(gdb) info macro N
Defined at /home/jimb/gdb/macros/play/sample.c:9
#define N 28
(gdb) macro expand N Q M
expands to: 28 < 42
(gdb) print N Q M
$1 = 1
(gdb)
```

As we step over directives that remove `N`'s definition, and then
give it a new definition, GDB finds the definition (or lack
thereof) in force at each point:

```
(gdb) next
Hello, world!
12        printf ("We're so creative.\n");
(gdb) info macro N
The symbol `N' has no definition as a C/C++ preprocessor macro
at /home/jimb/gdb/macros/play/sample.c:12
(gdb) next
We're so creative.
14        printf ("Goodbye, world!\n");
(gdb) info macro N
Defined at /home/jimb/gdb/macros/play/sample.c:13
#define N 1729
(gdb) macro expand N Q M
expands to: 1729 < 42
(gdb) print N Q M
$2 = 0
(gdb)
```

---

Go to the [first](Summary%20of%20GDB.md), [previous](Examining%20Data.md), [next](Tracepoints.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
