---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/pr_add_files/pr_add_files.html
archived_at: '2026-07-15T07:29:48.029527Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Organizing%20Xcode%20Projects.md)[Previous](The%20Project%20Window.md)

# Files in a Project

The files in a project are the fundamental
building blocks from which you create your end product. Files contain
the source code that you write and serve as the inputs to the build system
for creating a product. They can also hold notes, performance metrics,
and the like to aid you in the development process.

This chapter discusses the files in a project, describes how
Xcode references project files, and shows you how to add files,
frameworks, and folders to your project. It also describes how to
use source trees to set up alternative access paths for project
files and how to use a cross-project reference to access the contents
of another project.

For each source file included in a project, Xcode tracks file
attributes, such as the name and type, as well as other information. Figure 5-1 shows the
information that Xcode tracks for source files.

__Figure 5-1__  A source file

!

The name is the file system name for the file. The file type
identifies the file as being one of several classifications (source
file, image file, text file, and so on.) Depending on the file type,
Xcode stores additional information about the file, such as the
file encoding, type of line endings and so forth.

The path to the file specifies the file system location for
the file; the path type—which you can modify—indicates how Xcode
stores the path; that is, whether it is absolute or relative to
the project directory or another location. [How Files Are Referenced](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgewueqsdirdekq2c) describes
the various ways in which Xcode stores paths.

You can view and edit these file attributes in the file inspector.

The project lets you pull together all of the files and other
information required to build a set of related software products.
Within a project, you use a target to specify the files needed for
an individual product. The files can reside at any location in your
file system; they do not need to be placed in your project folder.
A project can contain:

- Files. A
  source file is any file that Xcode uses in building a target, including
  source code files, resource files, image files, and others. For
  files you need direct access to in Xcode—for example, files you
  wish to edit using Xcode’s editor—you should explicitly add a
  reference to each file to the project. This includes source code
  files you want Xcode to compile.
- Folders. If you have a folder of files that you manipulate as
  a whole—such as a folder of help files—you can simply add a
  reference to the folder to your project. This allows you to manipulate
  the folder in Xcode instead of touching each file individually. (To access
  any of the files individually from Xcode, you must also add a reference
  to the file to your project.)
- Frameworks. You can add a reference to each of the frameworks
  that your product links against. This gives you easy access to the
  framework’s headers, directly in the project window.

When you create a project using Xcode’s project templates,
described in [Choosing a Project Template](Creating%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgawugsceirdueqke),
Xcode populates the project with a small set of default files required
to build the associated product. For example, the figure below shows
the contents of a new project created using the Carbon Application
project template. This project builds a small C application with
a NIB-based interface that links to the Carbon framework. The project
contents have been expanded in the Groups & Files list to display
its contents in outline view. Of course, keep in mind that the contents
of a project vary depending on the project template and the products
it creates.

__Figure 5-2__  The
project contents in the Groups & Files list

!

The example project contains the following items:

- The Sources
  group contains implementation files; in this case the `main.c` file.
- The Resources group contains resource files for the application.
  This includes the `main.nib` file that
  defines the user interface, the `Info.plist` property
  list file, and the `Infoplist.strings` files
  containing strings used in the interface.
- The External Frameworks and Libraries group contains references
  to the frameworks that define the system interfaces used by the
  application’s code. You can view a framework’s header files
  by disclosing the contents of the framework in the Groups & Files
  list.
- The Products group contains references to the products created
  when the project’s targets are built. A _product reference_ is
  a special type of file reference that refers to the build system
  output for a particular target. A product reference lets you view
  your target’s products right in the Groups & Files list. You
  can use the product reference to refer to the product in the same
  way you use a file reference to refer to a project file. Note, however,
  that the product reference does not actually refer to anything until
  you have built that target.

Xcode keeps a reference to each file, folder, and framework
you add to your project. In this way, Xcode can find your files
directly when it builds a product. However, Xcode also provides
build settings for specifying general search paths for various items,
such as headers and libraries. These include the Header Search Paths,
Library Search Paths, and Framework Search Path build settings.

Xcode stores the location, or path, for each file, framework,
and folder in a project. Xcode uses this path to locate the item.
Xcode can store this as an absolute path or relative to another
file system location. You choose the way that a given file, framework,
or folder is referenced when you add it to the project. You can
also change the reference type for an item in the file inspector.
Xcode supports the following reference styles, each of which is available
in the Reference Type menu:

- Relative
  to Enclosing Group. The path is relative to the folder associated
  with the file’s group. If the file is not in a group or the group
  has no associated folder, the path is relative to the project’s
  folder. This is the default setting for files in your project’s folder.
- Relative to Project. The path is relative to the project’s
  folder, regardless of whether the file is in a group with an associated
  folder.
- Relative to Build Product. The path is relative to the folder
  that contains the project’s build products. This reference style
  is the default for items that are created by one of the project’s
  targets.
- Relative to _source path_. The path is
  relative to a user-defined source path. You can define a source
  path in the Source Trees pane of Xcode Preferences. Note that this reference
  type is not available to you until you have defined at least one
  source tree.
- Absolute Path. The path is absolute from the root directory
  (/). This is useful in a limited set of circumstances, when you
  want to locate a file at a particular path. In most cases, you should
  use a relative path; absolute paths are fragile and break easily
  when you move projects between computers.

If a file is inside your project folder or its build folder
(created by Xcode when it creates a new project), use one of the
first three reference styles.

If Xcode can’t find a file, folder, or framework at the
path stored for it in the project, Xcode displays the item in red
in the project window.

If you created a new project using one of the project templates,
or if you converted an existing project, your project will already
have a number of groups and files in it, as well as frameworks,
folders, and product references. Regardless of whether your project already
includes files or was created completely empty, you will likely
have to add files or frameworks to your project at some point.

You can add a file, folder, or framework to your project by
dragging it from the Finder to the project source group or by choosing
Project > Add to Project and using the navigation dialog to choose
the item to add.

There are two ways for you to add files or folders to your
project:

- In the project
  window Groups & Files list, select the group to add the files
  to, and choose Project > Add to Project. Use the resulting dialog
  to navigate to and choose the file or files to add. If you want
  to add all of the files in a given folder, you may simply choose
  the folder. The files or folders you add are placed after the items
  currently selected in the Groups & Files list, if any.
- Drag the icons for the files or folders from the Finder to
  the project window Groups & Files list. A line shows you where
  the files will be added.

As a shortcut, you can add a file that is open in an editor
window to the project by selecting Project > Add Current File
to Project. The editor window must have focus.

Once you have selected the file or files to add to the project, using
either of the two methods described above, Xcode displays a dialog,
shown below, that allows you to specify how the files are added
to the project.

__Figure 5-3__  Adding
files to a project

!

Here is what the dialog contains:

1. The “Copy
   items into destination group’s folder (if needed)” option controls
   whether or not the files are copied into your project folder on
   disk. If you select this option, Xcode copies over any files that
   are not already present in the project folder. If the project folder
   contains subfolders for groups, then the files are copied into the appropriate
   subfolder.
2. The Reference Type menu specifies how the location of the
   file is stored. For a description of the various reference styles
   available to you, see [How Files Are Referenced](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgewueqsdirdekq2c). Note that this menu does not
   contain any source paths until you have defined one or more source trees
   in the Xcode Preferences window. Once you have defined a source
   path, it appears at the bottom of the Reference Type menu and you
   can choose it for the files and folders you add.
3. The Text Encoding menu specifies the encoding for the file
   or files. This is the character set that Xcode uses to display and
   save a file. For more information on file encodings, see [Choosing File Encodings](Inspecting%20File%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvguwueqkci5eegsce).
4. The Add To Targets group allows you to add the file to one
   or more of the targets currently defined in your project. If the
   checkbox next to a target name is checked, the file is added to
   that target when it is added to the project. When you add a file
   to a target, that file is built when the target is built. You can
   specify which files are included in a target at any time; this option
   allows you to add the file to your project and to any necessary
   targets in one step.

The remaining options apply only if the selection of files
to add to the project includes one or more folders. Xcode can add
folders in two ways:

1. Group. Xcode recursively
   creates groups for the folder and its subfolders. Each of the files
   in these folders is added to the project and is placed in the group
   for the appropriate folder. If you choose to copy the files into
   the project’s folder, Xcode duplicates the folder hierarchy. If
   you move a file to the folder outside of Xcode, Xcode does not add
   the file to the project.

   To add a folder as a group, select
   “Recursively create groups for any added folders.”
2. Folder Reference. Xcode adds the folder itself to the project
   but not its contents. This is useful if you need to manipulate the
   folder as a whole but not the individual items within it. One example
   is a folder of help files that you edit outside of Xcode and that you
   want Xcode to move into the application’s Resources folder when
   you build the application.

   To add a folder as a folder reference,
   select “Create Folder References for any added folders.”

Similar to adding files, you add frameworks to a project by
doing either of the following:

- Select the
  group to add the framework to in the Groups & Files list, and
  choose Project > Add to Project. Use the resulting dialog to
  navigate to and choose the appropriate framework on the system—for
  example, `AddressBook.framework`.
- Drag the framework to the project window Groups & Files
  list.

After you have selected a framework, Xcode presents the same
options described in [Adding Files and Folders](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgewueq2jirauorsj). The following options apply to
frameworks:

- The Reference
  Type menu in the dialog specifies how the location of the framework is
  stored. For a description of the various reference styles available
  to you, see [How Files Are Referenced](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgewueqsdirdekq2c).
- The Add to Targets group box allows you to add the framework
  to one or more of the targets currently defined in your project.
  If the checkbox next to a target name is checked, the framework
  is also included in that target when it is added to the project.
- The Text Encoding menu specifies the encoding used for the
  files in the framework. For more information on file encodings,
  see [Choosing File Encodings](Inspecting%20File%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvguwueqkci5eegsce).

You can remove any files, folders, or frameworks from your
project by selecting them in the Groups & Files list and pressing
Delete. You can also select the files to remove and choose Edit
> Delete.

Xcode displays a dialog asking whether you wish to delete
the actual files or just the project’s references to them. If
you choose Delete References, Xcode deletes only the project’s
references to those files; the files remain intact on the disk.
If you choose Delete References & Files, Xcode deletes the references
from the project, and deletes the referenced files from the disk. The
files are deleted immediately; they are not moved to the Trash.

Source trees are root paths that can be used to define common
access paths and locations for target outputs. A source tree defines
a name and a location on the local file system. When you add files
and folders to your project, you can specify their location relative
to any source tree defined for your computer. Xcode stores the file
reference relative to this source tree. Any other user who has the
same source tree defined is able to work on the same project seamlessly,
provided that the file actually exists at the source tree location
on their computer as well.

Source trees let you keep common resources in locations other
than the project folder of an individual project and still transfer
projects back and forth between team members and their various computers
without breaking the project’s file references. This is particularly useful
if you have a set of common files or resources that are used in
a number of projects, and therefore cannot live in the project folder.
Everyone working on a common project should have the same source
trees defined; while the locations assigned to those source trees
may differ, the names must be the same in order for Xcode to locate
the necessary files and materials on the developer’s computer.

Xcode supports global source trees; that is, any source trees
that you define are available to all of your projects. Source trees
are stored for each user, so if you have multiple developers using
a single computer, you will have to define the source trees for
each user, even though the location for those source trees is the
same. Once you have defined a source tree, it is available to you
from the Add Files dialog, to use when adding file, folder, and framework
references to your project. You can also select the source tree
from the Path Type pop-up menu in the file inspector, described
in [Inspecting File, Folder, and Framework References](Inspecting%20File%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvguwueqkcjfbukscj).

You can edit source trees in the Source Trees pane of Xcode
Preferences. To open this pane, choose Xcode > Preferences and
click Source Trees. To add a source tree, click the plus (+) button
beneath the source tree table. Xcode adds an entry in the table.
Add the following information to the entry:

- Setting Name
  is the name of the source tree. This name must be the same for all
  users who wish to use this same source tree to refer to common files.
- Display Name is the name that Xcode shows for the source tree
  in dialogs, inspectors, and anywhere else the source tree is used
  in the user interface. For example, this is the name used in the
  Path Type menu of the file inspector.
- Path is the full path to the files and other resources located
  using this source tree on the user’s system. This path may vary
  from computer to computer, and from user to user.

To delete a source tree, select the source tree in the table
and click the minus (-) button. To edit a source tree, double-click
the entry for the source tree in the appropriate table column and
type the changed text.

In addition to file, framework, and folder references, Xcode
projects can contain a cross-project reference; that is, they can
refer to another project outside of the current one. It is not always
feasible or desirable to keep all related targets and products in
a single project. However, you may still need to reference targets
or products that reside in a different project. For example, you
may have several applications that rely on a common framework that
resides in a different project. In this case, you can add a reference
to the project containing the framework to the project containing
the application. This reference, called a _cross-project
reference_, lets you access the targets and products of
the referenced project from your current project.

To create a reference to another project, choose Project >
Add to Project and select the project bundle (the `.xcode` bundle) of
the project you wish to reference. Xcode adds a reference to the
source group for your current project, visible in the Groups &
Files list. The project reference is indicated by the project icon.
Clicking the disclosure triangle next to the project reference shows
the product references that the other project contains. These product
references can be added to targets in the current project.

You can relate targets in the current project to targets in
the referenced project by creating a target dependency. You can
add a dependency on a target in the referenced project in the same
way that you would add a dependency to a target within the same
project. See [Adding a Target Dependency](Targets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugsscjfduusce) to
learn more about target dependencies.

For projects that use cross-project references, you should
use a common build location; doing so ensures that Xcode can automatically
locate products created by targets in those projects. For more on
build locations, see [Build Locations](Building%20a%20Product.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmztfvbecssdjfeugqy).

[Next](Organizing%20Xcode%20Projects.md)[Previous](The%20Project%20Window.md)

