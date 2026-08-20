---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/bs_targets/bs_targets.html
archived_at: '2026-07-15T07:29:03.206093Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Build%20Phases.md)[Previous](The%20Build%20System.md)

# Targets

The organizing principle of the Xcode build
system is the target. A _target_ contains the instructions
for building a finished product from a set of files in your project.
Some common types of products are frameworks, libraries, applications,
and command-line tools. Each target builds a single product. A simple
Xcode project has just one target, which produces one product from
the project’s files. A larger development effort with multiple products
may require a more complex project containing several related targets.
For example, a project for a client-server software package may
contain targets that create these products:

- A client
  application
- A server application
- Command-line tool versions of the client and server functionality
- A private framework that all the other targets use

Figure 23-1 shows the targets you may have in a project
such as the one described above, and the products that those targets
create.

__Figure 23-1__  Targets and products

!

When you initiate a build, Xcode builds the product specified
by the current, or active, target and any targets on which the active
target depends. In the Groups & Files list, the active target
is marked by a checkmark in a round green circle. You can also see which target
is active, as well as change the active target, in the Active Target
pop-up menu in the project and Build Results windows, as described
in [Building a Product](Building%20a%20Product.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmztfvbuuqsiizdeesa).

This chapter describes targets in Xcode and the information
that they contain, and shows you how to create and modify targets.

A target is a blueprint for creating a product; the target
organizes the inputs to the build system process—the source files
and the instructions for processing them—required to create that
product. These inputs are:

- _Files_.
  Each target contains a list of files that the build system takes
  as inputs and performs various operations on—such as compiling,
  linking, copying, and so forth—to arrive at the final product.
  Examples of source files are source code files, headers, resource
  files, and so forth.
- _Build phases_. Build phases organize the
  source files of a target according to the operations required to
  build a target’s product. Each build phase consists of a list
  of input files and a task to be performed on each of those input
  files. Common build phases include compiling files, linking object
  files, and copying resource files.

  Xcode populates each new
  target with a default set of build phases. You can add or remove
  build phases to change the operations performed by Xcode when building
  the target. For further details on build phases, see [Build Phases](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawugssbi5ceiscj).
- _Build settings_. A build setting contains
  information on how to perform the operations required to build a
  product. For example, a build setting can specify command-line options
  for Xcode to pass to the compiler. Build settings can contain tool-specific options, paths
  to build files and product directories, and other information used
  by Xcode to determine how to perform build operations.

  Each
  target contains a list of build settings. Although you will most
  likely make most of your build setting changes at the target level,
  build settings can be modified in a number of other locations, such
  as build styles, as well. By modifying build settings at these other
  layers, you can quickly make a change and apply it to multiple targets, conditionally
  change the way a product is built, and so forth.

  Because
  build settings represent variable aspects of the build process,
  they are the most flexible means of customizing the build process.
  See [Build Settings](Build%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdjfdecrch) for more information
  on using build settings.
- _Build rules_. A target’s build rules determine
  how each source file in the target is processed. Each build rule
  consists of a condition—such as files matching the type “.c”—and
  an action. Typically, this action specifies the tool Xcode should
  invoke to process files that meet the condition; this is how Xcode
  determines the compiler to use for compiling source files. Build
  rules apply only to the Compile Sources and Build ResourceManager
  Resources build phases. Xcode defines a default set of build rules, but
  you can define your own custom build rules for a target. For more
  information on using build rules, see [Build Rules](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawueqsdindekrck).

__Figure 23-2__  A
target

!

A target and the product that it creates are closely related;
every target has an associated product type. When you create a new
target from a target or project template, you choose the target’s
product type, as described in [Creating a New Target](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugsceijbukq2j).

Based on the product type, Xcode specifies initial values
for certain product-specific build settings. For example, when you
create a target that builds an application, Xcode assigns it the
build setting specification INSTALL_PATH = `"/Applications"` based
on the product type. Any subsequent changes you make to the target
after creating it may override these default values. Note that the
project and target templates contain additional configuration information
that Xcode uses when it creates new targets.

When you create a new project from one of the Xcode project
templates, Xcode automatically creates a target for you. If, however,
your project needs to contain more than one target—usually because
you are creating more than one product—you can also add new targets
to an existing project. This section shows you how to:

- Create a
  new target.
- Duplicate an existing target.
- Remove unused targets from the project.

If you are adding new targets to your project, chances are
you’ve already made a number of decisions about product type,
programming language, and framework. Xcode provides a number of
target templates to support your choices. The selection of target
templates is similar to the selection of project templates. The
target specifies the target’s product type, a list of default
build phases, and default specifications for some build settings.
A target template typically includes all build settings and build
phases required to build a basic instance of the specified product.
Unlike the project templates provided by Xcode, the target templates
do not specify any default files; you must add files to the target
yourself, as described in [Working with Files in a Target](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugskijfduoqkh).

You can create a new target and add it to an existing project
in either of the following ways:

- Choose Project
  > New Target.
- Control-click in the Groups & Files list and choose Add
  > New Target from the contextual menu.

Xcode presents you with the New Target Assistant, shown here,
which lets you choose from a number of possible target templates.
Each target template corresponds to a particular type of product,
such as an application or loadable bundle. Select one of these templates
and click Next. Enter the name of the target; if more than one project
is open, you can choose which project to add the new target to from
the Add to Project menu. When you click Finish, Xcode creates a
new target configured for the specified product type. Xcode also
creates a reference to the target’s product and places it in your
project, although the product does not exist on disk until you build
the target.

__Figure 23-3__  The
New Target Assistant

!

Xcode provides the target templates listed in the following
tables. Table 23-1 lists templates that create targets using
Xcode’s native build system. Because it performs all target and
file-level dependency analysis for targets using the native build
system, Xcode can offer detailed feedback about the build process
and integration with the user interface for these targets.

__Table 23-1__  Xcode target templates

| Target template | Creates |
| _BSD_ |  |
| Dynamic Library | A dynamic library, written in C, that makes use of BSD. |
| Shell Tool | A command-line utility, written in C. |
| Static Library | A static library, written in C, that makes use of BSD. |
| _Carbon_ |  |
| Application | An application, written in C or C++, that links against the Carbon framework. |
| Dynamic Library | A dynamic library that links against the Carbon framework. |
| Framework | A framework based on the Carbon framework. |
| Loadable Bundle | A bundle, such as a plug-in, that can be loaded into a running program. |
| Shell Tool | A command-line utility based on the Carbon framework. |
| Static Library | A static library, written in C or C++, based on the Carbon framework. |
| _Cocoa_ |  |
| Application | An application, written in Objective-C or Objective-C++, that links against the Cocoa framework. |
| Dynamic Library | A dynamic library that links against the Cocoa framework. |
| Framework | A framework based on the Cocoa framework. |
| Loadable Bundle | A bundle, such as a plug-in, that can be loaded into a running program. |
| Shell Tool | A command-line utility based on the Cocoa framework. |
| Static Library | A static library, written in Objective-C or Objective-C++, based on the Cocoa framework. |
| _Java_ |  |
| Application | An application, written in Java, and packaged as an application bundle. |
| Applet | A Java applet, built as a JAR file. |
| Tool | A command-line utility, written in Java and built as a JAR file. |
| _Kernel Extension_ |  |
| Generic Kernel Extension | A kernel extension |
| IOKit Driver | A device driver that uses the I/O Kit. |

Xcode also supports targets that use Project Builder’s Jam-based
build system. Table 23-2 lists the templates that create targets using
the Project Builder build system, called legacy targets. Note that
Jam-based targets are supported only for compatibility with existing
Project Builder projects. Where possible, you should use native
targets instead. Legacy targets are discussed further in [Converting a Project Builder Target](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugq2fivcekqsj).

__Table 23-2__  Legacy target templates

| Template | Creates |
| Application | An application bundle. |
| Bundle | A standard bundle. |
| _Cocoa_ |  |
| Application | An application, written in Objective-C or Objective-C++, that links against the Cocoa framework |
| Framework | A framework. |
| _Java_ |  |
| Application | An application, written in Java, and packaged as an application bundle. |
| Applet | A Java applet, built as a JAR file. |
| Package |  |
| Tool | A command-line utility, written in Java and built as a JAR file. |
| _Kernel Extension_ |  |
| Generic Kernel Extension | A kernel extension |
| IOKit Driver | A device driver that uses the I/O Kit. |
| Library | A dynamic or static library |
| Tool | A command-line utility. |

In addition to the target templates described above, Xcode
defines a handful of target templates that do not necessarily correspond
to a particular product type. These targets are described in the
next section.

Xcode defines a handful of target templates that do not necessarily
correspond to a particular product type. Instead, these targets
can be used to:

- Build a group
  of targets together
- Build a product using an external build system
- Run a shell script
- Copy files to a specific location in the filesystem

Xcode defines a special type of target that lets you build
a group of targets at once, even if those targets do not depend
on each other. An _aggregate target_ does not have
an associated product and it does not contain build information,
such as build rules. An aggregate target depends on each of the
targets you want to build together. For example, you may have a
suite of applications and want to build them at once for a final
build. You would create an aggregate target and make it depend on
each of the individual application targets; to build the entire
application suite, just build the aggregate target.

An aggregate target may contain a custom Run Script build
phase or a Copy Files build phase, but it does not contain any other
build phases.

Xcode allows you to create targets that do not use Xcode’s
own native build system but instead use an external build tool that
you specify. For example, if you have an existing project with a
makefile, you can use an external target to run `make` and
build the product.

An external target creates a product but does not contain
build phases. Instead, it calls a build tool in a directory. With
an external target, you can take full advantage of Xcode’s editor,
class browser, and source-level debugger. However, many Xcode features—such
as ZeroLink and Fix and Continue—rely on the build information
maintained by Xcode for targets using the native build system. As
a result, these are not available to an external target. Furthermore,
you must maintain your custom build system yourself. For instance, if
you need to add files to an external target built using `make`,
you must edit the makefile yourself.

A Shell Script target is an aggregate target that contains
only one build phase, a Run Script build phase. Building a Shell
Script target simply runs the associated shell script. Shell Script
targets are useful if you have custom build steps that need to be
performed. While Run Script build phases allow you to add custom
steps to the build process for a single target, a Shell Script target
lets you define a custom build operation that you can use with many
different targets. For example, if your project has several targets
that each use the files generated by a Shell Script target, you
can make each of those targets depend upon the Shell Script target.

A Copy Files target is an aggregate target that contains only
one build phase, a Copy Files build phase. Building a Copy Files
target simply copies the associated files to the specified destination
in the filesystem. Copy Files targets are useful if you have custom
build steps that require files that are not specific to any other
targets to be copied. While Copy Files build phases allow you to
add a step to the build process for a single target that copies
files in that target, a Copy Files target lets you copy files that
are not specific to any one target. For example, if your project
has several targets that require the same files to be installed
at a particular location, you can use a Copy Files target to copy
the files, and make each of the other targets depend upon the Copy
Files target.

There are a number of reasons why you might need to duplicate
a target: you require two targets that are very similar but contain
slight differences in the files or build phases that they include,
or you have a complicated set of options that you build with and
would prefer to simply start with a copy of a target that already
contains those build settings.

Xcode allows you to duplicate a target, creating a copy that
contains all of the same files, build phases, dependencies and build
settings. You can create a copy of a target in the following way:

1. In the Groups
   & Files list, select the target you which to copy.
2. Choose Edit > Duplicate or Control-click and choose Duplicate
   from the contextual menu.

If your project contains targets that are no longer in use,
you can remove them from the project in the following ways:

1. Select the
   target to delete in the Groups & Files list.
2. Press the Delete key or choose Edit > Delete.

When you delete a target, Xcode also deletes the product reference
for the product created by that target and removes any dependencies
on the deleted target.

In a complex project, you may have several targets that create
a number of related products. Frequently, these targets need to
be built in a specified order. Returning to the example of the client-server
software package created by the project shown in [Figure 23-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugssbincumq2h), you’ll
see that the client application, server application, and command-line
tool targets each link to the private framework created by another
target in the same project.

Before the application and command-line tool targets can be
built, the framework target must be built. Because they require
the private framework in order to build, each of the application
and command-line tool targets is said to depend upon the target
that creates the framework. You can use a _target dependency_ to
ensure that Xcode builds targets in the proper order; in this example,
you would add a dependency upon the framework target to each of
the application and command-line tool targets.

However, the applications and command-line tool in the client-server
package must still be built individually. None of these targets
requires the product created by any target other than the framework
target. Xcode provides another mechanism for grouping targets that you
want to build together, but that are otherwise unrelated; this is
an aggregate target. The following sections show you how to add
a target dependency and create an aggregate target, and gives an
example of how you can use these tools to organize a software development
effort with multiple products and projects.

When you build a target with a dependency upon another target,
Xcode makes sure that this other target is built and up-to-date
before building the active target. That way, you can guarantee that
when target A needs the product created by target B, target B is
built before target A. In addition, if there are errors building
target B, Xcode doesn’t build target A.

You can view and modify a target’s dependencies:

- In the General
  pane of the target inspector. The Direct Dependencies list in the
  bottom half of the General pane shows the other targets upon which
  the current target depends.

  To add a target dependency, click
  the plus sign button and select the target upon which you want the
  current target to depend in the resulting dialog. The list of targets includes
  all of the other targets in the current project, as well as the
  targets in any referenced projects. Targets in referenced projects
  are grouped according to the project to which they belong; click
  the disclosure triangle next to the project icon to see the targets
  in that project. For more information on referencing other projects,
  see [Referencing Other Projects](Files%20in%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgewugsscjjeeuq2k).

  To
  remove a target dependency, select it in the list and click the
  minus button.
- In the Groups & Files list. Click the disclosure triangle
  next to the target; the targets that the current target depends
  on are listed before the build phases in the target. You can make
  the current target depend on another target by dragging that target
  to the current target in the Groups & Files list. To delete
  a target dependency, select it in the Groups & Files list and
  press Delete or choose Edit > Delete. Figure 23-4 shows
  a target dependency in the Groups & Files list.

__Figure 23-4__  A target dependency in the Groups
& Files list

!

To build several related targets at the same time, even if
they aren’t dependent on each other, create an aggregate target. As
described in [Special Types of Targets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugskiirceiskc), an aggregate target does not produce
a product itself and it does not contain build rules or information
property list entries. Instead it exists so that you can make it
dependent on other targets. To build a group of related targets,
just build the aggregate target.

To create an aggregate target, choose Project > New Target
and select Aggregate from the New Target Assistant. For each target
you want to build with this aggregate target, add a target dependency
to the aggregate target, as described in the [Adding a Target Dependency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugsscjfduusce).

Note that, while it does not contain any other build phases,
an aggregate target can include a Run Script or Copy Files build
phase.

Suppose that your company has two teams working on separate
applications, that one application includes an internal library,
and that each application relies on a framework supplied by a third
team. Figure 23-5 shows one way to set up your software development
with three Xcode projects, using target dependencies, aggregate
targets, and cross-project dependencies to relate the various products.

In Figure 23-5, the `Juicer_app` project
contains the `Juicer_app` target,
for building the Juicer application, and the `Juicer_lib` target,
for building an internal library. The application target depends
on the library target, and also has a cross-project dependency on
the `Mixer_framework` target
in the `Mixer_framework` project.
Finally, the `Juicer_app` project
contains the `Juicer_aggregate` target,
as a convenience for building the entire suite of projects.

In Figure 23-5, the `Blender_app` project
contains a target for building the Blender application. The Blender
target also has a cross-project dependency on the Mixer framework.

__Figure 23-5__  Three projects with dependencies

!

Finally, the `Mixer_framework` project
contains a target for building the Mixer framework, used by both
the Juicer and Blender applications.

Given this combination of projects, targets, and dependencies,
the following statements are true:

- Building
  the Juicer target builds the Juicer library, if it needs updating,
  and also builds the Mixer framework, if it needs updating.
- Building the Juicer aggregate target builds the Juicer application,
  which builds the Juicer library, if it needs updating. The aggregate
  target also builds the Blender application and the Mixer framework.
- Building the Juicer library does not cause any other targets
  to be built.
- Building the Blender target builds the Mixer framework, if
  it needs updating.

When you add files to a project, you can have Xcode also add
those files to one or more targets. When you add files to a target
in this way, Xcode automatically assigns them to the appropriate
build phase, based on the file’s type. This is the easiest way
to add files to a target. However, you may have existing files in
your project that you wish to add to a target, or find that you
no longer need a target file. This section describes how to view
the files in a target and shows you how to add and remove target
files.

To view all of the files included in a target, select the
target in the Groups & Files list; all targets are organized
into the Targets smart group. The detail view shows all of the files and
folders in the target, similar to what you see in the following
figure. If one is not already open in the current window, open a
detail view by choosing View > Detail.

__Figure 23-6__  Viewing
targets in the project window

!!

You can also see a target’s files grouped according to the
operation performed on those files during the build process. If
you click the disclosure triangle next to a target, you will see
the build phases for that target. Build phases, described in further
detail in [Build Phases](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawugssbi5ceiscj), represent a
task performed when the target is built. To see the files in a particular build
phase, click the disclosure triangle next to the build phase or
select the build phase and open a detail view.

You can change which files are included in a target from the
project window. To add files to a target, you can:

- Drag the
  file reference or references to the appropriate build phase of the
  given target in the Groups & Files list. For native targets,
  Xcode does not let you drag a file to a build phase that does not
  accept that type of file as an input. For example, you cannot drag
  a NIB file to the Compile Sources build phase. See [Build Phases](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawugssbi5ceiscj) for more information on
  the available build phases and their files.
- Specify that a file be included in a target when you add that
  file to your project, as described in [Adding Files, Frameworks, and Folders to a Project](Files%20in%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgewugsscirbukssf).
- To add a file to the active target, find the file in the detail
  view or in the Groups & Files list and select the checkbox in
  the Target column for that file. If the Target column is not visible,
  choose View > Detail View Columns > Target or View > Groups
  & Files Columns > Target.

To remove a file from a target, do the following in the Groups
& Files list:

1. Click the
   disclosure triangle next to the target to reveal the target’s
   build phases.
2. Click the disclosure next to the build phase to which the
   file belongs.
3. Select the file to remove from the target and click Delete
   or choose Edit > Delete.

To remove a file from the active target, find the file in
the detail view or in the Groups & Files list and deselect the
checkbox in the Target column for that file. Xcode removes the file from
the target, but does not remove the file reference from the project.

Like most other project items, targets have inspector and
Info windows that allow you to view and modify target settings.
As previously described in [Anatomy of a Target](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugskiinbumqkc), a target
defines the instructions necessary to create a product. Each target
has an associated set of files, tasks and settings that together
constitute these instructions. You can edit and inspect many of
these settings in the target inspector.

The information available in the inspector window varies,
depending on the type of target. The inspector window for native
targets lets you view and edit all target settings and build information
associated with that target. The inspector window for legacy and external
targets contains only general information. To edit build information
for either of these types of targets, you must use the target editor.

The inspector window is the primary means of viewing and editing
the information in native targets. Figure 23-7 shows the inspector
window for a native target.

__Figure 23-7__  The Info window for a native target

!

This window contains the following panes:

- The General
  pane contains general information about a target, such as its name,
  the name of the associated product, and target dependencies. The
  General pane is described in [Editing General Target Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wueqsdirauessf).
- The Build pane lets you view and edit build settings for the
  target. The Build pane is described in [Editing Build Settings in the Xcode Application](Build%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueq2jjfaucskf).
- The Rules pane displays the current system build rules, as
  well as any custom build rules defined for the current target. The
  Rules pane is described in [Build Rules](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawueqsdindekrck).
- The Properties pane lets you edit information property list
  entries for targets that create products requiring Info.plist files,
  such as applications and other bundles. If the target does not have
  an Info.plist file, this pane is not visible in the inspector. This
  pane is described in [Editing Information Property List Entries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wueq2jincemr2b).
- Comments. The Comments pane lets you associate notes or other
  documentation with the target. See [Adding Comments to Project Items](Organizing%20Xcode%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruhawueq2jjfcukq2d) for
  more information.

You can view and edit only general target information in the
inspector window for Jam-based Project Builder targets and external
targets. You cannot configure build information for these targets.
The inspector window for legacy and external targets contains the following
panes:

- The General
  pane contains general information about a target, such as its name,
  the name of the associated product, and target dependencies. The
  General pane is described in [Editing General Target Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wueqsdirauessf).
- Comments. The Comments pane lets you associate notes or other
  documentation with the target. See [Adding Comments to Project Items](Organizing%20Xcode%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruhawueq2jjfcukq2d) for
  more information.

If you have an existing Project Builder project with a Jam-based
target, you can convert your target to use the Xcode native build
system to edit build settings or build rules for the target in an
inspector or Info window.

To edit the build settings for Jam-based and external targets
in Xcode, use the target editor, described in [Editing Build Settings for Legacy and External Targets](Build%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdineeqr2g).

In the General pane of the target inspector, you can edit
basic target settings for any target in Xcode. The General pane
contains the following settings:

- Name. This
  is the name Xcode uses to refer to the target. To rename the target,
  click in the text field and type the new name.
- Type. This is type of product created by the target. The product
  type is determined when you create the target; you cannot change
  it.
- Product. The name of the product created from the target;
  for example, “MyApp.app.” The Product Name (PRODUCT_NAME) build
  setting specifies the product name, excluding any extension; in
  this example, “MyApp.”By default, this is the same as the target
  name. To change the name of the product, you can change the name
  of the target or customize the Product Name build setting.

  To
  change the product extension—in this case, “app”—change
  the value of the Wrapper Extension (WRAPPER_EXTENSION) build setting.
- Dependencies. A list of the targets upon which the current
  target depends. See [Adding a Target Dependency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugsscjfduusce).

Information property list entries contain information used
by the Finder and system software. This information ends up in a
file called `Info.plist` that’s
contained within the product’s bundle. If a product does not come
in the form of a bundle, it has no `Info.plist` file.

The `Info.plist` file
tells the Finder what the bundle’s icon is, what documents it
can open, what URLs it can handle, and so on. Unlike build settings,
property list entries do not affect the build process but are simply
copied directly into the bundle’s `Info.plist` file
at the end of the build process. For a list of entries used by the
system and Finder, see _[Runtime Configuration Guidelines](../../Mac%20OSX/Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_.

The Properties pane of the target inspector, shown below,
allows you to edit information property list entries for native
targets. This pane is only visible for targets that create products
with Info.plist files.

__Figure 23-8__  The
Properties pane of the target inspector window

!

The top section of the pane allows you to edit basic information
about the product, such as the name of the associated executable,
the identifier, type and creator, version information, and an icon
to associate with the finished product. Note that the name of the icon
here must match the name of an icon file that is copied into the
Resources folder of the product bundle.

The Principal Class and Main Nib File options are specific
to Cocoa applications and bundles. The Principal Class corresponds
to `NSPrincipalClass`.
The Main Nib File field specifies the nib file that’s automatically
loaded when the application is launched. It corresponds to the information
property list key `NSMainNibFile`.

The Document Types table allows you to specify which documents
your finished product can handle. You can add and remove document
types from this list using the plus and minus buttons. Here is what’s
in the Document Types table:

- Name is the
  name of the document type. For example, “Apple Sketch Document.”
- Class is the subclass of NSDocument that this document uses.
  Use this field only if you’re writing a document-based Cocoa application.
- Extensions contains a list of the filename extensions for
  this document type. Don’t include the period in the extension.
  For example, “sketch” and “draw2”.
- UTI contains a list of Uniform Type Identifiers (or UTIs)
  for the document. UTIs are strings that uniquely identify abstract
  types. They can be used to describe a file format or data type,
  but can also be used to describe type information for other sorts
  of entities, such as directories, volumes, or packages. For more
  information on UTIs, see the header file `UTType.h`,
  available as part of LaunchServices.framework in Mac OS X v. 10.3
  and later.
- MIME Types contains a list of the MIME types for the document.
- OS Types contains a list of four-letter codes for the document.
  These codes are stored in the documents’ resources or information
  property list files. For example, “sktc”.
- Icon File is the name of the file that contains the document
  type’s icon.
- Role describes how the application uses the documents of this
  type. You can choose from three values:

  - Editor means this
    application can display, edit, and save documents of this type.
  - Viewer means this application can display, but not edit, documents
    of this type.
  - None means this application can neither display nor edit documents
    of this type but instead uses them in some other way. For example,
    the Finder could declare an icon for font documents.
- Package specifies whether the document is a single file or
  a file package.

To edit a document type, click the type’s line in the Document
Types list and edit the document type information.

You may have additional keys that you need to include in your `Info.plist` file;
for example, applications that include Apple Help help books need
two additional `Info.plist` entries.
To add these additional keys, you can edit the `Info.plist` file
directly, by clicking the Open Info.plist as File button at the
bottom of the Properties pane. You can refer to build settings in
the `Info.plist` file.
For example, `$(PRODUCT_NAME)` expands
to the base name of the product built by the target.

You can set properties on multiple targets; simply select
the targets in the project window and open an Info or inspector
window. In the Properties pane, you can edit the values of properties
that apply to more than one target.

You cannot configure Info.plist entries for Jam-based Project
Builder targets in the target inspector. To edit the Info.plist
entries for Jam-based targets in Xcode, select the target in the
Groups & Files list. If you have an editor open in the project
window, Xcode displays the Project Builder target editor. To view
this target editor in a separate window, double-click the target.
Select Info.plist Entries in the left side of the target editor;
Xcode displays the target’s Info.plist entries in the target editor.

Xcode supports existing Project Builder targets that use the
Project Builder build system, based on the Jam software build tool.
Based on the information it maintains for a Jam-based target—build
phases and build settings—Xcode creates a text-based Jamfile for
the target and then invokes the `jam` command
to perform the build. You can continue to use your existing Project
Builder targets, or even create new Jam-based targets.

Although Xcode recognizes and can build Project Builder targets
using the Jam-based build system, there are many advantages to converting
to “native” targets that use Xcode’s native build system.
One advantage is shorter build times, particularly for incremental builds.
In addition, many of the new Xcode features—such as ZeroLink,
and Fix and Continue—work only with native targets.

Xcode’s native build system performs its own dependency
analysis and directly invokes the necessary build commands. The
native build system takes advantage of the detailed information
that the Xcode application maintains about a project’s targets
and relationships to provide finer control over the build process
and better feedback from the build system than you can obtain from
using an external tool.

To convert all Jam-based targets in your project to the native
build system, choose Project > Upgrade All Targets in Project
to Native.

To upgrade a single target to use the native build system,
select that target in the Groups & Files list and choose Project
> Upgrade _target name_ to Native.

Xcode creates a new copy of each target, configures it to
create the appropriate product type, and adds it to the Targets
group. Your existing Jam-based targets remain unchanged. Xcode preserves
all target dependencies when upgrading targets to the native build system.

Xcode generates a log file that shows you the results of the
upgrade to native targets. The information in this log file includes
the product type created by the upgraded target, locations of common
support files—such as Info.plist files, and changes made to any
build settings.

[Next](Build%20Phases.md)[Previous](The%20Build%20System.md)

