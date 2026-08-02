---
title: Universal Binary Programming Guidelines, Second Edition
apple_id: TP40002217
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/universal_binary/universal_binary_intro/universal_binary_intro.html
archived_at: '2026-07-15T08:16:38.143760Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Building%20a%20Universal%20Binary.md)

# Introduction

_Universal Binary Programming Guidelines_ will assist experienced developers to build and modify their Mac OS X applications to run as universal binaries. _Universal binaries_ run natively on Macintosh computers using PowerPC or Intel microprocessors and deliver optimal performance for both architectures in a single package.

This document is designed to help developers determine exactly how much work needs to be done and provides useful tips for general as well as specific code modification scenarios. It describes the prerequisites for building code as a universal binary and shows how to do so using Xcode 2.2. It also discusses the differences between the Intel and PowerPC architectures that can affect code behavior and provides guidelines for ensuring that universal binary code builds correctly.

This version of _Universal Binary Programming Guidelines_ represents a significant update since its introduction at the Apple Worldwide Developers Conference in June, 2005. It brings together all the information that developers need to make the transition to Intel-based Macintosh computers. This version includes pointers to newly revised tools documentation—[Building Universal Binaries](../../Developer%20Tools/Xcode%20Project%20Management%20Guide/Building%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojtfvjvomy), _[GCC Porting Guide](https://developer.apple.com/library/archive/releasenotes/DeveloperTools/GCC40PortingReleaseNotes/Introduction.html#//apple_ref/doc/uid/TP40002069)_, _[SDK Compatibility Guide](../../Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_, and more—as well as improved guidelines and tips. Anyone who has an older version of _Universal Binary Programming Guidelines_ will want to replace it with this version.

Any developer who currently has an application that runs in Mac OS X will want to read this document to learn how to modify their code so that it runs natively on all current Apple hardware. Developers who have not yet written an application for the Macintosh, but are planning to do so, will want to follow the guidelines in the document to ensure that their code can run as a universal binary.

This document is organized into the following chapters:

- [Building a Universal Binary](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywviucykjcummjqge) shows how to use Xcode 2.2 to build native and universal binaries, describes build options, and provides troubleshooting information for code that doesn’t run properly on an Intel-based Macintosh computer.
- [Architectural Differences](Architectural%20Differences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugawviucykjcummjqge) outlines the major differences between the x86 and PowerPC architectures. Understanding the differences will help you to write portable code.
- [Swapping Bytes](Swapping%20Bytes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugmwviucykjcummjqge) describes byte-ordering differences in detail, provides a list of byte-swapping routines, and discusses strategies for a number of scenarios that require you to swap bytes. This is a must-read chapter for all Mac OS X developers. It will help you understand how to avoid byte-ordering issues when transferring data and data files between architectures.
- [Guidelines for Specific Scenarios](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewviucykjcummjqge) contains tips for a variety of situations that are not common to most applications.
- [Preparing Vector-Based Code](Preparing%20Vector-Based%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqhawviucykjcummjqge) discusses the options available for those developers who have high-performance computing needs.

This document contains the following appendixes:

- [Rosetta](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawviucykjcummjqge) describes the translation process that allows PowerPC binaries to run on an Intel-based Macintosh computer.
- [Architecture-Independent Vector-Based Code](Architecture-Independent%20Vector-Based%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgmwviucykjcummjqge) uses matrix multiplication as an example to show how to write vector code with a minimum amount of architecture-specific coding.
- [32-Bit Application Binary Interface](32-Bit%20Application%20Binary%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugywviucykjcummjqge) provides information on where to find details.
- [64-Bit Application Binary Interface](64-Bit%20Application%20Binary%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmznknlts) provides information on where to find details.

The document assumes the following:

- Your application runs in Mac OS X.

  Your application can use any of the Mac OS X development environments: Carbon, Cocoa, Java, or BSD UNIX.

  If your application runs in the UNIX operating system but not specifically in Mac OS X, you should first read _[Porting UNIX/Linux Applications to OS X](../../Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt)_.

  If your application runs only in the Windows operating system, you should first read _[Porting to Mac OS X from Windows Win32 API](../../Porting/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ta2i)_.

  If you are new to Mac OS X, you should take a look at _[Mac Technology Overview](../Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.
- You know how to use Xcode.

  Currently Xcode is the only GUI tool available that compiles code to run universally.

  If you are unfamiliar with Xcode, you might want to take a look at _[Xcode Workspace Guide](../../Developer%20Tools/Xcode%20Workspace%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmrq)_.

  If you have been using CodeWarrior, you should read _[Porting CodeWarrior Projects to Xcode](../../Developer%20Tools/Porting%20CodeWarrior%20Projects%20to%20Xcode/Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydq)_.

The term _x86_ is a generic term used in some parts of this book to refer to the class of microprocessors manufactured by Intel. This book uses the term x86 as a synonym for IA-32 (Intel Architecture 32-bit).

[Next](Building%20a%20Universal%20Binary.md)

