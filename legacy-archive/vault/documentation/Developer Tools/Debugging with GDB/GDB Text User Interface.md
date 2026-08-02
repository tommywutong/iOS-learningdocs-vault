---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_23.html
archived_at: '2026-07-15T07:31:03.342194Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Command%20Interpreters.md), [next](Using%20GDB%20under%20GNU%20Emacs.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [GDB Text User Interface](Debugging%20with%20GDB.md#apple-krhugmrshe)

The GDB Text User Interface, TUI in short, is a terminal
interface which uses the `curses` library to show the source
file, the assembly output, the program registers and GDB
commands in separate text windows.

The TUI is enabled by invoking GDB using either

`` `gdbtui' `` or `` `gdb -tui' ``.

## [TUI overview](Debugging%20with%20GDB.md#apple-krhugmrtga)

The TUI has two display modes that can be switched while
GDB runs:

- A curses (or TUI) mode in which it displays several text
  windows on the terminal.
- A standard mode which corresponds to the GDB configured without
  the TUI.

In the TUI mode, GDB can display several text window
on the terminal:

**_command_**
: This window is the GDB command window with the GDB
prompt and the GDB outputs. The GDB input is still
managed using readline but through the TUI. The _command_
window is always visible.

**_source_**
: The source window shows the source file of the program. The current
line as well as active breakpoints are displayed in this window.

**_assembly_**
: The assembly window shows the disassembly output of the program.

**_register_**
: This window shows the processor registers. It detects when
a register is changed and when this is the case, registers that have
changed are highlighted.

The source and assembly windows show the current program position
by highlighting the current line and marking them with the `` `>' `` marker.
Breakpoints are also indicated with two markers. A first one
indicates the breakpoint type:

**`B`**
: Breakpoint which was hit at least once.

**`b`**
: Breakpoint which was never hit.

**`H`**
: Hardware breakpoint which was hit at least once.

**`h`**
: Hardware breakpoint which was never hit.

The second marker indicates whether the breakpoint is enabled or not:

**`+`**
: Breakpoint is enabled.

**`-`**
: Breakpoint is disabled.

The source, assembly and register windows are attached to the thread
and the frame position. They are updated when the current thread
changes, when the frame changes or when the program counter changes.
These three windows are arranged by the TUI according to several
layouts. The layout defines which of these three windows are visible.
The following layouts are available:

- source
- assembly
- source and assembly
- source and registers
- assembly and registers

On top of the command window a status line gives various information
concerning the current process begin debugged. The status line is
updated when the information it shows changes. The following fields
are displayed:

**_target_**
: Indicates the current gdb target
(see section [Specifying a Debugging Target](Specifying%20a%20Debugging%20Target.md#apple-kncugmjvga)).

**_process_**
: Gives information about the current process or thread number.
When no process is being debugged, this field is set to `No process`.

**_function_**
: Gives the current function name for the selected frame.
The name is demangled if demangling is turned on (see section [Print settings](Examining%20Data.md#apple-kncugnrt)).
When there is no symbol corresponding to the current program counter
the string `??` is displayed.

**_line_**
: Indicates the current line number for the selected frame.
When the current line number is not known the string `??` is displayed.

**_pc_**
: Indicates the current program counter address.

## [TUI Key Bindings](Debugging%20with%20GDB.md#apple-krhugmrtge)

The TUI installs several key bindings in the readline keymaps
(see section [Command Line Editing](Command%20Line%20Editing.md#apple-kncugmrwhe)).
They allow to leave or enter in the TUI mode or they operate
directly on the TUI layout and windows. The TUI also provides
a _SingleKey_ keymap which binds several keys directly to
GDB commands. The following key bindings
are installed for both TUI mode and the GDB standard mode.

**`C-x C-a`**
: 

**`C-x a`**
: 

**`C-x A`**
: Enter or leave the TUI mode. When the TUI mode is left,
the curses window management is left and GDB operates using
its standard mode writing on the terminal directly. When the TUI
mode is entered, the control is given back to the curses windows.
The screen is then refreshed.

**`C-x 1`**
: Use a TUI layout with only one window. The layout will
either be `` `source' `` or `` `assembly' ``. When the TUI mode
is not active, it will switch to the TUI mode.
Think of this key binding as the Emacs `C-x 1` binding.

**`C-x 2`**
: Use a TUI layout with at least two windows. When the current
layout shows already two windows, a next layout with two windows is used.
When a new layout is chosen, one window will always be common to the
previous layout and the new one.
Think of it as the Emacs `C-x 2` binding.

**`C-x o`**
: Change the active window. The TUI associates several key bindings
(like scrolling and arrow keys) to the active window. This command
gives the focus to the next TUI window.
Think of it as the Emacs `C-x o` binding.

**`C-x s`**
: Use the TUI _SingleKey_ keymap that binds single key to gdb commands
(see section [TUI Single Key Mode](#apple-kncugmrtgi)).

The following key bindings are handled only by the TUI mode:

**`PgUp`**
: 
Scroll the active window one page up.

**`PgDn`**
: Scroll the active window one page down.

**`Up`**
: Scroll the active window one line up.

**`Down`**
: Scroll the active window one line down.

**`Left`**
: Scroll the active window one column left.

**`Right`**
: Scroll the active window one column right.

**`C-L`**
: Refresh the screen.

In the TUI mode, the arrow keys are used by the active window
for scrolling. This means they are available for readline when the
active window is the command window. When the command window
does not have the focus, it is necessary to use other readline
key bindings such as `C-p`, `C-n`, `C-b` and `C-f`.

## [TUI Single Key Mode](Debugging%20with%20GDB.md#apple-krhugmrtgi)

The TUI provides a _SingleKey_ mode in which it installs a particular
key binding in the readline keymaps to connect single keys to
some gdb commands.

**`c`**
: 
continue

**`d`**
: down

**`f`**
: finish

**`n`**
: next

**`q`**
: exit the _SingleKey_ mode.

**`r`**
: run

**`s`**
: step

**`u`**
: up

**`v`**
: info locals

**`w`**
: where

Other keys temporarily switch to the GDB command prompt.
The key that was pressed is inserted in the editing buffer so that
it is possible to type most GDB commands without interaction
with the TUI _SingleKey_ mode. Once the command is entered the TUI
_SingleKey_ mode is restored. The only way to permanently leave
this mode is by hitting `q` or `` `C-x s' ``.

## [TUI specific commands](Debugging%20with%20GDB.md#apple-krhugmrtgm)

The TUI has specific commands to control the text windows.
These commands are always available, that is they do not depend on
the current terminal mode in which GDB runs. When GDB
is in the standard mode, using these commands will automatically switch
in the TUI mode.

**`info win`**
: 
List and give the size of all displayed windows.

**`layout next`**
: 
Display the next layout.

**`layout prev`**
: Display the previous layout.

**`layout src`**
: Display the source window only.

**`layout asm`**
: Display the assembly window only.

**`layout split`**
: Display the source and assembly window.

**`layout regs`**
: Display the register window together with the source or assembly window.

**`focus next | prev | src | asm | regs | split`**
: 
Set the focus to the named window.
This command allows to change the active window so that scrolling keys
can be affected to another window.

**`refresh`**
: 
Refresh the screen. This is similar to using `C-L` key.

**`tui reg float`**
: 
Show the floating point registers in the register window.

**`tui reg general`**
: Show the general registers in the register window.

**`tui reg next`**
: Show the next register group. The list of register groups as well as
their order is target specific. The predefined register groups are the
following: `general`, `float`, `system`, `vector`,
`all`, `save`, `restore`.

**`tui reg system`**
: Show the system registers in the register window.

**`update`**
: 
Update the source window and the current execution point.

**`winheight name +count`**
:

**`winheight name -count`**
: 
Change the height of the window name by count
lines. Positive counts increase the height, while negative counts
decrease it.

**`tabset`**
: 
Set the width of tab stops to be nchars characters.

## [TUI configuration variables](Debugging%20with%20GDB.md#apple-krhugmrtgq)

The TUI has several configuration variables that control the
appearance of windows on the terminal.

**`set tui border-kind kind`**
: 
Select the border appearance for the source, assembly and register windows.
The possible values are the following:

**`space`**
: Use a space character to draw the border.

**`ascii`**
: Use ascii characters + - and | to draw the border.

**`acs`**
: Use the Alternate Character Set to draw the border. The border is
drawn using character line graphics if the terminal supports them.

**`set tui active-border-mode mode`**
: 
Select the attributes to display the border of the active window.
The possible values are `normal`, `standout`, `reverse`,
`half`, `half-standout`, `bold` and `bold-standout`.

**`set tui border-mode mode`**
: 
Select the attributes to display the border of other windows.
The mode can be one of the following:

**`normal`**
: Use normal attributes to display the border.

**`standout`**
: Use standout mode.

**`reverse`**
: Use reverse video mode.

**`half`**
: Use half bright mode.

**`half-standout`**
: Use half bright and standout mode.

**`bold`**
: Use extra bright or bold mode.

**`bold-standout`**
: Use extra bright or bold and standout mode.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Command%20Interpreters.md), [next](Using%20GDB%20under%20GNU%20Emacs.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
