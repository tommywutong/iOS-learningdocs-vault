---
title: 'Compiling Ruby. Part 4: progress update - Low Level Bits 🇺🇦'
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/compiling-ruby-part-4/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:bf0769c1f84ebf97'
translated: false
---

> 原文：[Compiling Ruby. Part 4: progress update - Low Level Bits 🇺🇦](https://lowlevelbits.org/compiling-ruby-part-4/)　·　Low Level Bits (Alex Denisov)

# Compiling Ruby. Part 4: progress update

_Published on Nov 30, 2023_

This article is part of the series "Compiling Ruby," in which I'm documenting my journey of building an ahead-of-time (AOT) compiler for [DragonRuby](https://dragonruby.org), which is based on [mruby](https://mruby.org) and heavily utilizes [MLIR](https://mlir.llvm.org) and [LLVM](https://llvm.org) infrastructure.

This series is mostly a brain dump, though sometimes I'm trying to make things easy to understand. Please, let me know if some specific part is unclear and you'd want me to elaborate on it.

Here is what you can expect from the series:

- Motivation

  : some background reading on what and why
- Compilers vs Interpreters

  : a high level overview of the chosen approach
- RiteVM

  : a high-level overview of the mruby Virtual Machine
- MLIR and compilation

  : covers what is MLIR and how it fits into the whole picture
- **[Progress update](https://lowlevelbits.org/compiling-ruby-part-4/): short progress update with what's done and what's next**
- Exceptions

  : an overview of how exceptions work in Ruby
- Garbage Collection (TBD): an overview of how mruby manages memory
- Fibers (TBD): what are fibers in Ruby, and how mruby makes them work

---

It’s been a while since I wrote the last blog post. One of the reasons is that so far, I had to change a lot of things in the implementation due to the exception support.

I’m writing a short progress update on where we are and what’s coming next.

### What Happened

During this year, I gave two short talks related to this project:

- a high-level overview of the project

  (EuroLLVM dev meeting)
- intro into exception handling in LLVM

  (LLVM Social Berlin)

The state as of EuroLLVM (May 2023) was as follows:

- out of

  bytecode operations
- out of

  files
- out of
- of tests were passing (1033 out of 1416 it could compile)

### Current Status

The three missing opcodes were all about exception handling, and this is what (so far) took the most time to implement. I have some drafts on the details, and I plan to publish them before the end of the year.

With the proper exception handling in place, things are finally starting to take the right shape. There is still much work to do, but it’s more predictable now.

Some new stats:

- all bytecode operations are implemented 🎉
- all the ruby code in the repo is now compiled (stdlib, gems, tests) 🎉
- of the tests are passing (1378 out of 1450) 🎉

### Next Steps

The test suite now drives the next steps:

- the majority of the failing tests (42 out of 71) are due to the missing fibers implementation
- the second biggest group is various proc/methods metadata for runtime reflection
- the next big part is related to JIT/runtime evaluation (i.e., when you can execute arbitrary Ruby code not known/visible at compile time)
- and there is a long tail of more minor things

Besides that, I need to figure out a better build system for all of it. Currently, It’s a mess glued together by CMake scripts and CMake templates. It works perfectly for development and testing, but I’d hate to use such a system as an end user.

Ideally, I want a one-click solution that would take Ruby files as input and produce a native executable.

What is the state of the art when it comes to build systems/orchestration of compilation? Please let me know if you have any pointers 🙌

---

**Thank you so much for reaching this far!**

The next article is about exceptions - [Exceptions](https://lowlevelbits.org/compiling-ruby-part-5/)
