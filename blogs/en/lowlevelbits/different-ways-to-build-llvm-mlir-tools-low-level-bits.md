---
title: Different ways to build LLVM/MLIR tools - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/different-ways-to-build-llvm/mlir-tools/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:830f3676f4336819'
translated: false
---

> 原文：[Different ways to build LLVM/MLIR tools - Low Level Bits 🇺🇦](https://lowlevelbits.org/different-ways-to-build-llvm/mlir-tools/)　·　Low Level Bits (Alex Denisov)

# Different ways to build LLVM/MLIR tools

_Published on May 02, 2025_

This is a mirror of the Substack article   
 [Different ways to build LLVM/MLIR tools](https://lowlevelbits.com/p/different-ways-to-build-llvmmlir)  
 The most recent version is there.

LLVM and MLIR frameworks are typically used to build compilers for various use cases, but I’m using word “tools” here to cover a broader set of possibilities (compilers, language plugins, analyzers, etc.).

If you want to build such a tool, then you obviously need to somehow “connect” your code to LLVM or MLIR libraries.

In this article I’m not going to cover how to do the build itself (I believe there are plenty of great resources out there already), but rather focus on various ways to actually obtain those LLVM libraries and what kinds of features those options bring with them.

I’m also considering the simplest integration: CMake and C++, no fancy build systems, no fancy languages. Different build systems and languages would require different considerations.

Effectively, this article is organized as a table with different ways to get LLVM/MLIR on one axis, and various available features on another.

The actual table is at the very end.

## Features

Here is a non-exhaustive list of different features that I consider important.  
 If you believe something is missing, please leave a comment.

[Leave a comment](https://lowlevelbits.com/p/different-ways-to-build-llvmmlir/comments)

### (Fast) Build Times

Obviously, everyone wants to have fast build times. There are two slightly different angles to this story: if you decide to build LLVM from scratch, it would obviously take long time. But even if you don’t build LLVM from scratch, you may still have to wait for way too long due to the static linking.

Also, building LLVM/MLIR from scratch without caching is going to be a huge bottleneck on the CI.

### Debugging Experience

Once in a while things go south, so you need to debug not only your code, but also look into what’s “wrong” inside of LLVM.  
 What I mean here is not just having debug info and assertions enabled, but also facilities like `-debug-only=.`  
 One example from MLIR is debugging long conversion pipelines/pattern matching, when things don’t quite work the way you’d expect.

### Testing Infrastructure

Both LLVM and MLIR heavily rely on integration testing using [lit](https://llvm.org/docs/CommandGuide/lit.html) and [filecheck](https://llvm.org/docs/CommandGuide/FileCheck.html).  
 None of these are part of the “official distribution” unfortunately. While the official lit can be installed as a separate python package, for filecheck your best bet is third-party solutions, which are actually pretty good starting points if you don’t need very advanced filecheck features (e.g. [mull-project/filecheck.py](https://github.com/mull-project/filecheck.py) or [AntonLydike/filecheck](https://github.com/AntonLydike/filecheck)).

### Bleeding Edge

This is also an important factor. As a starting point, you can just use whatever is available from your default OS package manager (e.g. apt or homebrew), but at some point you may need to pick something much newer due to bugfixes or new features.

### Dynamic Linking

This is more of a niche feature, but it is very important if you are working on any kind of plugins, or if you don’t want to deal with long static linking time during development.

## Different LLVM distributions

Here I’m considering more or less cross-platform solutions, so I’m not covering Debian/Ubuntu specific [repo](https://apt.llvm.org). Which leaves us with three options: (semi-)official versions from an OS package manager, precompiled binaries (submitted by volunteers), and BYOB: “bring your own build” story.

### (Semi-)official OS packages

These are the packages maintained by the OS maintainers and not necessarily by LLVM maintainers. These packages are the easiest way to start: just call `apt/brew install llvm` and you are done.

The packages come with dynamic libraries, which enables both fast build times and plugin support. The packages usually contain everything that is needed for testing, but they of course lack the debugging story.

The other inconvenience might be the age of the package: depending on the OS and its stability guarantees, the package might be way too old for your use case.  
 For LLVM it’s probably fine, but it gets trickier for MLIR as the APIs are less stable across the recent versions.

### Precompiled packages

These packages are available as the release artifacts, for example [20.1.4](https://github.com/llvm/llvm-project/releases/tag/llvmorg-20.1.4) or [18.1.8](https://github.com/llvm/llvm-project/releases/tag/llvmorg-18.1.8).

On one hand, this is the most convenient way to get those binaries: the most recent binaries appear there just a few days after the official release.  
 On the other hand, some packages are prepared by volunteers, so some releases might be missing the build for your specific OS/version, and the presence of e.g. [LLVM-20.1.4-Linux-X64.tar.xz](https://github.com/llvm/llvm-project/releases/download/llvmorg-20.1.4/LLVM-20.1.4-Linux-X64.tar.xz) build doesn’t guarantee compatibility with e.g. Ubuntu 20.04 due to the the “old” glibc.

Just as with the official OS packages, the debugging story is not there: the packages are built in the release mode.

In general, these packages are kinda the “best effort”: if it works - great, if not - well, you are out of luck.

### Build your own LLVM

This is obviously the most flexible approach: you can build any version/commit on any supported OS, you get the debugging facilities if you wish so, all the testing infrastructure is there, it’s your choice whether to use dynamic or static linking.

But of course the price is the long build times, especially if you want to get more than just LLVM (e.g, MLIR or clang libraries).

## Summary

As a conclusion, the exact option depends on your use case.  
 Just to start with, you can pick the official package available on your OS and then decide whether you need more.

If you need the newest version, then the precompiled packages from LLVM releases page is your best bet, especially when it comes to CI integration.

However, at least at some point, you may consider building your own version of LLVM/MLIR libraries for local development, but still stick to the precompiled packages for CI checks.

To wrap it up, here is a table that sums it all up.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F670d014b-2b4f-4576-982b-a7066b2d4dcd_3268x1716.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F670d014b-2b4f-4576-982b-a7066b2d4dcd_3268x1716.png)
