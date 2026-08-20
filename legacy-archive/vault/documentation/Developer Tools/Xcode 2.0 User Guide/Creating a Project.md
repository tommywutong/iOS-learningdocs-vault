---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/pr_creating/pr_creating.html
archived_at: '2026-07-15T07:29:50.019028Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](The%20Project%20Window.md)[Previous](Projects%20in%20Xcode.md)

# Creating a Project

Once you know what product you are working
on, you need an Xcode project. If you are working on a new product,
and do not already have an Xcode project, you can create one from
scratch. Xcode provides project templates to help you create a wide
variety of products.

If you are working on an existing product, you probably already
have a project. If you have an existing Xcode project, you can simply
open the project in Xcode, as described in [Opening and Closing Projects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgawviucykjcummjqgy).
If you have an existing CodeWarrior project, you can import your
project into a new Xcode project. Or, if you have an existing Project
Builder project, you can simply open it in Xcode.

This chapter shows you how to create a new project and describes
the available project templates. It also shows you how to import
CodeWarrior, Project Builder, and ProjectBuilderWO projects.

Fairly early in your design process, you make decisions related
to the type of product (application, library, command-line tool,
and so on) and language or languages (C, C++, Objective-C, Java,
and others) you plan to use. For a Mac OS X product, you also decide which
Apple technologies to use, and whether to use an application framework,
such as Cocoa or Java.

Once you’ve resolved these issues, you’ll find that Xcode
provides a wide variety of project templates to support your goals. Table 3-1 provides
brief descriptions for the project templates currently supplied
by Xcode. You can find similar descriptions when you select a project
template in the New Project Assistant in Xcode. When you add a target
to a project, you’ll get a selection of targets to choose from
that is similar to the list of available project templates. For
more information on targets and target templates, see [Creating Targets](Targets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugskiinceurcc).

The project template you choose specifies a default target
and it also determines the default source files, resources, framework
references, and other information that Xcode includes automatically
in the project. A project generally contains all the information
it needs to build a product for its default target. This includes
a minimal set of source files that you can compile into a running
product, as well as default build settings.

__Table 3-1__  Xcode project templates

| Project template | Use to create |
| Empty Project | A project with no files or targets. |
| _Action_ | _Action_ |
|
| Automator actions are loadable bundles that perform discrete tasks for users to link together in a workflow, using the Automator application. For more information, see _[Automator Programming Guide](../../Apple%20Applications/Automator%20Programming%20Guide/Introduction%20to%20Automator%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinjq)_. | Automator actions are loadable bundles that perform discrete tasks for users to link together in a workflow, using the Automator application. For more information, see _[Automator Programming Guide](../../Apple%20Applications/Automator%20Programming%20Guide/Introduction%20to%20Automator%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinjq)_. |
| AppleScript Automator Action | An Automator action written using AppleScript. |
| Cocoa Automator Action | An Automator action written in Objective-C. |
| _Application_ | _Application_ |
| AppleScript Application | An AppleScript Studio application: a simple Cocoa application which can be written in AppleScript, Objective-C, and other languages. |
| AppleScript Document-based Application | An AppleScript Studio application that uses the Cocoa document architecture. |
| AppleScript Droplet | An AppleScript Studio application that processes files dropped on it. |
| Carbon Application | An application, based on the Carbon framework, that uses nib files for resources (a _nib file_ typically defines and lays out objects for a product’s graphical interface). |
| Cocoa Application | An application, based on the Cocoa framework, that is written in Objective-C and relies on nib files to define its graphical interface. |
| Cocoa Document-based Application | A Cocoa application that uses the Cocoa document architecture. |
| Cocoa-Java Application | A Cocoa application that is written in Java. |
| Cocoa-Java Document-based Application | A Cocoa application that is written in Java and uses the Cocoa document architecture. |
| Core Data Application | An application, based on the Cocoa framework, that is written in Objective-C and uses the Core Data framework to save and restore objects. For more information on the Core Data framework, see _Data Modeling Guide_ and _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_. |
| Core Data Document-based Application | A Core Data application that uses the Cocoa document architecture. |
| _Bundle_ | _Bundle_ |
|
| A bundle is a file system directory that stores executable code and the software resources related to that code. Bundle templates are for loadable bundles—code (such as application plug-ins) that can be loaded when it is needed. For more information, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_. | A bundle is a file system directory that stores executable code and the software resources related to that code. Bundle templates are for loadable bundles—code (such as application plug-ins) that can be loaded when it is needed. For more information, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_. |
| Carbon Bundle | A bundle that links against the Carbon framework. |
| CFPlugin Bundle | A bundle that links against the Core Foundation framework. |
| Cocoa Bundle | A bundle that links against the Cocoa framework. |
| _Command Line Utility_ | _Command Line Utility_ |
| A command-line tool is a utility without a graphical user interface. Command-line utilities are typically used in the command-line environment. | A command-line tool is a utility without a graphical user interface. Command-line utilities are typically used in the command-line environment. |
| C++ Tool | A tool that links against the stdc++ library. |
| CoreFoundation Tool | A tool that links against the Core Foundation library. |
| CoreServices Tool | A tool that links against the Core Services library. |
| Foundation Tool | A tool that links against the Foundation framework. (Foundation is one of the frameworks in the Cocoa framework.) |
| Standard Tool | A tool written in C. |
| _Dynamic Library_ | _Dynamic Library_ |
| A dynamic library is a library for which binding of undefined symbols is delayed until execution; code in dynamic shared libraries can be shared by multiple, concurrently running programs. | A dynamic library is a library for which binding of undefined symbols is delayed until execution; code in dynamic shared libraries can be shared by multiple, concurrently running programs. |
| BSD Dynamic Library | A dynamic library, written in C, that makes use of BSD (a part of the Mac OS X kernel environment; BSD stands for Berkeley Software Distribution) |
| Carbon Dynamic Library | A dynamic library that links against the Carbon framework. |
| Cocoa Dynamic Library | A dynamic library that links against the Cocoa framework. |
| External Build System | A project that contains no files but has a single target which you can configure to use any command-line build tool. |
| _Framework_ | _Framework_ |
| In Mac OS X, a _framework_ is a hierarchical directory that encapsulates a dynamic library and shared resources in a single package. You access many Mac OS X technologies in Xcode through frameworks. For more information, see _[Framework Programming Guide](../../Mac%20OSX/Framework%20Programming%20Guide/Introduction%20to%20Framework%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dg2i)_. Note that Cocoa is an _application_ framework—one which supplies the basic building blocks of an application, to which you add your own code and features—that is implemented as a framework (as defined above). | In Mac OS X, a _framework_ is a hierarchical directory that encapsulates a dynamic library and shared resources in a single package. You access many Mac OS X technologies in Xcode through frameworks. For more information, see _[Framework Programming Guide](../../Mac%20OSX/Framework%20Programming%20Guide/Introduction%20to%20Framework%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dg2i)_. Note that Cocoa is an _application_ framework—one which supplies the basic building blocks of an application, to which you add your own code and features—that is implemented as a framework (as defined above). |
| Carbon Framework | A framework that links against the Carbon framework. |
| Cocoa Framework | A framework that links against the Cocoa framework. |
| _Java_ | _Java_ |
| Ant-based Application Jar | An application, written in Java and built as a JAR file ( JAR is the Java Archive file format). The application is built using the Ant build tool. The project contains a default `build.xml` file. |
| Ant-based Empty Project | An empty project with no files, that contains a single external target configured to use the Ant build tool. You must supply the `build.xml` file. |
| Ant-based Java Library | A library, written in Java and packaged as a JAR file, that is built using the Ant build tool. The project contains a default `build.xml` file. |
| Java AWT Applet | An AWT-based Java applet, built as a JAR file (AWT is the Advanced Windowing Toolkit). |
| Java AWT Application | An AWT-based application, built as an application bundle. |
| Java JNI Application | A JAR file-based JNI Application (JNI is the Java Native Interface). |
| Java Swing Applet | A Swing-based Java applet, built as a JAR file. |
| Java Swing Application | A Swing-based application, built as an application bundle. |
| Java Tool | A library or application, built as a JAR file. |
| _Kernel Extension_ | _Kernel Extension_ |
| A _kernel extension_ (or KEXT) is a piece of code that can be dynamically loaded into the Mac OS X kernel. A driver is a kernel extension that supports one or more devices. | A _kernel extension_ (or KEXT) is a piece of code that can be dynamically loaded into the Mac OS X kernel. A driver is a kernel extension that supports one or more devices. |
| Generic Kernel Extension | A kernel extension. |
| IOKit Driver | A device driver that uses the I/O Kit (an object-oriented framework for developing device drivers for Mac OS X). |
| _Standard Apple Plug-ins_ | _Standard Apple Plug-ins_ |
| Plug-ins for standard Apple applications, including Interface Builder, preference panes, the Screen Effects pane in System Preferences, and Sherlock. | Plug-ins for standard Apple applications, including Interface Builder, preference panes, the Screen Effects pane in System Preferences, and Sherlock. |
| Address Book Action Plug-in for C | A C-based plug-in that implements an Address Book action. See _[Address Book Programming Guide for Mac](../../User%20Experience/Address%20Book%20Programming%20Guide%20for%20Mac/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyto2i)_ for more information. |
| Address Book Action Plug-in for Objective-C | An Objective-C-based plug-in that implements an Address Book action. |
| AppleScript Xcode Plug-in | An AppleScript-based plug-in for Xcode. |
| IBPalette | A plug-in for Interface Builder that adds a palette of user-interface items. |
| Image Unit Plug-in for Objective-C | An Objective-C-based plug-in that implements one or more image filters for Core Image. For more information on creating image units, see _[Core Image Programming Guide](../../Graphics%20Imaging/Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_. |
| Installer Plug-in | An Objective-C-based plug-in that implements a custom interface for the Installer. |
| Metadata Importer | A metadata importer that allows Mac OS X to extract metadata from custom document formats for use with Spotlight. See _[Spotlight Importer Programming Guide](../../Carbon/Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_. |
| PreferencePane | A plug-in for a preference pane bundle that can be used with the System Preferences application or an application’s user preferences. |
| Screen Saver | A plug-in for a screen saver bundle that can be used with the Screen Effects panel in the System Preferences application. |
| Sherlock Channel | A plug-in for a Sherlock Channel that can be used with the Sherlock Internet search application. See _[Sherlock Channels](../../Apple%20Applications/Sherlock%20Channels/Introduction%20to%20Sherlock%20Channels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdc2i)_. |
| Sync Schema | A `.syncschema` bundle that allows your application to sync user data with other applications and devices on the same computer using Sync Services. See _[Sync Services Programming Guide](../../Cocoa/Sync%20Services%20Programming%20Guide/Introduction%20to%20Sync%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnzy)_. |
| _Static Library_ | _Static Library_ |
| A library for which all referenced symbols are bound at link time. | A library for which all referenced symbols are bound at link time. |
| BSD Static Library | A static library, written in C, that makes use of BSD (see BSD Dynamic Library above) |
| Carbon Static Library | A static library that links against the Carbon framework. |
| Cocoa Static Library | A static library that links against the Cocoa framework. |

The project template names and descriptions should give you
a good idea of which project template is right for your product.
One way to learn more about a project template is to create a project
with that template, examine its contents, and see what happens when
you build it. Project templates may change, and new templates are
added from time to time with releases of Xcode, but by trying out
a template, you can easily examine its default contents in that
version of Xcode.

To create a new project, choose File > New Project. Xcode displays
the New Project Assistant, shown here.

__Figure 3-1__  The
New Project Assistant

!

The first screen of the assistant shows the available project
templates; these are described in [Choosing a Project Template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgawugsceirdueqke). You
can choose a project template from this list, or you can select
Empty Project to create a new project with nothing in it.

When you select a template from this list, a brief description
appears in the text field directly below the template list. If there
is no text field visible, grab the resize control below the template
list and drag it upward.

After you select a project template, click Next; Xcode displays
the second screen of the assistant. In this screen, assign a name
to the new project and select a location for the project folder. If
you type in a path containing directories that do not exist on disk,
Xcode will create those directories for you before creating the
new project. By default, the Project Directory path is set to '~/'
which specifies that the project directory be placed at the top-level
of your home directory. When you click Finish, Xcode creates a new
project from the specified template.

If you already have existing code in another IDE, you can
import your project contents into Xcode. Xcode provides an assistant
for importing CodeWarrior and ProjectBuilderWO projects. Xcode also
opens Project Builder projects. This section describes how to use Xcode’s
project importer and open Project Builder projects in Xcode.

If you have existing code in a CodeWarrior project, you can
use the Xcode importer to import your CodeWarrior project and create
a corresponding Xcode project. This section gives a brief description
of how to import a CodeWarrior project into Xcode and lists a few steps
that you can take to make the conversion process easier. While this
section assumes that you are converting a project that builds an
application, many of the steps apply to other types of software
as well.

To make it easier to get your project building in Xcode, you
may need to make some changes to your project before you import
it. Each of these steps is described in further detail in _Moving
Projects from CodeWarrior to Xcode_.

1. Convert your
   code to use Carbon.
2. Set the Project Type setting of your CodeWarrior project to
   Application Package to build your application as a package.
3. Build the application in the Mach-O format. Mach-O is the
   native executable format in Mac OS X and is the only format supported
   by Xcode.
4. Remove unnecessary targets from the project.

To import your project:

- Choose File
  > Import Project, which opens the Import Project Assistant.
- Select Import CodeWarrior Project and click the Next button.
- Click the Choose button and navigate to the CodeWarrior project
  file to import (or type in the path and filename).

  You can
  specify a name for the new project in the New Project Name field.
  Otherwise, Xcode automatically uses the same name as that of the
  project that you are importing. The Xcode importer creates the new
  project in the same folder as the CodeWarrior project file.
- When you import a CodeWarrior project, Xcode determines the
  location of the CodeWarrior root folder (referred to as `{Compiler}` in
  CodeWarrior’s search path) and adds it to the Source Trees list
  in the Preferences window.

  Select Import “Global Source Trees”
  from CodeWarrior if you want the importer to add any global source
  trees from CodeWarrior’s preferences to the Source Trees list
  in Xcode.
- Select 'Import referenced projects' to import any additional
  CodeWarrior projects referenced by the project you are currently
  importing.
- Click the Finish button to dismiss the assistant and start
  the import.

  When the import is complete, the new project window
  opens.

Most projects will not build immediately; see _Moving
Projects from CodeWarrior to Xcode_ for more information
on how to get your new Xcode project to build.

If you already have an existing Project Builder project, there
is very little you have to do to get it converted to, and building
in, Xcode. Xcode works seamlessly with Project Builder projects.
You can simply open the project in Xcode, by double-clicking on
the project (`.pbproj`) bundle, dragging
the project bundle to the Xcode application, or using the Open command
in Xcode and selecting the project bundle.

Note that if you also have Project Builder installed on your
computer, double-clicking the `.pbproj` bundle
will open the project in Project Builder. To open the project in
Xcode, you will have to use one of the other methods mentioned here.

Once you have opened your Project Builder project in Xcode,
it should build with little or no additional work on your part.
If you wish to take advantage of some of Xcode’s more significant
features, such as ZeroLink, Fix and Continue, and the like, you
will have to convert the targets in your project to use the native
build system. Xcode does not automatically upgrade the existing
targets, which use Project Builder’s Jam-based build system, when
you open the project. To learn more about converting native targets,
see [Converting a Project Builder Target](Targets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugq2fivcekqsj).

Xcode also supports importing projects from ProjectBuilderWO.
To import a ProjectBuilderWO project, do the following:

1. Choose File
   > Import Project.
2. From the Import Project Assistant, choose Import ProjectBuilderWO
   Project and click Next.
3. Type the path to the ProjectBuilderWO project in the ProjectBuilderWO
   Project field or click Choose to select the project from an Open
   dialog.
4. Type the name you want to use for the new Xcode project in
   the New Project Name field and click Finish. If you do not specify
   a different name, Xcode uses the name of the existing project.

Xcode imports the ProjectBuilderWO project and creates a new
Xcode project file. Where possible, Xcode imports the targets in
the ProjectBuilderWO project as native targets. If the ProjectBuilderWO
project contains targets not supported by Xcode’s native build
system, the importer imports those targets as Jam-based targets.

To open any project, choose File > Open. To open a project
you’ve recently used, select the project from the File > Recent
Projects menu. To close a project, you can choose File > Close Project,
or close the project window.

You can have Xcode automatically remember the state of a project’s
windows and restore them when you next open the project. To do so,
choose Xcode > Preferences, click General, and select “Save
window state” in the Environment options. If this option is disabled, opening
a project displays only the project window. If this option is enabled,
opening the project restores the project window and any other open
windows to the state they were in when you last closed the project.

[Next](The%20Project%20Window.md)[Previous](Projects%20in%20Xcode.md)

