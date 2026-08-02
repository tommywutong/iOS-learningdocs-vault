---
title: Xcode Workspace Guide
apple_id: TP40006920
resource_type: Guide
platform: iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeWorkspace/310-User_Scrips/user_scripts.html
archived_at: '2026-07-15T07:30:31.356227Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Workspace Guide](Introduction.md)


[Next](Resetting%20Xcode.md)[Previous](Keyboard%20Shortcuts.md)

# User Scripts

User scripts are shell scripts you can define in your workspace and that you can execute by choosing them from the User Scripts menu or using a keyboard shortcut. With these scripts you can invoke command-line tools and perform operations on the selected text. For example, you can sort the selected lines in the text editor.

Xcode provides a number of mechanisms for working with user scripts. These features include:

- The ability to execute text in a text editor window as a shell command or series of commands
- A number of built-in script variables and utility scripts you can use in menu scripts or other scripts

This chapter describes how to manage and use Xcode user scripts.

Xcode provides predefined user scripts that let you open files, perform searches, add comments to your code, sort text, and even add HeaderDoc templates that can help you document your header files. And you can use these files as examples to help write custom scripts.

The User Scripts menu (Figure 8-1) shows the predefined user scripts and the user scripts you add. This menu reflects the user-script hierarchy defined in the Edit User Scripts window, shown in Figure 8-2.

__Figure 8-1__  User Scripts menu

!

__Figure 8-2__  The Edit User Scripts window

!

You use the user-scripts editor to add, modify, and delete user scripts. You can also add user-script groups (menu groups) and separators.

Adding a user script adds a corresponding menu item to the User Scripts menu. You can define the script in the text editor pane of the user-scrips editor, or you can specify the location of an existing shell script in your file system.

A user script has four attributes, whose values you specify in the Edit User Scripts window:

- __Input.__ The script’s input. It can be nothing, the selection, or the current file.
- __Directory.__ The script’s initial working directory. It can be your home directory, the path indicated by the selected text, or the file system root directory (`/`).
- __Output.__ The script’s output mechanism. It can be none, a dialog, the Clipboard, and others.
- __Errors.__ The destination of the script’s error messages. It can be none, a dialog, the Clipboard, or the script’s regular output mechanism.

To add a user script:

1. Select the user-script group into which you want to add the user script.
2. Choose User Scripts > Edit User Scripts to open the Edit User Scripts window.
3. Click the Add Script button (+) and choose one of the following items from the menu:

   - __New Shell Script.__ Creates a user-script menu item and a blank shell script, which you edit in the editor pane.
   - __Add Script File.__ Creates a user-script menu item and prompts you for the location of an existing shell script file.
   - __Add Automator Workflow.__ Creates a user-script menu item and prompts you for the location of an existing Automator workflow.
4. Enter the name and keyboard shortcut (if desired) for the user script in the user-script list, as shown in Figure 8-3.

   __Figure 8-3__  Adding a shell script

   !
5. Choose values from the Input, Directory, Output, and Errors menus.

To remove a user script, user-script group, or separator, select it and click the Remove Script button.

To edit a file-based user script, select the script in the user-scripts list and click the Edit Script button (this button is available only for file-based user scripts).

Sometimes it may be more convenient to create a user script based on an existing one instead of writing one from scratch. To create a custom user script based on a predefined user script:

1. Choose User Scripts > Edit User Scripts to open the Edit User Scripts window.
2. Select the user script to duplicate.
3. Click the Add Script button and choose Duplicate Script from the menu.
4. Customize the script and its attributes as appropriate.

The following sections describe advanced features of shell-based user scripts. The topics covered include variables you can use in menu script definitions, variables expanded prior to script execution, and special user output script markers.

Shell-based user scripts can also contain a variety of special variables that are expanded by Xcode each time the script is executed. The following sections describe the supported variables.

These variables are replaced by text in the active window:

- `%%%{PBXSelectedText}%%%` is replaced by the selected text in the active text object.
- `%%%{PBXAllText}%%%` is replaced by the entire text in the active text object.

The text is expanded verbatim with no quotation marks. In most shells this would be a dangerous practice because the selection might include single or double quotation marks or any number of other special shell characters. One safe way to use this in a Bourne shell script, for example, is to have it expand within “here-doc” style input redirection like so:

```
cat << EOFEOFEOF
%%%{PBXSelectedText}%%%
EOFEOFEOF
```

The script above would simply print the selected text to the standard output.

These variables are replaced by information on the text in the active window:

- `%%%{PBXTextLength}%%%` is replaced by the number of characters in the active text object.
- `%%%{PBXSelectionStart}%%%` is replaced by the index of the first character in the selection in the active text object.
- `%%%{PBXSelectionEnd}%%%` is replaced by the index of the first character after the selection in the active text object.
- `%%%{PBXSelectionLength}%%%` is replaced by the number of characters in the current selection in the active text object.

This variable Is replaced by the path to the file for the active text object if it can be determined:

`%%%{PBXFilePath}%%%`

This result may not be accurate. Xcode tries to find the file path first by walking up the responder chain looking for a window controller that has a document. If it finds one it uses the document’s filename. If it does not find one, it uses name of the window’s represented file. For more information, see [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) and [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument).

Sometimes this variable expands to nothing and sometimes it may expand to a filename that is not really a text file containing the text of the active text object. In the Xcode text editor this works correctly. In other text areas in Xcode (like the build log or any text field) it does not do anything reasonable.

This variable is replaced by the path to the folder that contains a number of built-in utility scripts and commands:

`%%%{PBXUtilityScriptsPath}%%%`

These scripts and commands can be used from user scripts to provide functionality such as presenting a dialog to ask the user for a string or to ask the user to choose a folder or file, or to add to the menu bar of the host application. See [Built-in Utility Scripts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdombxfvbeqqscjjeeqqi) for descriptions of the available utility scripts.

When a user script is done executing, Xcode scans the output for certain special markers. Only one output marker is supported. This variable specifies an exact selection within the output:

`%%%{PBXSelection}%%%`

By default, Xcode sets the selection to be an insertion point after the newly inserted output text. But if the output contains one or two instances of this special marker, it uses them to determine the selection. If there is one such marker, it identifies an insertion point selection. If there are two, all the text between them is selected. Xcode then removes the markers from the output.

Xcode provides several useful built-in utility scripts, which you can use in the user scripts you create.

To use one of these scripts, preface it with the expansion variable `%%%{PBXUtilityScriptsPath}%%%`, which specifies the location of the script. For example, the following statement displays a dialog to get input from the user and places the result in the variable `STRING`. The original text displayed in the dialog is “DefaultString”.

```
STRING = `%%%{PBXUtilityScriptsPath}%%%/AskUserForStringDialog "DefaultString" "DefaultWindowName"`
```

In addition to the `AskUserForStringDialog` script, Xcode provides built-in scripts to:

- Choosing a new file
- Choose an existing file or folder
- Choose an application

For details, see [Built-in Utility Scripts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdombxfvbeqqscjjeeqqi).

Xcode provides several useful utility scripts that are built in to Xcode itself. These scripts can be used in menu definition file scripts or in MPW-style worksheet content. To use one of these scripts, use the `%%%{PBXUtilityScriptsPath}%%%` expansion variables. For an example, see [Using Utility Scripts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdombxfvjvomy).

`AskUserForStringDialog [`_default-string_`]`

Displays a dialog in the active application and returns the string that the user enters. If supplied, _default-string_ is the initial content of the text field.

`AskUserForExistingFileDialog [`_prompt-string_`]`

`AskUserForExistingFolderDialog [`_prompt-string_`]`

Displays a standard open dialog and returns the path of the file or folder that the user chooses. If supplied, _prompt-string_ is the prompt in the dialog. Otherwise a default prompt is used.

`AskUserForNewFileDialog [`_prompt-string_ `[`_default-name_`]]`

Displays a standard save dialog and returns the path of the new file. If supplied, _prompt-string_ is the prompt in the dialog. Otherwise, a default prompt is used. If supplied, _default-name_ is the default name for the new file.

`AskUserForApplicationDialog [`_title-string_ `[`_prompt-string_`]]`

Displays an application picker dialog and returns the path of the application the user chose. If supplied, _title-string_ is the title for the dialog. Otherwise, a default title is used. If supplied, _prompt-string_ is the prompt in the dialog. Otherwise, a default prompt is used.

`SetMenu add script` _script__menu-title__key-equiv__input-treatment__output-treatment__index_ `[`_menu-path_ `...]`

Adds a menu item to an existing menu in Xcode. The menu item has the name _menu-title_, and the keyboard shortcut _key-equiv_. (Use `""` for no keyboard shortcut.) When the user chooses this command, it invokes the script _script_, getting its input from _input-treatment_ and placing its output in _output-treatment_. The new item is inserted at _index_ in the menu identified by _menu-path_. If you don’t specify _menu-path_ the item appears in the menu bar. _menu-path_ contains the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index starting at the end of all the original items in the menu. For example, the index `0` in the File menu would generally be the first item after Print (usually the last item in the File menu of an application). Index `2` would be after the second custom item in a menu. Use negative indices to count from the end of a menu. Index `-1` means “at the end,” and Index `-2` means “right before the last item.”

The _key-equiv_, _input-treatment_, and _output-treatment_ arguments use the same syntax as the values of the menu definition file directives `PBXKeyEquivalent`, `PBXInput`, and `PBXOutput` respectively. For example, if _input-treatment_ is `Selection`, the selected text is the input for the new menu item's script.

This is the most complicated form of the `SetMenu` command. Usually it is better to use the form described in[Adding a Menu Item from a Menu Definition Script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdombxfvjvomjt) in conjunction with menu script definition files.

`SetMenu add scriptfile` _script-path__index_ `[`_menu-path_ `...]`

Adds menu items to an existing menu in Xcode. The items are read from _script-path_. See [Adding a Menu Item from Any Script File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdombxfvjvomjs) for details on the file format. Details such as the menu items keyboard shortcuts, and input and output treatment are defined within the file. The new items are inserted at the given _index_ in the menu specified by _menu-path_. If you don’t specify _menu-path_, the item appears in the main menu bar. _menu-path_ contains the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index starting at the end of all the original items in the menu. For example, the index `0` in the File menu would generally be the first item after the Print command (usually the last item in the File menu of an application). Index `2` would be after the second custom item in a menu. Use negative indices to count from the end of a menu. Index `-1` means “at the end,” and Index `-2` means “right before the last item.”

`SetMenu add submenu` _submenu-name__index_ `[`_menu-path_ `...]`

Adds a submenu to an existing menu in Xcode. The submenu's title is _submenu-name_. Initially, it has no items. The new submenu is inserted at _index_ in the menu specified by _menu-path_. If you don’t specify _menu-path_, the item appears in the main menu bar. _menu-path_ contains the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index starting at the end of all the original items in the menu. For example, the index `0` in the File menu would generally be the first item after the Print command (usually the last item in the File menu of an application). Index `2` would be after the second custom item in a menu. Use negative indices to count from the end of a menu. Index `-1` means “at the end,” and Index `-2` means “right before the last item.”

`SetMenu add separator` _index_ `[`_menu-path_ `...]`

Adds a separator to an existing menu in Xcode. The new separator is inserted at _index_ in the menu specified by _menu-path_. If you don’t specify _menu-path_, the item appears in the main menu bar. _menu-path_ contains the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index starting at the end of all the original items in the menu. For example, the index `0` in the File menu would generally be the first item after the Print command (usually the last item in the File menu of an application). Index `2` would be after the second custom item in a menu. Use negative indices to count from the end of a menu. Index `-1` means “at the end,” and Index `-2` means “right before the last item.”

`SetMenu remove item` _index_ `[`_menu-path_ `...]`

Removes a custom item from an existing menu in Xcode. The custom item at _index_ in the menu specified by _menu-path_. If you don’t specify _menu-path_, the item is removed from the main menu bar. _menu-path_ contains the titles of menus and submenus that lead to the desired menu.

_index_ is a zero-based index starting at the end of all the original items in the menu. For example, the index `0` in the File menu would generally be the first item after the Print command (usually the last item in the File menu of an application). Index `2` would be after the second custom item in a menu. Use negative indices to count from the end of a menu. Index `-1` means “at the end,” and Index `-2` means “right before the last item.”

Only items and submenus added by a `SetMenu` command can be removed by the `SetMenu remove item` command. You cannot remove the standard Xcode menu items.

`SetMenu remove all [`_menu-path_ `...]`

Removes all custom items from an existing menu in Xcode. All custom items in the menu identified by _menu-path_ are removed. If you don’t specify _menu-path_, the item is removed from the main menu bar. _menu-path_ contains the titles of menus and submenus that lead to the desired menu.

This command applies to items and custom submenus but does not recurse into original submenus. For example, if you add an item to the File menu and you add a menu called My Scripts to the main menu bar, `SetMenu remove all` removes the My Scripts menu but does not remove the custom item in the File menu. `SetMenu remove all File` removes the custom item from the File menu.

Only items and submenus added by a `SetMenu` command can be removed by the `SetMenu remove all` command. You cannot remove the standard Xcode menu items.

[Next](Resetting%20Xcode.md)[Previous](Keyboard%20Shortcuts.md)

