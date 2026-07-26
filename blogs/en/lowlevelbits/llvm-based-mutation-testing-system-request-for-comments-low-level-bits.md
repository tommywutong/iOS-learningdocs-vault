---
title: LLVM-based Mutation Testing System. Request For Comments - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/llvm-based-mutation-testing-system.-request-for-comments/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ccf2ccc5aef20151'
translated: false
---

> 原文：[LLVM-based Mutation Testing System. Request For Comments - Low Level Bits 🇺🇦](https://lowlevelbits.org/llvm-based-mutation-testing-system.-request-for-comments/)　·　Low Level Bits (Alex Denisov)

# LLVM-based Mutation Testing System. Request For Comments

_Published on Apr 14, 2016_

Several years ago I discovered very powerful technique - [Mutation Testing](https://en.wikipedia.org/wiki/Mutation_testing). Since then I was (and still am) dreaming to have a tool which will do the job for languages like C, Objective-C and C++.

Now I have confidence in that it can be implemented using LLVM.

Outline for this article:

- overview of mutation testing
- mutation testing system - proof of concept
- thoughts on potential implementation of MT system using LLVM

#### Acknowledgements

I want to say ’thanks’ explicitly to [Markus Schirp](https://github.com/mbj) and [Henry Coles](https://github.com/hcoles) for their work on [Mutant](https://github.com/mbj/mutant) and [Pitest](https://github.com/hcoles/pitest) and hints they gave me several years ago.

Also, I want to say ’thanks’ to all the people involved into development of LLVM.

### Mutation Testing in a nutshell

There is a strong belief that code coverage is a meaningful metric. That is incorrect.

Obviously, if code coverage is 0% then you have some problems. On the other hand having 100% code coverage means literally nothing.

Consider the following situation: you have a test case which covers implementation of a function `sum`. You may assume that sum of two positive numbers will result in a positive number, which is greater than 0.

Here is the test:

```c
test_result test_sum() {
  int result = sum(9, 5);
  if (result > 0) {
    return success;
  }

  return fail;
}
```

Implementation of the `sum` function is rather simple. But, since you missed your morning coffee you write a wrong operator there:

```c
int sum(int a, int b) {
  return a * b;
}
```

You run the tests - everything is working.

You check code coverage - oh wow, 100%.

You didn’t spot the problem because you trust your tests. And because you rely on code coverage. Neither of these is acceptable.

This situation raises very valid question - **who tests the tests?**

One of the answers is Mutation Testing.

The idea is that MT system generates lots of variations of a program under test (in this case function `sum`) which are slightly different from original program. Then the system evaluates test against each mutant and check the result. If test failed, then mutant is killed, otherwise - it is survived.

Ideally all mutants should be killed. Only then you can claim that your tests are valid and correct.

Here is one potential mutation:

```diff
 int sum(int a, int b) {
-  return a * b;
+  return a + b;
 }
```

Multiplication was replaced by addition. In fact the implementation is correct now, but the test will not fail, since condition `sum(9, 5) > 0` still holds.

This survived mutant should give a hint to developer that something is wrong.

### Proof of Concept

**I do claim that such a system can be built on top of LLVM using LLVM IR/bitcode, JIT and [ponies](https://lh6.googleusercontent.com/hY5_U3eO3lPP2fhwcZgCFHC9IpOomMR1YIXz4kDML1hpliTNmaZ5DLrTzyKq9RMAMIYwPocbSkzGiRSUrVzwpyHeSBxVDbR3MHK41bHiE7feidNeUOXqPrwfv1ZNb2tEWPR4msan).**

So far I have managed to create a proof of concept which obviously lacks tons of features and skips lots of real problems.

Code is available [here](https://github.com/AlexDenisov/mutation-testing-poc).

_It is not intended to be runnable on your machine, since it uses ‘slightly forked’ LLVM with couple of functions that were ‘missing’._

So far it does very little:

- loads LLVM IR from bitcode files into memory
- finds first test function
- finds a function (testee) used from test function
- replaces first occurrence of ‘+’ with ‘-’
- prints diff (using libgit2) between original and mutated function
- runs test against original function and mutated function
- compares test results, assuming mutant is killed when results are different

I guess it doesn’t look impressive and mind-blowing. However, this proof of concept inspires me to start working on a real system, despite that it will take enormous amount of time since (almost) all this work I do in my spare time.

### Next Steps

The next step actually is to start implementing the system that can be used in production.

Below you can see a high level overview of an algorithm I have in my head. It is a swift-like pseudocode. Please, follow the comments!

```swift
/*

    Classes used within the algorithm

*/

/* Basic instruction, e.g. a + b */
class Instruction {

}

/* Represents set of istructions in a single scope, e.g. if/else branch */
class BasicBlock {
  let instructions : [Instruction]
}

/* Function is a function, that's it */
class Function {
  let basicBlocks : [BasicBlock]
}

/* Representation of a source file */
class Module {
  let functions : [Function]
}

/* Shows instruction that needs to be mutated */
class MutationPoint {
  let instruction : Instruction
  let basicBlock : BasicBlock
  let function : Function
  let module : Module
}

/*

    Algorithm

*/

/* Load all files into memory */
let modules = loadProgramModules()

/*

    Find all functions that represent test

    'testFinder' is an abstraction intended to hide language/framework specific logic.
    Example classes are 'CPP_GTest_TestFinder', 'ObjC_XCTest_TestFinder',
    'ObjC_Cedar_TestFinder' and so on.

*/
let tests = testFinder.findAllTests(modules)

for test in tests {
  /*
      For each test we need to find a set of functions that can be mutated in some way
  */
  let testeeFunctions = mutationFinder.findAllTesteeFunctions(test)
    for testee in testeeFunctions {
    /*
        For each testee we do the following:

        Testee belongs to a module, we need to make two copies of this module:
        one copy will contain only testee (moduleWithOriginal)
        another one will contain all functions but testee (moduleWithoutTesteeFunction)

        Having this split we can mutate function inside of 'moduleWithOriginal'
        without affecting and recompiling potentially big module
    */

    let moduleWithOriginal = copyOfModuleWithOnlyFunction(testee.module, testee)
    let moduleWithoutTesteeFunction = copyOfModuleWithoutFunction(testee.module, testee)

    /*

        Now we can create JIT engine using all modules, excluding the module of testee.
        In fact the latter one if replaced by 'moduleWithoutTesteeFunction'

    */

    let modulesWithoutTesteeModule = modules.without(testee.module)
    var executionEngine = executionEngineWithModules(modulesWithoutTesteeModule)
    executionEngine.addModule(moduleWithoutTesteeFunction)

    /*

        Having JIT engine in place we can run the test against original implementation of testee

    */

    executionEngine.addModule(moduleWithOriginal)
    let originalResult = executionEngine.runTest(test)
    executionEngine.removeModule(moduleWithOriginal)

    /*

        Now we need to find all places where we can apply mutation

    */

    let mutationPoints = mutationFinder.findAllMutationPoints(functino)
    for point in mutationPoints {
        /*

            And for each such place we are getting copy of 'moduleWithOriginal'
            within applied mutation

        */

        let moduleWithMutation = applyMutationOnModule(point, moduleWithOriginal)

        /*

            Now we run the test against the mutant

        */

        executionEngine.addModule(moduleWithMutation)
        let mutationResult = executionEngine.runTest(test)
        executionEngine.removeModule(moduleWithMutation)

        /*

            And finally compare results

        */

        analyzeResults(originalResult, mutationResult)
    }
  }
}
```

As you can see the starting point here is a bitcode, which means the system is language agnostic.

However this approach has it’s own drawbacks - bitcode should contain debug information so that IR can be mapped back to high level code, which is not always the case with heavily optimized code.

Being able to re-run test just by replacing a module with mutated function gives an ability to increase performance drastically. However, execution may interrupt because of signal (segfault, bad access, etc.) or it may go into an infiinte loop. To fix those problems there might be a need to run each mutant as a separate process.

Besides that there are quite a few open questions such as:

- how to get bitcode for each translation unit (source file) automatically
- how to compare test results of original and mutated program for different testing frameworks
- how to deal with tests that are touching OS resources such as file system, I/O, etc

Obviously, there are many more questions and problems that I’m not aware of yet.

### Conclusion

LLVM gives us an ability to build a powerful, language and framework agnostic system for Mutation Testing.

I want to use this ability to build this tool and to get as much fun as possible.

Besides motivating myself by making this public commitment, this blog post has two other goals:

- get comments from people who are heavily involved in LLVM and/or mutation testing systems development
- to attract people who may be willing to join the project when I have something to show

If you have something to add or want to share your knowledge or concerns - please do it.
