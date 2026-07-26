---
title: 'How to learn compilers: LLVM Edition - Low Level Bits 🇺🇦'
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/how-to-learn-compilers-llvm-edition/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:89651574a51c1a4b'
translated: false
---

> 原文：[How to learn compilers: LLVM Edition - Low Level Bits 🇺🇦](https://lowlevelbits.org/how-to-learn-compilers-llvm-edition/)　·　Low Level Bits (Alex Denisov)

# How to learn compilers: LLVM Edition

_Published on Nov 04, 2021_

This is a mirror of the Substack article   
 [How to learn Compilers (LLVM Edition)](https://lowlevelbits.com/p/how-to-learn-compilers-llvm-edition)  
 The most recent version is there.

Compilers and Programming Languages is a huge topic. You cannot just take a learning path and finish it at some point. There are many different areas, each of which is endless.

Here, I want to share some links that would help to learn compilers. The list could not be exhaustive - everyone is busy, and no one has time to read the [Dragon Book](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools).

The main criteria behind each link:

- I can personally recommend the material as I went through it
- each entry should be relatively short and can be consumed in a reasonable time

I’m a big fan of learning through practicing. Thus the main focus is on LLVM, as you can go and do something cool with real-world programs!

The list consists of four groups: general theory, front-end, middle-end, and back-end.

At the first run, you can take the first item from each group, and it should put you on solid ground.

### Disclaimer

There are a lot of excellent resources out there! Some of them are not on the list because of my subjective judgment, and the others are not here because I’ve never seen them!

**Please, share your favorite resource either via [email](https://lowlevelbits.org/cdn-cgi/l/email-protection#e48588819ca4888b938881928188868d9097ca8b9683) or on [Twitter](https://twitter.com/1101_debian/status/1456346324794806274).**

### General Theory / Introduction

- [AOSA book: LLVM](http://aosabook.org/en/llvm.html). This is a chapter from the [Architecture of Open Source Applications](http://aosabook.org/en/index.html) book. It is written by Chris Lattner and covers high-level LLVM design.
- [Compilers](https://online.stanford.edu/courses/soe-ycscs1-compilers). The course is taught by Alex Aiken. In this course, you build a compiler for a real programming language from scratch. It covers the whole compilation pipeline: parsing, type-checking, optimizations, code generation. Besides practical parts, it also dives into the theory.
- [Automata Theory](https://online.stanford.edu/courses/soe-ycsautomata-automata-theory). The course is taught by Jeffrey Ullman. This one is pretty heavy on theory. It starts with relatively simple topics like state machines and finite automata (deterministic and otherwise). It gradually moves on to more complex things like Turing-machines, computational complexity, famous P vs. NP, etc.

or

- [Theory of Computation](https://ocw.mit.edu/courses/mathematics/18-404j-theory-of-computation-fall-2020/). This course is taught by Michael Sipser. It is similar to the one above but delivered in a different style. It goes into more detail on specific topics.

### Front-end

The compiler front-end is where the interaction with the actual source code happens. The compiler parses the source code into an Abstract Syntax Tree (AST), does semantic analysis and type-checking, and converts it into the intermediate representation (IR).

The Compilers course from the above covers the general parts. Here are some links specific to Clang:

- [Understanding the Clang AST](https://jonasdevlieghere.com/understanding-the-clang-ast/). This article is written by Jonas Devlieghere. It goes into detail and touches implementation details of Clang’s AST. It also has a lot of excellent links to dive deeper into the subject.
- [clang-tutor](https://github.com/banach-space/clang-tutor/). This repository maintained by Andrzej Warzyński. It contains several Clang plugins covering various topics, from simple AST traversals to more involved subjects such as automatic refactoring and obfuscation.

### Middle-end

The middle-end is a place where various optimizations happen. Typically, the middle-ends use some intermediate representation. The intermediate representation of LLVM is usually referred to as LLVM IR or LLVM Bitcode. In a nutshell, it is a human-readable assembly language for a pseudo-machine (i.e., the IR does not target any specific CPU). The LLVM IR maintains certain properties: it is in a Static Single Assignment (SSA) form organized as a Control-Flow Graph (CFG).

- [LLVM IR Tutorial - Phis, GEPs and other things, oh my!](https://www.youtube.com/watch?v=m8G_S5LwlTo). This is a great talk by Vince Bridgers and Felipe de Azevedo Piovezan.
- [Introduction to LLVM](https://www.youtube.com/watch?v=J5xExRGaIIY). A one-hour-long talk/tutorial from LLVM Developers meeting given by Eric Christopher and Johannes Doerfert. Another great tutorial that better builds on top of the previous video.
- [CS 6120: Advanced Compilers](https://www.cs.cornell.edu/courses/cs6120/2020fa/self-guided/). The course is taught by Adrian Sampson. The title says “advanced,” but it covers what one would expect in a modern production-grade compiler: SSA, CFG, optimizations, various analyses.
- [Bitcode Demystified](https://lowlevelbits.org/bitcode-demystified/)(🔌). This one is from me. It gives a high-level description of what’s the LLVM Bitcode is.
- [llvm-tutor](https://github.com/banach-space/llvm-tutor). This one is also from Andrzej Warzyński. It covers LLVM plugins (so-called passes) that allow one to analyze and transform the programs in the LLVM IR form.

### Back-end

The last phase of the compilation is a back-end. This phase aims to convert the intermediate representation into a machine code (zeros and ones). The zeros and ones later can be run on the CPU. Therefore, to understand the back-end, you need to understand the machine code and how CPUs work.

- [Build a Modern Computer from First Principles: From Nand to Tetris](https://www.coursera.org/learn/build-a-computer). Taught by Shimon Schocken and Noam Nisan. This course starts backward: first, you build the logic gates (and, or, xor, etc.), then use the logic gates to construct Arithmetic-Logic Unit (ALU), and then use the ALU to build the CPU. Then you learn how to control the CPU with zeros and ones (machine code), and eventually, you develop your assembler to convert the human-readable assembly into the machine code.
- [Parsing Mach-O files](https://lowlevelbits.org/parsing-mach-o-files/)(🔌). This is a short article written by me. It shows how to parse object files on macOS (Mach-O). If you are on Linux or Windows, search for similar articles on `elf` and `PE/COFF` files, respectively.
- [Performance Analysis and Tuning on Modern CPUs](https://book.easyperf.net/perf_book). The book by Denis Bakhvalov. While it is about performance, it gives an excellent introduction to how CPUs work.

### Bonus points

Here are some more LLVM related channels I recommend looking at:

- [LLVM’s YouTube channel](https://www.youtube.com/channel/UCv2_41bSAa5Y_8BacJUZfjQ). Here you can find a lot of talks from developer meetings.
- [LLVM Weekly](https://llvmweekly.org). A weekly newsletter run by Alex Bradbury. This is the single newsletter I am aware of that doesn’t have ads!
- [LLVM Blog](https://blog.llvm.org). This is, well, LLVM’s blog.
- [LLVM Tutorials](https://llvm.org/docs/tutorial/). Good starting points, even if you know nothing about compilers.
- [Embedded in academia](https://blog.regehr.org/archives/category/compilers). John Regehr’s blog has lots of goodies when it comes to LLVM and compilers!

### Strings attached

As I mentioned in the beginning, Compilers is a huge field! If you go through the material above, you will learn a lot, but you will still have a few knowledge gaps in the whole compilation pipeline (I certainly do). But the good thing is - you’d know what the gaps are and how to address them!

Good luck!
