---
title: GCC Porting Guide
apple_id: TP40002069
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/GCC40PortingReleaseNotes/Articles/PortingGuidelines.html
archived_at: '2026-07-26T19:54:15.356550Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [GCC Porting Guide](Introduction%20to%20GCC%20Porting%20Guide.md)



# Retired Document

__Important:__
Xcode 4.2 and later do not support GCC. You should use the Clang compiler instead.

# General Guidelines for Using GCC

The following sections provide guidance for developers who are coming to the GCC compiler (and possibly Xcode) for the first time. These guidelines are intended to help you find the information you need to modify your existing projects to support GCC 4.0 or later.

## Making Your Transition Easier

When you compile existing code for the first time with the GCC 4.0 compiler, you may be shocked to see a lot of warnings in code that had previously compiled cleanly. Don't panic. This is not an unusual occurrence. The GCC 4.0 compiler is much more strict about code compliance than its predecessors and many of its peers.

Although the best way to remove warnings is to fix your code, if you are just starting your transition this may seem like a daunting task. Luckily, GCC supports a full range of options to suppress warnings. During the initial stages of your transition, you might want to use these options to hide warnings until you can fix the legitimate errors reported by the compiler. Once your executable builds without errors, though, you should enable warnings again and begin to fix those problems too. Starting with version 4.0, the GCC compiler is much better at warning you of potential problems. You should heed these warnings and fix the potential problems.

For information about the warnings and errors you are most likely to see under GCC 4.0, see [Step 2: Compile Your Code in GCC 4.0](Porting%20from%20GCC%203.3%20to%20GCC%204.0.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanzrfuytamzsg42q). For a list of compiler options you can use to disable warnings, see _GNU C/C++/Objective-C 4.0.1 Compiler User Guide_ or the `gcc` man page.

## Auto-Vectorization

A feature introduced in GCC 4.0.1 is the ability to automatically generate AltiVec (Velocity Engine) or SSE instructions for some types of scalar code. When auto-vectorization is enabled, the compiler looks for loops that might benefit from the use of vector instructions. Loops that process scalar values sequentially are very inefficient compared to the same loop coded with vectors. Using vectors, a loop can process multiple values simultaneously during a single loop iteration. This reduces the total number of iterations (and thus CPU cycles) needed to process the same amount of data.

If you were already considering rewriting some of your scalar code to use vectors, you should try auto-vectorization first:

- If you are using Xcode 2.2 or later, you enable auto-vectorization by modifying the build settings for your project. (Note that auto-vectorization is generally more appropriate for deployment configurations because it also causes compiler optimizations to be enabled.) Select the desired configuration and enable the "Auto-vectorization" code generation option.
- If you are using GCC directly from the command line, add `-ftree-vectorize` to your compiler options. Auto-vectorization also requires at least the `-O2` or `-Os` optimization level. If you are compiling code for the PowerPC architecture, the target CPU must also be set to G4 or higher (`-mcpu=G4` or `-mcpu=G5`). For Intel-based Macintosh computers, vectorization is available for all supported CPU types.

__Note:__ Auto-vectorization occurs only on code that does not already contain vector instructions. If your software contains hand-tuned AltiVec or SSE code, the auto-vectorization feature does not attempt to optimize your code further.

For information on how to port your AltiVec code to SSE, see _[AltiVec/SSE Migration Guide](../../../documentation/Performance/AltiVec-SSE%20Migration%20Guide/Introduction%20to%20AltiVec-SSE%20Migration%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomrz)_. For additional resources and support on how to transition your software so that it runs on Intel-based Macintosh computers, see Apple's Developer Transition Resource Center at [http://developer.apple.com/transition/](https://developer.apple.com/transition/).

## Creating Universal Binaries From the Command Line

Although it is easiest to build universal binaries from Xcode 2.1 or later, you can also build them from the command line using GCC 4.0 or later. To build a version of your binary for Intel-based Macintosh computers, you must set the `-arch` option of the GCC compiler to `i386` and build a separate version of your binary away from your PowerPC object files and binary. Once you have compiled binaries for both architectures, you can use the `lipo` tool to merge them into a single executable file.

For fundamental information on how to create universal binaries, _[Universal Binary Programming Guidelines, Second Edition](../../../documentation/Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_ is required reading. For additional information on developing executables for multiple architectures and multiple versions of Mac OS X, see _[SDK Compatibility Guide](../../../documentation/Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_. For reference information about the GCC compiler, including command-line options for different architectures, see the `gcc` man page or _GNU C/C++/Objective-C 4.0.1 Compiler User Guide_. Finally, for information about how to merge two or more binaries into a single Mach-O executable, see the `lipo` man page.

## Migrating CodeWarrior Projects

If you are currently using CodeWarrior to build your projects, you must convert your CodeWarrior project to Xcode before you can use GCC 4.0. Xcode makes the process of converting CodeWarrior projects easier by providing automated support for the import process. However, you may still need to make some changes to your project for it to be imported cleanly.

For detailed information on how to migrate your CodeWarrior projects to Xcode, see _[Porting CodeWarrior Projects to Xcode](../../../documentation/Developer%20Tools/Porting%20CodeWarrior%20Projects%20to%20Xcode/Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydq)_.

## Working With the C++ Runtime Environment

For projects containing C++ source code, you need to be aware that the runtime environment for C++ changed between Mac OS X v10.3.8 and v10.3.9. Prior to Mac OS X v10.3.9, the standard C++ library was provided as a static library that you would then link directly into your executables. In Mac OS X v10.3.9 and later, this library was changed to be a dynamic shared library.

New programs built using GCC 4.0 are automatically configured to use the new dynamic shared library version of the C++ runtime. Using the dynamic shared library is advantageous as it generally results in smaller application size and faster application load times. The new library also provides general improvements to the C++ runtime and better compatibility.

If you are migrating a project from an earlier version of GCC to GCC 4.0 or later, you must make sure that you remove any references to `libstdc++.a` from your project. (In Xcode, look for this library in the External Frameworks and Libraries group.) The `libstdc++.a` file is the older, static version of the C++ library. If this file is still in your project, you may encounter link errors due to the presence of two copies of the C++ standard library.

For additional information about changes to the C++ runtime, see _[C++ Runtime Environment Programming Guide](../../../documentation/Developer%20Tools/C%2B%2B%20Runtime%20Environment%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnrw)_.
