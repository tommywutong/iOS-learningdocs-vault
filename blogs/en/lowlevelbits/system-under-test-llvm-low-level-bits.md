---
title: 'System Under Test: LLVM - Low Level Bits 🇺🇦'
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/system-under-test-llvm/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:23d4349ef0d3f0e8'
translated: false
---

> 原文：[System Under Test: LLVM - Low Level Bits 🇺🇦](https://lowlevelbits.org/system-under-test-llvm/)　·　Low Level Bits (Alex Denisov)

# System Under Test: LLVM

_Published on Mar 24, 2016_

**UPD:** The series of blog-posts “System Under Test” became a full-fledged project and has moved to its own [domain](http://systemundertest.org). The most recent version of this article lives [here](http://systemundertest.org/llvm) now.

This article is part of series [“System Under Test”](https://lowlevelbits.org/system-under-test). It provides an overview of the test suites that are used by LLVM project to maintain a quality of its libraries and tools on a high level.

### What is LLVM about?

[http://llvm.org](http://llvm.org) says that

> The LLVM Project is a collection of modular and reusable compiler and toolchain technologies.

It is not that much I can add here besides one link:

[The Architecture of Open Source Applications: LLVM](http://aosabook.org/en/llvm.html) by Chris Lattner.

which sheds light on compilers in general and LLVM particularly.

LLVM is rather an umbrella project than a single project. It consists of compiler, debugger, linker, assemblers for several CPUs and of the most important - its Core: back-end and middle-end.

In this article I refer to LLVM as a back-end + middle-end, rather than the whole umbrella (that would be too much for one post).

### Tests

LLVM is a huge project. Therefore it has quite a few groups of tests: unit tests, regression tests, performance tracking and fuzzing tests. Since the project is not trivial the tools used for testing are mostly written from scratch and are part of LLVM project. Though, I wish I could use some of them without having LLVM as their dependency.

#### Unit Tests

Amount of unit tests is pretty small comparing to regression tests. One reason behind that decision is that LLVM internals constantly change all the time. Supporting tests under such conditions is very time consuming. However there are still parts that do not change very often, that is they are good target for unit testing. These tests are located in ‘unittests’ directory.

They can be run using `make`:

```sh
make check-llvm-unit
```

Showing this beautiful output:

![Unit tests](https://lowlevelbits.org/img/sut_llvm/unit_tests.png)

As you can see there are about 1,5k tests, and that leads to a pretty short execution time: ~30 seconds using 4 threads.

Unit Tests are written using [Google Test](https://github.com/google/googletest) framework. Here is an example of a simple test:

```cpp
// unittests/Support/YAMLParserTest.cpp
TEST(YAMLParser, SameNodeIteratorOperatorNotEquals) {
  SourceMgr SM;
  yaml::Stream Stream("[\"1\", \"2\"]", SM);

  yaml::SequenceNode *Node = dyn_cast<yaml::SequenceNode>(
                                              Stream.begin()->getRoot());

  auto Begin = Node->begin();
  auto End = Node->end();

  EXPECT_TRUE(Begin != End);
  EXPECT_FALSE(Begin != Begin);
  EXPECT_FALSE(End != End);
}
```

Pretty trivial. Let’s move forward and look at another, more interesting group of tests.

#### Regression Tests

The aim of this test suite is to verify the output of different tools, hence the internals can change separately from tests, making support less time-consuming. This test suite located in `test` directory. It is the largest group of tests used in LLVM. It is 10 times bigger than Unit Tests: ~15k vs ~1,5k. It takes about 4 minutes to run on my machine using 4 threads.

```sh
make check-llvm
```

The output is pretty similar to one above:

![Regression tests](https://lowlevelbits.org/img/sut_llvm/regression_tests.png)

Regression Tests (unlike Unit Tests) are using custom tools such as [lit (LLVM Integrated Tester)](http://llvm.org/docs/CommandGuide/lit.html) and [FileCheck](http://llvm.org/docs/CommandGuide/FileCheck.html). Let’s look at simple test to illustrate how it works:

```llvm
; RUN: %lli %s | FileCheck %s

@flt = internal global float 12.0e+0
@str = internal constant [18 x i8] c"Double value: %f\0A\00"

declare i32 @printf(i8* nocapture, ...) nounwind
declare i32 @fflush(i8*) nounwind

define i32 @main() {
  %flt = load float, float* @flt
  %float2 = frem float %flt, 5.0
  %double1 = fpext float %float2 to double
  call i32 (i8*, ...) @printf(i8* getelementptr ([18 x i8], [18 x i8]* @str, i32 0, i64 0), double %double1)
  call i32 @fflush(i8* null)
  ret i32 0
}

; CHECK: Double value: 2.0
```

This test can be split into three parts:

Run command (the top line):

```llvm
; RUN: %lli %s | FileCheck %s
```

Expectations (the bottom line):

```llvm
; CHECK: Double value: 2.0
```

The rest (LLVM IR in the middle) is the body.

All tests in this suite have one or more ‘run’ command. `lit` uses set of rules to substitute the string into real runnable command. Substitutions are either built-in (such as `%s`) or configurable (such as `%lli`). `lit` replaces `%s` with the full path to a file under test, e.g.:

```
~/llvm/test/ExecutionEngine/frem.ll
```

Configurable substitutions however are taken from `lit.cfg` file, which is basically a Python script.

For example, this config says that `%lli` is to be replaced with `/usr/local/bin/lli`

```python
lli = '/usr/local/bin/lli'
config.substitutions.append( ('%lli', lli ) )
```

Having these parameters in place `lit` will run the test using this command:

```sh
/usr/local/bin/lli ~/llvm/test/ExecutionEngine/frem.ll | FileCheck ~/llvm/test/ExecutionEngine/frem.ll
```

Which will interpret `frem.ll` using LLVM Interpreter (`lli`) and pass the output to the `FileCheck`. `FileCheck` in turn takes two arguments: filename with expectations and input that needs to be examined.

Summary of this example:

The test interprets the body (LLVM IR) from `~/llvm/test/ExecutionEngine/frem.ll` using LLVM Interpreter (`%lli` aka `/usr/local/bin/lli`) and checks if the output of interpretation contains string `Double value: 2.0`.

Both `lit` and `FileCheck` have lots of useful options. Consider looking at documentation to learn more.

_**upd 22.06.16:**_ As Daniel Dunbar [mentioned](https://twitter.com/daniel_dunbar/status/745285660626452480) it possible to use `lit` without LLVM, simply by installing it using `pip`: `pip install lit`

#### Performance tracking

Performance is one of the most important goals of any software. LLVM is not an exception.

Here LLVM also uses custom tool - [LNT](http://llvm.org/docs/lnt/intro.html). This tool was initially written to be used inside LLVM, but its design allows it to be usable for performance testing of any other software.

[Performance tests suite](http://llvm.org/docs/TestingGuide.html#test-suite-overview) is not a part of LLVM source tree. It has to be fetched separately. It is a set of programs that are compiled and executed to track performance changes.

Besides `LNT` the test suite can be used within CMake as described in [LLVM test-suite Guide](http://llvm.org/docs/TestSuiteMakefileGuide.html)

At the moment of writing this article external test suite contains 485 test cases. It takes ~5 minutes to run them using `lit`.

#### Fuzz Testing

Another powerful technique used to increase quality of LLVM is [Fuzz Testing](https://en.wikipedia.org/wiki/Fuzz_testing).

Here as well LLVM has its own tool called [LibFuzzer](http://llvm.org/docs/LibFuzzer.html). The tool is so great that it is also used by [other software](http://llvm.org/docs/LibFuzzer.html#trophies) such as Python, PCRE, OpenSSL, SQLite, and other.

Here is an example of a fuzz test:

```c
// tools/llvm-as-fuzzer/llvm-as-fuzzer.cpp
extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {

  // Allocate space for locals before setjmp so that memory can be collected
  // if parse exits prematurely (via longjmp).
  StringRef Input((const char *)Data, Size);
  // Note: We need to create a buffer to add a null terminator to the
  // end of the input string. The parser assumes that the string
  // parsed is always null terminated.
  std::unique_ptr<MemoryBuffer> MemBuf = MemoryBuffer::getMemBufferCopy(Input);
  SMDiagnostic Err;
  LLVMContext &Context = getGlobalContext();
  std::unique_ptr<Module> M;

  if (setjmp(JmpBuf))
    // If reached, we have returned with non-zero status, so exit.
    return 0;

  // TODO(kschimpf) Write a main to do this initialization.
  if (!InstalledHandler) {
    llvm::install_fatal_error_handler(::MyFatalErrorHandler, nullptr);
    InstalledHandler = true;
  }

  M = parseAssembly(MemBuf->getMemBufferRef(), Err, Context);

  if (!M.get())
    return 0;

  verifyModule(*M.get());
  return 0;
}
```

`LibFuzzer` generates huge amount of different inputs using [Genetic programming](https://en.wikipedia.org/wiki/Genetic_programming) and calls `LLVMFuzzerTestOneInput` within each input. This test then tries to parse the input as an assembly. The parser should not crash.

At the moment there are two targets for fuzz testing within LLVM source tree: `llvm-as-fuzzer` and `llvm-mc-fuzzer`. They are located in `tools` directory.

### Summary

LLVM uses a few test suites for different needs. There are ~1,5k Unit Tests, ~15k Regression Tests. It takes ~4-5 minutes to run both tests in Debug mode on 2 y/o MacBook Pro using 4 threads.

LLVM uses Fuzzing Tests to prevent system from abnormal exit when erroneous input received.

LLVM has out-of-source-tree test-suite for performance tracking.

LLVM mostly uses custom tools for testing.

### Further Reading / Additional Material

- LLVM Testing Infrastructure Guide
- LLVM Integrated Tester
- FileCheck
- LibFuzzer
- LLVM test-suite Guide
- LNT Quickstart Guide
