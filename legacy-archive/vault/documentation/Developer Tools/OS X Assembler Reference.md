---
title: OS X Assembler Reference
apple_id: TP30000851
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2009-01-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/000-Introduction/introduction.html
archived_at: '2026-07-15T07:30:58.558268Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/010-Using_the_Assembler/using_asm.html)

# Introduction

The OS X assembler serves a dual purpose. It assembles the output of `gcc`, Xcode’s default compiler, for use by the OS X linker. It also provides the means to assemble custom assembly language code written for its supported platforms.

This document provides a reference for the use of the assembler, including basic syntax and statement layout. It also contains a list of the specific directives recognized by the assembler and complete instruction sets for the PowerPC and i386 processor architectures.

This document contains the following chapters:

- [Using the Assembler](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/010-Using_the_Assembler/using_asm.html#//apple_ref/doc/uid/TP30000820-TPXREF101) describes how to run the assembler and its relevant input/output files. It also discusses specific options that can be passed to the assembler on the command line.
- [Assembly Language Syntax](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/020-Assembly_Language_Syntax/asm_syntax.html#//apple_ref/doc/uid/TP30000821-TPXREF101) describes the basic syntax of assembly language elements and expressions.
- [Assembly Language Statements](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/030-Assembly_Language_Statements/asm_language.html#//apple_ref/doc/uid/TP30000822-TPXREF101) describes in greater detail the assembly language statements that make up an assembly language program.
- [Assembler Directives](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/040-Assembler_Directives/asm_directives.html#//apple_ref/doc/uid/TP30000823-TPXREF101) describes assembler directives specific to the OS X assembler and how to use them in your assembly code.
- [PowerPC Addressing Modes and Assembler Instructions](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/050-PowerPC_Addressing_Modes_and_Assembler_Instructions/ppc_instructions.html#//apple_ref/doc/uid/TP30000824-TPXREF101) contains information specific to the PowerPC processor architecture and provides a complete list of addressing modes and instructions relevant to it.
- [i386 Addressing Modes and Assembler Instructions](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/060-i386_Addressing_Modes_and_Assembler_Instructions/i386_intructions.html#//apple_ref/doc/uid/TP30000825-TPXREF101) contains information specific to the i386 processor architecture and provides a complete list of addressing modes and instructions relevant to it.
- [Mode-Independent Macros](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/900-Mode_Independent_Macros/macros.html#//apple_ref/doc/uid/TP30000851-CH213-CJBHHCCA) introduces the macros included in the OS X v10.4 SDK to facilitate the development of assembly code that runs in 32-bit PowerPC and 64-bit PowerPC environments.

This document also contains a revision history, and an index.

[Next](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler/010-Using_the_Assembler/using_asm.html)

