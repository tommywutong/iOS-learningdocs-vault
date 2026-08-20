---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/ed_file_attr/ed_file_attr.html
archived_at: '2026-07-15T07:29:46.485351Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Opening%2C%20Closing%2C%20and%20Saving%20Files.md)[Previous](Editing%20Source%20Files.md)

# Inspecting File Attributes

For each file, framework, and folder added
to your project, Xcode stores a number of important settings, such
as the path to the file and the file’s type. You can view and
edit settings for file, framework, and folder references in the
file reference inspector or Info window.

This chapter describes how to inspect file, folder, and framework
references in your project. It also describes how to change the
way in which Xcode handles a file by changing its type; and how
to control the way a file is displayed and saved, by changing the
file encoding and line ending.

You can view and edit settings for file, framework, and folder
references in the file reference inspector or Info window. To bring
up the Info window, click the Info button in the project window
toolbar. If you select more than one file reference, Xcode displays
one Info window that applies to all selected files. Attributes whose
values are not the same for all selected files are dimmed. Changing
an attribute’s value applies that change to all selected file references.

The Info window for a file, folder, or framework reference or
source group contains the following:

- The General
  pane, shown below, lets you modify a number of basic file attributes, including
  filename, location, reference style, and so forth.
- The Build pane lets you specify additional compiler flags
  for the file. The Build pane appears only when the file being inspected
  is a source code file. See [Per-File Compiler Flags](Build%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugsceijceiqsj) for
  more information on the contents of this pane.
- The SCM pane lets you view SCM information for the file. This
  pane is only available for files under version control. See [Viewing Revisions](Managing%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrxgawugsscircucr2h) for
  more information.
- The Comments pane lets you add notes, documentation, or other
  information about the file. See [Adding Comments to Project Items](Organizing%20Xcode%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruhawueq2jjfcukq2d) for
  more information on adding comments.

__Figure 13-1__  Inspecting
a file

!

Here is what you can see and edit in the General pane of the
file reference inspector:

1. The Name
   field displays the file’s name. To rename the file, type the new
   name in this field.
2. The Path field shows the location of the file; that is, it
   shows the path to the file. To change this location, click the Choose
   button next to the path. You will get a dialog that lets you choose
   a new path.
3. The Path Type menu indicates the reference style used for
   the file. These reference styles are described in [How Files Are Referenced](Files%20in%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgewueqsdirdekq2c).
   To change the way the file is referenced, choose a style from this
   menu.
4. The File Type menu lets you explicitly set the file’s type,
   overriding the actual file type of the file. How to change a file’s
   type is described further in [Overriding a File’s Type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvguwugsscjffeoqsb).
5. The “Include in index” checkbox controls whether Xcode
   includes the file when it creates the project’s symbolic index.
   See [Code Sense](Finding%20Information%20in%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgawueqsdjjeugrsc) for
   more information.
6. The File Encoding menu specifies the character set used to
   save and display the file. File encodings are discussed further
   in [Choosing File Encodings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvguwueqkci5eegsce).
7. The Line Endings pop-up menu specifies the type of line ending
   used in the file. Line endings are discussed further in [Changing Line Endings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvguwueq2jivaueq2j).
8. The next several options control tab and indent settings for
   the individual file. The Tab Width and Indent Width fields control
   the number of spaces that Xcode inserts when it indents your code
   or when you press the Tab key when you edit the file in the Xcode editor.
   To change either of these values, type directly in the field.

   The
   “Editor uses tabs” setting indicates whether pressing the Tab
   key inserts spaces or a tab when you are editing this file in Xcode’s
   editor. Controlling indentation in the editor is discussed further
   in [Setting Tab and Indent Formats](Formatting%20and%20Syntax%20Coloring.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgqwueq2jindueq2j).

   The Reset to Text Editing Defaults
   restores the line ending, file encoding, tab and indent settings
   to Xcode’s built-in defaults.
9. The Make File Localizable and Add Localization buttons at
   the bottom of the pane let you customize files for different regions.

The file encoding of a file defines the character set that Xcode uses
to display and save a file. If you type a character that isn’t
in the file’s encoding, Xcode asks whether you want to change
the encoding. Xcode uses the default single-byte string encoding,
if possible (usually Mac OS Roman), or Unicode if the file contains
double-byte characters.

To change the file encoding for one or more files, select
those files and open an inspector window. In the General pane of
the inspector window, choose the desired file encoding from the
File Encoding menu. Generally Unicode (UTF-8) is best for source
files and Unicode (UTF-16) is best for `.strings` files.
You can also change the file encoding of an open file by choosing
an item from the Format > File Encoding menu. When Xcode next
saves the file, it uses the new file encoding.

To choose the default file encoding for new files, open the
Text Editing pane in the Xcode Preferences window and choose an
encoding from the Default File Encoding menu.

UNIX, Windows, and Mac OS use different characters to denote
the end of a line in a text file. Xcode can open text files that
use any of these line endings. By default, it preserves line endings
when it saves text files. However, other utilities and editors may
require that a text file use specific line-ending characters. You
can change the type of line endings that Xcode uses for a single
file, or you can change the default line ending style that Xcode
uses for all new or existing files.

To change an individual file’s line endings, select the
file in the project window and open the inspector. In the General
pane of the inspector window, use the Line Endings menu to choose
Unix Line Endings (LF), Classic Mac Line Endings (CR), or Windows
Line Endings (CRLF).

To choose the default line endings used for all new or existing
files, choose Xcode > Preferences, click Text Editing, and choose
Unix (LF), Mac (CR), or Windows (CRLF) from the Line Encodings pop-up
menus:

- The “For
  new files” menu lets you choose the default line encoding that
  Xcode uses for all new files.
- The “For existing files” menu specifies the type of line
  encoding that Xcode uses when saving existing files that you have
  opened for editing in Xcode. To have Xcode preserve line endings
  for existing files, choose “Preserve” from this menu; this is
  the default value for the menu.

Generally, you don’t need to worry about line endings. If
you find that you must change line endings from the defaults assigned
by Xcode, keep these guidelines in mind when deciding which line
endings to use:

- Most Mac
  OS development applications, including CodeWarrior and BBEdit, can handle
  files that use UNIX, Mac OS, or Windows line endings.
- Many BSD command-line utilities, such as `grep` and `awk`,
  can handle only files with UNIX line endings.

By default, Xcode uses the type stored for a file on disk
to determine how to handle that file. A file’s type affects which
editor Xcode opens the file in, how the file is processed when you
build a target that includes the file, and how Xcode colors the
file when syntax coloring is enabled. You can change the way that
Xcode handles a file by overriding the file’s type.

The File Type menu in the General pane of the file inspector
lets you explicitly set the file’s type, overriding the actual
file type of the file. The File Type menu lists all of the file
types that Xcode is aware of; to set a file’s type, choose it
from this menu. Choosing Default For File discards any explicit
file type set for the file in Xcode and reverts to using the type stored
for the file on disk.

For more information on how Xcode determines how to process
files of a certain type, see [Build Rules](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawueqsdindekrck) and [Adding Files to a Build Phase](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawugssbizbumrkh).
For more information on how Xcode chooses the editor to use for
files of a certain type, see [Overriding How a File is Displayed](Using%20an%20External%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsguwueqkcjfeukske).

[Next](Opening%2C%20Closing%2C%20and%20Saving%20Files.md)[Previous](Editing%20Source%20Files.md)

