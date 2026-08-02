---
title: Mach-O Programming Topics
apple_id: TP40001519
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MachOTopics/0-Introduction/introduction.html
archived_at: '2026-07-15T07:25:16.143661Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Building%20Mach-O%20Files.md)

# Introduction

OS X supports a number of application environments, each with its own runtime rules, conventions, and file formats. In OS X, kernel extensions, command-line tools, applications, frameworks, and libraries (shared and static) are implemented using Mach-O (Mach object) files.

The OS X runtime architecture dictates how object files are laid out in the filesystem and how programs communicate with the kernel. The object file format used in OS X is Mach-O .

A Mach-O file has the following regions of data (the complete format is described in _OS X ABI Mach-O File Format Reference_):

- __Header:__ Specifies the target architecture of the file, such as PPC, PPC64, IA-32, or x86-64.
- __Load commands:__ Specify the logical structure of the file and the layout of the file in virtual memory.
- __Raw segment data:__ Contains raw data for the segments defined in the load commands.

The following list describes other runtime environments supported in OS X:

- 

  _Classic_ is a Mac app that runs Mac OS 9 within its address space and provides bridging services that allow OS X to interact with Mac OS 9 applications. Both classic 68K applications and PowerPC Code Fragment Manager (CFM) applications can run under Mac OS 9 in Classic. (Mac OS 9 does not support the 68K variant of Code Fragment Manager, so you cannot run CFM-68K applications in OS X.)
- 

  _LaunchCFMApp_ is a command-line tool that runs programs created for the PowerPC Code Fragment Manager. The file format used by such programs is called _Preferred Executable Format (PEF)_. Carbon provides bridging for Code Fragment Manager applications that allows them to link to Mach-O–based code, but—for ease of debugging if for no other reason—it’s generally a good idea to use Mach-O for Carbon applications.
- 

  The HotSpot _Java virtual machine_ is a Mac app that executes Java bytecode applications and applets.
- The _OS X kernel_ supports kernel extensions (KEXTs), which are static Mach-O executable files that are loaded directly into the address space of the kernel. Because errant code can write directly to memory used by the kernel, kernel extensions have the potential to crash the operating system. You should generally avoid implementing functionality as kernel extensions if possible.

The Code Fragment Manager is documented in _Mac OS Runtime Architectures_, available from the Apple Developer Connection website.

This document discusses how you use the Mach-O file format. It describes what types of programs you can build, how programs are loaded and executed, how you can change the way programs are loaded and executed, how to load code at runtime, and how to load and link code at runtime. If you create or load bundles, shared libraries, or frameworks, you’ll probably want to read and understand everything in this document.

If you write development tools for OS X, you need to understand the information presented in this document.

This document is also useful for developers of shared libraries and frameworks, and for developers of applications that need to load code at runtime.

This document contains the following articles:

- [Building Mach-O Files](Building%20Mach-O%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmryfvjvomi) describes how Mac apps are built and describes the types of programs you can develop.
- [Executing Mach-O Files](Executing%20Mach-O%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmrzfvjvomi) provides an overview of the OS X dynamic loading process.
- [Loading Code at Runtime](Loading%20Code%20at%20Runtime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmzqfvjvomi) describes how to use shared libraries and frameworks and how to load plug-ins at runtime.
- [Indirect Addressing](Indirect%20Addressing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmjzfvjvomi) explains how a Mach-O file refers to symbols defined in another Mach-O file.
- [Position-Independent Code](Position-Independent%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkmryfvjvomi) discusses the method by which the dynamic linker loads a region of code at a non-fixed virtual memory address.
- [x86-64 Code Model](x86-64%20Code%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanbufvjvomi) describes differences in the OS X x86-64 user-space code model from the System V x86-64 code model.

This document also contains a revision history and an index.

You can access full reference documentation for the standard command-line development tools using the `man` tool on the command line, or by choosing Open Man Page from the Xcode Help menu.

This document provides information on the Mach-O runtime architecture. It does not address the following:

- Descriptions of the data structures that make up a Mach-O file. You can find this information in _OS X ABI Mach-O File Format Reference_.
- If you are loading code at runtime but cannot or do not wish to use the `CFBundle` opaque type or the `NSBundle` class, you should refer to _OS X ABI Dynamic Loader Reference_.
- The GCC C++ application binary interface—the specification of C++ class member layout, function/method name mangling, and related C++ issues. This information is documented for GCC 3.0 and later at [http://www.codesourcery.com/cxx-abi/abi.html](http://www.codesourcery.com/cxx-abi/abi.html).
- The GCC Objective-C data structures and dynamic runtime functions. For this information, see _[The Objective-C Programming Language](../../Cocoa/The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_.
- The runtime environment of the OS X kernel, Darwin. See _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_ for more information.

Source code from the Darwin project can be downloaded from [http://developer.apple.com/darwin/](https://developer.apple.com/darwin/).

You might also find the following books useful in conjunction with this document:

- _Mac OS Runtime Architectures_, Apple Computer, Inc. Available at [http://developer.apple.com/tools/mpw-tools/books.html](https://developer.apple.com/tools/mpw-tools/books.html). Documents the classic 68K segment loader architecture, as well as the Code Fragment Manager Preferred Executable executable format used with classic PowerPC applications and with many Carbon applications.
- _Linkers and Loaders_, John R. Levine, Morgan Kaufmann, 2000, ISBN 1-55860-496-0. Describes the workings and operation of standard linkers from the earliest program loaders to the present dynamic link editors. Among the contents of this book are discussions of the classic BSD `a.out` format, the Executable and Linking Format (ELF) preferred by many current operating systems, the IBM System/360 linker output format, and the Microsoft Portable Executable (PE) format.
- _System V Application Binary Interface AMD64 Architecture Processor Supplement_. Found at [http://www.x86-64.org/documentation](http://www.x86-64.org/documentation), this document describes the System V x86-64 environment, on which the OS X x86-64 environment is based.

[Next](Building%20Mach-O%20Files.md)

