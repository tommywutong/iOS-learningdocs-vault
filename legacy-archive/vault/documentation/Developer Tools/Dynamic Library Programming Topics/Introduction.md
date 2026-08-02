---
title: Dynamic Library Programming Topics
apple_id: TP40001869
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html
archived_at: '2026-07-15T07:24:25.774382Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Dynamic%20Libraries.md)

# Introduction

Apps are rarely implemented as a single module of code because operating systems implement much of the functionality apps need in libraries. To develop apps, programmers link their custom code against these libraries to get basic functionality, such as the ability to write to standard output or draw complex images using a graphics card. However, linking to libraries creates large executable files and wastes memory. One way to reduce the file size and memory footprint of apps is to reduce the amount of code that is loaded at app launch. Dynamic libraries address this need; they can be loaded either at app launch time or at runtime. Dynamic libraries provide a way for apps to load code when it’s actually needed.

To load dynamic libraries at runtime, apps should use a set of efficient and portable functions, called dynamic loader compatibility functions. Using these functions ensures that dynamic libraries are loaded in the most efficient way and facilitates the porting of apps from one platform to another.

This document is intended for developers of dynamic libraries and developers who use dynamic libraries in their apps. You should be familiar with the Mac OS, UNIX, Solaris, or Linux operating systems. You should also be an experienced C, C++, or Objective-C programmer.

This document explains how dynamic libraries are loaded at app launch time and how to use the DLC functions, `dlopen`, `dlsym`, `dladdr`, `dlclose`, and `dlerror`, to load dynamic libraries at runtime. This document also provides guidelines for developing dynamic libraries to be used by client apps.

This document doesn’t address the needs of Carbon or Cocoa programmers who need to load code packaged in a framework or a bundle at runtime or those who want to learn how to package dynamic libraries into frameworks or bundles. The documents _[Framework Programming Guide](../../Mac%20OSX/Framework%20Programming%20Guide/Introduction%20to%20Framework%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dg2i)_, and _[Code Loading Programming Topics](../../Cocoa/Code%20Loading%20Programming%20Topics/Introduction%20to%20Dynamically%20Loading%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2te2i)_ provide information tailored specifically to Carbon and Cocoa developers.

After reading this document, you will understand how dynamic libraries should be implemented so they can be used effectively by client apps. You will also know how to use the cross-platform DLC functions to load dynamic libraries at runtime.

This document is comprised by the following articles:

- [Overview of Dynamic Libraries](Overview%20of%20Dynamic%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnztfvjvomi) explains what dynamic libraries are and how they are used by apps. It also provides an overview of the OS X dynamic loader and its cross-platform programming interface.
- [Dynamic Library Design Guidelines](Dynamic%20Library%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomjz) explains how to name and export public symbols so that they are easy to use by clients and how to implement static initializers and finalizers. This article also provides tips on how to manage compatibility and dependency issues. Finally, this article lists issues to consider when implementing a dynamic library using C++ or Objective-C.
- [Dynamic Library Usage Guidelines](Dynamic%20Library%20Usage%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmryfvjvomjq) shows how to correctly load and use dynamic libraries in apps or in other dynamic libraries. It also provides specific details for using C++–based libraries and Objective-C–based libraries.
- [Creating Dynamic Libraries](Creating%20Dynamic%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomi) demonstrates how to develop dynamic libraries so that they are easy to use by developers who want to take advantage of them in their products.
- [Using Dynamic Libraries](Using%20Dynamic%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvomjq) describes the process of installing and using dynamic libraries. It also shows how to interpose the functions exported by a dynamic library.
- [Logging Dynamic Loader Events](Logging%20Dynamic%20Loader%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanzxfvjvomi) explains how to turn on dynamic loader logging and identifies the events that can be logged.
- [Run-Path Dependent Libraries](Run-Path%20Dependent%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbwfvjvomi) describes how to create run-path dependent libraries and how to use them in executables.

To complement the information provided in this document, consult the following documents:

- _[Code Size Performance Guidelines](../../Performance/Code%20Size%20Performance%20Guidelines/Introduction%20to%20Code%20Size%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2ds2i)_ focuses on techniques you can use to reduce the size of your code and use memory efficiently by grouping code into modules according to functionality.
- “[Executing Mach-O Files](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MachOTopics/1-Articles/executing_files.html#//apple_ref/doc/uid/TP40001829)” in _[Mach-O Programming Topics](../Mach-O%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjz)_ describes the app-launch process. In particular this article explains how the dynamic loader binds imported symbols and explains the advantages of using a two-level namespace instead of a flat namespace. This article also explains the different storage classes and symbol attributes you can use to control the visibility of a dynamic library’s exported symbols.
- “[Loading Code at Runtime](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MachOTopics/1-Articles/loading_code.html#//apple_ref/doc/uid/TP40001830)” in _[Mach-O Programming Topics](../Mach-O%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjz)_ explains how to package a dynamic library as a framework, which provides features such as resource management and a streamlined versioning model.

You can find further information on dynamic libraries in the following documents:

- _[Framework Programming Guide](../../Mac%20OSX/Framework%20Programming%20Guide/Introduction%20to%20Framework%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dg2i)_ explains how to package dynamic libraries into frameworks.
- _[Porting UNIX/Linux Applications to OS X](../../Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt)_ explains how to use dynamic libraries (plug-ins) to reduce the amount of platform-specific code in an app.
- _How to Write Shared Libraries_ ([http://people.redhat.com/drepper/dsohowto.pdf](http://people.redhat.com/drepper/dsohowto.pdf)) describes in great detail Linux’s shared objects (dynamic libraries) and provides guidelines on the design and implementation of a library’s API and ABI, including compatibility, performance, and security issues.
[Next](Overview%20of%20Dynamic%20Libraries.md)

