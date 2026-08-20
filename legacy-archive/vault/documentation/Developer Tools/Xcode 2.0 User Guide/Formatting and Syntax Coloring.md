---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/ed_text_editing_prefs/ed_preferences.html
archived_at: '2026-07-15T07:29:48.006042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Code%20Completion.md)[Previous](The%20Xcode%20Editor.md)

# Formatting and Syntax Coloring

Xcode provides a number of formatting and coloring
options to help you keep your code well formed and readable. Syntax
coloring makes it easy to understand the structure of your code
by using different fonts or colors to identify different code elements,
such as comments. With syntax-aware indenting, Xcode makes it simple
to keep your code well-formed and neat by automatically indenting
code and formatting it as appropriate for the current context. This chapter
describes options for indenting code, matching parentheses, and
using syntax coloring.

Xcode uses colors and fonts to distinguish among different
types of code elements in a source code file. For example, you can
display comments in green and keywords in boldface. Xcode maintains
syntax coloring rules that specify a color and font for each code element
you can customize. These rules apply to all languages for which
Xcode supports syntax coloring.

Xcode supports syntax coloring for many different programming
languages; to see the languages that it supports, use the Format
> Syntax Coloring menu. Xcode uses a file’s type to determine
how to interpret and color the contents of the file.

By default, syntax-coloring is enabled for all files that
you open in Xcode’s editor. You can disable syntax-coloring, or
customize the syntax-coloring rules, in the Fonts & Colors pane of
Xcode Preferences. For more information on the Fonts & Colors
preference pane, see [Fonts & Colors Preferences](Xcode%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgewugskiivceorsf). You can also enable or disable syntax-coloring for
individual files open in an editor.

To turn syntax coloring on and off for all files that you
open, choose Xcode > Preferences, click Fonts & Colors, and
use the Syntax Coloring option.

To set the color for a particular type of code element, select
the code element from the Syntax Coloring pop-up menu and change
its color and font. For example, to change the color used for strings,
select Strings from this pop-up menu and click the color well to
bring up the color palette. You can customize syntax coloring rules
for the code elements listed in Table 16-1.

__Table 16-1__  Syntax coloring rules

| Syntax Coloring Rule | Specifies font and color for |
| Comments | Comments in source code, denoted by // or enclosed between ‘/\*’ and ‘\*/’ character pairs. |
| Documentation Comments | Text of documentation using HeaderDoc or JavaDoc style markup. |
| Documentation Comment Keywords | Keywords used to identify documentation using HeaderDoc or JavaDoc style markup. |
| Strings | String constants in source code. |
| Keywords | Keywords in source code. |
| Characters | Character constants in source code. |
| Numbers | Numeric constants in source code. |
| Preprocessor | Preprocessor directives. |

By default, all syntax-coloring rules use the same font—the
font specified by the Editor Font option, described in [Setting Default Fonts and Colors](The%20Xcode%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmzrfvbegskcifbesry)—but
different colors. You can, however, have Xcode change both font
and color based on the code element. To use other fonts for other
types of code elements, choose Xcode > Preferences, click Fonts
& Colors, and select the “Allow separate fonts” option.
Unless this option is enabled, Xcode does not allow you to change
the font for an individual syntax-coloring rule.

To change the font used for a particular code element, choose
that code element from the Syntax Coloring pop-up menu and click
Set Font to open the Fonts window.

Xcode uses the syntax coloring rules in the Fonts & Colors
pane to determine how to display files in its editor. You can, however,
have Xcode preserve syntax coloring when copying and pasting, or
when printing text from a code editor. These options are available in
the Fonts & Colors pane of Xcode Preferences. To have syntax
coloring appear when you print a file, select the “Use colors
when printing” option. Otherwise, if you have specified different
fonts for any of the code elements, Xcode uses those when printing,
but uses only a single color.

To choose whether to preserve colors and fonts when copying
code from an editor, use the “Copy colors and fonts” option.
When this option is enabled, as it is by default, Xcode preserves
both font and color information when it copies text to the clipboard.

You can control syntax coloring for individual files using
the Format > Syntax Coloring menu. This menu lets you turn syntax
coloring on or off for a file in an editor window and set the type
of syntax coloring used for that file. By default, Xcode uses the
file type of the current file to determine how to color the file’s
contents. However, you can specify that Xcode use syntax coloring
appropriate for a particular language by choosing that language from
the Format > Syntax Coloring menu.

To turn syntax coloring off for a file, choose Format >
Syntax Coloring > None. To turn syntax coloring back on, using
the type of the file to determine the appropriate syntax coloring,
choose Format > Syntax Coloring > Default for file type.

To keep all of your code visible in the editor, you can have
Xcode wrap lines when they reach the right edge of a code editor.
To turn on line wrapping for all files you open in Xcode, choose Xcode >
Preferences, click Indentation, and select “Wrap lines in editor.” Otherwise,
Xcode does not move text to the next line until you insert a carriage
return. To wrap lines for an individual file in an editor window,
choose Format > Wrap Lines.

You can also have Xcode automatically indent wrapped lines,
to visually distinguish them from other lines. Enter the number
of spaces to indent lines by in the “Indent wrapped lines by”
field.

Xcode’s editor supports syntax-aware indenting to make it
simple to author neat and readable code. When you use syntax-aware
indenting, Xcode automatically indents and formats your code as
you type; pressing Return or Tab moves the insertion point to the appropriate
level by examining the syntax of the surrounding lines. You can
also choose to indent code manually.

This section shows you how to configure syntax-aware indenting,
how to manually format text in the editor, and how to control the
format of tabs and automatic indentation.

Xcode gives you a number of ways to control how it automatically
formats your code. You can control which characters cause Xcode
to indent a line, what happens when you press the Tab key, and how
Xcode indents braces and comments.

Syntax-aware indenting is not enabled by default; to turn
it on, choose Xcode > Preferences, click Indentation, and select
the “Syntax-aware indenting” option. For more information on
the options available in the Indentation preferences pane, see [Indentation Preferences](Xcode%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgewugskiirfeersb).

When you use syntax-aware indenting, you usually press the
Tab key to tell the editor to indent the text on the current line.
But when you’re at the end of the line, you may want to insert
a tab character before, say, you insert a comment. To choose the
circumstances when pressing the Tab key reindents a line, open the
Indentation pane of Xcode Preferences and use the “Tab indents”
menu in the syntax-aware indenting options. You can choose the following
options:

- “In leading
  white space” indents only when the insertion point is at the beginning
  of a line or in the white space at the beginning of a line.
- “Always” indents when the insertion point is anywhere
  in the line.
- “Never” never indents the line.

To insert a tab character regardless of this option’s setting,
press Option-Tab. Similarly, to perform syntax-aware indenting,
regardless of this option’s setting, press Control-I.

You can have Xcode automatically indent braces to help you
easily see the level of nesting in your code and keep your code
readable. In addition, to help you keep braces balanced, you can
opt to have Xcode automatically insert a closing brace when you
type an opening brace.

To choose how much an opening brace is indented when it appears
on a line by itself, choose Xcode > Preferences, click Indentation,
and use the “Indent solo ‘{’ by:” field. If this field is
greater than 0, Xcode automatically indents opening braces to the
level of the previous line plus the specified number of characters.
By default, the value of this field is 0.

To choose whether to insert a closing brace automatically
when you type an opening brace, choose Xcode > Preferences, click
Indentation, and use the “Automatically insert closing ‘}’”
option.

To choose which characters cause Xcode to a automatically
indent a line whenever they’re typed, choose Xcode > Preferences,
click Indentation, and use the “Automatically indented characters”
options.

You can choose how to indent C++-style (`//`)
comments when they appear on lines by themselves. You cannot automatically
indent C++-style comments that appear at the end of code lines.

To automatically indent C++-style comments that appear on
lines by themselves, choose Xcode > Preferences, click Indentation,
and use the “Indent // comments” option.

To align consecutive C++-style comments that appear on lines
by themselves, choose Xcode > Preferences, click Indentation,
and use the “Align consecutive // comments” option.

Both these options are on by default when syntax-aware indenting
is enabled.

If you choose not to use syntax-aware indenting, you must
do any indentation and formatting manually. When syntax-aware indenting
is disabled, pressing Tab inserts a tab and pressing Return inserts
a carriage return and moves the cursor to the same level as the previous
line. You can also indent a block of text to the left or right by
selecting the text and choosing Format > Shift Left or Format
> Shift Right.

When syntax-aware indenting is turned off, Xcode may still
indent newly added lines to the level of the previous line when
you press Return. To turn this off, add the Return key to the key-equivalents
list of the Insert Newline action in Key Bindings preferences. For information
on configuring key bindings for actions, see [Customizing Key Equivalents](Customizing%20Key%20Equivalents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgawueqkcjjdegsch).

Whether you indent a line manually, or rely on Xcode’s syntax-aware
indenting, you can control the width of tabs and indents, as well
as whether Xcode inserts Tab characters or spaces. You can specify
default values for all files you open in Xcode, as well as customizing
these settings for individual files.

You can set how many spaces to indent when the editor automatically
indents or when you press the Tab key. To set the default indent
or tab width for every file you open, open the Indentation pane
of Xcode Preferences and change the “Tab width” or “Indent
width” setting.

To override the default indent or tab width for one or more
specific files, select the files in the Groups & Files list
and open the inspector window. In the General pane, change the Indent
Width or Tab Width setting.

If you change a file’s default indent or tab width, those
settings are in effect for everyone who views that file.

The editor can insert a series of spaces instead of a tab
whenever it indents code or you press Tab. This ensures that your
code looks the same on other computers no matter how wide their
tabs are set. However, this means that changing the width of tabs
won’t affect code you’ve already written.

To specify that the editor uses spaces instead of tabs, choose Xcode >
Preferences, click Text Editing, and select “Insert ‘tabs’
instead of spaces” option. These options are saved in your own
preferences but not in the file itself. When other people edit the
file, their preferences for that file take effect.

You can also specify this setting on a per-file basis. To
choose whether the editor uses tabs or spaces when editing a certain
file, select the file in the Groups & Files list, open the inspector
window, and select “Editor uses tabs.”

Xcode provides a number of ways to help you match pairs of
delimiters (parentheses, braces, and brackets). Xcode assists you
in the following ways:

- When you
  type a closing delimiter, Xcode causes its counterpart to blink.
- When syntax-aware indenting is enabled, Xcode can automatically
  insert a closing brace each time you type and opening brace, as
  described in [Choosing How to Indent Braces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgqwviucykjcummjqgq).
- When you double-click any delimiter, Xcode selects the entire
  expression that it and its counterpart enclose. You can also choose
  to select the delimiters themselves.
- You can use the Format > Balance command to select the
  text surrounding the insertion point, up to the nearest set of enclosing
  delimiters.

You can further control Xcode’s behavior when selecting
text within a pair of enclosing delimiters in the Text Editing pane
of Xcode Preferences. Use the following Editing Options:

- Select to
  matching brace. When this option is enabled, double-clicking a delimiter automatically
  selects the enclosed expression, including the delimiters themselves. This
  option is enabled by default when you turn on syntax-aware indenting.
- Omit braces in selection. When this option is enabled, double-clicking
  a delimiter selects the enclosed expression, but does not include
  the delimiters themselves in the selection. This option is disabled
  by default.

[Next](Code%20Completion.md)[Previous](The%20Xcode%20Editor.md)

