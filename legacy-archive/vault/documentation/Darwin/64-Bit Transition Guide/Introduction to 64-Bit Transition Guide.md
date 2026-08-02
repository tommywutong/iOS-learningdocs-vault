---
title: 64-Bit Transition Guide
apple_id: TP40001064
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/intro/intro.html
archived_at: '2026-07-15T07:23:04.105857Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Should%20You%20Recompile%20Your%20Software%20as%20a%2064-Bit%20Executable.md)

# Introduction to 64-Bit Transition Guide

This document describes the 64-bit features that are available in OS X v10.4 and v10.5. You should read it to help you determine which of these features to use and how to use them.

For the purposes of this document, 64-bit computing is defined as support for a 64-bit address space—that is, support for concurrent use of more than 4 GB of memory by a single executable program—no more, no less.

OS X v10.8 uses a 64-bit kernel and fully supports 64-bit applications. The 64-bit kernel was originally introduced in OS X v10.6 (on some models of Mac hardware), and 64-bit application support was introduced in v10.5. Command-line 64-bit support was introduced in v10.4.

Mac app developers should, at a minimum, read the chapter [Should You Recompile Your Software as a 64-Bit Executable?](Should%20You%20Recompile%20Your%20Software%20as%20a%2064-Bit%20Executable.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqgywviucykjcummjqge). That chapter will help you determine whether it makes sense for your application to take advantage of 64-bit application support in OS X v10.5 and later.

Developers of device drivers and kernel extensions should also read this document. Beginning with v10.6, device drivers and kernel extensions must be compiled with a 64-bit slice to be loadable into a 64-bit kernel. Beginning with v10.8, all kernel device drivers and other extensions must be compiled with a 64-bit slice.

This document is organized into the following chapters:

- [Should You Recompile Your Software as a 64-Bit Executable?](Should%20You%20Recompile%20Your%20Software%20as%20a%2064-Bit%20Executable.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqgywviucykjcummjqge)—provides helpful guidance about whether you should recompile your application as a 64-bit executable.
- [Major 64-Bit Changes](Major%2064-Bit%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqg4wviucykjcummjqge)—describes the high-level architectural changes between a 32-bit and 64-bit environment.
- [Making Code 64-Bit Clean](Making%20Code%2064-Bit%20Clean.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzs)—explains the general changes needed to make an application 64-bit clean.
- [Compiling 64-Bit Code](Compiling%2064-Bit%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqhawviucykjcummjqge)—explains how to compile your application as a 64-bit executable.
- [High-Level 64-Bit API Support](High-Level%2064-Bit%20API%20Support.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgqwvgvzw)—summarizes changes to higher level APIs such as Carbon, Cocoa, and QuickTime and includes pointers to more detailed documentation on these changes.
- [Cross-Architecture Plug-in Support](Cross-Architecture%20Plug-in%20Support.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzx)—describes ways to support legacy plug-ins across architecture boundaries using helper hosts.
- [Performance Optimization](Performance%20Optimization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrshawvgvzr)—gives tips for spotting common performance regressions caused by transitioning your code to 64-bit.
- [Kernel Extensions and Drivers](Kernel%20Extensions%20and%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzr)—tells how to transition your drivers and other kernel extensions to 64-bit executables.

For additional information, see the following documents:

- _[Tools & Languages Starting Point](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Tools/index.html#//apple_ref/doc/uid/TP30001102)_ includes pointers to documentation that may help you solve 64-bit-related tools issues.
- _[64-Bit Transition Guide for Cocoa](../../Cocoa/64-Bit%20Transition%20Guide%20for%20Cocoa/Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbx)_ and _[64-Bit Guide for Carbon Developers](../../Carbon/64-Bit%20Guide%20for%20Carbon%20Developers/Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobr)_ provide information about Apple’s 64-bit application APIs.
- _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_ provides information about the Intel transition. You should read this document and add native Intel support to your application first, since many of the Intel changes also apply to a 64-bit port.
- _OS X ABI Mach-O File Format Reference_ provides 64-bit ABI information that is useful if you are writing assembly language code.
- _Xcode 4 Help_ provides information about using Xcode. You should be familiar with Xcode before you port your application or driver to 64-bit.

The `gcc`, `ld`, and `lipo` man pages may also be relevant to you.

[Next](Should%20You%20Recompile%20Your%20Software%20as%20a%2064-Bit%20Executable.md)

