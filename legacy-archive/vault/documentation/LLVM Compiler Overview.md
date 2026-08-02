---
title: LLVM Compiler Overview
apple_id: TP40010019
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/CompilerTools/Conceptual/LLVMCompilerOverview/index.html
archived_at: '2026-07-15T07:22:00.089865Z'
---
> 导航：[总目录](../README.md) · [documentation](../_indexes/documentation.md)



# LLVM Compiler Overview

The LLVM compiler is the next-generation compiler, introduced in Xcode 3.2 for Snow Leopard, based on the open source [LLVM.org](http://llvm.org/) project. The LLVM.org project employs a unique approach of building compiler technologies as a set of libraries. Capable of working together or independently, these libraries enable rapid innovation and the ability to attack problems never before solved by compilers. Multiple technology groups within Apple are active contributors within the LLVM.org community, and they use LLVM technology to make Apple platforms faster and more secure.

In Xcode, the LLVM compiler uses the Clang front end (a C-based languages project on LLVM.org) to parse source code and turn it into an interim format. Then the LLVM code generation layer (back end) turns that interim format into final machine code. Xcode also includes the LLVM GCC compiler, which uses the GCC compiler front end for maximum compatibility, and the LLVM back end, which takes advantage of LLVM's advanced code generator. This shows the flexibility of a library-based approach to compiler development. There are many other features, such as link-time optimization, more detailed diagnostic information, and even static analysis, that are made available to Xcode due to the adoption of LLVM.

Watch the videos listed on this page to gain a detailed introduction to LLVM technology. The following videos were taken at the 2011 LLVM Developers' Meeting:

- _Extending Clang_
- _LLVM MC in Practice_
- _Register Allocation in LLVM 3.0_

These videos were captured at the 2010 LLVM Developers' Meeting:

- _The LLVM Assembler and Machine Code Infrastructure_
- _The LLDB Modular Debugging Infrastructure_
- _libclang: Thinking Beyond the Compiler_
- _libc++: A Standard Library for C++0x_

These videos were captured at the 2009 LLVM Developers' Meeting:

- _State of Clang_
- _Future Works in LLVM Register Allocation_
- _ScalarEvolution and Optimization in LLVM_
- _OpenCL and LLVM_

Additional resources about LLVM technologies are available at the home page for the [LLVM.org](http://llvm.org/) project.
