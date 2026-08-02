---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/bs_build_settings/bs_build_settings.html
archived_at: '2026-07-15T07:28:54.297834Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Build%20Styles.md)[Previous](Build%20Phases.md)

# Build Settings

A _build setting_ is a variable
that contains information used to build a product. For each operation
performed in the build process—such as compiling Objective-C source
files—build settings control how that operation is performed.
For example, the information in a build setting can specify which
options Xcode should pass to the tool—in this case, the compiler—used
to perform that operation.

Build settings constitute the main method of customizing the
build process. They represent variable aspects of the build process
that Xcode consults as it builds a product.

This chapter explains how build settings are implemented and
how you can take advantage of them to communicate with the build
system. It explains the build setting syntax, the layers in which
you can specify build settings, and how you can use them to customize
the build process.

A build setting in Xcode has two parts: the name and the specification.
The _build setting name_ identifies the build setting
and can be used within other settings; in that sense, it is similar
to the names of environment variables in a command shell. The _build
setting specification_ is the information Xcode uses to
determine the value of the build setting at build time. A build
setting may also have a title, which is used to display the build
setting in the Xcode user interface.

__Figure 25-1__  A
build setting

!

The build system consults the value of build settings as it
generates tool invocations. For example, to generate profiling code
for all the source files compiled with `gcc`,
you turn on the Generate Profiling Code (GCC_GENERATE_PROFILING_CODE) build
setting. When Xcode creates the `gcc` command-line
invocation to compile a source file, it evaluates build settings
such as Generate Profiling Code to construct the argument list.

Build setting values may come from a number of different sources
at build time. Xcode stores build setting definitions in dictionaries
spread across several layers. Typically, you will be most interested
in the target and build style layers; however, it is important to understand
the various layers from which build setting values can be derived.
See [Build Setting Layers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugssci5cuoskj) for details.

Xcode has many built-in build settings that you can use to
customize the build process. Furthermore, you can define your own
build settings, which you can use to configure standard build settings
across several targets or access within scripts in Run Script build phases
to perform special tasks.

In addition to build settings, you can set _per-file
compiler flags_ that the build system uses when creating
tool invocations. They allow you to make changes to how a file is compiled
that do not affect any other files in the project. See [Per-File Compiler Flags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugsceijceiqsj) for
details.

Build setting names start with an uppercase letter or underscore
character; the remaining characters can be uppercase letters, underscore
characters, or numbers. For example, the build setting that specifies
the name of a product is called PRODUCT_NAME. This restriction on
the names of build settings helps identify build settings from other environment
variables in shell scripts. The Xcode application doesn’t allow
you to define build settings whose names don’t follow this convention.
You can define build settings at the command-line layer that circumvent this
restriction; for example, you can define a build setting called
“project_name” in the command-line layer. Because build setting names
are case-sensitive, however, the build system considers it a distinct
build setting and doesn’t override the value of the PROJECT_NAME build
setting.

The Xcode application displays titles for most of its standard
build settings in the project and target inspectors. For example,
the title of the PRODUCT_NAME build setting is Product Name. `xcodebuild` doesn’t
use build setting titles.

The value of a build setting is determined by evaluating the
build setting specification. A build setting specification can be
a value such as a string, number and so forth; or it can reference
the value of other build settings.

To reference a build setting value in a build setting specification,
use the name of the build setting surrounded by parentheses and
prefixed by the dollar-sign character ($). For example, the specification
of a build setting that refers to the value of the Product Name build
setting could be similar to `The name of this
target's product is $(PRODUCT_NAME)`.

In addition to the build settings provided by Xcode, you can
add _user-defined build settings_ to a project.
A user-defined build setting is one that is not referenced by the
build system. You can add them at the command line, build style,
target, and environment levels. You can reference properly named
user-defined build settings in build setting specifications and
scripts in Run Script build phases. User-defined build settings
don’t have a title.

The following list describes some circumstances in which you
may need to add user-defined build settings to a project:

- modify the
  value of build settings that are not displayed in the Xcode application
- specify a value that can be used by several build settings
  in different layers (see [Build Setting Evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdi5augr2j) for details)
- define a build setting you want to use in Run Script build
  phase scripts or a build-rule script

Build setting specifications are defined in a number of layers
depending on whether you build using the Xcode application or the `xcodebuild` tool. Figure 25-2 shows
these layers.

__Figure 25-2__  Build setting layers

!

The specifications of build settings configured in higher
layers override the specifications set at lower layers. The following
sections describe each of the build system layers in detail:

1. Command-line
   layer (`xcodebuild` only)

   The `xcodebuild` tool’s
   command invocation represents the highest layer in which you can
   configure build settings when building a product. The build settings
   configured in this layer are accessible only to `xcodebuild`.

   This
   layer gives you a way to customize builds done in batch mode from
   the command line without needing access to the Xcode application.
2. Build style layer

   The build style layer is available
   to both the Xcode application and the `xcodebuild` tool. It
   defines build setting variations for a build. These are changes
   to build setting definitions in the target layer and lower layers
   that allow you to produce different “flavors” of a product without
   having to create separate targets.

   Another use of the
   build style layer is to provide values for build settings to be
   shared by more than one target. All targets have access to the build
   settings in the active build style. When you have multiple targets
   with build settings that should be synchronized, a build style can
   be a convenient way to do so. See [Build Setting Evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdi5augr2j) for details.

   For
   more information on build styles, see [Build Styles](Build%20Styles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtgawugssbizcesr2g).
3. Target layer

   This is the main layer for specifying how
   a product is built. Generally, it’s the one that defines the largest
   number of build settings.

   The Xcode user interface displays
   most of the build settings defined in this layer. However, the specifications
   displayed may not correspond to the values the build system obtains
   when building a product, unless you’ve customized the specification. For
   example, Installation Path (INSTALL_PATH) has a default value of `/usr/local/lib` for targets
   that produce a static library. This value is not shown in the target
   inspector; that is, the value shown for Installation Path is empty.
   But if you set the build setting to `$(INSTALL_PATH)/mylib` in
   the target inspector, at build time, INSTALL_PATH is `/usr/local/lib/mylib`.

   Each
   target has its own set of build settings. That is, Xcode evaluates
   build settings for a target independently from the build settings
   defined in other targets. This is true even for dependent and aggregate
   targets.

   For more information on targets, see [Targets](Targets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugskiiveekq2h).
4. Project layer

   Xcode and `xcodebuild` use
   the Project layer to specify project-wide aspects, such as the location
   of the project itself. Build settings such as TEMP_DIR are specified
   in this layer. There is no mechanism for you to add build settings
   to this layer or modify the build setting specifications in it because
   you customize them in higher layers.
5. Environment layer

   The environment layer is composed of
   environment variables that correspond to build setting names. You
   can use it to configure build settings that must apply to more than one
   project. This layer, however, cannot access build settings configured
   in any other layer. For example, defining an environment variable
   named `MY_PRODUCT_NAME` as `My
   Company $(PRODUCT_NAME)` results in an undefined-variable
   error, unless you also define an environment variable named `PRODUCT_NAME`.

   You
   must follow the syntax described in [Build Setting Syntax](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugsscirduorkb) when
   defining the environment variables in your session.

To take advantage of build settings in your project, you must
understand how they are evaluated when Xcode builds your product.
Placing build setting specifications in particular build setting
layers provides you the ability to, for example, quickly change
an aspect of a product when building from the command line, configure
a product aspect only in one of a product’s alternate “flavors”
but not in all of them, or specify an aspect for all the projects
that you work on.

This article describes how Xcode evaluates build settings.
It provides details that help you determine where to place build
setting specifications to greatly customize the build process.

At build time, Xcode evaluates each build setting individually. Figure 25-3 shows
the order in which the build system evaluates build settings.

__Figure 25-3__  Build setting evaluation precedence

!

When the build system needs the value of a build setting,
it starts at the highest build setting layer available to it and
works down in the order shown in the following list:

1. Command invocation:
   Build settings defined in the `xcodebuild` invocation.
2. Build style: Build settings defined in the active build style.
3. Target: Build settings defined in the target being built.
4. Product: Build settings whose value depends on the type of
   product built by the target.
5. Environment variables: Build settings defined in the Xcode
   application environment or the shell from which `xcodebuild` is
   launched.

As soon as the build system finds a definition for the build
setting it’s looking for, it stops traversing the build setting
layers. However, if the build setting specification found includes
references to other build settings, it resolves them, which starts
the traversing process again, as many times as necessary to compute
the value of the original build setting.

If a build setting refers to itself (that is, the build setting
specification includes a reference to the build setting being evaluated),
the build system resolves the reference starting at the subsequent
build setting layer. The following sections provides examples illustrating
this process.

Imagine that you need to define a single build setting at
every build setting layer (except the noncustomizable project layer)
in order to build a product. This is a very unlikely case to be
sure, but one that illustrates how the process works. Table 25-1 shows
an example configuration for the LAYERED build setting throughout
the build setting layers. This example assumes that the product
is built from the command-line using `xcodebuild`:

__Table 25-1__  Configuration of the LAYERED build
setting

| Build setting layer | Build setting specification |
| Command line | `command line, $(LAYERED)` |
| Build style | `build style, $(LAYERED)` |
| Target | `target, $(LAYERED)` |
| Environment | `environment` |

Figure 25-4 shows how the build system would evaluate
the LAYERED build setting when building using `xcodebuild`.

__Figure 25-4__  Evaluation of the LAYERED build setting

!

To evaluate the LAYERED build setting, the build system does
the following:

1. Looks for
   a definition for `LAYERED` in
   the command-line layer (the highest available to `xcodebuild`).
   It finds the specification `command line, $(LAYERED)`.
2. Resolves `$(LAYERED)` starting
   at the next layer down, the build style layer. At this layer, it
   obtains the specification `build style, $(LAYERED)`.
   Because this specification also references the value of the LAYERED
   build setting, the build system continues to look in lower layers
   for the build setting specification.
3. Resolves `$(LAYERED)` starting
   at the target layer, obtaining `target, $(LAYERED)`.
4. Resolves `$(LAYERED)` starting
   at the environment layer, obtaining `environment`.

   The
   evaluation of LAYERED stops here because there are no build setting
   layers below the environment layer. When all the references are
   resolved, the final value of the build setting is computed as `command
   line, build style, target, environment`.

This example uses `$(LAYERED)` to
access the value of the same build setting at a lower layer. However,
you can also use `$(value)` for
that purpose. That is, replacing `$(LAYERED)` with `$(value)` in
the any of the build setting specifications at the command-line,
build-style, or target layers in the example above yields the same
result.

The process of evaluating a build setting specification that
references itself repeats recursively until the build system reaches
the environment layer or until the build system finds a build setting
specification that does not reference its own value.

The build system gives you a great deal of flexibility when
configuring build settings. The following example illustrates how
the build system evaluates the STAGGERED build setting, which is
defined in the Target layer and references the values of several
other build settings.

The value of the STAGGERED build setting is composed of data
and a caption for the data, with the caption shown first and both
elements separated by a colon (:) and a space. The specification
for STAGGERED contains references to two other build settings: LAYERED
(the data, explained in the previous section) and CAPTION (the caption
for the data). It also contains static elements (the colon and space
characters).

Figure 25-5 shows the evaluation of the STAGGERED build
setting.

__Figure 25-5__  Evaluation of the STAGGERED build
setting

!

These are the steps the build system takes to evaluate the
STAGGERED build setting:

1. Look for
   a specification for STAGGERED in the command-line layer. None is
   found.
2. Look for a specification for STAGGERED in the build style
   layer. None is found.
3. Look for a specification for STAGGERED in the target layer.

   The
   build system finds a specification for STAGGERED: `$(CAPTION):
   $(LAYERED)`. Here is where the evaluation of
   the STAGGERED build setting begins.
4. Resolve `$(CAPTION)` starting
   at the command-line layer:

   1. Look for a specification
      for CAPTION in the command-line layer. None is found.
   2. Look for a specification for CAPTION in the build style layer.
      None is found.
   3. Look for a specification for CAPTION in the target layer.
      The build system finds the specification `evaluation
      order`.

      The evaluation of CAPTION stops
      here because there are no references to other build settings. The
      final value of the CAPTION build setting is `evaluation
      order`.
5. Resolve `$(LAYERED)` starting
   at the command-line layer.

   1. Look for a specification
      for LAYERED in the command-line layer. The build system finds the
      specification `command line, $(LAYERED)`.
      The build system resolves the specification for LAYERED at this
      build setting layer as described in the previous section. The final
      value of the LAYERED build setting is `command
      line, build style, target, environment`.
6. Get the final value for the STAGGERED build setting by replacing
   the two references in the build setting’s specification with their
   values: `evaluation order: command line, build
   style, target, environment`.

Knowing the precedence that the build system uses when evaluating
build settings makes it easy to determine where to configure build
settings to tailor the build process for special situations. Following
the STAGGERED example, imagine you want to override the value of
the CAPTION build setting at the build style layer. All you would
have to do is configure the CAPTION build setting in the active
build style with the appropriate value.

Figure 25-6 shows the effects of overriding CAPTION in
the build style layer.

__Figure 25-6__  Evaluation of the STAGGERED build
setting with CAPTION overridden in the Build Style layer

!

These are the steps the build system takes to evaluate the
STAGGERED build setting after overriding CAPTION in the build style
build setting layer:

1. Look for
   a specification for STAGGERED in the command-line layer. None is
   found.
2. Look for a specification for STAGGERED in the build style
   layer. None is found.
3. Look for a specification for STAGGERED in the target layer.
   The build system finds `$(CAPTION): $(LAYERED)`.
4. Resolve `$(CAPTION)` starting
   at the command-line layer:

   1. Look for a specification
      for CAPTION in the command-line layer. None is found.
   2. Look for a specification for CAPTION in the build style layer.
      The build system finds `order of evaluation`.

      The
      evaluation of CAPTION stops here because there are no references
      to other build settings in its specification. Even though CAPTION
      is configured in the target layer, that specification has been overridden
      in the build style layer; therefore, it’s ignored. The final value
      of CAPTION in this example is `evaluation order`.
5. Look for a specification for LAYERED in the command-line layer.
   The build system finds `command line, $(LAYERED)`.

   1. Resolve the specification
      for LAYERED at this build setting layer as described earlier in
      this section, obtaining `command line, build
      style, target, environment`.
6. Get the final value for the STAGGERED build setting by replacing
   the two references in the build setting’s specification with their
   values: `order of evaluation: command line,
   build style, target, environment`.

A build style can define build settings that are shared among
all the targets processed during a build. Figure 25-7 illustrates
how two targets can use a build setting configured in the active
build style.

__Figure 25-7__  Sharing build setting values among
targets

!

When the aggregate target is built, DRESS_STYLE in target
A and HAIR_STYLE in target B evaluate to `eclectic`.

The Xcode application lets you access and edit build settings
at the target and build style layers. It provides a convenient graphical
user interface for changing build setting specifications. For native
targets, the target inspector lets you see build setting specifications
at the target layer. The project inspector lets you examine the
build settings defined for the project’s build styles. To view
and edit build settings for legacy Project Builder targets and external
targets, use the target editor.

You can view and edit build settings at the target level in
the Build pane of the target inspector. To modify build settings
at the build style level, use the Styles pane of the project inspector.
The interface for modifying build settings in these two inspector
window panes is almost identical.

__Figure 25-8__  The Build pane of a target Info window

!

Figure 25-8 shows the Build pane of the target inspector.
The target’s build settings appear in a table in the Build pane.
The columns show, from left to right:

- An icon indicating
  the type of setting. For example, settings that control warnings
  and errors are indicated by the warning icon.
- The Setting column contains the build setting title. This
  is a brief English-language description of the setting. To see the
  build setting name, open the help field, as described later in this
  section.
- The Value column contains the build setting specification. For
  Xcode’s standard build settings, this may be a string, a pop-up
  menu of possible values, or an on/off value. This specification
  can also reference the value of other build settings.

If you do not know what a particular build setting does, the
help field displays a longer description of the selected build setting.
If the help field is not visible, drag the resize control below
the build settings table to view the contents of the help field.
If you want to know the name of the build setting, you can also
find that in the help field.

You can search the table of build settings for a keyword or
other text string using the search field at the top of the pane. As
you type, Xcode filters the list to include only those settings
that match the text in the search field. For example, you can find
all build settings related to search paths by typing “search.”
Xcode searches both the build setting title and the build setting
description in the help field.

If you know the title of the build setting you are looking
for and keyboard focus is in the build settings table, you can simply
start typing the build setting name to select that build setting.

Note that the inspector does not tell you all the build settings
used when you press the Build button. The inspector shows only the
build settings defined at the target or build style layer. To learn
how to view all build settings used when you build, see [Finding Where a Build Setting is Defined](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdjbeeqskk).

As mentioned earlier in [Build Setting Layers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugssci5cuoskj), build
settings defined in a build style have higher precedence than those
defined in the target layer. If a build setting is defined in both
the active build style and in the active target, the definition
in the build style overrides that in the target. Xcode indicates
this in the target inspector by crossing out settings that are overridden
by the active build style. You can jump to the active build style’s
definition of that build setting by Control-clicking the build setting
and choosing Jump to Active Build Style. Xcode opens the project
inspector to the Styles pane and selects the build style’s definition
for the build setting. Build settings that are defined at the target level
are shown in boldface in the target inspector.

You can modify build settings for multiple targets at once;
the Build pane of the target inspector supports multiple selection.
To edit build settings for more than one target at a time, select
those targets in the project window and open an inspector window.

For a list of the build settings available in the Xcode application’s
user interface see [Build Setting Names and Their Corresponding Titles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugsscizeuussb). For a complete
list of Xcode build settings, see Xcode Build Settings or choose Help > Show Build Settings Notes.

For easy access to sets of related build settings, Xcode groups
build settings into several different collections. The Collection
pop-up menu above the build settings table contains a list of all
available groups of build settings. To view the build settings in
a group, choose that group from the pop-up menu, as shown in the
following figure.

__Figure 25-9__  Choosing
a build setting collection

!

Xcode provides groups for build settings that affect general
aspects of the build process—such as the location at which build
products are placed—as well as collections for tool-specific build
settings that affect compiler options. Build setting collections
have no effect on how the target is built.

To see all of the possible build settings and their definitions,
if any, choose All Settings from the Collection menu. Note that
tool-specific build settings appear in the target inspector only
if the target contains files that are built using that tool. For
example, if the target does not contain any resource files processed
using the Rez tool, the Rez-specific build settings do not appear
in the Collection menu.

The Customized Settings collection shows all of the build
settings that are defined at the current target or build style layer.
Like a smart group, the Customized Settings collection automatically
updates to reflect changes to build settings at the current layer.
For example, if you make a change to the value of a build setting
in one of the other collections, the Customized Settings collection
changes to include that build setting and its new definition.

For standard build settings, the interface for modifying a
build setting’s specification in the target and project inspectors
depends on the possible values for that build setting. These possible
values are:

- String. If a
  build setting takes a string as its value, select the build setting
  row and click Edit. If the build setting takes a single string as
  its value, Xcode displays a text field; type the string into this
  field. You can also edit the string simply by clicking in the Value column
  for the build setting and typing the value.

  If the build setting
  can contain one or more strings—for example, Header Search Paths—Xcode
  displays a table. To enter a string in this table, click the plus
  button and type the string into the table row added by Xcode. You
  can re-order the strings in the table by dragging the rows to the
  location at which you want them to appear.

  If you are
  entering file paths, you can simply drag the file or folder from
  the Finder into the text field or table, instead of typing the paths
  in yourself. Xcode will insert the path to the file.
- Boolean. If a build setting can have two states—enabled
  or disabled—the Value column contains a checkbox. A checkmark
  indicates that the build setting is enabled. To change the state
  of the build setting, click the checkbox.
- If a build setting has a finite number of possible values, Xcode displays
  a pop-up menu in the Value column. You can choose the desired value
  from this menu. For example, here is how you might select a build
  setting value from a menu:

__Figure 25-10__  Changing
the value of a build setting

!

In addition, Xcode provides a custom user interface for modifying
certain search path and architecture build settings, as described
in [Editing Search Paths](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdi5cusscc) and [Creating Multi-Architecture Binaries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdjbcekqki).

If you do not see the build setting you wish to modify, or
if you want to define your own custom build settings, you can add
build settings to the build settings table in the Build pane of
the inspector window. To add a new build setting to a target or
build style, click the plus (+) button below the build settings
table. Double-click in the Setting column and type the name of the
build setting, then double-click in the Value column and type the build
setting specification.

To delete a build setting from a target, select that build
setting and click the minus button (-).

Xcode defines a number of build settings for specifying general
search paths for files and frameworks used by targets in your project.
These build settings are:

- Header Search
  Paths (HEADER_SEARCH_PATHS)

  This is a list of paths to folders
  to be searched by the compiler for included or imported header files
  when compiling C, Objective-C, C++, or Objective-C++ source files.
- Library Search Paths (LIBRARY_SEARCH_PATHS)

  This is a
  list of paths to folders to be searched by the linker for static
  and dynamic libraries used by the product.
- Framework Search Paths (FRAMEWORK_SEARCH_PATHS)

  This
  is a list of paths to folders containing frameworks to be searched
  by the compiler for both included or imported header files when
  compiling C, Objective-C, C++, or Objective-C++, and by the linker
  for frameworks used by the product.
- Rez Search Paths (REZ_SEARCH_PATHS)

  This is a list of
  paths to search for files included by Carbon Resource Manager resources
  and compiled with the Rez tool.

Xcode supports recursive search paths. For each path that
you enter in one of these search path build settings, you can specify
that Xcode search the directory at that path, as well as any subdirectories
that directory contains.

You can edit search paths in much the same way that you edit
other build settings that contain lists of strings, as described
in [Editing Build Setting Specifications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugsscijcemr2e).
However, to specify that Xcode perform a recursive search for items
at a particular path, select the checkbox next to that path in the
Recursive column of the table that Xcode displays when you click
Edit in the target or build style inspector. When this is selected,
Xcode searches the directory at the specified location, and all
subdirectories in it, for the header, framework, library or resource.

Xcode performs a breadth-first search of the directory structure
at the search path, following any symlinks. Xcode searches locations
in the order in which they appear in the search paths table, from
top to bottom. It stops when it finds the first matching item, so
if you have multiple files or libraries of the same name at the
locations specified by a set of search paths, Xcode uses the first
one it finds.

Note that adding very deep directory structures to a list
of recursive search paths can increase your project’s build time.
The maximum number of paths that Xcode will expand a single recursive
search path to is 1024.

Xcode can create multi-architecture (or “fat”) binaries,
which are executable files that can contain code and data for more
than one CPU architecture. You can target multiple PowerPC-architecture
CPUs with a single binary file. The Architectures (ARCHS) build settings
lets you specify which architectures Xcode builds for. You can edit
this build setting in the target inspector: in the Build pane, select
the Architectures build setting and click Edit. Xcode displays a
list of all of the supported architectures. Select the checkbox next
to the architectures for which you want to build. You can build
for any of following architectures:

- 32-bit architectures:

  - G3
  - G4
  - G5
- 64-bit architecture: G5

Xcode compiles for each architecture individually and creates
a single fat file from these input files. For more information on
multi-architecture files, see _Mach-O File Format Reference_.

You cannot configure build information for Jam-based Project
Builder targets and external targets in the target inspector. To
edit the build settings for Jam-based and external targets in Xcode,
select the target in the Groups & Files list. If you have an
editor open in the project window, Xcode displays the Project Builder
target editor. To view this target editor in a separate window,
double-click the target.

On the left side of the target editor, Xcode displays a number
of groups of target settings appropriate for the current target.
Selecting any of these groups displays its settings in the editor
on the right side of the Target window.

To view the build settings for an external target, select
the Custom Build Settings group. To view the build settings for
a legacy Project Builder target, select the Expert View item in
the Settings group. The target editor displays a table of build
settings:

- The Name
  column contains the build setting name.
- The Value column contains the build setting specification.

Similar to the Build pane of the inspector window for native
targets, you can add and delete build settings using the plus (+)
and minus (-) buttons below the table. To edit a build setting,
double-click in the appropriate column and type the build setting
name or specification. The target editor for legacy targets also
includes a simpler interface for a number of common build settings
in the Simple View.

As Xcode constructs the command-line invocations for the various
tools it uses to build a product, it accesses the appropriate build
settings. Also, when it sets the environment variables for shell
scripts in Run Script build phases, it resolves most build settings
and sets environment variables with their values. Notable build
settings that are not passed as environment variables to shell scripts
are those geared specifically to tools such as `gcc`, `lex` and `yacc`.
You can identify these build settings by examining the prefixes
of build setting names. For example, Enable Trigraphs (GCC_ENABLE_TRIGRAPHS)
contains the prefix GCC, indicating that it’s exclusively tailored
for the `gcc` tool; therefore,
it isn't passed to shell scripts defined in Run Script build phases.

As you work on a project, you may need to determine where
and how a build setting is defined. Because build settings can be
identified by their name and their title (see [Build Setting Syntax](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugsscirduorkb) for details),
depending on where a build setting is defined (in the `xcodebuild` invocation,
in an environment variable, or the Xcode application’s user interface),
you need to map between a build setting name and its corresponding
build setting title.

This article provides tips on how to use the build system
to help you find build setting specifications and troubleshoot build
setting problems you may encounter.

During the development process you may need to find the top
definition of a build setting to change its value during a build.
That is, the specification that overrides all other specifications
throughout the build setting layers (see [Build Setting Evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdi5augr2j) and [Build Setting Layers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugssci5cuoskj) for
details). This section showcases a technique you can use to quickly
locate the top definition of a build setting.

Look for the top definition of a build setting in these places:

- The `xcodebuild` invocation
  (when building using `xcodebuild`)
- The target you’re interested in
- The active build style
- The output of the `env` command

Figure 25-11 shows the steps you would take to find the
definition of a build setting when you know the build setting’s
name or title.

__Figure 25-11__  [Finding the definition of a build
setting

!

1. If you’re
   building using `xcodebuild`,
   look for the build setting name in the tool’s invocation. If the
   build setting is part of the invocation, you found the definition.
2. Look for the build setting in the target you’re interested
   in. You can locate a particular build setting by selecting the All
   Settings collection in the Build pane of the target inspector and
   entering the name or the title of the build setting you’re looking
   for. See [Build Setting Names and Their Corresponding Titles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugsscizeuussb) for mappings
   of most build setting titles to the corresponding build setting
   names and vice versa.

   1. If the build setting
      has a line through it, it means that the build setting is overridden
      by the active build style. Look up the build setting in the active
      build style to find its definition. You can jump to the definition
      of the build setting in the active build style by Control-clicking
      the build setting and choosing Jump to Active Build Style.
   2. If the build setting is displayed in bold text, it means that
      it’s defined in the target and isn’t overridden by the active
      build style. This is the top definition of the build setting.
   3. If the build setting is displayed in nonbold text and doesn’t
      have a line through it, the build setting is defined in the project
      layer or the environment layer (see [Build Setting Layers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugssci5cuoskj) for details).
3. Look for the build setting in the build environment (the definitions
   of all the environment variables the Xcode application or `xcodebuild` have
   access to during the build process).

   1. Add a Run Script build
      phase to the target you’re interested in and make it the first build
      phase to make it easier to locate the script’s output.
   2. Add an invocation to the `env` command
      to the build phase’s shell script.
   3. If you’re building using the Xcode application, open the
      Build Results window, reveal the build log pane, and build the product.
      If you’re building using `xcodebuild`, invoke
      the tool from your shell as you normally would. See [Building a Product](Building%20a%20Product.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmztfvbuuqsiizdeesa) for information
      on how to build in Xcode.
   4. Look at the build log (the detailed log in the Build Results
      window if using the Xcode application). The build environment is
      listed after the group of `setenv` invocations
      that set environment variables that reflect most of the build setting values
      for the current build. Search that group for the name of the build
      setting you’re interested in. If the build setting is not in that
      group, the build setting is not defined for the target you are investigating.

      If
      the build setting is defined in the `setenv` group
      and the `env` group, you
      can override its value only in the target layer or above. If the
      build setting is defined only in the `env` group,
      look for the build setting definition among the environment variables
      defined in the user-configuration files for the logged-in user.
      If you find the build setting there, change its specification, log
      out, and log in.

This section contains several tables that map build setting
names to build setting titles and build setting titles to build
setting names for the general and compiler-related build settings
displayed in the Xcode user interface.

Table 25-2 maps the build setting names with the corresponding
build setting titles of the general build settings.

__Table 25-2__  General build settings by build setting
name

| Build setting name | Build setting title |
| ALTERNATE_MODE | Alternate Install Permissions |
| ALTERNATE_PERMISSIONS_FILES | Alternate Permissions Files |
| ALTERNATE_OWNER | Alternate Install Owner |
| ALTERNATE_GROUP | Alternate Install Group |
| COPYING_PRESERVES_HFS_DATA | Preserve HFS Data |
| CURRENT_PROJECT_VERSION | Current Project Version |
| DEPLOYMENT_LOCATION | Deployment Location |
| DEPLOYMENT_POSTPROCESSING | Deployment Post-processing |
| DYLIB_COMPATIBILITY_VERSION | Compatibility Version |
| DYLIB_CURRENT_VERSION | Current Version |
| EXPORTED_SYMBOLS_FILE | Exported Symbols File |
| FRAMEWORK_SEARCH_PATHS | Framework Search Paths |
| FRAMEWORK_VERSION | Framework Version |
| GENERATE_PKGINFO_FILE | Force Package Info Generation |
| HEADER_SEARCH_PATHS | Header Search Paths |
| INFOPLIST_FILE | Info.plist File |
| INIT_ROUTINE | Initialization Routine |
| INSTALL_GROUP | Install Group |
| INSTALL_MODE_FLAG | Install Permissions |
| INSTALL_OWNER | Install Owner |
| INSTALL_PATH | Installation Path |
| LIBRARY_SEARCH_PATHS | Library Search Paths |
| LIBRARY_STYLE | Library Style |
| MACOSX_DEPLOYMENT_TARGET | Mac OS X Deployment Target |
| OTHER_LDFLAGS | Other Linker Flags |
| PREBINDING | Prebinding |
| PRIVATE_HEADERS_FOLDER_PATH | Private Headers Folder Path |
| PRODUCT_NAME | Product Name |
| PUBLIC_HEADERS_FOLDER_PATH | Public Headers Folder Path |
| REZ_SEARCH_PATHS | Rez Search Paths |
| SECTORDER_FLAGS | Symbol Ordering Flags |
| SKIP_INSTALL | Skip Install |
| UNSTRIPPED_PRODUCT | Unstripped Product |
| VERSIONING_SYSTEM | Versioning System |
| WARNING_LDFLAGS | Warning Linker Flags |
| WRAPPER_EXTENSION | Wrapper Extension |
| ZERO_LINK | Zero Link |

Table 25-3 maps the build setting titles with the corresponding
build setting names of the general build settings.

__Table 25-3__  General build settings by build setting
title

| Build setting title | Build setting name |
| Alternate Install Group | ALTERNATE_GROUP |
| Alternate Install Owner | ALTERNATE_OWNER |
| Alternate Install Permissions | ALTERNATE_MODE |
| Alternate Permissions Files | ALTERNATE_PERMISSIONS_FILES |
| Compatibility Version | DYLIB_COMPATIBILITY_VERSION |
| Current Project Version | CURRENT_PROJECT_VERSION |
| Current Version | DYLIB_CURRENT_VERSION |
| Deployment Location | DEPLOYMENT_LOCATION |
| Deployment Post-processing | DEPLOYMENT_POSTPROCESSING |
| Exported Symbols File | EXPORTED_SYMBOLS_FILE |
| Force Package Info Generation | GENERATE_PKGINFO_FILE |
| Framework Search Paths | FRAMEWORK_SEARCH_PATHS |
| Framework Version | FRAMEWORK_VERSION |
| Header Search Paths | HEADER_SEARCH_PATHS |
| Info.plist File | INFOPLIST_FILE |
| Initialization Routine | INIT_ROUTINE |
| Install Group | INSTALL_GROUP |
| Install Permissions | INSTALL_MODE_FLAG |
| Install Owner | INSTALL_OWNER |
| Installation Path | INSTALL_PATH |
| Library Search Paths | LIBRARY_SEARCH_PATHS |
| Library Style | LIBRARY_STYLE |
| Mac OS X Deployment Target | MACOSX_DEPLOYMENT_TARGET |
| Other Linker Flags | OTHER_LDFLAGS |
| Prebinding | PREBINDING |
| Preserve HFS Data | COPYING_PRESERVES_HFS_DATA |
| Private Headers Folder Path | PRIVATE_HEADERS_FOLDER_PATH |
| Product Name | PRODUCT_NAME |
| Public Headers Folder Path | PUBLIC_HEADERS_FOLDER_PATH |
| Rez Search Paths | REZ_SEARCH_PATHS |
| Skip Install | SKIP_INSTALL |
| Symbol Ordering Flags | SECTORDER_FLAGS |
| Unstripped Product | UNSTRIPPED_PRODUCT |
| Versioning System | VERSIONING_SYSTEM |
| Warning Linker Flags | WARNING_LDFLAGS |
| Wrapper Extension | WRAPPER_EXTENSION |
| Zero Link | ZERO_LINK |

Table 25-4 maps the build setting names with the corresponding
build setting titles of the compiler-related build settings.

__Table 25-4__  GNU C/C++ compiler build settings
by build setting name

| Build setting name | Build setting title |
| GCC_ALTIVEC_EXTENSIONS | Enable AltiVec Extensions |
| GCC_C_LANGUAGE_STANDARD | C Language Dialect |
| GCC_CHAR_IS_UNSIGNED_CHAR | 'char' Type Is Unsigned |
| GCC_CW_ASM_SYNTAX | CodeWarrior-Style Inline Assembly |
| GCC_DEBUGGING_SYMBOLS | Level of Debug Symbols |
| GCC_DYNAMIC_NO_PIC | Generate Position Dependent Code |
| GCC_ENABLE_ASM_KEYWORD | Allow 'asm', 'inline', 'typeof' |
| GCC_ENABLE_CPP_EXCEPTIONS | Enable C++ Exceptions |
| GCC_ENABLE_CPP_RTTI | Enable C++ Runtime Types |
| GCC_ENABLE_FIX_AND_CONTINUE | Fix & Continue |
| GCC_ENABLE_OBJC_EXCEPTIONS | Enable Objective-C Exceptions |
| GCC_ENABLE_OBJC_GC | Enable Objective-C Garbage Collection |
| GCC_ENABLE_PASCAL_STRINGS | Recognize Pascal Strings |
| GCC_ENABLE_TRIGRAPHS | Enable Trigraphs |
| GCC_FAST_MATH | Relax IEEE Compliance |
| GCC_FAST_OBJC_DISPATCH | Accelerated Objective-C Dispatch |
| GCC_GENERATE_DEBUGGING_SYMBOLS | Generate Debug Symbols |
| GCC_GENERATE_PROFILING_CODE | Generate Profiling Code |
| GCC_INPUT_FILETYPE | Compile Sources As |
| GCC_MODEL_CPU | Target CPU |
| GCC_MODEL_PPC64 | Use 64-bit Integer Math |
| GCC_MODEL_TUNING | Instruction Scheduling |
| GCC_NO_COMMON_BLOCKS | No Common Blocks |
| GCC_NO_NIL_RECEIVERS | Assume Non-nil Receivers |
| GCC_ONE_BYTE_BOOL | Use One Byte 'bool' |
| GCC_OPTIMIZATION_LEVEL | Optimization Level |
| GCC_PFE_FILE_C_DIALECTS | C Dialects to Precompile |
| GCC_PRECOMPILE_PREFIX_HEADER | Precompile Prefix Header |
| GCC_PREFIX_HEADER | Prefix Header |
| GCC_PREPROCESSOR_DEFINITIONS | Preprocessor Macros |
| GCC_REUSE_STRINGS | Make Strings Read-Only |
| GCC_SHORT_ENUMS | Short Enumeration Constants |
| GCC_STRICT_ALIASING | Enforce Strict Aliasing |
| GCC_TREAT_NONCONFORMANT_CODE_ERRORS_AS_WARNINGS | Treat Nonconformant Code Errors as Warnings |
| GCC_TREAT_WARNINGS_AS_ERRORS | Treat Warnings as Errors |
| GCC_UNROLL_LOOPS | Unroll Loops |
| GCC_WARN_ABOUT_MISSING_PROTOTYPES | Missing Function Prototypes |
| GCC_WARN_ABOUT_RETURN_TYPE | Mismatched Return Type |
| GCC_WARN_ALLOW_INCOMPLETE_PROTOCOL | Incomplete Objective-C Protocols |
| GCC_WARN_CHECK_SWITCH_STATEMENTS | Check Switch Statements |
| GCC_WARN_EFFECTIVE_CPLUSPLUS_VIOLATIONS | Effective C++ Violations |
| GCC_WARN_FOUR_CHARACTER_CONSTANTS | Four Character Literals |
| GCC_WARN_HIDDEN_VIRTUAL_FUNCTIONS | Hidden Virtual Functions |
| GCC_WARN_INHIBIT_ALL_WARNINGS | Inhibit All Warnings |
| GCC_WARN_NON_VIRTUAL_DESTRUCTOR | Non-virtual Destructor |
| GCC_WARN_INITIALIZER_NOT_FULLY_BRACKETED | Initializer Not Fully Bracketed |
| GCC_WARN_MISSING_PARENTHESES | Missing Braces and Parentheses |
| GCC_WARN_PEDANTIC | Pedantic Warnings |
| GCC_WARN_SHADOW | Hidden Local Variables |
| GCC_WARN_SIGN_COMPARE | Sign Comparison |
| GCC_WARN_TYPECHECK_CALLS_TO_PRINTF | Typecheck Calls to printf/scanf |
| GCC_WARN_UNINITIALIZED_AUTOS | Uninitialized Automatic Variables |
| GCC_WARN_UNKNOWN_PRAGMAS | Unknown Pragma |
| GCC_WARN_UNUSED_FUNCTION | Unused Functions |
| GCC_WARN_UNUSED_LABEL | Unused Labels |
| GCC_WARN_UNUSED_PARAMETER | Unused Parameters |
| GCC_WARN_UNUSED_VALUE | Unused Values |
| GCC_WARN_UNUSED_VARIABLE | Unused Variables |
| OTHER_CFLAGS | Other C Flags |
| OTHER_CPLUSPLUSFLAGS | Other C++ Flags |
| WARNING_CFLAGS | Other Warning Flags |

Table 25-5 maps the build setting titles with the corresponding
build setting names of the compiler-related build settings.

__Table 25-5__  GNU C/C++ compiler build settings
by build setting title

| Build setting title | Build setting name |
| Accelerated Objective-C Dispatch | GCC_FAST_OBJC_DISPATCH |
| Allow 'asm', 'inline', 'typeof' | GCC_ENABLE_ASM_KEYWORD |
| Assume Non-nil Receivers | GCC_NO_NIL_RECEIVERS |
| C Dialects to Precompile | GCC_PFE_FILE_C_DIALECTS |
| C Language Dialect | GCC_C_LANGUAGE_STANDARD |
| 'char' Type Is Unsigned | GCC_CHAR_IS_UNSIGNED_CHAR |
| Check Switch Statements | GCC_WARN_CHECK_SWITCH_STATEMENTS |
| CodeWarrior-Style Inline Assembly | GCC_CW_ASM_SYNTAX |
| Compile Sources As | GCC_INPUT_FILETYPE |
| Effective C++ Violations | GCC_WARN_EFFECTIVE_CPLUSPLUS_VIOLATIONS |
| Enable AltiVec Extensions | GCC_ALTIVEC_EXTENSIONS |
| Enable C++ Exceptions | GCC_ENABLE_CPP_EXCEPTIONS |
| Enable C++ Runtime Types | GCC_ENABLE_CPP_RTTI |
| Enable Objective-C Exceptions | GCC_ENABLE_OBJC_EXCEPTIONS |
| Enable Objective-C Garbage Collection | GCC_ENABLE_OBJC_GC |
| Enable Trigraphs | GCC_ENABLE_TRIGRAPHS |
| Enforce Strict Aliasing | GCC_STRICT_ALIASING |
| Fix & Continue | GCC_ENABLE_FIX_AND_CONTINUE |
| Four Character Literals | GCC_WARN_FOUR_CHARACTER_CONSTANTS |
| Generate Profiling Code | GCC_GENERATE_PROFILING_CODE |
| Generate Debug Symbols | GCC_GENERATE_DEBUGGING_SYMBOLS |
| Generate Position Dependent Code | GCC_DYNAMIC_NO_PIC |
| Hidden Local Variables | GCC_WARN_SHADOW |
| Hidden Virtual Functions | GCC_WARN_HIDDEN_VIRTUAL_FUNCTIONS |
| Incomplete Objective-C Protocols | GCC_WARN_ALLOW_INCOMPLETE_PROTOCOL |
| Inhibit All Warnings | GCC_WARN_INHIBIT_ALL_WARNINGS |
| Initializer Not Fully Bracketed | GCC_WARN_INITIALIZER_NOT_FULLY_BRACKETED |
| Instruction Scheduling | GCC_MODEL_TUNING |
| Level of Debug Symbols | GCC_DEBUGGING_SYMBOLS |
| Make Strings Read-Only | GCC_REUSE_STRINGS |
| Mismatched Return Type | GCC_WARN_ABOUT_RETURN_TYPE |
| Missing Braces and Parentheses | GCC_WARN_MISSING_PARENTHESES |
| Missing Function Prototypes | GCC_WARN_ABOUT_MISSING_PROTOTYPES |
| No Common Blocks | GCC_NO_COMMON_BLOCKS |
| Non-virtual Destructor | GCC_WARN_NON_VIRTUAL_DESTRUCTOR |
| Optimization Level | GCC_OPTIMIZATION_LEVEL |
| Other C Flags | OTHER_CFLAGS |
| Other C++ Flags | OTHER_CPLUSPLUSFLAGS |
| Other Warning Flags | WARNING_CFLAGS |
| Pedantic Warnings | GCC_WARN_PEDANTIC |
| Precompile Prefix Header | GCC_PRECOMPILE_PREFIX_HEADER |
| Prefix Header | GCC_PREFIX_HEADER |
| Preprocessor Macros | GCC_PREPROCESSOR_DEFINITIONS |
| Recognize Pascal Strings | GCC_ENABLE_PASCAL_STRINGS |
| Relax IEEE Compliance | GCC_FAST_MATH |
| Short Enumeration Constants | GCC_SHORT_ENUMS |
| Sign Comparison | GCC_WARN_SIGN_COMPARE |
| Target CPU | GCC_MODEL_CPU |
| Treat Nonconformant Code Errors as Warnings | GCC_TREAT_NONCONFORMANT_CODE_ERRORS_AS_WARNINGS |
| Treat Warnings as Errors | GCC_TREAT_WARNINGS_AS_ERRORS |
| Typecheck Calls to printf/scanf | GCC_WARN_TYPECHECK_CALLS_TO_PRINTF |
| Uninitialized Automatic Variables | GCC_WARN_UNINITIALIZED_AUTOS |
| Unknown Pragma | GCC_WARN_UNKNOWN_PRAGMAS |
| Unroll Loops | GCC_UNROLL_LOOPS |
| Unused Functions | GCC_WARN_UNUSED_FUNCTION |
| Unused Labels | GCC_WARN_UNUSED_LABEL |
| Unused Parameters | GCC_WARN_UNUSED_PARAMETER |
| Unused Values | GCC_WARN_UNUSED_VALUE |
| Unused Variables | GCC_WARN_UNUSED_VARIABLE |
| Use 64-bit Integer Math | GCC_MODEL_PPC64 |
| Use One Byte 'bool' | GCC_ONE_BYTE_BOOL |

Table 25-6 shows GCC 4.0 build settings.

__Table 25-6__  GCC 4.0 build settings by build setting
title

| Build setting title | Build setting name |
| Auto-vectorization | GCC_AUTO_VECTORIZATION |
| Feedback-Directed Optimization | GCC_FEEDBACK_DIRECTED_OPTIMIZATION |
| Symbols Hidden by Default | GCC_SYMBOLS_PRIVATE_EXTERN |
| Inline Functions Hidden | GCC_INLINES_ARE_PRIVATE_EXTERN |

The build system provides facilities for customizing the build
process for groups of files assigned to specific build phases. It
includes the Other C Flags (OTHER_CFLAGS), Other C++ Flags (OTHER_CPLUSPLUSFLAGS),
Other Warning Flags (WARNING_CFLAGS), and Preprocessor Macros (GCC_PREPROCESSOR_DEFINITIONS)
build settings, among many others, to customize the invocation of
the compiler when processing C-based source files. However, sometimes
it’s necessary to specify compiler flags on a per-file basis.
For example, in a project that treats warnings as errors in general,
you may have a set of cross-platform source files where it’s more
convenient to allow some warnings to remain.

To set compiler flags for a file, select the source file and
open an inspector or Info window. Click Build to open the Build
pane, as shown in Figure 25-12. Type any compiler flags you wish to assign
to the file in the Additional Compiler Flags for Target field. Multiple
flags should be separated by spaces. You can use multiple selection
to assign compiler flags to a subset of the files in a target. Note
that the Build pane is only available for files containing source
code.

For each target that a file belongs to, Xcode maintains a
separate list of compiler flags assigned to a file. To specify compiler
flags for use with a file when it is built as part of a particular
target, select the file from the appropriate build phase in that
target and open an inspector window, as described above. If you
open an inspector window for the file from any other source or smart
group in the project window, Xcode assumes you want to assign compiler
flags to the file in the active target; thus, the Build pane is
only available if the file is part of the active target.

__Figure 25-12__  The Build pane of the file inspector

!

When the build system constructs the command-line invocation
for the tool that processes the source file, it adds the additional
compiler flags assigned to the file to the invocation. The build
system doesn’t validate the flags you add; that is, it doesn’t
test whether the compiler actually supports the options you add,
and it doesn’t investigate whether the options you add conflict
with the ones it generates. If you add a group of compiler options and
flags for a file and the file no longer compiles, you should remove
all the flags you added and add them back one at a time, making
sure the file compiles after you add each flag. You should also
consult the tool’s documentation to learn about possible conflicts.

The additional compiler flags specified for a file will always
be used when the file is processed as part of a build and cannot
be overridden in any of the build setting layers. See [Build Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdjfdecrch) for
information on build settings.

[Next](Build%20Styles.md)[Previous](Build%20Phases.md)

