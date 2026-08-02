---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/xc_workflow/workflow.html
archived_at: '2026-07-15T07:30:05.565975Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Projects.md)[Previous](Introduction%20to%20Xcode%202.0%20User%20Guide.md)

# Developing a Software Product With Xcode

Xcode can help you at each step in the process of developing a software product. That includes steps such as researching Apple technologies; writing and compiling code; and building, linking, testing, debugging, and optimizing the software for your product. By taking a closer look at these steps, you’ll see how Xcode fits into the development process.

This section gives a brief overview of the software development process and how Xcode helps you at each stage in that process. Figure 1-1 shows the typical development process and how it relates to Xcode.

__Figure 1-1__  Xcode and the software development process

!

Briefly, the stages of the development process are as follows:

- Define a product. The earliest stages in the creation of an application are conceptual; you decide what problem you are trying to solve and think about the best programmatic approach and the best interface design. You make fundamental decisions about the programming language you will use, the architecture of your application, and the Mac OS X technologies you will use. No matter what your decisions, chances are Xcode has a project template to support them.
- Design your program. The design process doesn’t stop with your decisions about programming language, Mac OS X technology, and product type. If your product has a graphical user interface, you can use the Interface Builder application to design the user interface for your application. Xcode knows how to work with Interface Builder nib files; a nib file contains the resources that describe the various user interface elements in our program’s interface. When you double-click a nib file in the Xcode application, the Interface Builder application opens. For more information on Interface Builder, see _Interface Builder Help_.

  If you are programming in an object-oriented language, Xcode’s design tools let you model classes in your application and entities that represent your data. The class modeling tool lets you understand the classes in your project, whether they’re written in Objective-C, C++, Java, or a mixture of those languages. The data modeling tool lets you diagram entities and the relationships between them, and define a schema for use with the Core Data framework. For more on Xcode’s design tools, see [Design Tools](Design%20Tools.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgqwugqkdjbdesq2j).
- Write source code. Once you have designed your program and user interface, you need to implement your design. Xcode’s editor has many features to facilitate your job, including code completion, direct linking to function, class, and method descriptions, support for syntax coloring, and many shortcuts for moving between files. For more on Xcode’s editor, see [Editing Source Files](Editing%20Source%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgewugrkhivdumscc).
- Choose a version control system. Version control systems let you track changes to your source files. Using version control, several developers can work on the same project at the same time. Xcode works with three version control systems: Concurrent Versions System (CVS), Subversion, and Perforce. To learn more about using version control in Xcode, see [Version Control](Version%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgiwueqkcinbuuq2k).
- Build your product. To create a program that you can run and test, you must first build the product. Building a product involves many steps, including compiling source files, linking object files, copying resource files, and more. Xcode includes a powerful build system that can build any Mac OS X software product. Xcode’s build system provides a user interface to industry-standard tools such as the GNU compiler collection. In addition, Xcode provides numerous opportunities to tailor the build process. To learn more about Xcode’s build system, see [The Build System](The%20Build%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgqwugqkdizeeuq2g).
- Debug and test your program. In most large application projects, debugging and tuning the code proceeds in parallel with implementation. Xcode includes a source-level debugger that provides a graphical user interface to the GNU debugger, GDB. GDB is a command-line debugger for C, Objective-C, C++, and Objective-C++ code. For more information on using GDB, see _[Debugging with GDB](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#//apple_ref/doc/uid/TP40000996)_ and _GDB Quick Reference_.

  The Xcode application lets you step through your code line by line, set and modify breakpoints, view variables, stack frames, and threads, and access GDB directly through a command line.

  In order to enhance your users’ perception of your application, you should minimize the application’s launch time, execution time, and memory footprint. Xcode Tools includes a number of tools, such as Shark, to help you achieve those goals. You can launch your program with many of these performance tools directly from Xcode. For more information on the performance tools included with Xcode Tools and on performance tuning in general, see _[Performance Overview](../../Performance/Performance%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjq)_.
- Deploy your product. The last step in application development is bundling the various object files, frameworks, and data files into a package that can be installed by the user. Xcode automatically packages all of the files that it knows are part of the application. Whenever possible, you should package your application for drag-and-drop installation. When necessary, however, as when you want to let the user install a new version of an application over an old one without replacing all the files, you can use the PackageMaker application to create an installation package. Installer, located in `/Applications/Utilities`, is the native installer for Mac OS X. PackageMaker and Installer are documented in _Software Distribution_.

As you work to define a software product, you typically draw from a number of sources, such as requirements specifications, existing software products, technology documentation, and your own knowledge of what you need to accomplish. In doing your analysis, you don’t want your choices to be restricted by your development environment—rather, you want to have confidence that the IDE supports the product decisions you make.

The following are some of the questions you might ask as you focus on defining a product. In most cases, you’ll find that Xcode can accommodate the requirements identified by your answers.

- What kind of product do you want to create: a new application, a plug-in for an existing application, a library to be used by several other products?

  Xcode provides project templates for creating applications, plug-ins, dynamic libraries, kernel extensions, and more. [Creating a Project](Creating%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgawueqkci5demsck) describes the project templates provided by Xcode. For a description of the various types of software you can develop on Mac OS X, see [Software Development Overview](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/SoftwareProducts/SoftwareProducts.html#//apple_ref/doc/uid/TP40001067-CH206) in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.
- Does the product have multiple parts? For example, is it an application with an embedded framework?

  An Xcode project can contain multiple targets, which each build a different product. For particularly large or complex products, you might choose separate projects—and Xcode can manage dependencies between them.
- What Mac OS X technologies are appropriate for your product?

  Xcode documentation contains both conceptual and reference material for a wide range of available technologies. For a good introduction, see _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.
- Do you need to deploy your product on multiple versions of Mac OS X?

  Xcode supports cross-development for different versions of Mac OS X, so that you can develop on one version and deploy to many, taking advantage of features in each version. For example, you can build on Mac OS X version 10.3 (Panther) and target version 10.1 or 10.2, as well as 10.3. To be able to use this feature, you must install SDKs as part of installing Xcode. For detailed information, see _[SDK Compatibility Guide](../SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_, in Tools Xcode Documentation.
- Do you need to do some rapid user-interface prototyping, or provide a complex interface for an administrative tool?

  AppleScript Studio lets you use AppleScript (or system languages such as C, Objective-C, or Java) to drive applications with complex user interfaces. For more information, see the learning path “Creating an AppleScript Studio Application” in Getting Started With AppleScript.
- Do you need to work on an existing CodeWarrior or Project Builder project?

  Xcode can import these projects. For details, see [Creating a Project](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrrhawviucykjcummjwgu).
- Do you have existing code that uses Cocoa or Carbon?

  _Cocoa_ is an object-oriented application environment designed specifically for developing native applications for Mac OS X. Cocoa applications are written in Objective-C or Java, but can also make use of C.

  _Carbon_ is a set of procedural C APIs for developing full-featured, high-performance, applications for Mac OS X.

  Xcode supports development with C, C++, Objective-C, Objective-C++, and Java, and provides project and target templates for many types of products.
- Do you need to provide a cross-platform solution or have existing code that uses Java?

  The Java application environment in Mac OS X provides a development environment, a runtime environment, and an application framework that includes AWT and Swing. For more information, see the documents in Java Documentation, as well as _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.
- Are you working as part of a team? With an existing code base?

  Xcode’s source control management (SCM) can manage your code, using CVS, Subversion, or Perforce.

  Team members can use source trees to define commonly named paths that point to different directories on different machines. For example, Xcode uses source trees when you import a CodeWarrior project. (For more on importing, see [Creating a Project](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrrhawviucykjcummjwgu).)

  Xcode scales well, from small to large projects, so you can divide the work into as many projects and targets as its scope requires. For more information on dividing up large projects, see [Dividing Your Work Into Projects and Targets](Organizing%20Xcode%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruhawviucykjcummjwge).

Of course these are not the only questions that you may need to resolve in the course of defining your product.

Once you have made your decisions about the type of product (application, library, command-line tool, and so on) and language or languages (C, C++, Objective-C, Java, and others) you plan to use, you’re ready to create a project.

Xcode provides the project as the primary workplace for your software development. When your design has reached the point where it’s time to start working on the code, you can do one of the following:

- Create a new project based on one of the templates described in [Table 3-1](Creating%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgawugsceijbukqsb).

  The new project contains a default target that is preconfigured to build a product of the type you specified when you chose the project template. Most projects also contain default source files, resource files, framework references, and other items.
- Import an existing Project Builder project by simply opening the project with Xcode.
- Import an existing CodeWarrior project.

  To import a CodeWarrior project, you must have CodeWarrior available on the same computer, and must take a specific import step. After importing, the new project is likely to require some modification before you can successfully build it. You can find detailed information on this process in _[Porting CodeWarrior Projects to Xcode](../Porting%20CodeWarrior%20Projects%20to%20Xcode/Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydq)_.
- Import an existing PBWO project (a project built with the older Project Builder for WebObjects application). Projects of this type should build with a minimum of additional steps.

Once you’ve created an Xcode project, you can add files, add targets, modify target settings, and make any required modifications to develop your software.

Before you plunge headlong into working with the project that you have just created, it’s a good idea to familiarize yourself the many ways in which you can organize and quickly access project information and items. Xcode provides many different ways for you to view, organize, and find information in your project, so you can work efficiently.

The Xcode project is the primary mechanism for grouping the files and information you need to build one or a set of related products. Within a project, a target specifies the files and other information needed to build a specific product. In addition, Xcode provides groups, as a way to organize information within a project, and to navigate to project files, symbols, and so on.

Xcode defines groups for source code, targets, errors and warnings, bookmarks and other items. You can also create your own groups to help you organize information in ways that make sense to you. To learn more about groups in Xcode, see [Groups in Xcode](The%20Project%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytembufvbecqsdijeuoqi).

[Organizing Xcode Projects](Organizing%20Xcode%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruhawueqkcizauqssj) provides a detailed look at the high-level issues involved in organizing complex projects and targets. It includes [Organizing Files](Organizing%20Xcode%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruhawueq2jivausqkk), which provides a more detailed look at working with groups.

Xcode provides convenient navigation at several levels, whether you’re editing source code in multiple files, looking up technical documentation, building, debugging, or performing other tasks.

The project window, described in [The Project Window](The%20Project%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytembufvbegskgirdemqq), offers several options for navigation:

- You can find any project file by first selecting the project group (which reveals a list of all the files in the project), then use filtered searching to find the file you’re looking for.
- You can define bookmarks to access specific file locations, then use the Bookmarks group to locate specific bookmarks.
- You can use the Project Symbols group to find a method or function and go directly to its source code.
- You can use the Errors and Warnings group to go directly to the specific line in your code where an error occurred.

To examine the hierarchy of classes defined in object-oriented languages, Xcode provides a class browser. Using the browser, you can navigate to code (both for Apple frameworks and for classes you have defined) and documentation.

Xcode also provides options for jumping between header and implementation files, jumping to methods or functions within a file, or instantly opening a selected or typed filename. And you can locate text by performing single-file or batch find operations, described in [Searching in a Project](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrrhawugscejbeuurcj).

An IDE should help you find the information you need while you’re working on a project. Here are some ways to search for information in Xcode.

Filtered searching is available in many places across the Xcode user interface. It refers to the ability to type letters in a search field so that as you type, Xcode filters an associated list, removing any items that don’t match the text you type.

For example, filtering is available in the project window for items such as files, symbols, and errors and warnings; in Info windows (described below) for build settings; and in the Developer Documentation window for symbol names defined by various Mac OS X technologies.

Searching for text in your project is a common task that must be fast and convenient. In Xcode, you can perform search and replace operations in a single file, or perform batch searches on multiple files and frameworks. You can search for text, regular expressions, or symbol definitions. You can also define complex search criteria to reuse, and you can store your search results for later reference. To learn more about searching in Xcode projects, see [Searching in a Project](Finding%20Information%20in%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgawueqkcizbuqrck).

The project window is the main starting point for getting information about items in your project. For most kinds of information, you won’t need more than a few steps:

1. Select an item in the project window.
2. If you need more information about a selected item, open an Info window (by pressing Command-I, choosing Get Info from the File menu, or clicking the Info button in the project window toolbar).

An Info window allows you to view, and in some cases modify, information on items in your project. For example, you can view and change file attributes for one or more selected files. To learn more about Info windows, see [Inspector and Info Windows](The%20Project%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytembufvbegskgi5cesry).

The importance of documentation in software development can’t be overemphasized. The technical documentation distributed with Xcode provides critical conceptual and reference documentation for creating high-quality, high-performance software for Mac OS X.

At different times in the product cycle, you’re likely to use the documentation to:

- Learn about the operating system and the technologies it supports
- Find and compare solutions for technical requirements
- Read about supported languages and frameworks
- Look up individual API definitions
- Learn how to use a required tool

When you install Xcode, technical documentation is installed on your hard drive. You can view it in the Developer Documentation window, accessed through the Help menu.

The Mac OS X documentation distributed with Xcode includes both Apple and open source documentation. Xcode also includes a variety of sample code, installed at `/Developer/Examples`. Documentation and sample code are also available, free of charge, at the Apple Developer Connection website at [http://developer.apple.com](https://developer.apple.com/). To learn more about viewing documentation in Xcode, see [Viewing Documentation](Finding%20Information%20in%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgawueqkcjjcekqkj).

Apple provides the open source HeaderDoc system for creating HTML reference documentation from embedded comments in C, C++, and Objective-C header files. Similar to JavaDoc, the system allows you to document your interfaces and export that information into HTML. For more information on HeaderDoc, see [http://developer.apple.com/darwin/projects/headerdoc/](https://developer.apple.com/darwin/projects/headerdoc/).

As you develop your software, you spend a lot of time editing files. To be efficient, you want to be able to work with familiar keystrokes and have access to features such as code completion, automatic indenting, syntax coloring, and so on. You also want to open files quickly, find API documentation, enter API declarations, move between header and implementation files, and work with as many or as few windows as you need.

Xcode handles these requirements through an advanced editor with many customizable features:

- You can, in Xcode’s Preferences window:

  - View and modify settings for syntax coloring, indenting, and source code formatting.
  - Turn on code completion, so the editor suggests context-sensitive function names, method names, and arguments as you type.
  - Customize keystroke equivalents for menu items and editing tasks to use the keystrokes you are most familiar with; Xcode provides predefined sets that are compatible with BBEdit, CodeWarrior, and even MPW (Macintosh Programmer’s Workshop, the Apple development environment for Mac OS 9).
  - Choose an external editor for any file type.
- You can edit in one or more standalone editor windows, or in an editor pane in the project window.
- You can use many Xcode shortcuts, such as Command–double-click to go from a selected function name to its definition.
- You can use features described in previous sections to quickly find a desired file, symbol, or text string.

For more information on Xcode’s editor, see [The Xcode Editor](The%20Xcode%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmzrfvbecqshinceosi). To learn more about code completion, see [Code Completion](Code%20Completion.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgywugsceijfeursg). To learn how to use an external editor with Xcode, see [Using an External Editor](Using%20an%20External%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsguwugsscjfauuqse).

In addition to source code, most projects include resources such as images, sounds, and nib resource files. Many project templates provide default resource files when you create a new project; these resource files are typically organized in the Resources source group. In addition, when you add resource files to a target, Xcode automatically adds them to the correct step of the build process, so that they will be added to your software.

Most Mac OS X software, including applications, plug-ins, and frameworks, is packaged in the form of a bundle. Xcode provides mechanisms both to help you localize resource files that need it, and, when you build your product, to copy localized resources into localized directories in your software bundle. At runtime, your source code can use various APIs provided by Mac OS X to obtain localized information from the bundle.

The following sections provide an overview of how to work with resources, support localization, and provide needed information to the Mac OS X system. To learn more about working with localized files in Xcode, see [Customizing for Different Regions](Customizing%20for%20Different%20Regions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvg4wugrsijfdeer2k).

Any Mac OS X software that is packaged in the form of a bundle requires an information property list file named `Info.plist`. This file, which is critical to configuring your software, contains key-value pairs that specify various information used at runtime, such as the version number. Information in the property list is used by Mac OS X (for example, when launching applications) and is also available to the product that contains the property list.

When you create a new project for a bundled product, Xcode automatically creates an `Info.plist` file for the project. When you build the product, Xcode copies the property list file into the product’s bundle. The information property list is associated with a target, and you can open an Info window on the target to modify property list values. You can also double-click a property list file in the project window to edit it as an XML text file.

Any text strings in your project that may be displayed to users should be localized. To do this, you place them in strings files, providing one localized variant for each language you support. A strings file, which has the extension `strings`, stores a series of keys and values, where the values are the strings and the keys uniquely identify the strings. Xcode supports localization with strings files by providing options to make a file localizable and to add files for local variants.

When you build your product, Xcode copies each localized strings file into the appropriate localized directory within the `Resources` directory of the product bundle. For example, if you localize for French, the French version of a strings file is copied to the `French.lproj` directory in the bundle. Mac OS X provides various APIs you can use in your source code to obtain localized information from a bundle, such as the correct text string to display for the user’s current locale. For more information, see _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_.

The `InfoPlist.strings` file is an example of a strings file. It is used to provide localized values for any properties in the `Info.plist` file that may be displayed to users. When you create a new project for a bundled product, Xcode automatically creates this file in the Resources group. By default, it provides just an English variant, but you can add localized strings files for other languages you support.

A nib file, which has the extension `nib`, is a resource file that stores user interface information for a product. You create nib files with Interface Builder, which provides a powerful mechanism for graphically laying out the user interface for your software. When you add a nib file to a target, Xcode adds it to the correct stage of the build process, which causes it to be copied into the product’s bundle when you build the product. Your code then has access, at runtime, to user interface items in the nib file.

In previous versions of the Mac OS, applications traditionally used Resource Manager `.r` (text) and `.rsrc` (compiled) resource files. While nib files are now the preferred mechanism for defining user interface items, Xcode has built-in support for Resource Manager resources as well.

When you add a Resource Manager resource file to a target, Xcode recognizes it by its extension. When it builds the target, Xcode automatically compiles `.r` files with the Rez tool. Xcode then copies the resulting `.rsrc` file into the `Resources` folder of the product bundle. If you localize any `.r` files, a `.rsrc` file is copied into the appropriate localized directory as well.

For related information about these types of resources, see Working With Resources in _[Porting CodeWarrior Projects to Xcode](../Porting%20CodeWarrior%20Projects%20to%20Xcode/Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydq)_.

Once a product has been designed, you spend time in the edit/build/debug cycle: adding or modifying code, building the product, testing it, and repeating these steps, as you find and correct bugs or add additional features. You’ve seen Xcode’s editing features in [Editing Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrrhawugscei5beqqkf). The following sections describe tools, features, and performance enhancements Xcode provides so that you can take control of the coding cycle.

The Xcode Tools include the Xcode application, Interface Builder, and a set of integrated compilers, debuggers, and build tools. Along with many tools created by Apple, Xcode incorporates several tools from the UNIX open source community. Together, these tools build on years of software development experience and take advantage of the UNIX-compatible underpinnings of Mac OS X.

Among the open source tools available in the Xcode IDE are the GCC compiler (which supports development in C, C++, Objective-C and Objective-C++), the GDB source code debugger, and the `javac` and Jikes Java compilers. Apple contributes to improvements in many of these open source tools. Standard UNIX tools are available in subdirectories of `/usr`.

Tools that originate with Apple include:

- `ld`, a linker that supports dynamic shared libraries.

  To work efficiently with dynamic shared libraries at runtime, the Mac OS X runtime architecture provides the `dyld` (dynamic loader) library manager.
- `xcodebuild`, a command-line tool for building Xcode projects.
- Terminal, an application for doing command-line work in shell windows.

In addition, Xcode includes tools to help you locate hard-to-find bugs, such as memory leaks and bugs in threaded code, as well as tools to help you analyze and optimize the performance of your software.

For more information, see the documents in Tools Xcode Documentation and Performance Documentation.

The Xcode build system provides flexibility and customizability to your workflow. You can control the build process from the toolbar or with keyboard shortcuts, can view errors in the project window or in a separate Build Results window, and can go quickly from errors to the offending line of source code. In the Build Results window, you can control the level of detail—for example, you can choose whether to show warning messages and whether to display build steps.

What takes place at build time depends on several factors. When you create a new project in Xcode, it contains a great deal of build information, including default build settings, build rules that specify tools for processing source files, build styles for development and deployment builds, and build phases for performing the steps of the actual build. To learn more about the information that goes into building a product, see [The Build System](The%20Build%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgqwugqkdizeeuq2g).

For a simple project, default values are sufficient for Xcode to build your product, performing such steps as compiling, linking, and copying files to the appropriate locations in an application bundle. For projects with special requirements, Xcode provides numerous options for controlling the process. For example, you can set per-file compiler flags or add a step to the build process that executes a shell script to perform special processing.

The open source GNU Debugger, GDB, sits behind Xcode’s debugger user interface. It also makes available powerful command-line debugging features. As a result, you can debug at whatever level is most comfortable for you. You can work in the user interface for most of your debugging tasks, but drop down to the command line to take advantage of advanced features that are less commonly needed. For debugging Java products, Xcode communicates directly with the Java Virtual Machine. To learn more about Xcode’s debugger, see [Running in Xcode’s Debugger](Running%20in%20Xcode%E2%80%99s%20Debugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrthewueqkcircugr2j).

Beside the standard features you expect in an IDE, Xcode sports a number of innovative features that can speed up your edit/build/debug cycle and make a big contribution to an efficient workflow:

- Code completion allows the editor to suggest context-sensitive function names, method names, and arguments as you type.
- Predictive compilation reduces the time required to compile single file changes by beginning to compile a file while you are still editing it.
- Distributed builds can dramatically reduce build time for large projects by distributing compiles to available computers on the network. And if you have a dual-CPU machine, Xcode automatically takes advantage of the second CPU for compiling and other operations.
- Fix and Continue improves your debugging efficiency by allowing you to change the source in a file, recompile just that file, and run the changed code without stopping the current debugging session.
- ZeroLink shortens link time for development builds and lets you quickly relaunch your application after making changes. (Don’t forget to turn ZeroLink off for deployment builds!)

To learn more about these features, see [Optimizing the Edit-Build-Debug Cycle](Optimizing%20the%20Edit-Build-Debug%20Cycle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtgqwugqsiijcusssk), [Using ZeroLink](Linking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtgmwugsceincuqrce), and [Using Fix and Continue](Using%20Fix%20and%20Continue.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrugqwugqkdjfduuskj).

Performance optimization should be an integral part of the development cycle, and should include steps such as providing a plan to continually measure and improve the performance of your code. Xcode Tools provide a number of tools to help you fine-tune your software, including tools to:

- Examine memory use and find leaks
- Analyze where your software spends its time, in both application code and system code
- Determine what an unresponsive application is doing
- Graphically track the activity of an application’s threads

You can launch your program in many of these tools directly from the Xcode application. For more information on analyzing and optimizing your software in Mac OS X, see the learning paths in [Getting Started With Performance](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Performance/index.html#//apple_ref/doc/uid/TP30001082).

You can work most efficiently when your development environment complements the way you like to work. Xcode provides many options for customizing its interface, from setting the keystrokes for menu and text-editing equivalents, to configuring the contents and layout of the project window, to setting conventions for editing code.

The Xcode Preferences window is the key to customization, and you should spend some time investigating it. It provides access to settings for features such as text editing, syntax coloring, indentation, navigation, building, debugging, source code management, and key bindings for menus and text editing. To learn more about Xcode’s Preferences, see [Xcode Preferences](Xcode%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgewugskijbcucrkk).

You can customize Xcode’s project window and many other windows too. For example, Xcode provides a number of different project window configurations, or layouts, for you to choose from. You can embed an editor and specify which columns and groups should be shown in the project window. You can also customize toolbars and menus, and control the amount of information shown in the Build Results window.

Mac OS X incorporates the FreeBSD variant of UNIX, which includes a command-shell environment. The Terminal application provides an interface for invoking command-line utilities and executing shell scripts. You can build Xcode projects from a shell with the `xcodebuild` command, in order to, for example, run nightly builds. For more information, see [Building From the Command Line](Building%20a%20Product.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmztfvbecssejbcukry).

Xcode also makes it easy to execute shell scripts as part of your development work. You can execute selected text as a shell script or run scripts from the User Scripts script menu. That menu contains default scripts that you can execute as is, or use as examples for scripts you write. You can also write shell scripts that Xcode executes during the build process.

For more information on modifying your work environment and working with shell scripts in Xcode, see [Customizing Xcode](Customizing%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvhewueqkcjbceor2i).

[Next](Projects.md)[Previous](Introduction%20to%20Xcode%202.0%20User%20Guide.md)

