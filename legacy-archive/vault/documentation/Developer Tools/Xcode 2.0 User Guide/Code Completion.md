---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/ed_code_completion/ed_code_completion.html
archived_at: '2026-07-15T07:29:41.452029Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Using%20an%20External%20Editor.md)[Previous](Formatting%20and%20Syntax%20Coloring.md)

# Code Completion

Xcode includes a feature, called Code Sense,
which maintains a rich store of information about the symbols defined
in your project and its included files. Xcode uses this feature
as a basis for code completion. Xcode supports code completion for
C, C++, Objective-C, Objective-C++, Java, and AppleScript.

When you are writing code, you often must type out or copy
and paste long identifier names and lists of arguments. Code completion
offers you a shortcut. As you type the beginning of an identifier
or a keyword, Xcode suggests likely matches, based on the text you
have already typed and the surrounding context of the file. This
chapter describes how to use code completion and how to set code
completion options. It also describes text macros, a feature that
provides shortcuts for inserting common code constructs, using the code
completion mechanism.

As you type, Xcode builds a list of likely symbol names, based
on the text you have already typed and the surrounding context of
the file. If completion suggestions are available, Xcode indicates
this by underlining the text that you have entered. You can view and
select from the possible matches by:

1. Bringing
   up the completion list and choosing a symbol name. Pressing the
   Escape key or choosing Edit > Completion List brings up a list
   of all of the possible matches for the current context. For functions
   and methods, this includes the return type as well as the function
   or method prototype. The button in the bottom-right corner of the
   completion list lets you toggle the sort order of the completion
   suggestions. By default, the list is sorted alphabetically, indicated
   by the letter “A” in this button. You can also choose to sort
   the list according to relevance ranking; click the button to change
   the sort order.

   You can choose the appropriate match from this
   list or continue typing to narrow the list further. To enter a symbol
   from the completion list, select it and hit Return or Tab. Xcode
   enters the remaining text for you and optionally inserts placeholders
   for any necessary function or method arguments.

   The
   completion list stays open until you select a completion suggestion
   or dismiss the list by typing the completion key or choosing Edit
   > Completion List again.
2. Cycling through the available completions. Instead of bringing
   up a list of all completions, can you choose to have Xcode insert
   the next available completion directly in your code. When you choose
   Edit > Next Completion or type Control-period, Xcode inserts
   and selects the first completion in the completion list, without displaying
   the entire list. Choosing Edit > Next Completion or typing Control-period again
   replaces the previous completion with the next completion in the
   list, and so forth. In this way, you can cycle through the available
   suggestions until you get the correct symbol name.

__Figure 17-1__  Using
code completion

!

Xcode uses information about symbols and their scope within
your code to determine the contents of the completion list. When
there are syntax errors in the context, Xcode limits its scope analysis
to the current code line.

Xcode also provides keyboard shortcuts for common code completion
tasks. For example, to bring up the completion list, you can type Escape. To
move to the next argument in a declaration that Xcode has completed
for you, type Control–slash. To change the keyboard shortcuts
associated with these commands, open the Key Bindings pane of Xcode Preferences,
as described in [Customizing Key Equivalents](Customizing%20Key%20Equivalents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgawueqkcjjdegsch).
In the Text Key Bindings pane, change the key sequences associated
with the Code Sense actions. These are Code Sense Complete List,
Code Sense Next Completion, Code Sense Previous Completion, Code
Sense Select Next Placeholder and Code Sense Select Previous Placeholder.

The previous section describes the default interface for code
completion. However, Xcode provides a number of options for customizing
code completion behavior. Code completion settings apply to all
projects that you open.

You can control how much or how little information Xcode gives
you as you type. To control how code completion suggestions are
made, use the following options:

- Select “Indicate
  when completions are available” to have Xcode indicate when it
  has suggestions for matching symbols by underling the text you have
  typed. This option is enabled by default. If you turn it off, completions
  are still available to you, but Xcode does not underline the text.
  You can open the completion list to see suggestions, or cycle through
  the available completions, as described in the previous section.
- Select “Automatically suggest on member call / access”
  to have Xcode automatically display the completion list when in
  the context of a function or method call, or when accessing the
  members of a data structure. If you choose this option, you can
  also specify the amount of the delay, after you stop typing, before
  Xcode displays the completion list. Specify the amount of time,
  in seconds, of this delay in the “Suggestion delay” field. By
  default, this delay is half a second.

Xcode also lets you control how functions and methods are
completed. To have Xcode insert the name, as well as placeholders
for the arguments to the function or method, select “Insert argument
placeholders for completions.”Otherwise, Xcode only inserts the
name of the function or method. This option is on by default.

To choose how functions and methods are displayed in the completion
list, use the “Show arguments in pop-up list” option. Select
this option to have Xcode display functions and methods with their
list of arguments in the completion list. Otherwise, Xcode only
displays the function or method name. This option is on by default.

Using code completion to automatically complete symbol names
saves you a lot of typing. In the course of writing source code,
however, you still spend a lot of time typing the same basic code
constructs—such as `alloc` and `init` methods
in Objective-C programs, for example—over and over again. To help
you with this, Xcode includes a set of text macros. Text macros
let you insert common constructs and blocks of code with a menu
item or keystroke, instead of typing them in directly.

You can insert a text macro in either of the following two
ways:

1. Choose Edit
   > Insert Text Macro and then choose a text macro from one of
   the language-specific menus. Xcode provides built-in text macros
   for common C, C++, Objective-C, Java, and HTML constructs.
2. Type the completion prefix for the text macro and use code
   completion to insert the remaining text, just as you would complete
   a symbol name. Each text macro provided by Xcode has a completion
   prefix, a string that Code Sense uses to identify the text macro.
   When you type this string, Xcode includes the text macro in the
   completion list; you can select it from this list or cycle through
   the appropriate completions, as described in [Using Code Completion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgywugsscirbuqrck).

The inserted text includes placeholders for arguments, variables,
and other program-specific information. For example, choosing Edit
> Insert Text Macro > C > If Block inserts the following
text at the current insertion point in the active editor:

```
if (<#condition#>) {
     <#statements#>
}
```

Replace the placeholders `<#condition#>` and `<#statements#>` with
your own code. You can cycle through the placeholders in a text
macro in the same way you can cycle through function arguments with
code completion. A text macro can also define one placeholder to be
replaced with the current selection, if any. When you select text
in the active editor and insert a text macro, Xcode substitutes
the selected text for this placeholder. For the If Block text macro
described above, Xcode substitutes the selected text for the `<#statements#>` placeholder.
For example, if the current selection in the text editor is `CFRelease(someString);`, inserting
the If Block text macro gives you the following:

```
if (<#condition#>) {
CFRelease(someString);
}
```

If there is no selection, Xcode simply inserts the `<#statements#>` placeholder,
as in the previous example.

Some text macros have several variants. For example, the text
macro for inserting an HTML heading has variants for the different
levels of headings. For text macros that have multiple variants,
repeatedly choosing that text macro from the Insert Text Macro menus cycles
through the different versions of that macro. For example, choosing
Insert Text Macro > HTML > Heading a single time inserts `<$(h1)><#!text!#></$(h1)>`;
choosing it again inserts `<$(h2)><#!text!#></$(h2)>`.

[Next](Using%20an%20External%20Editor.md)[Previous](Formatting%20and%20Syntax%20Coloring.md)

