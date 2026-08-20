---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_24.html
archived_at: '2026-07-15T07:31:03.351914Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Text%20User%20Interface.md), [next](The%20GDB-MI%20Interface.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Using GDB under GNU Emacs](Debugging%20with%20GDB.md#apple-krhugmrtgu)

A special interface allows you to use GNU Emacs to view (and
edit) the source files for the program you are debugging with
GDB.

To use this interface, use the command `M-x gdb` in Emacs. Give the
executable file you want to debug as an argument. This command starts
GDB as a subprocess of Emacs, with input and output through a newly
created Emacs buffer.

Using GDB under Emacs is just like using GDB normally except for two
things:

- All "terminal" input and output goes through the Emacs buffer.

This applies both to GDB commands and their output, and to the input
and output done by the program you are debugging.

This is useful because it means that you can copy the text of previous
commands and input them again; you can even use parts of the output
in this way.

All the facilities of Emacs' Shell mode are available for interacting
with your program. In particular, you can send signals the usual
way--for example, `C-c C-c` for an interrupt, `C-c C-z` for a
stop.

- GDB displays source code through Emacs.

Each time GDB displays a stack frame, Emacs automatically finds the
source file for that frame and puts an arrow (`` `=>' ``) at the
left margin of the current line. Emacs uses a separate buffer for
source display, and splits the screen to show both your GDB session
and the source.

Explicit GDB `list` or search commands still produce output as
usual, but you probably have no reason to use them from Emacs.

If you specify an absolute file name when prompted for the `M-x
gdb` argument, then Emacs sets your current working directory to where
your program resides. If you only specify the file name, then Emacs
sets your current working directory to to the directory associated
with the previous buffer. In this case, GDB may find your
program by searching your environment's `PATH` variable, but on
some operating systems it might not find the source. So, although the
GDB input and output session proceeds normally, the auxiliary
buffer does not display the current source and line of execution.

The initial working directory of GDB is printed on the top
line of the GDB I/O buffer and this serves as a default for
the commands that specify files for GDB to operate
on. See section [Commands to specify files](GDB%20Files.md#apple-kncugmjug4).

By default, `M-x gdb` calls the program called `gdb'. If you
need to call GDB by a different name (for example, if you
keep several configurations around, with different names) you can
customize the Emacs variable `gud-gdb-command-name` to run the
one you want.

In the GDB I/O buffer, you can use these special Emacs commands in
addition to the standard Shell mode commands:

**`C-h m`**
: Describe the features of Emacs' GDB Mode.

**`C-c C-s`**
: Execute to another source line, like the GDB `step` command; also
update the display window to show the current file and location.

**`C-c C-n`**
: Execute to next source line in this function, skipping all function
calls, like the GDB `next` command. Then update the display window
to show the current file and location.

**`C-c C-i`**
: Execute one instruction, like the GDB `stepi` command; update
display window accordingly.

**`C-c C-f`**
: Execute until exit from the selected stack frame, like the GDB
`finish` command.

**`C-c C-r`**
: Continue execution of your program, like the GDB `continue`
command.

**`C-c <`**
: Go up the number of frames indicated by the numeric argument
(see section `Numeric Arguments' in The GNU Emacs Manual),
like the GDB `up` command.

**`C-c >`**
: Go down the number of frames indicated by the numeric argument, like the
GDB `down` command.

In any source file, the Emacs command `C-x SPC` (`gud-break`)
tells GDB to set a breakpoint on the source line point is on.

If you type `M-x speedbar`, then Emacs displays a separate frame which
shows a backtrace when the GDB I/O buffer is current. Move
point to any frame in the stack and type `RET` to make it become the
current frame and display the associated source in the source buffer.
Alternatively, click `Mouse-2` to make the selected frame become the
current one.

If you accidentally delete the source-display buffer, an easy way to get
it back is to type the command `f` in the GDB buffer, to
request a frame display; when you run under Emacs, this recreates
the source buffer if necessary to show you the context of the current
frame.

The source files displayed in Emacs are in ordinary Emacs buffers
which are visiting the source files in the usual way. You can edit
the files with these buffers if you wish; but keep in mind that GDB
communicates with Emacs in terms of line numbers. If you add or
delete lines from the text, the line numbers that GDB knows cease
to correspond properly with the code.

The description given here is for GNU Emacs version 21.3 and a more
detailed description of its interaction with GDB is given in
the Emacs manual (see section `Debuggers' in The GNU Emacs Manual).

---

Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Text%20User%20Interface.md), [next](The%20GDB-MI%20Interface.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
