---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/custom_scripts/custom_scripts.html
archived_at: '2026-07-15T07:29:17.730323Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Using%20CVS.md)[Previous](Xcode%20Preferences.md)

# Using Scripts To Customize Xcode

Xcode provides a number of mechanisms for working
with scripts and customizing your work environment, including:

- The ability
  to execute text in a text editor window as a shell command or series
  of commands
- The automatic execution of a startup script when Xcode is
  launched
- The automated creation of an extensible User Scripts menu
  with menu items that execute shell scripts
- A number of built-in script variables and utility scripts
  you can use in menu scripts or other scripts
- A shell-file build phase that lets you add the execution of
  shell script files to the build process for a target. Build phases
  described in [Build Phases](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawugssbi5ceiscj).

Xcode provides a keyboard equivalent for executing any shell
command that appears in a text editor window. To use this feature,
you select the command text and press Control-R. The results appear
below the command in the text editor window, autoscrolling if necessary
to show the output.

Xcode creates a new shell each time you execute a command,
so there is no shared context between different executions. For
example, if you execute a command that changes the directory, the
next command you execute will not execute in that directory. To
overcome this, you can select two commands together and press Control-R.

You might recognize the similarity between this feature and
using the Enter key to execute commands in MPW. One way to take
advantage of this feature is to keep a file of commonly used commands
and execute them as needed. Or you might use an empty text file
as a scratch area to type and execute commands.

You can also add custom menu items to execute frequently used
shell scripts. Any scripts you execute can take advantage of many
special script variables and built-in scripts defined by Xcode.
For more information, see [The Startup Script and the User Scripts Menu](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwviucykjcummjrgy).

Xcode provides a number of scripting mechanisms to enhance
your productivity and customize your work environment. Xcode can
run a startup script every time it is launched. This script can
perform whatever custom actions you want to happen on each startup,
but is also responsible for creating custom menus in its menu bar,
specifically for launching your own specialized scripts. When you
launch Xcode, it looks for a script named `StartupScript` and
executes it if found. Xcode first looks for a StartupScript file
at `~/Library/Application Support/Apple/Developer Tools/`;
if none is found, Xcode falls back to the default StartupScript
file installed at `/Library/Application Support/Apple/Developer
Tools/`. This script can use any shell, as long as it
starts with a standard `#!` comment
to identify the shell.

Xcode provides a default startup script and menu definition
files that together add a User Scripts menu to the Xcode menu bar.
The User Scripts menu is identified by the script icon in the Xcode
menu bar, shown Figure 40-1. A _menu definition file_ is
a special kind of shell script that contains one or more menu definitions
and some associated script statements. A _menu definition_ uses
variables and built-in scripts defined by Xcode to add menus or
menu items to the User Scripts menu (or to other menus). Choosing
one of the resulting menu items causes the associated script statements
to be executed.

The default menu definition files add items to the User Scripts
menu that let you open files, perform searches, add comments to
your code, sort text, and even add HeaderDoc templates that can
help you document your header files. And you can use these files
as examples to help write additional menu definitions.

You can customize Xcode’s existing StartupScript and User
Scripts menu, or you can override them entirely, by placing your
own versions at `~/Library/Application Support/Apple/Developer
Tools/`.

The following sections describe how Xcode creates the User
Scripts menu and provide examples of how you can take advantage
of the startup script and the User Scripts menu to customize your
Xcode environment. For a full description of the available variables
and how they are used in scripts, see [Menu Script Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwueqsdivauurkd).

When you install Xcode, the following files are installed
in `/Library/Application Support/Apple/Developer
Tools/`:

- the default
  version of the script `StartupScript`;
  this version is a Perl script that builds the User Scripts menu
- a `Scripts` folder
  containing a number of menu definition files; these are simply shell scripts
  that define menu items and the commands to execute when those items
  are chosen. Menu definition files are interpreted in UTF-8 encoding,
  which is a strict superset of ASCII, so plain ASCII is fine too

You can override either or both of these default files by
placing your own StartupScript file and Scripts directory at `~/Library/Application
Support/Apple/Developer Tools`. Note that doing so entirely
overrides the default StartupScript or Scripts folder installed
with Xcode. You might find it easier to create copies of Xcode’s
default StartupScript file and Scripts folder and modify these.
If you do so, be aware that you will not automatically see bug fixes
or improvements made to the default scripts installed at `/Library/Application
Support/Apple/Developer Tools/`, as Xcode will
load the scripts you have installed at `~/Library/Application
Support/Apple/Developer Tools`. To work around this, you
can compare the files in the two locations (using `diff` or
a similar comparison tool) and update your copies of the scripts
as needed.

When you launch Xcode, the following steps take place:

1. Xcode looks
   for a StartupScript file finds the file `~/Library/Application
   Support/Apple/Developer Tools/StartupScript` and,
   if found, executes it. If no StartupScript file is found at the
   user location, Xcode looks in the default location, `/Library/Application
   Support/Apple/Developer Tools`. The StartupScript script
   is invoked with no arguments or input and its output is discarded.
2. The startup script looks for directories in `~/Library/Application
   Support/Apple/Developer Tools/Scripts`. If
   no Scripts directory exists at this location, Xcode then looks in
   the default location, `/Library/Application Support/Apple/Developer
   Tools/Scripts`. If the script finds any directories in
   the `Scripts` folder, it
   creates a new menu corresponding to that directory. If Xcode finds
   an image file named `menuIcon.tiff` at
   the top level of the directory, it uses the image as the menu’s
   title in Xcode’s menu bar. Otherwise, it uses the textual name of
   the directory as the menu’s title.

   Take a look inside the `Scripts` directory.
   Navigate through the `10-User Scripts` directory and
   see how the scripts are categorized and divided. Those with the
   extension `.sh` are shell
   files, while those with the extension `.pl` are
   Perl files.
3. For each valid menu definition file Xcode finds within each
   directory, the startup script adds corresponding menu items to the
   appropriate menu.

   - Files with a numeric prefix in their names are added in ascending
     order.
   - Files that do not have a prefix are added alphabetically,
     after files that do have prefixes.
   - Files that have a numeric prefix followed immediately by three
     dashes are interpreted as a request for a menu separator.
   - The User Scripts menu supports a menu hierarchy. The name
     of each immediate subdirectory of `~/Library/Application
     Support/Apple/Developer Tools/Scripts` becomes
     the name of the corresponding menu. The immediate subdirectories
     of each of those directories become submenus of the corresponding
     menu.Menu definition files within the subdirectories are added as
     commands in the corresponding submenu. You can specify where subdirectory
     and submenu names appear in the menus by adding numeric prefixes
     to the filenames.

Figure 40-1 shows the default User Scripts menu that
results from the scripts that ship with Xcode. The Search submenu
is open, showing several menu items. In this case the menu items
do not have key equivalents, though some items in other submenus
do have key equivalents.

__Figure 40-1__  The User Scripts menu

!

You can easily customize your work environment by adding menus,
submenus, and menu items to the menu bar to handle frequently performed
operations. To do so, you create a menu definition file, name it
appropriately to specify its location in the User Scripts menu (or
a menu of your own creation), and place it in the appropriate location
in the `Scripts` directory.

For a simple example, the following steps describe how to
copy one of the menu definition files from the Sort submenu and
use it to add two new menu items to the Sort submenu. That section
also describes how the startup script determines where to insert
menu items (either into the main User Scripts menu or into a submenu),
and how to insert a menu separator.

1. Duplicate
   the file `10-sort.sh` in `~/Library/Application
   Support/Apple/Developer Tools/Scripts/10-User Scripts/50-Sort`.
2. Rename the new file `20-reverse_sort.sh`.
3. Open the file in Xcode.
4. Change the line `# %%%{PBXName=Sort Selection}%%%` to `#
   %%%{PBXName=Reverse Sort Selection}%%%`. This
   line provides the name for the first new menu item.
5. The five lines starting with `# %%%{PBXNewScript}%%%` actually
   define a second menu item. Change the line `#
   %%%{PBXName=Sort File}%%%` to `#
   %%%{PBXName=Reverse Sort File}%%%`. This line
   provides the name for the second new menu item.
6. Change the line `sort <&0` to `sort
   -r <&0`. This tells the sort command
   to reverse the result of comparison, so that lines with greater
   key values appear earlier in the output instead of later.
7. Quit Xcode, then launch it again. The items Reverse Sort Selection
   and Reverse Sort File now appear in the Sort submenu of the User
   Scripts menu. Choosing the items performs sorts that are reversed
   from those performed by the original menu items.

The section [Using Variables in a Menu Definition Script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwueqkki5becr2e) takes a closer
look at the special variables you worked with in this example.

You can remove items from the User Scripts menu by removing
their menu definition files from `~/Library/Application
Support/Apple/Developer Tools/Scripts`. If
you don’t need the User Scripts menu at all, you can either move
the entire `Scripts` directory,
or move the `StartupScript` file, from `~/Library/Application
Support/Apple/Developer Tools.`

Xcode provides a number of variables you can use in menu definition
scripts to get information from, or pass information to, Xcode.
These special variables start with `%%%{` and
end with `}%%%`. You can
use them to specify the menu name, key equivalent, input treatment,
output treatment, and arguments for the script. They can also control
whether the script’s output is displayed incrementally or all
at once when the script is finished. (For a full description of
the available variables and other options you can use in scripts,
see [Menu Script Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwueqsdivauurkd).)

Listing 40-1 shows the original menu definition file `10-sort.sh`,
which was referred to in [How to Add an Item to the User Scripts Menu](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwueqkkirbuersd). The numbered
lines in this script are described below.

__Listing 40-1__  The menu definition file 10-sort.sh

```
#! /bin/sh                              -1-
#
# sort.sh - alphabetically sorts the lines of the selection or file
#
# -- PB User Script Info --
# %%%{PBXName=Sort Selection}%%%        -2-
# %%%{PBXInput=Selection}%%%            -3-
# %%%{PBXOutput=ReplaceSelection}%%%    -4-
# %%%{PBXKeyEquivalent=}%%%             -5-
#
# %%%{PBXNewScript}%%%                  -6-
# %%%{PBXName=Sort File}%%%
# %%%{PBXInput=AllText}%%%
# %%%{PBXOutput=ReplaceAllText}%%%
# %%%{PBXKeyEquivalent=}%%%

#                                       -7-
echo -n "%%%{PBXSelection}%%%"
sort <&0
echo -n "%%%{PBXSelection}%%%"
```

1. This line
   identifies the shell for the menu definition. A menu definition
   can use any shell, as long as it starts with a standard `#!` comment
   to identify the shell. As mentioned previously, menu definition
   files are interpreted in UTF-8 encoding, which is a strict superset
   of ASCII, so plain ASCII is fine too.
2. The built-in variable in this line (`%%%{PBXName=Sort
   Selection}%%%` ) is the first of four built-in
   variables the script uses in its first menu definition. The variable
   specifies the name of the menu or menu item; if you don’t specify
   a name, the name of the menu file is used.
3. `%%%{PBXName=Selection}%%%`
   specifies that the script for this menu item should take its input
   from the current selection; if you don’t specify an input location,
   the script gets no input. The possible input options are described
   in [Specifying Where to Get Input](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwueqsdivfeer2k).
4. `%%%{PBXOutput=ReplaceSelection}%%%`
   specifies that the script’s output should replace the current
   selection (that is, the sorted text should replace the original,
   unsorted text); if you don’t specify an output location, the output
   is discarded. The possible input options are described in [Specifying Where to Place Output](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwueqsdijdueskb).
5. `%%%{PBXKeyEquivalent=}%%%`
   specifies the key equivalent for the menu item; in this case, there
   is no key equivalent specified. The characters you use to specify
   key equivalents are listed in [Specifying the Menu Item’s Key Equivalent](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwueqsdireusrkc).
6. This line, containing the variable `%%%{PBXNewScript}%%%`,
   starts a second menu definition. It is similar to the first definition,
   except that it gets all the text of the current document as its
   input (`%%%{PBXInput=AllText}%%%`)
   and replaces all the text with its output (`%%%{PBXOutput=ReplaceAllText}%%%`).
   For related information, see [Placing Multiple Menu Items in One Script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwueqsdijeeerse).
7. Both menu definitions use the same three lines at the bottom
   of the file to perform the sort operation. The variable `%%%{PBXSelection}%%%` specifies
   an exact selection within the output. Inserting this variable before
   and after the sort operation (by echoing it, with `-n` to
   omit a trailing newline character) results in Xcode selecting the
   entire output text—that is, selecting the sorted text.

In addition to the variables described in [Using Variables in a Menu Definition Script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwueqkki5becr2e), Xcode provides several useful built-in
utility scripts. These scripts can be used in menu definition files
or in other scripts you write.

To use one of these scripts, you preface it with the expansion
variable `%%%{PBXUtilityScriptsPath}%%%`,
which specifies the location of the script. For example, the following
statement displays a dialog to get input from the user and places
the result in the variable `STRING`.
The original text displayed in the dialog is “DefaultString”.

```
STRING = `%%%{PBXUtilityScriptsPath}%%%/AskUserForStringDialog "DefaultString"`
```

In addition to the `AskUserForStringDialog` script,
Xcode provides built-in scripts to:

- Choose an
  existing file or folder
- Choose a new file
- Choose an application
- Add a menu item from a menu definition file, or from any script
  file
- Add a submenu
- Add a menu separator
- Remove a custom menu item or remove all custom menu items
  from a menu

For details, see [Built in Utility Scripts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwuesccijfeqscb).

As described previously, when you launch Xcode, it looks for
a file named `StartupScript` located
at `~/Library/Application Support/Apple/Developer
Tools/` and executes it if found. Xcode ships with
a default `StartupScript` and
a number of menu definition files that together create and populate
the User Scripts menu.

These simple features clearly provide many options for customizing
your Xcode environment:

- You can modify
  the User Scripts menu by deleting unused menu definition files or adding
  new ones you write.
- You can modify `StartupScript` to,
  for example, call additional scripts you write. Or you can replace `StartupScript` completely.
- Xcode provides many built-in script variables and utility
  scripts you can use in menu scripts or other scripts. You can even
  add items to other menus or create new custom menus and menu items.
- Many Xcode build settings can be accessed from scripts.
- Your scripts can use Perl or other languages.
- Your shell scripts can execute AppleScript scripts, using
  the `osascript` command.

The following sections describe the features and terminology
you can use in working with menu scripts. Topics covered include
menu script definition variable expansion, pre-execution variable
expansion, and special user output script markers.

In addition to the standard script statements in a menu script
definition, Xcode parses certain special directives from the file
content to allow control over various menu script options. These
directives can specify the menu name, key equivalent, input treatment, output
treatment, and arguments for the script. They can also control whether
the script's output is displayed incrementally or all at once when
the script is finished. These special variable expansions start
with "%%%{" and end with "}%%%". Any recognized
directives will be parsed and deleted from the script text as the
file is first being read in (even so, all the example scripts put
these directives in shell comments). The following directives are supported.

`%%%{PBXName=`_menu-title_`}%%%` sets
the name of the script currently being defined to _menu-title_.
If not set, the menu item’s name is the file name.

`%%%{PBXKeyEquivalent=`_key-equiv_`}%%%` sets
the key equivalent for the menu item to _key-equiv_.
If not set, the menu item will have no key equivalent. A _key-equiv_ begins
with characters specifying the modifiers and ends with a character
that will actually be the key equivalent. Modifier characters are:

- `@` is
  Command
- `~` is Option
- `^` is Control
- `$` is Shift

Most key equivalents should begin with `@`.
Modifier characters are recognized until the first non-modifier
character. The rest is the actual key. If the key is also a modifier character,
precede it with a `\`.
For example `@b` is Command-B,
and `@~\@` is Command-Option-@.
Remember that a menu script definition file must be Unicode (UTF-8)
if it contains non-ASCII characters (such as function keys) as key
equivalents. Note that you can insert a function key into a file
by pressing Control-Q and then the function key (such as Home, F5,
or Page Up).

`%%%{PBXInput=`_input-treatment_`}%%%` specifies
where the script gets its input for `stdin`.
If not set, the script gets no input. The possible values for _input-treatment_ are:

- `None` uses
  no input
- `Selection` uses
  the selected text as input
- `AllText` uses all
  the text in the window as input

`%%%{PBXOutput=`_output-treatment_`}%%%` specifies
where to send the output from the script. If not set, the output
is discarded. The possible values for _output-treatment_ are:

- `Discard` discards
  any output
- `ReplaceSelection` replaces
  the current selected text with the output
- `ReplaceAllText` replaces
  the complete text with the output
- `InsertAfterSelection` inserts
  the output after the currently selected text
- `AppendToAllText` appends
  output to the end of the complete text
- `SeparateWindow` shows
  output in a separate window (currently an alert panel)
- `Pasteboard` puts
  the output on the pasteboard

`%%%{PBXArgument=`_arg_`}%%%` specifies
an argument to pass to the script. You can use this expansion zero
or more times, each one adds a new argument to pass to the script.

`%%%{PBXIncrementalDisplay=`_flag_`}%%%` specifies
whether to display the script’s output as it arrives. If _flag_ is `YES` and
the output goes to the text view (that is, not to a separate window
or the clipboard), then the output is displayed as it arrives. If _flag_ is `NO`,
the output is displayed after the script finishes. The default is `NO`.

`%%%{PBXNewScript}%%%` signals
the beginning of a new script. Use this directive if you want to
define more than one menu item, each with its own settings, in a
single script. When this directive is encountered, all the previous
directives are considered complete, a menu command is created, and
everything is reset to start specifying settings for a new menu
item.

Menu Scripts can also contain a variety of special variables
that will be expanded by Xcode each time the script is executed.
Several variables are supported.

These variables are replaced by text in the active window:

- `%%%{PBXSelectedText}%%$` is
  replaced by the selected text in the active text object.
- `%%%{PBXAllText}%%%` is
  replaced by the entire text in the active text object.

The text is expanded verbatim with no quoting. In most shells
this would be fairly dangerous because the selection might include
single or double quotes or any number of other special shell characters.
One safe way to use this in a Bourne shell script, for example, is
to have it expand within "here-doc" style input redirection
like so:

```
cat << EOFEOFEOF
%%%{PBXSelectedText}%%%
EOFEOFEOF
```

The above script would simply print the selected text to the
standard output.

These variables are replaced by information on the text in
the active window:

- `%%%{PBXTextLength}%%%` is
  replaced by the number of characters in the active text object.
- `%%%{PBXSelectionStart}%%%` is
  replaced by the index of the first character in the selection in
  the active text object.
- `%%%{PBXSelectionEnd}%%%` is
  replaced by the index of the first character after the selection
  in the active text object.
- `%%%{PBXSelectionLength}%%%` is
  replaced by the number of characters in the current selection in
  the active text object.

`%%%{PBXFilePath}%%%` is
replaced by the path to the file for the active text object, if
it can be determined. This may not be accurate. Xcode tries to find
the file path first by walking up the responder chain looking for
an NSWindowController that has an NSDocument. If it finds one it
will use the document's `fileName`. If it
does not find one, it will use the `representedFilename` of
the window, if it has one.

Note that this implies that sometimes this will expand to
nothing and sometimes it may expand to a file name that is not really
a text file containing the text of the active text object. In Xcode
text file editors, this works correctly, in other text areas in
Xcode (like the build log or any text field) it will not do anything
reasonable.

`%%%{PBXUtilityScriptsPath}%%%` is
replaced by the path to the folder that contains a number of built
in utility scripts and commands that can be used from user scripts
to provide functionality such as using a dialog to ask the user
for a string or to ask the user to choose a folder or file, or to
add to the menu bar of the host application. See below for descriptions of
the available utility scripts.

When a User Script is done executing, Xcode scans the output
for certain special markers. Currently only one marker is supported.

`%%%{PBXSelection}%%%` specifies
an exact selection within the output. By default Xcode will set
the selection to be an insertion point after all the newly inserted
output text. But if the output contains one or two instances of
this special marker, it will use them to determine the selection.
If there is one such marker, it identifies an insertion point selection.
If there are two, all the text between them is selected. The markers
are removed from the output.

Xcode provides several useful utility scripts that are built-in
to Xcode itself. These scripts can be used in menu definition file
scripts or in MPW-style worksheet content. To use one of these scripts,
use the `%%%{PBXUtilityScriptsPath}%%%` expansion
variables. For an example, see [Working With Built-in Utility Scripts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwviucykjcummjrha).

`AskUserForStringDialog [`_default-string_`]`

Displays a dialog in the active application and returns the
string that the user enters. If supplied, _default-string_ is
the initial contents of the text field.

`AskUserForExistingFileDialog [`_prompt-string_`]``AskUserForExistingFolderDialog
[`_prompt-string_`]`

Displays a standard open dialog and returns the path of the
file or folder that the user chooses. If supplied, _prompt-string_ is
the prompt in the dialog. Otherwise a default prompt is used.

`AskUserForNewFileDialog [`_prompt-string_ `[`_default-name_`]]`

Displays a standard save dialog and returns the path of the
new file. If supplied, _prompt-string_ is
the prompt in the dialog. Otherwise, a default prompt is used. If
supplied, _default-name_ is the default
name for the new file

`AskUserForApplicationDialog [`_title-string_ `[`_prompt-string_`]]`

Displays an application picker dialog and returns path of
the application the user chose. If supplied, _title-string_ is
the title for the dialog. Otherwise, a default title is used. If supplied, _prompt-string_ is
the prompt in the dialog. Otherwise, a default prompt is used.

`SetMenu add script` _script__menu-title__key-equiv__input-treatment__output-treatment__index_ `[`_menu-path_ `...]`

Adds a new menu item to an existing menu in Xcode. The menu
item has the name _menu-title_, and
the key equivalent _key-equiv_. (Use `""` for
no key equivalent.) When the user chooses this command, it invokes
the script _script_, getting its input
from _input-treatment_ and placing
its output in _output-treatment_. The
new item is inserted at _index_ in
the menu identified by menu-path. If you don’t specify _menu-path_ the
item appears in the main menu bar. _menu-path_ contains
the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index
starting at the end of all the original items in the menu. For example,
the index `0` in the File
menu would generally be the first item after Print (usually the
last item in the File menu of an application.) Index `2` would
be after the second custom item in a menu. Use negative indices
to count from the end of a menu. Index `-1` means
at the end, and Index `-2` means
right before the last item.

The _key-equiv_, _input-treatment_,
and _output-treatment_ arguments use
the same syntax as the values of the menu definition file directives `PBXKeyEquivalent`, `PBXInput`,
and `PBXOutput` respectively.
For example, if _input-treatment_ is `Selection`,
the selected text is the input for the new menu item's script.

This is the most complicated form of the `SetMenu` command.
Usually it is better to use the next form in conjunction with menu
script definition files.

`SetMenu add scriptfile` _script-path__index_ `[`_menu-path_ `...]`

Adds new menu items to an existing menu in Xcode. The items
are read from _script-path_. See the
menu script definition files notes above for details on the file
format. Details such as the menu titles key equivalents, and input
and output treatment are defined within the file. The new items
are inserted at the given _index_ in
the menu specified by _menu-path_. If
you don’t specify _menu-path_ the
item appears in the main menu bar. _menu-path_ contains
the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index
starting at the end of all the original items in the menu. For example,
the index `0` in the File
menu would generally be the first item after the Print (usually
the last item in the File menu of an application.) Index `2` would
be after the second custom item in a menu. Use negative indices
to count from the end of a menu. Index `-1` means
at the end, and Index `-2` means
right before the last item

`SetMenu add submenu` _submenu-name_i_ndex_ `[`_menu-path_ `...]`

Adds a new submenu to an existing menu in Xcode. The submenu's
title is _submenu-name_. Initially,
it has no items. The new submenu is inserted at _index_ in
the menu specified by the _menu-path_.
If you don’t specify _menu-path_ the
item appears in the main menu bar. _menu-path_ contains
the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index
starting at the end of all the original items in the menu. For example,
the index `0` in the File
menu would generally be the first item after the Print (usually
the last item in the File menu of an application.) Index `2` would
be after the second custom item in a menu. Use negative indices
to count from the end of a menu. Index `-1` means
at the end, and Index `-2` means
right before the last item

`SetMenu add separator` _index_ `[`_menu-path_ `...]`

Adds a new separator to an existing menu in Xcode. The new
separator is inserted at _index_ in
the menu specified by the _menu-path_.
If you don’t specify _menu-path_ the
item appears in the main menu bar. _menu-path_ contains
the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index
starting at the end of all the original items in the menu. For example,
the index `0` in the File
menu would generally be the first item after the Print (usually
the last item in the File menu of an application.) Index `2` would
be after the second custom item in a menu. Use negative indices
to count from the end of a menu. Index `-1` means
at the end, and Index `-2` means
right before the last item

`SetMenu remove item` _index_ `[`_menu-path_ `...]`

Removes a custom item from an existing menu in Xcode. The
custom item at _index_ in the menu
specified by the _menu-path_. If you
don’t specify _menu-path_ the item
is removed from the main menu bar. _menu-path_ contains
the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index
starting at the end of all the original items in the menu. For example,
the index `0` in the File
menu would generally be the first item after the Print (usually
the last item in the File menu of an application.) Index `2` would
be after the second custom item in a menu. Use negative indices
to count from the end of a menu. Index `-1` means
at the end, and Index `-2` means
right before the last item

Only items and submenus added by a `SetMenu` command
may be removed by the `SetMenu remove item` command.
You cannot remove Xcode's real menu items.

`SetMenu remove all [`_menu-path_ `...]`

Removes all custom items from an existing menu in Xcode. All
custom items in the menu identified by the given _menu-path_ are
removed. If you don’t specify _menu-path_ the
item is removed from the main menu bar. _menu-path_ contains
the titles of menus and submenus that lead to the desired menu.

This command applies to items and custom submenus, but does
not recurse into original submenus. For example, if you added an
item to the File menu and you added a whole submenu called My Scripts
to the main menu bar, `SetMenu remove all` removes
the My Scripts submenu, but does not remove the custom item in the
File menu. `SetMenu remove all File` removes
the custom item from the File menu.

Only items and submenus added by a `SetMenu` command
can be removed by the `SetMenu remove all` command.
You cannot remove Xcode's real menu items.

[Next](Using%20CVS.md)[Previous](Xcode%20Preferences.md)

