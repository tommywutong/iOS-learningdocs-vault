---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/ed_external_editor/ed_external_editor.html
archived_at: '2026-07-15T07:29:46.032784Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Customizing%20for%20Different%20Regions.md)[Previous](Code%20Completion.md)

# Using an External Editor

Xcode lets you choose the editors used for
the files in your project. You can use Xcode’s built-in editor
or use an external editor such as BBEdit. Generally, Xcode uses
the filename extension to choose how to edit a file. For example,
it edits an `.rtf` file
with its own built-in RTF editor and a `.c` file
with its own built-in source code editor.

You can temporarily change how a file is viewed, or permanently
change how files of a certain type are viewed. To change how a file
is viewed, you can do any of the following:

- To have files
  of a certain type always open in a different editor, change the
  preferred editor for that file type to that editor.
- To have files of a certain type always open in the application
  specified for them in the Finder, change the preferred editor for
  that file type to “Open With Finder.”
- To temporarily force Xcode to treat a file as a different
  file type, and open it with the appropriate editor, use the Open
  As command.
- To temporarily force Xcode to open a file with the default
  application chosen for it in the Finder, use the Open With Finder
  command.

You can temporarily override how Xcode displays a file. For
example, you can choose to view a particular HTML file as plain
text, so you can edit it instead of viewing it as rendered HTML.

To force a file to be displayed differently than is specified
by the default rule for that file type, select the file in the Groups
& Files list or detail view and choose an option from the File
> Open As menu. You can also Control-click the file, and choose
an option from the Open As menu in the contextual menu Xcode displays.

You can permanently change how Xcode edits a particular type
of file. In particular, you can specify how files of a certain type
are treated and you can choose which editor is used to handle those
files. For example, you can choose to view all HTML files as plain
text, so you can edit them. Or you can choose to edit all your source
files in BBEdit.

To see the file types that Xcode recognizes, choose Xcode
> Preferences and click File Types. The File Types pane lists
all of the folder and file types that Xcode handles and the preferred
editor for each of those types. These file and folder types are
organized into groups, from the most general to the most specific.
Click the disclosure triangle next to an entry in the File Type
column to reveal its contents.

To change the editor used for a particular file type, find
the entry for the file type, click in the Preferred Editor column,
and choose an option from the menu that appears. For example, to
change Xcode to view all HTML files—including documentation files—as plain
text, expand the following entries: file, then text, and then text.html.
As mentioned earlier, Xcode already treats most HTML files as plain
text by default; the value in the Preferred Editor column for the
text.html entry is “Plain Text File,” indicating the preferred
editor for plain text files. However, the value in the Preferred
Editor column for the text.html.documentation entry is “HTML File,”
which overrides the text.html setting. To make Xcode treat HTML
documentation files as plain text, select text.html.documentation,
click in the Preferred Editor column and choose “Plain Text File” from
the pop-up menu, as shown here.

__Figure 18-1__  Changing
how a file is viewed

!

With this change, Xcode uses the preferred editor for plain
text files to open all HTML files. In the example shown in the previous
figure, the preferred editor for plain text files is Xcode’s default
text editor.

You can also specify an external editor to use or have Xcode
use the user’s preferred application, as specified by the Finder,
when opening files of a given type, as described in the following
sections.

Xcode does not limit you to using its built-in editors to
view and edit your files. You can specify an external editor of
your choosing as the preferred editor for opening files of a given
type. To choose an external editor for all files of a particular
type:

1. Choose Xcode >
   Preferences, and click File Types.
2. Find the appropriate file type and click in the Preferred
   Editor column; a pop-up menu appears.
3. Select an option from the External Editor submenu. Currently,
   you can choose from the following options:

   - BBedit.
   - Text Wrangler.
   - SubEthaEdit.
   - `emacs`.
   - `xemacs`.
   - `vi`. Note that support
     for `vi` in Xcode is limited
     to opening the file in the editor.
   - Other. Choose this option to specify an external editor other
     than the ones specified earlier. When you select this option, a
     dialog that allows you to navigate to the application you wish to
     use as your external editor appears.

   Note
   that many of these external editors do not appear in the External
   Editor menu unless they are installed on your computer.

For example, to edit all your source files with BBEdit, open
the File Types preference pane and expand these entries: file, then
text. Select the source code entry, and choose External Editor > BBEdit
from the pop-up menu that appears when you click in the Preferred
Editor column.

There are some restrictions when you’re using an external
editor:

- When you
  build a project, Xcode lists modified files and asks you whether
  you want to save them. Files in BBEdit and Text Wrangler are listed,
  but files in other editors are not. You need to save those files
  yourself before starting a build.
- When you double-click a find result or a build error, most
  editors do not scroll to the line with the find result or error.
  BBEdit and Text Wrangler can.

To use `emacs` as
an external editor, you must add these lines to your `~/.emacs` file:

```
(autoload 'gnuserv-start "gnuserv-compat"
          "Allow this Emacs process to be a server for client  processes." t)
(gnuserv-start)
```


You can choose to open a file with the application chosen
for it in the Finder. This lets you open files that Xcode cannot
handle, or view a file using your preferred editor. If you edit a
file in almost any other application, Xcode cannot save it for you
before building a target. Some applications, such as Interface Builder
and WebObjects Builder, communicate with Xcode and so can save your
files before your project is built. Check the application’s documentation
to see if it can, too.

To always have Xcode use your preferred application to open
files of a certain type:

- Choose Xcode
  > Preferences and click File Types.
- Find the appropriate file type and choose Open With Finder
  from the pop-up menu that appears when you click in the Preferred
  Editor column.

Note that you can only set this preference for file types
that Xcode recognizes. To open files that Xcode cannot handle, or
to temporarily override the settings in the File Types pane of Xcode
Preferences and open a file using the Finder-specified application:

- In the Groups
  & Files list or detail view, Control-click the file and choose
  Open with Finder.

If you have the embedded editor open, single-clicking a filename
still loads the file in the editor. But if you configure Xcode to
use an external editor to edit the file, you cannot edit the file
within Xcode. That is, the file is read-only in Xcode’s built-in
editor.

[Next](Customizing%20for%20Different%20Regions.md)[Previous](Code%20Completion.md)

