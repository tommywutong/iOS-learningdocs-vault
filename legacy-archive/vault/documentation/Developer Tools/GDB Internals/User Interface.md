---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_4.html
archived_at: '2026-07-15T07:31:03.848317Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Algorithms.md), [next](libgdb.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [User Interface](GDB%20Internals.md#apple-krhugmjx)

GDB has several user interfaces. Although the command-line interface
is the most common and most familiar, there are others.

## [Command Interpreter](GDB%20Internals.md#apple-krhugmjy)

The command interpreter in GDB is fairly simple. It is designed to
allow for the set of commands to be augmented dynamically, and also
has a recursive subcommand capability, where the first argument to
a command may itself direct a lookup on a different command list.

For instance, the `` `set' `` command just starts a lookup on the
`setlist` command list, while `` `set thread' `` recurses
to the `set_thread_cmd_list`.

To add commands in general, use `add_cmd`. `add_com` adds to
the main command list, and should be used for those commands. The usual
place to add commands is in the `_initialize_xyz` routines at
the ends of most source files.

To add paired `` `set' `` and `` `show' `` commands, use
`add_setshow_cmd` or `add_setshow_cmd_full`. The former is
a slightly simpler interface which is useful when you don't need to
further modify the new command structures, while the latter returns
the new command structures for manipulation.

Before removing commands from the command set it is a good idea to
deprecate them for some time. Use `deprecate_cmd` on commands or
aliases to set the deprecated flag. `deprecate_cmd` takes a
`struct cmd_list_element` as it's first argument. You can use the
return value from `add_com` or `add_cmd` to deprecate the
command immediately after it is created.

The first time a command is used the user will be warned and offered a
replacement (if one exists). Note that the replacement string passed to
`deprecate_cmd` should be the full name of the command, i.e. the
entire string the user should type at the command line.

## [UI-Independent Output--the `ui_out` Functions](gdbint_toc.md#apple-krhugmjz)

The `ui_out` functions present an abstraction level for the
GDB output code. They hide the specifics of different user
interfaces supported by GDB, and thus free the programmer
from the need to write several versions of the same code, one each for
every UI, to produce output.

### [Overview and Terminology](GDB%20Internals.md#apple-krhugmrq)

In general, execution of each GDB command produces some sort
of output, and can even generate an input request.

Output can be generated for the following purposes:

- to display a _result_ of an operation;
- to convey _info_ or produce side-effects of a requested
  operation;
- to provide a _notification_ of an asynchronous event (including
  progress indication of a prolonged asynchronous operation);
- to display _error messages_ (including warnings);
- to show _debug data_;
- to _query_ or prompt a user for input (a special case).

This section mainly concentrates on how to build result output,
although some of it also applies to other kinds of output.

Generation of output that displays the results of an operation
involves one or more of the following:

- output of the actual data
- formatting the output as appropriate for console output, to make it
  easily readable by humans
- machine oriented formatting--a more terse formatting to allow for easy
  parsing by programs which read GDB's output
- annotation, whose purpose is to help legacy GUIs to identify interesting
  parts in the output

The `ui_out` routines take care of the first three aspects.
Annotations are provided by separate annotation routines. Note that use
of annotations for an interface between a GUI and GDB is
deprecated.

Output can be in the form of a single item, which we call a __field__;
a __list__ consisting of identical fields; a __tuple__ consisting of
non-identical fields; or a __table__, which is a tuple consisting of a
header and a body. In a BNF-like form:

**`<table> ==>`**
: `<header> <body>`

**`<header> ==>`**
: `{ <column> }`

**`<column> ==>`**
: `<width> <alignment> <title>`

**`<body> ==>`**
: `{<row>}`

### [General Conventions](GDB%20Internals.md#apple-krhugmrr)

Most `ui_out` routines are of type `void`, the exceptions are
`ui_out_stream_new` (which returns a pointer to the newly created
object) and the `make_cleanup` routines.

The first parameter is always the `ui_out` vector object, a pointer
to a `struct ui_out`.

The format parameter is like in `printf` family of functions.
When it is present, there must also be a variable list of arguments
sufficient used to satisfy the `%` specifiers in the supplied
format.

When a character string argument is not used in a `ui_out` function
call, a `NULL` pointer has to be supplied instead.

### [Table, Tuple and List Functions](GDB%20Internals.md#apple-krhugmrs)

This section introduces `ui_out` routines for building lists,
tuples and tables. The routines to output the actual data items
(fields) are presented in the next section.

To recap: A __tuple__ is a sequence of __fields__, each field
containing information about an object; a __list__ is a sequence of
fields where each field describes an identical object.

Use the __table__ functions when your output consists of a list of
rows (tuples) and the console output should include a heading. Use this
even when you are listing just one object but you still want the header.

Tables can not be nested, nor can a tuple or list element be a table.
Tuples and lists can be nested up to a maximum of five levels.

The overall structure of the table output code is something like this:

```
  ui_out_table_begin
    ui_out_table_header
    ...
    ui_out_table_body
      ui_out_tuple_begin
        ui_out_field_*
        ...
      ui_out_tuple_end
      ...
  ui_out_table_end
```

Here is the description of table-, tuple- and list-related `ui_out`
functions:

**Function: void __ui_out_table_begin__ _(struct ui_out \*uiout, int nbrofcols, int nr_rows, const char \*tblid)_**
: 
The function `ui_out_table_begin` marks the beginning of the output
of a table. It should always be called before any other `ui_out`
function for a given table. nbrofcols is the number of columns in
the table. nr_rows is the number of rows in the table.
tblid is an optional string identifying the table. The string
pointed to by tblid is copied by the implementation of
`ui_out_table_begin`, so the application can free the string if it
was `malloc`ed.

The companion function `ui_out_table_end`, described below, marks
the end of the table's output.

**Function: void __ui_out_table_header__ _(struct ui_out \*uiout, int width, enum ui_align alignment, const char \*colhdr)_**
: 
`ui_out_table_header` provides the header information for a single
table column. You call this function several times, one each for every
column of the table, after `ui_out_table_begin`, but before
`ui_out_table_body`.

The value of width gives the column width in characters. The
value of alignment is one of `left`, `center`, and
`right`, and it specifies how to align the header: left-justify,
center, or right-justify it. colhdr points to a string that
specifies the column header; the implementation copies that string, so
column header strings in `malloc`ed storage can be freed after the
call.

**Function: void __ui_out_table_body__ _(struct ui_out \*uiout)_**
: 
This function delimits the table header from the table body.

**Function: void __ui_out_table_end__ _(struct ui_out \*uiout)_**
: 
This function signals the end of a table's output. It should be called
after the table body has been produced by the list and field output
functions.

There should be exactly one call to `ui_out_table_end` for each
call to `ui_out_table_begin`, otherwise the `ui_out` functions
will signal an internal error.

The output of the tuples that represent the table rows must follow the
call to `ui_out_table_body` and precede the call to
`ui_out_table_end`. You build a tuple by calling
`ui_out_tuple_begin` and `ui_out_tuple_end`, with suitable
calls to functions which actually output fields between them.

**Function: void __ui_out_tuple_begin__ _(struct ui_out \*uiout, const char \*id)_**
: 
This function marks the beginning of a tuple output. id points
to an optional string that identifies the tuple; it is copied by the
implementation, and so strings in `malloc`ed storage can be freed
after the call.

**Function: void __ui_out_tuple_end__ _(struct ui_out \*uiout)_**
: 
This function signals an end of a tuple output. There should be exactly
one call to `ui_out_tuple_end` for each call to
`ui_out_tuple_begin`, otherwise an internal GDB error will
be signaled.

**Function: struct __cleanup__ _\*make_cleanup_ui_out_tuple_begin_end (struct ui_out \*uiout, const char \*id)_**
: 
This function first opens the tuple and then establishes a cleanup
(see section [Coding](Coding.md#apple-kncugmjqg4)) to close the tuple. It provides a convenient
and correct implementation of the non-portable[(1)](GDB%20Internals-2.md#apple-izhu6vbr) code sequence:

```
struct cleanup *old_cleanup;
ui_out_tuple_begin (uiout, "...");
old_cleanup = make_cleanup ((void(*)(void *)) ui_out_tuple_end,
                            uiout);
```

**Function: void __ui_out_list_begin__ _(struct ui_out \*uiout, const char \*id)_**
: 
This function marks the beginning of a list output. id points to
an optional string that identifies the list; it is copied by the
implementation, and so strings in `malloc`ed storage can be freed
after the call.

**Function: void __ui_out_list_end__ _(struct ui_out \*uiout)_**
: 
This function signals an end of a list output. There should be exactly
one call to `ui_out_list_end` for each call to
`ui_out_list_begin`, otherwise an internal GDB error will
be signaled.

**Function: struct __cleanup__ _\*make_cleanup_ui_out_list_begin_end (struct ui_out \*uiout, const char \*id)_**
: 
Similar to `make_cleanup_ui_out_tuple_begin_end`, this function
opens a list and then establishes cleanup (see section [Coding](Coding.md#apple-kncugmjqg4))
that will close the list.list.

### [Item Output Functions](GDB%20Internals.md#apple-krhugmrt)

The functions described below produce output for the actual data
items, or fields, which contain information about the object.

Choose the appropriate function accordingly to your particular needs.

**Function: void __ui_out_field_fmt__ _(struct ui_out \*uiout, char \*fldname, char \*format, ...)_**
: 
This is the most general output function. It produces the
representation of the data in the variable-length argument list
according to formatting specifications in format, a
`printf`-like format string. The optional argument fldname
supplies the name of the field. The data items themselves are
supplied as additional arguments after format.

This generic function should be used only when it is not possible to
use one of the specialized versions (see below).

**Function: void __ui_out_field_int__ _(struct ui_out \*uiout, const char \*fldname, int value)_**
: 
This function outputs a value of an `int` variable. It uses the
`"%d"` output conversion specification. fldname specifies
the name of the field.

**Function: void __ui_out_field_fmt_int__ _(struct ui_out \*uiout, int width, enum ui_align alignment, const char \*fldname, int value)_**
: 
This function outputs a value of an `int` variable. It differs from
`ui_out_field_int` in that the caller specifies the desired width and alignment of the output.
fldname specifies
the name of the field.

**Function: void __ui_out_field_core_addr__ _(struct ui_out \*uiout, const char \*fldname, CORE_ADDR address)_**
: 
This function outputs an address.

**Function: void __ui_out_field_string__ _(struct ui_out \*uiout, const char \*fldname, const char \*string)_**
: 
This function outputs a string using the `"%s"` conversion
specification.

Sometimes, there's a need to compose your output piece by piece using
functions that operate on a stream, such as `value_print` or
`fprintf_symbol_filtered`. These functions accept an argument of
the type `struct ui_file *`, a pointer to a `ui_file` object
used to store the data stream used for the output. When you use one
of these functions, you need a way to pass their results stored in a
`ui_file` object to the `ui_out` functions. To this end,
you first create a `ui_stream` object by calling
`ui_out_stream_new`, pass the `stream` member of that
`ui_stream` object to `value_print` and similar functions,
and finally call `ui_out_field_stream` to output the field you
constructed. When the `ui_stream` object is no longer needed,
you should destroy it and free its memory by calling
`ui_out_stream_delete`.

**Function: struct __ui_stream__ _\*ui_out_stream_new (struct ui_out \*uiout)_**
: 
This function creates a new `ui_stream` object which uses the
same output methods as the `ui_out` object whose pointer is
passed in uiout. It returns a pointer to the newly created
`ui_stream` object.

**Function: void __ui_out_stream_delete__ _(struct ui_stream \*streambuf)_**
: 
This functions destroys a `ui_stream` object specified by
streambuf.

**Function: void __ui_out_field_stream__ _(struct ui_out \*uiout, const char \*fieldname, struct ui_stream \*streambuf)_**
: 
This function consumes all the data accumulated in
`streambuf->stream` and outputs it like
`ui_out_field_string` does. After a call to
`ui_out_field_stream`, the accumulated data no longer exists, but
the stream is still valid and may be used for producing more fields.

__Important:__ If there is any chance that your code could bail
out before completing output generation and reaching the point where
`ui_out_stream_delete` is called, it is necessary to set up a
cleanup, to avoid leaking memory and other resources. Here's a
skeleton code to do that:

```
 struct ui_stream *mybuf = ui_out_stream_new (uiout);
 struct cleanup *old = make_cleanup (ui_out_stream_delete, mybuf);
 ...
 do_cleanups (old);
```

If the function already has the old cleanup chain set (for other kinds
of cleanups), you just have to add your cleanup to it:

```
  mybuf = ui_out_stream_new (uiout);
  make_cleanup (ui_out_stream_delete, mybuf);
```

Note that with cleanups in place, you should not call
`ui_out_stream_delete` directly, or you would attempt to free the
same buffer twice.

### [Utility Output Functions](GDB%20Internals.md#apple-krhugmru)

**Function: void __ui_out_field_skip__ _(struct ui_out \*uiout, const char \*fldname)_**
: 
This function skips a field in a table. Use it if you have to leave
an empty field without disrupting the table alignment. The argument
fldname specifies a name for the (missing) filed.

**Function: void __ui_out_text__ _(struct ui_out \*uiout, const char \*string)_**
: 
This function outputs the text in string in a way that makes it
easy to be read by humans. For example, the console implementation of
this method filters the text through a built-in pager, to prevent it
from scrolling off the visible portion of the screen.

Use this function for printing relatively long chunks of text around
the actual field data: the text it produces is not aligned according
to the table's format. Use `ui_out_field_string` to output a
string field, and use `ui_out_message`, described below, to
output short messages.

**Function: void __ui_out_spaces__ _(struct ui_out \*uiout, int nspaces)_**
: 
This function outputs nspaces spaces. It is handy to align the
text produced by `ui_out_text` with the rest of the table or
list.

**Function: void __ui_out_message__ _(struct ui_out \*uiout, int verbosity, const char \*format, ...)_**
: 
This function produces a formatted message, provided that the current
verbosity level is at least as large as given by verbosity. The
current verbosity level is specified by the user with the `` `set
verbositylevel' `` command.[(2)](GDB%20Internals-2.md#apple-izhu6vbs)

**Function: void __ui_out_wrap_hint__ _(struct ui_out \*uiout, char \*indent)_**
: 
This function gives the console output filter (a paging filter) a hint
of where to break lines which are too long. Ignored for all other
output consumers. indent, if non-`NULL`, is the string to
be printed to indent the wrapped text on the next line; it must remain
accessible until the next call to `ui_out_wrap_hint`, or until an
explicit newline is produced by one of the other functions. If
indent is `NULL`, the wrapped text will not be indented.

**Function: void __ui_out_flush__ _(struct ui_out \*uiout)_**
: 
This function flushes whatever output has been accumulated so far, if
the UI buffers output.

### [Examples of Use of `ui_out` functions](gdbint_toc.md#apple-krhugmrv)

This section gives some practical examples of using the `ui_out`
functions to generalize the old console-oriented code in
GDB. The examples all come from functions defined on the
`breakpoints.c' file.

This example, from the `breakpoint_1` function, shows how to
produce a table.

The original code was:

```
 if (!found_a_breakpoint++)
   {
     annotate_breakpoints_headers ();

     annotate_field (0);
     printf_filtered ("Num ");
     annotate_field (1);
     printf_filtered ("Type           ");
     annotate_field (2);
     printf_filtered ("Disp ");
     annotate_field (3);
     printf_filtered ("Enb ");
     if (addressprint)
       {
         annotate_field (4);
         printf_filtered ("Address    ");
       }
     annotate_field (5);
     printf_filtered ("What\n");

     annotate_breakpoints_table ();
   }
```

Here's the new version:

```
  nr_printable_breakpoints = ...;

  if (addressprint)
    ui_out_table_begin (ui, 6, nr_printable_breakpoints, "BreakpointTable");
  else
    ui_out_table_begin (ui, 5, nr_printable_breakpoints, "BreakpointTable");

  if (nr_printable_breakpoints > 0)
    annotate_breakpoints_headers ();
  if (nr_printable_breakpoints > 0)
    annotate_field (0);
  ui_out_table_header (uiout, 3, ui_left, "number", "Num");		/* 1 */
  if (nr_printable_breakpoints > 0)
    annotate_field (1);
  ui_out_table_header (uiout, 14, ui_left, "type", "Type");		/* 2 */
  if (nr_printable_breakpoints > 0)
    annotate_field (2);
  ui_out_table_header (uiout, 4, ui_left, "disp", "Disp");		/* 3 */
  if (nr_printable_breakpoints > 0)
    annotate_field (3);
  ui_out_table_header (uiout, 3, ui_left, "enabled", "Enb");	/* 4 */
  if (addressprint)
    {
     if (nr_printable_breakpoints > 0)
       annotate_field (4);
     if (TARGET_ADDR_BIT <= 32)
       ui_out_table_header (uiout, 10, ui_left, "addr", "Address");/* 5 */
     else
       ui_out_table_header (uiout, 18, ui_left, "addr", "Address");/* 5 */
    }
  if (nr_printable_breakpoints > 0)
    annotate_field (5);
  ui_out_table_header (uiout, 40, ui_noalign, "what", "What");	/* 6 */
  ui_out_table_body (uiout);
  if (nr_printable_breakpoints > 0)
    annotate_breakpoints_table ();
```

This example, from the `print_one_breakpoint` function, shows how
to produce the actual data for the table whose structure was defined
in the above example. The original code was:

```swift
   annotate_record ();
   annotate_field (0);
   printf_filtered ("%-3d ", b->number);
   annotate_field (1);
   if ((int)b->type > (sizeof(bptypes)/sizeof(bptypes[0]))
       || ((int) b->type != bptypes[(int) b->type].type))
     internal_error ("bptypes table does not describe type #%d.",
                     (int)b->type);
   printf_filtered ("%-14s ", bptypes[(int)b->type].description);
   annotate_field (2);
   printf_filtered ("%-4s ", bpdisps[(int)b->disposition]);
   annotate_field (3);
   printf_filtered ("%-3c ", bpenables[(int)b->enable]);
   ...
```

This is the new version:

```swift
   annotate_record ();
   ui_out_tuple_begin (uiout, "bkpt");
   annotate_field (0);
   ui_out_field_int (uiout, "number", b->number);
   annotate_field (1);
   if (((int) b->type > (sizeof (bptypes) / sizeof (bptypes[0])))
       || ((int) b->type != bptypes[(int) b->type].type))
     internal_error ("bptypes table does not describe type #%d.",
                     (int) b->type);
   ui_out_field_string (uiout, "type", bptypes[(int)b->type].description);
   annotate_field (2);
   ui_out_field_string (uiout, "disp", bpdisps[(int)b->disposition]);
   annotate_field (3);
   ui_out_field_fmt (uiout, "enabled", "%c", bpenables[(int)b->enable]);
   ...
```

This example, also from `print_one_breakpoint`, shows how to
produce a complicated output field using the `print_expression`
functions which requires a stream to be passed. It also shows how to
automate stream destruction with cleanups. The original code was:

```swift
    annotate_field (5);
    print_expression (b->exp, gdb_stdout);
```

The new version is:

```swift
  struct ui_stream *stb = ui_out_stream_new (uiout);
  struct cleanup *old_chain = make_cleanup_ui_out_stream_delete (stb);
  ...
  annotate_field (5);
  print_expression (b->exp, stb->stream);
  ui_out_field_stream (uiout, "what", local_stream);
```

This example, also from `print_one_breakpoint`, shows how to use
`ui_out_text` and `ui_out_field_string`. The original code
was:

```swift
  annotate_field (5);
  if (b->dll_pathname == NULL)
    printf_filtered ("<any library> ");
  else
    printf_filtered ("library \"%s\" ", b->dll_pathname);
```

It became:

```swift
  annotate_field (5);
  if (b->dll_pathname == NULL)
    {
      ui_out_field_string (uiout, "what", "<any library>");
      ui_out_spaces (uiout, 1);
    }
  else
    {
      ui_out_text (uiout, "library \"");
      ui_out_field_string (uiout, "what", b->dll_pathname);
      ui_out_text (uiout, "\" ");
    }
```

The following example from `print_one_breakpoint` shows how to
use `ui_out_field_int` and `ui_out_spaces`. The original
code was:

```swift
  annotate_field (5);
  if (b->forked_inferior_pid != 0)
    printf_filtered ("process %d ", b->forked_inferior_pid);
```

It became:

```swift
  annotate_field (5);
  if (b->forked_inferior_pid != 0)
    {
      ui_out_text (uiout, "process ");
      ui_out_field_int (uiout, "what", b->forked_inferior_pid);
      ui_out_spaces (uiout, 1);
    }
```

Here's an example of using `ui_out_field_string`. The original
code was:

```swift
  annotate_field (5);
  if (b->exec_pathname != NULL)
    printf_filtered ("program \"%s\" ", b->exec_pathname);
```

It became:

```swift
  annotate_field (5);
  if (b->exec_pathname != NULL)
    {
      ui_out_text (uiout, "program \"");
      ui_out_field_string (uiout, "what", b->exec_pathname);
      ui_out_text (uiout, "\" ");
    }
```

Finally, here's an example of printing an address. The original code:

```swift
  annotate_field (4);
  printf_filtered ("%s ",
        hex_string_custom ((unsigned long) b->address, 8));
```

It became:

```swift
  annotate_field (4);
  ui_out_field_core_addr (uiout, "Address", b->address);
```

## [Console Printing](GDB%20Internals.md#apple-krhugmrw)

## [TUI](GDB%20Internals.md#apple-krhugmrx)

---

Go to the [first](Requirements.md), [previous](Algorithms.md), [next](libgdb.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
