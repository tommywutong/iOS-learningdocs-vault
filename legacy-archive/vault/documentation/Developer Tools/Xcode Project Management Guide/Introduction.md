---
title: Xcode Project Management Guide
apple_id: TP40006917
resource_type: Guide
platform: iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeProjectManagement/000-Introduction/introduction.html
archived_at: '2026-07-15T07:28:06.426436Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Part%20I-%20Project%20Organization.md)

# Introduction

An Xcode project is a repository for all the information required to build one or more software products. It contains all the elements used to build your products and maintains the relationships between those elements. You can think of it as a kit that contains all the parts to build one or more products, plus the instructions on how to build them. A project gives you a convenient place to find every file and piece of information associated with your work.

This document introduces the various parts of a project, shows you how to create projects, and describes how to organize the contents of a project. This document also describes the project window, Xcode’s interface for performing project management tasks, and shows how to use that interface to find and discover information in Xcode.

You should read this document if you plan on developing software products for iOS OS or Mac OS X. To get the best out of this document, you should be familiar with basic software development concepts, such as object-oriented programming, compilation, and debugging. You should also be familiar with Objective-C, the main programming language used in Apple platforms.

This document contains the following chapters, which are divided in two parts:

[Part I: Project Organization](Part%20I-%20Project%20Organization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjxfvbuqnjnknltc) describes how Xcode projects are organized and how to find information in them.

- [Overview of an Xcode Project](Overview%20of%20an%20Xcode%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnrtfvjvomjr) describes the contents of an Xcode project and gives an overview of the information required to develop software with Xcode.
- [Creating Projects](Creating%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnrufvbecqshizdeqsq) shows you how to create a project or import CodeWarrior projects and describes the available project templates.
- [Files in Projects](Files%20in%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnrwfvbecqsgifeeusi) discusses the files in a project, describes how Xcode references project files, shows you how to add files, frameworks, and folders to your project, and describes how to use source trees and cross-project references.
- [Searching Files and Projects](Searching%20Files%20and%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnrzfvbecqskinbekry) describes how to use Xcode to find information about your project’s contents.
- [Viewing Project Symbols and Classes](Viewing%20Project%20Symbols%20and%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjxfvbuqmznknltc) shows how to find information about the classes defined in a project and its included frameworks.
- [Localizing Files](Localizing%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmobtfvbumscjizbeosq) describes the process of internationalizing your product by localizing some of its files.
- [Using the Organizer](Using%20the%20Organizer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjxfvbuqmrxhewvgvzt) describes the Organizer and shows how you can use it to organize and work on multiple projects on one window, including non–Xcode projects.

[Part II: Product Development](Part%20II-%20Product%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjxfvbuqnrnknltc) describes how to perform the major development tasks, including static analysis to find bugs in your code early and building your product.

- [Building Products](Building%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojtfvjvomjt) shows how to build products in Xcode and how to take advantage of multiple CPUs during a build. It also describes how to target releases of a platform different from the one for which you’re developing your product.
- [Analyzing Code](Analyzing%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjxfvbuqnbnknlte) describes how to use the static analyzer to identify and fix code flaws.
- [Defining Executable Environments](Defining%20Executable%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojyfvbecqscifduisa) describes how to view the executables in your project and how to configure an executable environment.
- [Running Programs](Running%20Programs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjxfvbuqmrygawvgvzs) shows how to run your programs after you’ve built them in Xcode.

These documents provide overview or additional information about developing software products for Apple platforms:

- _[A Tour of Xcode](../A%20Tour%20of%20Xcode/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojq)_ provides a hands-on introduction to the development of software products for Mac OS X.
- _[The Objective-C Programming Language](../../Cocoa/The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ describes the Objective-C programming language and runtime environment.
[Next](Part%20I-%20Project%20Organization.md)

