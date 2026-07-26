---
title: 'Options for porting Objective-C/Cocoa apps to Windows | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/04/options-for-porting-objective-ccocoa.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:d56e324db7838725'
translated: false
---

> 原文：[Options for porting Objective-C/Cocoa apps to Windows | Cocoa with Love](https://www.cocoawithlove.com/2010/04/options-for-porting-objective-ccocoa.html)　·　Cocoa with Love (Matt Gallagher)

There are a few different options for porting Objective-C/Cocoa applications to Windows. Each option has different advantages and offers different capabilities. In this post, I'll give an overview of some of these options, their advantages and disadvantages.

## Introduction

In this post, I'll look at the options available for porting Objective-C/Cocoa applications to Windows. There are other ways of writing compiled programs that are designed to be portable across multiple platforms (Qt, WxWidgets, Java, pure command-line C, etc) and numerous virtualized environments that are inherently platform independent (Java, Mono, etc) but this is a Cocoa blog so I'm going to ignore all of these.

A warning: porting software from the Mac to Windows is tricky and this post is not intended to solve those tricky situations. If you decide to port an Objective-C program to another platform, expect to build a lot of software via the command-line, track down bugs in libraries you didn't write and handle weird and cryptic error messages at every stage. Keeping a common codebase across multiple platforms is good in the long-run but can actually be slower than a complete re-write to set up in the first place.

## Recreating POSIX on Windows

Before I actually get to discussing porting Objective-C/Cocoa programs to Windows, I need to discuss the target environment. Specifically, the difficulty of getting the POSIX layer from the Mac to run on Windows.

Much of what is considered to be "standard C" on the Mac actually falls outside the minimalist standard C library and is part of the BSD system on the Mac. TCP/IP sockets, many file I/O calls, getting information about the current user; these are all traits of the BSD-derived POSIX layer on the Mac.

The first issue to solve when porting to Windows often involves looking at how to replace this BSD derived functionality. The short answer is that you normally need an API that will offer you POSIX-like behavior on Windows.

Generally, this involves one of two approaches: Cygwin or MinGW.

### Cygwin

[Cygwin](http://www.cygwin.com/) is the better known of the two because it is intended as a user-environment. It aims to recreate a full POSIX system, with full POSIX compatibility on top of Windows. Many ports of X-Windows applications from *nix systems (Linux, UNIX, etc) to Windows run on top of Cygwin because it comes the closest to offering source-level compatibility with *nix systems.

However, Cygwin comes with a disadvantage: if you write your project using Cygwin, then your user must also have Cygwin installed. Cygwin is not really a way to write native Windows applications, it is a way to write native Cygwin applications (and Cygwin runs on top of Windows).

### MinGW

The alternative to Cygwin is normally [MinGW](http://www.mingw.org/). MinGW is not a user environment like Cygwin. Although MSYS — a light terminal and user system — can be run on MinGW, generally the MSYS environment is only used by developers for building and testing applications, not by end users.

MinGW uses a different philosophy to Cygwin when it comes to implementing the POSIX subsystem: MinGW attempts to implement those parts of a POSIX system that can be easily mapped onto calls within the native WIN32 API on Windows. This has the huge advantage that your target users do not need to have anything except Windows installed. Unfortunately, it also means that some features (like sockets) will behave slightly differently because they will obey the native Windows behaviors, rather than the standard POSIX behaviors.

Where Cygwin programs are normally compiled on Windows, MinGW includes significant support for cross-compiling so that you can build Windows applications from different platforms.

## CoreFoundation

The minimalist approach to compiling an Objective-C program for Windows is to use Apple's own CoreFoundation APIs and Objective-C runtime and compile them for Windows.

CoreFoundation and the Objective-C runtime are both open source under Apple's APSL license:

- CoreFoundation
- CFNetwork (from Mac OS X 10.4 —

  later versions not open source

  )
- CommonCrypto
- Objective-C runtime
- Security

This solution is not real "Cocoa" (it is only the very simple subset of CoreFoundation and a few supporting frameworks) but it does have the major advantage of being efficient, thoroughly tested and maintained by Apple.

In fact, Apple themselves have a [guide on how to use these files to compile on Linux and Windows under Cygwin](http://developer.apple.com/opensource/cflite.html). You can also look at an alternate setup process on [CFLite](http://karaoke.kjams.com/wiki/CFLite).

### Advantages

CoreFoundation is thoroughly tested and efficiently written. It also offers a high degree of compatibility between Mac to Windows.

### Disadvantages

Not really Cocoa; only CoreFoundation (no Foundation or AppKit). Old version of CFNetwork.

Historically, many people have [had objections to the specific terms of the APSL](http://www.gnu.org/philosophy/historical-apsl.html). The Free Software Foundation have [withdrawn their objections following version 2.0 of the APSL](http://www.gnu.org/philosophy/apsl.html) (although they still wish it was a copy-left license, that's an issue for the licensors, not the users of the license).

## GNUstep

[GNUstep](http://www.gnustep.org/) is the oldest open source implementation of OpenStep, which became Cocoa. It is well established and fairly stable. You can build GNUstep applications on Linux, Windows under Cygwin or Visual Studio or on the Mac.

The easiest way to get started with GNUstep on Windows is to use the [GNUstep Windows Installer](http://www.gnustep.org/experience/Windows.html). You will need to install the System, Core and Devel components to begin coding. The advantage is that this will install all the MSYS/MinGW components required. For help with the installation process, there's a futher guide to [Installation on Windows](http://wiki.gnustep.org/index.php/Installation_on_Windows).

### Advantages

GNUstep is a complete application framework and has been in regular development for over a decade. It will integrate with most development environments and can be built in its entirety on Windows, Linux and many other *nix systems.

GNUstep also has a (relatively) large development community and a huge amount of [developer documentation](http://wiki.gnustep.org/index.php/Developer_Guides) (a real rarity in the world of OpenSource).

### Disadvantages

Any application written for GNUstep must be distributed with the GNUstep installer (since the whole GNUstep system must exist to allow functionality).

GNUstep is more like its own operating system (or at least its own windowing system) than a toolkit within an existing operating system. GNUstep does not use native window drawing commands on any platform.

## The Cocotron

[The Cocotron](http://www.cocotron.org/) had its first release in 2006. Its primary goal is to enable cross-compiling from Xcode on the Mac to other platforms (primarily Windows).

This cross-compiling from Xcode is The Cocotron's key defining feature: you must build all your projects in Xcode running on a Mac, even if the deployment targets are Windows or Linux. However, this means that The Cocotron's main pipeline concentrates exactly on the task of porting Mac programs to Windows.

The [installation for The Cocotron](http://www.cocotron.org/Info/Getting_Started) is a multi-step process but is relatively straightforward.

By default, The Cocotron encourages you to [debug your Windows products under Windows using Insight-GDB](http://www.cocotron.org/Tools/Debugging/Insight-GDB) (a reasonably user-friendly wrapper around GDB running under MinGW) directly on Windows.

An alternative approach for debugging is to use XCXDB ([download the XCXDB Installation here](http://groups.google.com/group/cocotron-dev/files)). This allows you to remotely debug from Xcode on the Mac to your Windows machine, so you can handle all building and debugging from Xcode. XCXDB has the added advantage that it adds project templates to Xcode to make cross-compiling projects easier to create.

### Advantages

Build and potentially debug everything from the original project in Xcode. The framework was designed with porting from the Mac to Windows in mind.

Natively builds for WIN32, meaning that final products look and feel like native Windows applications and the installation is not dependant on installing another large project (AppKit, Foundation and other .DLLs must be included with the executable but they are very small).

Simple, in-built support for NIB files, CoreData, fast enumeration, Objective-C 2.0 properties and other features that are either missing from GNUstep, external packages or still in-progress.

Aims for source level compatibility with Mac OS X, something which is not necessarily a goal of GNUstep.

### Disadvantages

The least mature of the options listed so far. It is possible to encounter bugs at low levels that you may need to fix for yourself.

While a huge amount is implemented, you won't have to go far to encounter APIs that are not. Significant portions of some classes are not implemented at all. While the interfaces exist, they will lead to a runtime exception as the program runs over a `NSUnimplementedMethod()`.

The current state of XCXDB remote debugging and Insight debugging are inferior to native debugging in an IDE.

## Conclusion

If you're only porting a command-line program to Windows, then you're spoiled for choice — all of the options I've listed will handle that (although CoreFoundation does not offer a full Foundation API).

I chose to implement the current [public beta of ServeToMe](http://zqueue.com/servetome/index.html) for Windows using The Cocotron as I think The Cocotron offers the best experience for porting a graphical user-interface Mac application to Windows. The ability to build and debug the entire project from the original Xcode project was the key feature I sought. However, it was not without issues. I'll discuss how I got ServeToMe running in The Cocotron with XCXDB next week, the issues I had and their solutions.

Despite The Cocotron's immaturity relative to GNUstep and many missing APIs, enabling a Cocoa project to be built from the Mac and deployed and debugged on Windows in a single step is a huge advantage. Further, native WIN32 at the back end (as annoying as WIN32 is to write) is better for your end-users than a system that requires Cygwin underneath.

Of course, if you needed to target Linux with an Objective-C application or you need to build on platforms other than the Mac, you'd want to use GNUstep instead. While Cocotron has Linux/X11 support underway, it is not really ready for mainstream adoption at this time.
