---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_2.html
archived_at: '2026-07-15T07:31:03.312174Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Summary%20of%20GDB.md), [next](Getting%20In%20and%20Out%20of%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [A Sample GDB Session](Debugging%20with%20GDB.md#apple-krhugni)

You can use this manual at your leisure to read all about GDB.
However, a handful of commands are enough to get started using the
debugger. This chapter illustrates those commands.

In this sample session, we emphasize user input like this: __input__,
to make it easier to pick out from the surrounding output.

One of the preliminary versions of GNU `m4` (a generic macro
processor) exhibits the following bug: sometimes, when we change its
quote strings from the default, the commands used to capture one macro
definition within another stop working. In the following short `m4`
session, we define a macro `foo` which expands to `0000`; we
then use the `m4` built-in `defn` to define `bar` as the
same thing. However, when we change the open quote string to
`<QUOTE>` and the close quote string to `<UNQUOTE>`, the same
procedure fails to define a new synonym `baz`:

```shell
$ cd gnu/m4
$ ./m4
define(foo,0000)

foo
0000
define(bar,defn(`foo'))

bar
0000
changequote(<QUOTE>,<UNQUOTE>)

define(baz,defn(<QUOTE>foo<UNQUOTE>))
baz
C-d
m4: End of input: 0: fatal error: EOF in string
```

Let us use GDB to try to see what is going on.

```
$ gdb m4
GDB is free software and you are welcome to distribute copies
 of it under certain conditions; type "show copying" to see
 the conditions.
There is absolutely no warranty for GDB; type "show warranty"
 for details.

GDB 6.3.50.20050815-cvs, Copyright 1999 Free Software Foundation, Inc...
(gdb)
```

GDB reads only enough symbol data to know where to find the
rest when needed; as a result, the first prompt comes up very quickly.
We now tell GDB to use a narrower display width than usual, so
that examples fit in this manual.

```
(gdb) set width 70
```

We need to see how the `m4` built-in `changequote` works.
Having looked at the source, we know the relevant subroutine is
`m4_changequote`, so we set a breakpoint there with the GDB
`break` command.

```
(gdb) break m4_changequote
Breakpoint 1 at 0x62f4: file builtin.c, line 879.
```

Using the `run` command, we start `m4` running under GDB
control; as long as control does not reach the `m4_changequote`
subroutine, the program runs as usual:

```
(gdb) run
Starting program: /work/Editorial/gdb/gnu/m4/m4
define(foo,0000)

foo
0000
```

To trigger the breakpoint, we call `changequote`. GDB
suspends execution of `m4`, displaying information about the
context where it stops.

```
changequote(<QUOTE>,<UNQUOTE>)

Breakpoint 1, m4_changequote (argc=3, argv=0x33c70)
    at builtin.c:879
879         if (bad_argc(TOKEN_DATA_TEXT(argv[0]),argc,1,3))
```

Now we use the command `n` (`next`) to advance execution to
the next line of the current function.

```
(gdb) n
882         set_quotes((argc >= 2) ? TOKEN_DATA_TEXT(argv[1])\
 : nil,
```

`set_quotes` looks like a promising subroutine. We can go into it
by using the command `s` (`step`) instead of `next`.
`step` goes to the next line to be executed in _any_
subroutine, so it steps into `set_quotes`.

```
(gdb) s
set_quotes (lq=0x34c78 "<QUOTE>", rq=0x34c88 "<UNQUOTE>")
    at input.c:530
530         if (lquote != def_lquote)
```

The display that shows the subroutine where `m4` is now
suspended (and its arguments) is called a stack frame display. It
shows a summary of the stack. We can use the `backtrace`
command (which can also be spelled `bt`), to see where we are
in the stack as a whole: the `backtrace` command displays a
stack frame for each active subroutine.

```
(gdb) bt
#0  set_quotes (lq=0x34c78 "<QUOTE>", rq=0x34c88 "<UNQUOTE>")
    at input.c:530
#1  0x6344 in m4_changequote (argc=3, argv=0x33c70)
    at builtin.c:882
#2  0x8174 in expand_macro (sym=0x33320) at macro.c:242
#3  0x7a88 in expand_token (obs=0x0, t=209696, td=0xf7fffa30)
    at macro.c:71
#4  0x79dc in expand_input () at macro.c:40
#5  0x2930 in main (argc=0, argv=0xf7fffb20) at m4.c:195
```

We step through a few more lines to see what happens. The first two
times, we can use `` `s' ``; the next two times we use `n` to avoid
falling into the `xstrdup` subroutine.

```
(gdb) s
0x3b5c  532         if (rquote != def_rquote)
(gdb) s
0x3b80  535         lquote = (lq == nil || *lq == '\0') ?  \
def_lquote : xstrdup(lq);
(gdb) n
536         rquote = (rq == nil || *rq == '\0') ? def_rquote\
 : xstrdup(rq);
(gdb) n
538         len_lquote = strlen(rquote);
```

The last line displayed looks a little odd; we can examine the variables
`lquote` and `rquote` to see if they are in fact the new left
and right quotes we specified. We use the command `p`
(`print`) to see their values.

```
(gdb) p lquote
$1 = 0x35d40 "<QUOTE>"
(gdb) p rquote
$2 = 0x35d50 "<UNQUOTE>"
```

`lquote` and `rquote` are indeed the new left and right quotes.
To look at some context, we can display ten lines of source
surrounding the current line with the `l` (`list`) command.

```
(gdb) l
533             xfree(rquote);
534
535         lquote = (lq == nil || *lq == '\0') ? def_lquote\
 : xstrdup (lq);
536         rquote = (rq == nil || *rq == '\0') ? def_rquote\
 : xstrdup (rq);
537
538         len_lquote = strlen(rquote);
539         len_rquote = strlen(lquote);
540     }
541
542     void
```

Let us step past the two lines that set `len_lquote` and
`len_rquote`, and then examine the values of those variables.

```
(gdb) n
539         len_rquote = strlen(lquote);
(gdb) n
540     }
(gdb) p len_lquote
$3 = 9
(gdb) p len_rquote
$4 = 7
```

That certainly looks wrong, assuming `len_lquote` and
`len_rquote` are meant to be the lengths of `lquote` and
`rquote` respectively. We can set them to better values using
the `p` command, since it can print the value of
any expression--and that expression can include subroutine calls and
assignments.

```
(gdb) p len_lquote=strlen(lquote)
$5 = 7
(gdb) p len_rquote=strlen(rquote)
$6 = 9
```

Is that enough to fix the problem of using the new quotes with the
`m4` built-in `defn`? We can allow `m4` to continue
executing with the `c` (`continue`) command, and then try the
example that caused trouble initially:

```
(gdb) c
Continuing.

define(baz,defn(<QUOTE>foo<UNQUOTE>))

baz
0000
```

Success! The new quotes now work just as well as the default ones. The
problem seems to have been just the two typos defining the wrong
lengths. We allow `m4` exit by giving it an EOF as input:

```
C-d
Program exited normally.
```

The message `` `Program exited normally.' `` is from GDB; it
indicates `m4` has finished executing. We can end our GDB
session with the GDB `quit` command.

```
(gdb) quit
```

---

Go to the [first](Summary%20of%20GDB.md), [previous](Summary%20of%20GDB.md), [next](Getting%20In%20and%20Out%20of%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
