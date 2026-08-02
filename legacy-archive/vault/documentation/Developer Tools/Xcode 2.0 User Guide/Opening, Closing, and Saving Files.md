---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/ed_open_and_close/ed_open_close.html
archived_at: '2026-07-15T07:29:47.999090Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](The%20Xcode%20Editor.md)[Previous](Inspecting%20File%20Attributes.md)

# Opening, Closing, and Saving Files

Xcode gives you a number of ways to get to,
and open, files in your project. This chapter describes how to open
files in your preferred editor—by default, Xcode’s editor—and describes
a number of shortcuts for opening files by name or from an open
editor.

There are many ways to open files in Xcode. From an open project,
you can open any of your project files by clicking or double-clicking
the file. Files open in the preferred editor for the file’s type.
If this is Xcode’s editor, you have the option of opening file
in a separate editor window or in the editor attached to most Xcode
windows.

There are also many shortcuts for opening files. The Open
Quickly command lets you type a path or filename to open a file.
From an editor, you can open a file by name, jump to the header
associated with an implementation file and vice versa, or jump to
files included by the current file.

If you already have a project window open, you can open a
file by selecting it in the Groups & Files list in the project
window. If you have the editor open inside of the project window,
a single click on the file name will open the file in the editor.
Otherwise, double-clicking the file in the Groups & Files list
opens the file in a separate editor window.

If the file’s name is in red, Xcode cannot find the file.
Select the file, open the inspector, and click the Choose button
next to Path in the General pane.

If you have a code editor open and you have previously opened
the file, you can choose the file’s name from the pop-up menu
that lists recently viewed files, in the navigation bar at the top
of the code editor.

You can quickly open a header or source file that’s related
to the file displayed in the editor.

To open the related header for an implementation file open
in the editor, and vice versa:

- Click the
  Go to Counterpart icon in the navigation bar of the code editor,
  as described in [The Navigation Bar](The%20Xcode%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmzrfvbecqshijaugqy)
- Choose View > Switch to Header/Source File.

For example, if `main.c` is
in the editor, this opens `main.h`;
if `main.h` is in the editor,
it opens `main.c`.

You can also view all the files that the current file includes,
as well as all the files that include the current file. To view
the list of files that the file in the editor includes and that include
this file, click the Included Files icon in the navigation bar of
the code editor. A menu pops up with the name of the current file
in the center. Above it are the names of the files that this file
includes. Below it are the names of the files that include this
file. To open one of the files, choose it from the menu.

In addition to shortcuts to open related files, Xcode also
provides a shortcut that allows you to open files by name or path,
without having to navigate to the file using the Open File dialog.
To open a file by name, use one of the following shortcuts. You
can open files using these shortcuts even if the file is not in
your project.

- To open a
  file whose name appears in a code editor, select the name and choose
  File > Open Quickly.
- To open a file by typing its name, choose File > Open Quickly
  and enter the filename in the Path field.

Xcode first looks for the file in the current project and
then searches a list of directories that it maintains for use with
the Open Quickly command. A number of common directories—such
as `System/Library/Frameworks`—are already
included in this list by default. You can add your own commonly
accessed directories to this list in the Opening Quickly pane of
Xcode Preferences, described in [Opening Quickly Preferences](Xcode%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgewugskijbduercj).

Open Quickly searches the directories in the order in which
they appear in this pane. If Open Quickly doesn’t display the
file you expected, check whether a file with the same name as the
one you wish to open exists in your project or at a location higher
up in the list of directories to search.

If you know the path to a file, you can also use the Open
Quickly command to open the file, without adding a new directory
to the list of search paths, by choosing File > Open Quickly
and entering the path. For example, to open the file `MyNotes.rtf` located
in your Documents folder you would type `~/Documents/MyNotes.rtf`.

Files in a project remain open until you explicitly close
the file or close the project. Open files in an editor appear in
the pop-up menu of recently viewed files. To close a file, choose File
> Close File _filename_.

Xcode indicates which files you’ve modified by highlighting
their icons in gray in the Groups & Files list, detail view,
and in the pop-up menu of recently viewed files. You can save your
changes in a number of ways:

- To save changes
  to the current file, choose File > Save.
- To save a copy of a file, choose File > Save As. Xcode
  saves a copy of the file under the name you specify. If the file
  is part of your project, Xcode also changes the file reference in
  your project to refer to the copy.
- To make a backup of a file, hold the Option key and choose
  File > Save a Copy As. Xcode saves a copy of the file under the
  name you specify, but does not modify the file reference in your
  project, if one exists.
- To save all open files, choose File > Save All.

Xcode can also be configured to automatically save all changed
files before beginning a build. To specify whether files are saved
automatically when you build a target:

1. Choose Xcode >
   Preferences and click Building.
2. In the “For Unsaved Files” menu, choose Ask Before Building,
   Always Save, Never Save, or Cancel Build.

If you don’t have write permission for a file, Xcode warns
you when you try to edit it. You can choose to edit such files,
but you can save your changes only if you have write permission
for the containing folder. In this case, you can choose whether Xcode changes the
file’s permissions to make it writable.

To have Xcode change the file’s permissions, choose Xcode >
Preferences, click Text Editing, and select “Save files as writable”
in Save Options. Otherwise, Xcode preserves the file’s current
permissions.

[Next](The%20Xcode%20Editor.md)[Previous](Inspecting%20File%20Attributes.md)

