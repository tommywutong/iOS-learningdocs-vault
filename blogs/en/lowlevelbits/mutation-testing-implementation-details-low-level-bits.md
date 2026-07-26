---
title: 'Mutation Testing: implementation details - Low Level Bits 🇺🇦'
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/mutation-testing-implementation-details/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:87856ee946dc5d1b'
translated: false
---

> 原文：[Mutation Testing: implementation details - Low Level Bits 🇺🇦](https://lowlevelbits.org/mutation-testing-implementation-details/)　·　Low Level Bits (Alex Denisov)

# Mutation Testing: implementation details

_Published on Jun 14, 2017_

Last week we had a discussion with guys who want to build a mutation testing system for .NET. If you want to join, please talk to them here: [https://gitter.im/dot-NET-mutation-testing/Lobby](https://gitter.im/dot-NET-mutation-testing/Lobby)

Few people already shared their experience in a written form: [https://gist.github.com/hcoles/36bd67d8927a205c480576f4632f9289](https://gist.github.com/hcoles/36bd67d8927a205c480576f4632f9289) [https://gist.github.com/jameswiseman76/7400896ab2f0eb6ecf33c414173e995d](https://gist.github.com/jameswiseman76/7400896ab2f0eb6ecf33c414173e995d)

I decided to do the same. I tried to organize my thoughts nicely but failed miserably. Sorry for that.

_Note: I am writing about our tool [Mull](https://github.com/mull-project/mull)._

## AST vs. Bitcode

Mutations can be done either at a high level (source code) or a lower level (bitcode). We decided to pick the latter one. The main reason: we could bring mutation testing for any LLVM-based language. Later we learned that this approach has significant advantages but also serious disadvantages.

I will outline them below.

### Cons

#### Build Tools

So far we tried to add support for five languages: C, C++, Objective-C, Rust, and Swift.

To make it work, we must compile source code into bitcode. It is super straightforward if you want to compile one file: each compiler has an option to emit LLVM bitcode. However, it is a pain when it comes to a real-world project where you normally have many files. Rust and Swift both have some standard way of building things, despite that there is no option to emit bitcode for the whole project (I will talk about LTO later). As for C family, there is the whole zoo of build tools: shell scripts, makefiles, ninja, CMakeLists, Visual Studio, Xcode, etc.

We had to make some workarounds to overcome these problems. Fortunately, we found a semi-elegant way of handling this at least for C and C++ (should work for Swift and Rust as well though). We could use Link-Time Optimization, this way compiler would produce not object files, but files that contain bitcode. It works perfectly on OS X, but I see a problem on Linux: for some reason, linker (`ld.gold`) could not link bitcode files together which make build system to fail. To avoid this problem, we had to ask ninja to fail only after 1000 errors (`ninja -k 1000`).

#### Mapping bitcode back to source code

First I thought that it would be a trivial task since everything in the original code should have a corresponding instruction in the bitcode. But, for instance, this line of C++ code:

```c++
some_vector.push_back(make_pair(foo, bar));
```

Will be expanded into several hundred (!) of instructions, if one of those instructions crashes than a good IDE should show a corresponding line of code. Hence, all those hundreds of instructions are mapped to the same place in the original code. Another problem that all the following pieces of code have the same representation on the IR level:

```c
x +  1 // sadd %x,  1
x -  1 // sadd %x, -1
x += 1 // sadd %x,  1
x++    // sadd %x,  1
```

Another problem: syntactic sugar. For instance:

```c
a = b + c;
```

If `b` and `c` are simple types, then this is an addition, but, if these are objects then this a function call. An end user might be a bit confused why some function related mutation was applied at the addition.

#### Applying mutations

The first naive approach was to iterate over instructions and check whether we can apply mutation on this instruction or not. If we can apply a mutation, then we just replace this instruction (or remove it) with another. This approach generates lots of junk mutations (c) @hcoles. Now we learned that looking at single instruction is not enough: we must look at patterns and instructions around. Simple addition in C compiles into a single instruction, while in Rust we get several of them: one for addition, one for overflow check, one to report an error if it overflows, and so on. We may end up having several implementations of the same mutation: one for C/C++, one for Rust, etc.

### Pros

#### Build Tools

As far as I know, the AST of Clang is not designed to be mutable. Even though it has a thing called AST Rewriters, it might be super slow since a rewriter outputs rewritten AST on disk. Taking this into account mutation on the bitcode level is a reasonable solution, especially given that everything is happening in memory. We didn’t investigate whether ASTs of Rust or Swift are mutable or not, but this is not required since current approach is language agnostic.

#### Applying mutations

Mutations are very similar at the bitcode level. We don’t have to replicate each compiler to make a mutation and to build the source code into executable code - everything is covered by LLVM. This process is quite fast since everything is happening in memory and we have a common ground for any language: we feed JIT engine with bitcode (original or mutated) and ask it to run the program, no I/O involved.

## Program Execution

One of the biggest advantages is that the algorithm for program execution is the same for each language/test framework. Below I describe the algorithm using pseudo code

```swift
struct Result {
  let status   // failed, passed, timed out, etc
  let duration // how much time it took to run a program
}

struct MutationPoint {
  let module    // where the mutation is located
  let metadata  // some utility data
}

/// we give N seconds for original test to complete
let Timeout = N

/// Program under test is represented as a
/// set of bitcode modules
let modules = loadModules()

/// First we find tests. Each language + test framework
/// has custom implementation of a Test Finder
let tests = findTests(modules)

for test in tests {
  /// Then for each test we find places where we can
  /// apply mutation - Mutation Point
  /// Each language may have it's own set of Mutation Operators
  let mutationPoints = findMutationPoints(test, modules)

  /// Given we know what we want to mutate
  /// We can start execution of each mutant
  let originalResult = runTest(test, modules, Timeout)
  if originalResult != Passed {
    /// Report an error and skip this test
    /// One could also fail early, but we decided not to
  }

  /// Now it's time to run a test against each mutant
  for point in mutationPoints {
    /// Mutant is a copy of original module
    /// within the mutation
    let mutant = applyMutation(point)

    /// To run the test against mutant we need
    /// to replace the original module in the
    /// set of modules
    let mutatedModules = modules.replace(point.module, mutant)

    /// Mutant should not take X times more time than
    /// the original test
    /// Otherwise we consider it as a timed out
    let timeout = originalResult * X
    let mutationResult = runTest(test, mutatedModules, timeout)
    /// The mutationResult can be now reported
    /// We are done here, taking the next mutant
  }
}
```

It is important to notice that each test run is done in a child process because mutation could lead to crash or an infinite loop.

The current implementation of the scheduling is not elegant and not efficient. We fork a process (watchdog), the watchdog forks two other processes: timer and worker. The timer does nothing but sleeps for N milliseconds. The worker executes the test or mutant. The watchdog is waiting for either process to finish. If the timer finishes first, then the worker timed out, we kill it and report timeout. If the worker stops first, then we terminate the timer and proceed. To report the result, we must check whether the worker process crashed, and if not what is the exit status.

Besides that, it is important to be able to get the output (stdout/stderr) from the worker process.

We would need to come up with another solution that would allow us to parallelize the execution efficiently.

There are few things that I omit in the algorithm, but I will cover them in the next section.

## Optimizations

No matter how fast machine is, the execution may take a lot of time. The algorithm itself is not optimal and could be improved. But there are few places where you could put some levers to control the number of mutations. First place is `findTests`: you could configure a program to run the only subset of tests. It is very convenient during analysis of a program under test. Another place is `findMutationPoints`. Currently, our approach here is different from the one Pitest has. We do not use code coverage to find places where to add mutations. Instead, we use static analysis to build a call graph. For example:

```c
void test_foo() {
  assert(foo() == 5);
}

int foo() {
  /// ...
  return bar();
}

int bar() {
   /// ...
   return buzz();
}

int buzz() {
  /// ...
  return x;
}
```

Here we have the following call ‘graph’:

```
test_foo -> foo -> bar -> buzz
```

If we look at this list from left to right, then we might see that each function is at some distance from the test. Using this information we can ask the system to not look for mutation points farther than two hops from a test. By using these two filters, you can significantly improve feedback time.

Another trick we did: we have an option called ‘Dry Run.’ In this mode, the system does whatever it normally does, except that it doesn’t apply any mutations and it doesn’t run the mutants. Instead, it reports each mutation result status as DryRun, including its distance from a test and estimated duration as it’s timeout. Using this information you could decide which distance is optimal for this very particular project. We also found it useful to run as a first on an unknown project, just to get understanding what kind of a beast we are working with.

**UPD:** re: static analysis:

We decided to go this way because it felt like a good solution. However, it turned out that we cannot build the call graph reliably: a function (caller) instead of calling another function (callee) directly could pass a pointer to the callee to some other function, which would then call the callee indirectly via a pointer. Another example: polymorphism. Just recently we found that we cannot find a call to a polymorphic function. However, we did not try to solve this problem yet.

It is very likely that we would need to switch to another solution.

We could determine the call tree by using Compiler On Demand (COD) capability of LLVM’s JIT engine. The idea is the following: the system asks JIT to execute a function from a module, when the JIT hits unresolved function it calls back the system asking to resolve the function. At this callback, we can register the unresolved function as part of the call tree and then resolve the function the function and give it back to the JIT engine. I am going to investigate if this approach is working, but there is another problem: this way we could get a set of all called functions, but seems like we cannot build the actual tree and can’t measure the distance (unless the callback provides the caller function).

## Reporting

Reporting is one of the trickiest parts, in my opinion. We are still trying to find a nice way to present results to an end user. So far we come up with the following solution.

At the very end of execution, the system spits out SQLite file with information about mutations points, tests, execution results, and so on.

Next, one could feed this SQLite file into our [reporter](https://github.com/mull-project/mull-reporter-sqlite), that would generate nice HTML page like [this one](https://lowlevelbits.org/IRTests/)(Warning: Heavy page!).

Having an SQLite file is very handy: we could do different analysis of the same program without restarting potentially long running process.

## Nearest Plans

- add more test frameworks for C++
- optimize algorithms to speed up the system
- find a nice way to present reports
- add more mutation operators
- ~~add Linux support~~ done!

## That’s it

Feel free to ask questions. There are must be many things I missed about the topic.
