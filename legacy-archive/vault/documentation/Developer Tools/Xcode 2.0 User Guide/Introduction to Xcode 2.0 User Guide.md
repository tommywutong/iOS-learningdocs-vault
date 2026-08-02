---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/intro/intro.html
archived_at: '2026-07-15T07:29:48.022342Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Developing%20a%20Software%20Product%20With%20Xcode.md)

# Introduction to Xcode 2.0 User Guide

Software development can be thought of as a
complex problem space in which you manage files to produce products.
The types of files can include source files, resource files, and
supporting files (documentation, timelines, notes, or any other
files that help you build the software but aren’t part of the
product). You use various tools to process the files into a variety
of outputs. To automate the process and keep track of all the details
and interactions, you use an IDE.

The Xcode IDE is designed to help you work in this type of
problem space. It allows you to perform most tasks quite simply,
using its basic user interface. Many features should be familiar
to most developers. Xcode is Apple's tool suite and integrated development environment
(IDE) for creating Mac OS X software. The Xcode application includes
a full-featured code editor, a debugger, compilers, and a linker.
The Xcode application provides a user interface to many industry-standard
and open-source tools, including GCC, javac, jikes, and GDB. It
provides all of the facilities you need to build a program for Mac
OS X, whether it’s an application, kernel extension, or command-line
tool.

This document describes the Xcode application and how you
can use it to develop software for Mac OS X. It provides a comprehensive
guide to Xcode’s features and user interface. This document is
intended for developers using Xcode to build software for Mac OS
X. This document is written for Xcode 2.0.

This document contains several parts, each of which contains
chapters devoted to a major functional area of the Xcode application.
These parts are:

- [Developing a Software Product With Xcode](Developing%20a%20Software%20Product%20With%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrrhawueqkcjfceeqsi) describes
  the development process and how Xcode helps you with each step along
  the way.
- [Projects](Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrug4wueqkcizeuoscd) introduces the Xcode
  project and its primary components, and covers important project
  management concepts. The chapters in this part show you how to create
  an Xcode project, add and manage project files, organize project
  items, and modify project attributes. They describe the project
  window and other important Xcode user interface conventions; as
  well as mechanisms for finding information in your Xcode project,
  including documentation lookup, project-wide searches, and the class
  browser.
- [Design Tools](Design%20Tools.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgqwugqkdjbdesq2j) describes the class modeling and data modeling
  design tools included in Xcode. The chapters in this part describe
  common user interface features of these two tools, demonstrate how
  to model classes in your application, and describe how to create
  a schema for use with the Core Data framework.
- [Editing Source Files](Editing%20Source%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgewugrkhivdumscc) describes Xcode’s source code editor.
  The chapters in this part describe the user interface for Xcode’s
  built-in editor, and show you how to use features such as code completion,
  text macros, and the navigation bar to quickly author source code
  and navigate source code files. They also discuss how to use an
  external application to edit project files.
- [Version Control](Version%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgiwueqkcinbuuq2k) discusses
  the version control systems supported by the Xcode application.
  The chapters in this part show you how to configure a version control system
  in Xcode and how to perform common version control tasks, such as
  updating files, committing changes, and comparing file revisions.
- [The Build System](The%20Build%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgqwugqkdizeeuq2g) describes
  Xcode’s build system and how to use Xcode to build a product.
  The chapters in this section describe targets, build styles, and
  the other information that Xcode uses to build a product. They also
  show you how you can customize the build process by adding custom
  tasks to the build process or change the way a product is built
  by modifying build settings. This part also includes information on
  features that you can use to reduce the amount of time it takes
  to build, such as distributed builds, precompiled prefix headers,
  and predictive compilation.
- [Debugging](Debugging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvhawueqkcirbusq2g) describes
  Xcode’s graphical debugger and shows you how to run and debug
  your program in Xcode. The chapters in this part demonstrate how
  to use features such as Fix and Continue, which lets you make changes
  to your program while it is running and continue your debugging
  session, and remote debugging, which allows you to debug an application
  running on a remote host.
- [Customizing Xcode](Customizing%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvhewueqkcjbceor2i) describes
  how you can customize your work environment using scripts, preferences,
  and custom key bindings sets.

For an introduction to the developer tools available for Mac
OS X, see [Getting Started With Tools](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Tools/index.html#//apple_ref/doc/uid/TP30001102).

For an introduction to Mac OS X system architecture and system
technologies, see _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

To see a full list of the tools available with Xcode Tools,
see Mac OS X Developer Tools in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

To learn more about the types of software you can create for
Mac OS X, see [Software Development Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx) in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

To learn more about the Mac OS X standard user interface,
see _Apple Human Interface Guidelines_.

For a tutorial introduction to Xcode, see _[A Tour of Xcode](../A%20Tour%20of%20Xcode/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojq)_.

For tips on converting Code Warrior projects and other existing
code to build in Xcode, see _[Porting CodeWarrior Projects to Xcode](../Porting%20CodeWarrior%20Projects%20to%20Xcode/Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydq)_.

To learn more about the GNU compiler collection, see _GNU C/C++/Objective-C Compiler_.

For more information on debugging with GDB, see _[Debugging with GDB](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#//apple_ref/doc/uid/TP40000996)_.

For information on using cross-development to develop for
multiple versions of Mac OS X, see _[SDK Compatibility Guide](../SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_.

In addition, many other documents are referred to or recommended
throughout this document.

[Next](Developing%20a%20Software%20Product%20With%20Xcode.md)

