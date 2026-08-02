---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_4.html
archived_at: '2026-07-15T07:31:03.597013Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Getting%20In%20and%20Out%20of%20GDB.md), [next](Running%20Programs%20Under%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [GDB Commands](Debugging%20with%20GDB.md#apple-krhugmju)

You can abbreviate a GDB command to the first few letters of the command
name, if that abbreviation is unambiguous; and you can repeat certain
GDB commands by typing just `RET`. You can also use the `TAB`
key to get GDB to fill out the rest of a word in a command (or to
show you the alternatives available, if there is more than one possibility).

## [Command syntax](Debugging%20with%20GDB.md#apple-krhugmjv)

A GDB command is a single line of input. There is no limit on
how long it can be. It starts with a command name, which is followed by
arguments whose meaning depends on the command name. For example, the
command `step` accepts an argument which is the number of times to
step, as in `` `step 5' ``. You can also use the `step` command
with no arguments. Some commands do not allow any arguments.

GDB command names may always be truncated if that abbreviation is
unambiguous. Other possible command abbreviations are listed in the
documentation for individual commands. In some cases, even ambiguous
abbreviations are allowed; for example, `s` is specially defined as
equivalent to `step` even though there are other commands whose
names start with `s`. You can test abbreviations by using them as
arguments to the `help` command.

A blank line as input to GDB (typing just `RET`) means to
repeat the previous command. Certain commands (for example, `run`)
will not repeat this way; these are commands whose unintentional
repetition might cause trouble and which you are unlikely to want to
repeat. User-defined commands can disable this feature; see
section [User-defined commands](Canned%20Sequences%20of%20Commands.md#apple-kncugmrsgq).

The `list` and `x` commands, when you repeat them with
`RET`, construct new arguments rather than repeating
exactly as typed. This permits easy scanning of source or memory.

GDB can also use `RET` in another way: to partition lengthy
output, in a way similar to the common utility `more`
(see section [Screen size](Controlling%20GDB.md#apple-kncugmrrha)). Since it is easy to press one
`RET` too many in this situation, GDB disables command
repetition after any command that generates this sort of display.

Any text from a `#` to the end of the line is a comment; it does
nothing. This is useful mainly in command files (see section [Command files](Canned%20Sequences%20of%20Commands.md#apple-kncugmrsgy)).

The `C-o` binding is useful for repeating a complex sequence of
commands. This command accepts the current line, like `RET`, and
then fetches the next line relative to the current line from the history
for editing.

## [Command completion](Debugging%20with%20GDB.md#apple-krhugmjw)

GDB can fill in the rest of a word in a command for you, if there is
only one possibility; it can also show you what the valid possibilities
are for the next word in a command, at any time. This works for GDB
commands, GDB subcommands, and the names of symbols in your program.

Press the `TAB` key whenever you want GDB to fill out the rest
of a word. If there is only one possibility, GDB fills in the
word, and waits for you to finish the command (or press `RET` to
enter it). For example, if you type

```
(gdb) info bre TAB
```

GDB fills in the rest of the word `` `breakpoints' ``, since that is
the only `info` subcommand beginning with `` `bre' ``:

```
(gdb) info breakpoints
```

You can either press `RET` at this point, to run the `info
breakpoints` command, or backspace and enter something else, if
`` `breakpoints' `` does not look like the command you expected. (If you
were sure you wanted `info breakpoints` in the first place, you
might as well just type `RET` immediately after `` `info bre' ``,
to exploit command abbreviations rather than command completion).

If there is more than one possibility for the next word when you press
`TAB`, GDB sounds a bell. You can either supply more
characters and try again, or just press `TAB` a second time;
GDB displays all the possible completions for that word. For
example, you might want to set a breakpoint on a subroutine whose name
begins with `` `make_' ``, but when you type `b make_TAB` GDB
just sounds the bell. Typing `TAB` again displays all the
function names in your program that begin with those characters, for
example:

```
(gdb) b make_ TAB
GDB sounds bell; press TAB again, to see:
make_a_section_from_file     make_environ
make_abs_section             make_function_type
make_blockvector             make_pointer_type
make_cleanup                 make_reference_type
make_command                 make_symbol_completion_list
(gdb) b make_
```

After displaying the available possibilities, GDB copies your
partial input (`` `b make_' `` in the example) so you can finish the
command.

If you just want to see the list of alternatives in the first place, you
can press `M-?` rather than pressing `TAB` twice. `M-?`
means `META ?`. You can type this either by holding down a
key designated as the `META` shift on your keyboard (if there is
one) while typing `?`, or as `ESC` followed by `?`.

Sometimes the string you need, while logically a "word", may contain
parentheses or other characters that GDB normally excludes from
its notion of a word. To permit word completion to work in this
situation, you may enclose words in `'` (single quote marks) in
GDB commands.

The most likely situation where you might need this is in typing the
name of a C++ function. This is because C++ allows function
overloading (multiple definitions of the same function, distinguished
by argument type). For example, when you want to set a breakpoint you
may need to distinguish whether you mean the version of `name`
that takes an `int` parameter, `name(int)`, or the version
that takes a `float` parameter, `name(float)`. To use the
word-completion facilities in this situation, type a single quote
`'` at the beginning of the function name. This alerts
GDB that it may need to consider more information than usual
when you press `TAB` or `M-?` to request word completion:

```
(gdb) b 'bubble( M-?
bubble(double,double)    bubble(int,int)
(gdb) b 'bubble(
```

In some cases, GDB can tell that completing a name requires using
quotes. When this happens, GDB inserts the quote for you (while
completing as much as it can) if you do not type the quote in the first
place:

```
(gdb) b bub TAB
GDB alters your input line to the following, and rings a bell:
(gdb) b 'bubble(
```

In general, GDB can tell that a quote is needed (and inserts it) if
you have not yet started typing the argument list when you ask for
completion on an overloaded symbol.

For more information about overloaded functions, see section [C++ expressions](Using%20GDB%20with%20Different%20Languages.md#apple-kncugmjrge). You can use the command `set
overload-resolution off` to disable overload resolution;
see section [GDB features for C++](Using%20GDB%20with%20Different%20Languages.md#apple-kncugmjrgu).

## [Getting help](Debugging%20with%20GDB.md#apple-krhugmjx)

You can always ask GDB itself for information on its commands,
using the command `help`.

**`help`**
: 

**`h`**
: You can use `help` (abbreviated `h`) with no arguments to
display a short list of named classes of commands:

```
(gdb) help
List of classes of commands:

aliases -- Aliases of other commands
breakpoints -- Making program stop at certain points
data -- Examining data
files -- Specifying and examining files
internals -- Maintenance commands
obscure -- Obscure features
running -- Running the program
stack -- Examining the stack
status -- Status inquiries
support -- Support facilities
tracepoints -- Tracing of program execution without
               stopping the program
user-defined -- User-defined commands

Type "help" followed by a class name for a list of
commands in that class.
Type "help" followed by command name for full
documentation.
Command name abbreviations are allowed if unambiguous.
(gdb)
```

**`help class`**
: Using one of the general help classes as an argument, you can get a
list of the individual commands in that class. For example, here is the
help display for the class `status`:

```
(gdb) help status
Status inquiries.

List of commands:

info -- Generic command for showing things
 about the program being debugged
show -- Generic command for showing things
 about the debugger

Type "help" followed by command name for full
documentation.
Command name abbreviations are allowed if unambiguous.
(gdb)
```

**`help command`**
: With a command name as `help` argument, GDB displays a
short paragraph on how to use that command.

**`apropos args`**
: The `apropos` command searches through all of the GDB
commands, and their documentation, for the regular expression specified in
args. It prints out all matches found. For example:

```
apropos reload
```

results in:

```
set symbol-reloading -- Set dynamic symbol table reloading
                                 multiple times in one run
show symbol-reloading -- Show dynamic symbol table reloading
                                 multiple times in one run
```


**`complete args`**
: The `complete args` command lists all the possible completions
for the beginning of a command. Use args to specify the beginning of the
command you want completed. For example:

```
complete i
```

results in:

```
if
ignore
info
inspect
```

This is intended for use by GNU Emacs.

In addition to `help`, you can use the GDB commands `info`
and `show` to inquire about the state of your program, or the state
of GDB itself. Each command supports many topics of inquiry; this
manual introduces each of them in the appropriate context. The listings
under `info` and under `show` in the Index point to
all the sub-commands. See section [Index](Index.md#apple-kncugmzvgy).

**`info`**
: 

This command (abbreviated `i`) is for describing the state of your
program. For example, you can list the arguments given to your program
with `info args`, list the registers currently in use with `info
registers`, or list the breakpoints you have set with `info breakpoints`.
You can get a complete list of the `info` sub-commands with
`help info`.

**`set`**
: You can assign the result of an expression to an environment variable with
`set`. For example, you can set the GDB prompt to a $-sign with
`set prompt $`.

**`show`**
: In contrast to `info`, `show` is for describing the state of
GDB itself.
You can change most of the things you can `show`, by using the
related command `set`; for example, you can control what number
system is used for displays with `set radix`, or simply inquire
which is currently in use with `show radix`.

To display all the settable parameters and their current
values, you can use `show` with no arguments; you may also use
`info set`. Both commands produce the same display.

Here are three miscellaneous `show` subcommands, all of which are
exceptional in lacking corresponding `set` commands:

**`show version`**
: 

Show what version of GDB is running. You should include this
information in GDB bug-reports. If multiple versions of
GDB are in use at your site, you may need to determine which
version of GDB you are running; as GDB evolves, new
commands are introduced, and old ones may wither away. Also, many
system vendors ship variant versions of GDB, and there are
variant versions of GDB in GNU/Linux distributions as well.
The version number is the same as the one announced when you start
GDB.

**`show copying`**
:

**`info copying`**
: Display information about permission for copying GDB.

**`show warranty`**
:

**`info warranty`**
: Display the GNU "NO WARRANTY" statement, or a warranty,
if your version of GDB comes with one.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Getting%20In%20and%20Out%20of%20GDB.md), [next](Running%20Programs%20Under%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
