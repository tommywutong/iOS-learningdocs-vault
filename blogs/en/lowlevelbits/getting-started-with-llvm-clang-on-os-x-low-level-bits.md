---
title: Getting Started With LLVM/Clang on OS X - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/getting-started-with-llvm/clang-on-os-x/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f09d1789bf2ddecd'
translated: false
---

> 原文：[Getting Started With LLVM/Clang on OS X - Low Level Bits 🇺🇦](https://lowlevelbits.org/getting-started-with-llvm/clang-on-os-x/)　·　Low Level Bits (Alex Denisov)

# Getting Started With LLVM/Clang on OS X

_Published on Dec 27, 2014_

This article is a guide how to set up development environment for Clang on OS X. The following topics are covered:

- getting sources
- setting up IDE/compiling
- debugging

_The article doesn’t cover basics of compiler construction. If you’re looking for a theory take a look at Summary section at the bottom of the page._

### Getting sources

Clang (and other projects from LLVM suite) uses SVN as a main version control system, but also provides a git mirror. Alternatively, you can use unofficial git mirror from Github, which updates every hour.

In this tutorial I use git as a VCS, but you may use an SVN without any restrictions.

To build Clang from sources you need to clone 4 projects: LLVM, Clang, compiler-rt and clang-tools-extra.

Let’s grab the latest sources:

```bash
mkdir ~/Projects/clang_dev
cd ~/Projects/clang_dev
git clone http://llvm.org/git/llvm.git
git clone http://llvm.org/git/clang.git llvm/tools/clang
git clone http://llvm.org/git/clang-tools-extra.git llvm/tools/clang/tools/extra
git clone http://llvm.org/git/compiler-rt.git llvm/projects/compiler-rt
```

You can checkout particular branch if you’re interested in a particular version (e.g. 3.4)

```bash
mkdir ~/Projects/clang_dev
cd ~/Projects/clang_dev
export BRANCH=release_34
git clone http://llvm.org/git/llvm.git -b $BRANCH
git clone http://llvm.org/git/clang.git llvm/tools/clang -b $BRANCH
git clone http://llvm.org/git/clang-tools-extra.git llvm/tools/clang/tools/extra -b $BRANCH
git clone http://llvm.org/git/compiler-rt.git llvm/projects/compiler-rt -b $BRANCH
```

From to time to time you have to update the sources if you use `HEAD`. If you don’t want to do it manually, just put the script into `clang_dev` directory:

```bash
#!/bin/env sh
root=`~/Projects/clang_dev`
cd $root/llvm && git pull origin master
cd $root/llvm/tools/clang && git pull origin master
cd $root/llvm/projects/compiler-rt && git pull origin master
cd $root/llvm/tools/clang/tools/extra && git pull origin master
```

and make it executable

```bash
chmod +x update.sh
```

### Setting up IDE and compiling

LLVM uses CMake, which supports a few build systems, such as NMake, GNU/Make, Visual Studio, Xcode, etc.

Let’s create the project for Xcode

```bash
cd ~/Projects/clang_dev
mkdir build
cd build
cmake -G Xcode CMAKE_BUILD_TYPE="Debug" ../llvm
```

open it

```bash
open LLVM.xcodeproj
```

and find something to do (it’s not about ‘make tea’, but about ‘go for a party’), indexing will take a while and, unfortunately, Xcode is almost unresponsive due to the project processing.

Well, once the project indexing is over you can build the clang.

But before, probably, you need to cleanup the list of targets/schemes.

Click on ‘ALL_BUILD’

![ALL_BUILD target](https://lowlevelbits.org/img/getting-started-with-clang/all_build_target.png)

choose ‘Manage Schemes…'

![Manage Schemes...](https://lowlevelbits.org/img/getting-started-with-clang/manage_schemes.png)

you’ll see a huge list of available targets, you don’t need most of them so feel free to hide ‘useless’ ones by unchecking ‘Show’ flag:

![Schemes](https://lowlevelbits.org/img/getting-started-with-clang/schemes.png)

If we just build and run clang, then it’ll do nothing, let’s add some parameters, for instance, print version.

Select `Edit scheme`:

![Edit scheme](https://lowlevelbits.org/img/getting-started-with-clang/edit_scheme.png)

and add `-v` to the `Arguments passed on launch`:

![Version arguments](https://lowlevelbits.org/img/getting-started-with-clang/version_arguments.png)

That’s pretty much it, just hit `Cmd + R` and it’ll build clang and run built binary with a specified parameter.

When build done (it also takes a while) and program executed you’ll see the clang version in the Xcode output window

![Clang version](https://lowlevelbits.org/img/getting-started-with-clang/clang_version.png)

### Debugging

Clang is a big project therefore debugging without a decent GUI tool is not an easy task. Fortunately, we have Xcode.

In this example we’re going to debug a parser and semantic analysis phase of clang.

Create a file `/tmp/sum.c` which contains the following code:

```c
int sum(int a, int b) {
     return a + b;
}
```

and specify the file as an argument for a clang binary, with additional parameters:

![Debug arguments](https://lowlevelbits.org/img/getting-started-with-clang/debug_arguments.png)

`clang` executable itself is just a driver, which determines what to do next with all received parameters. By default it calls ‘clang compiler’ and passes the parameters, but it calls it as a separate process, so it’s hard to debug in a traditional way. By specifying `-cc1` option it calls compiler directly, in the same process.

Since we aren’t going to compile the source, but only make semantic analysis, we can add `-fsyntax-only` argument.

Let’s start debugging.

Find a `ParseExpr.cpp`, set a breakpoint at the `ParseExpression` method:

![Breakpoint](https://lowlevelbits.org/img/getting-started-with-clang/breakpoint.png)

and run. When program reach this breakpoint you can retrieve some useful information.

Most of LLVM’ classes have method `dump` which prints all valuable information about an object. You can easily access it by evaluating LLDB command `expression` (or simply `expr`):

![Dump](https://lowlevelbits.org/img/getting-started-with-clang/dump.png)

Here you see an AST representation of the addition expression from a `sum` method: `a + b`.

### Summary

As you can see this article is not a comprehensive guide, but only a very small instruction set, which might be helpful if you just started playing with compiler internals and want to try to touch them.

If you’re looking for a more theoretical and practical information I’d recommend to read the following articles:

- The Architecture of Open Source Applications: LLVM

  by

  Chris Lattner
- objc.io #6. The Compiler

  by

  Chris Eidhof

**Stay tuned if you interested how-to write tests for Clang and LLVM.**

**Happy hacking!**
