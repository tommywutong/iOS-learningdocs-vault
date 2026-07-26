---
title: How to use LLVM API with Swift. Addendum - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/how-to-use-llvm-api-with-swift.-addendum/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:777e3a89bc2aa5cc'
translated: false
---

> 原文：[How to use LLVM API with Swift. Addendum - Low Level Bits 🇺🇦](https://lowlevelbits.org/how-to-use-llvm-api-with-swift.-addendum/)　·　Low Level Bits (Alex Denisov)

# How to use LLVM API with Swift. Addendum

_Published on Jan 27, 2016_

In the [previous article](https://lowlevelbits.org/how-to-use-llvm-api-with-swift/) I showed how to use LLVM with Swift.

That time I didn’t set up JIT engine properly. Few days later I dived a bit deeper and finally managed to run the program using [MCJIT](http://llvm.org/docs/MCJITDesignAndImplementation.html) - new LLVM JIT engine, where ‘MC’ states for ‘machine code’. This engine is different from ‘classical’ JIT, but this is out of scope of this article. For more information please consider looking at documentation.

### MCJIT Execution Engine

Here is the snippet used to create interpreter:

```swift
let engine = UnsafeMutablePointer<LLVMExecutionEngineRef>.alloc(alignof(LLVMExecutionEngineRef))
var error =  UnsafeMutablePointer<UnsafeMutablePointer<Int8>>.alloc(alignof(UnsafeMutablePointer<Int8>))

LLVMLinkInInterpreter()

if LLVMCreateInterpreterForModule(engine, module, error) != 0 {
  print("can't initialize engine: \(String.fromCString(error.memory)!)")
  // TODO: cleanup all allocated memory ;)
  exit(1)
}
```

In this snippet the type of execution engine specified explicitly, though it could be more general.

It is possible to use function `LLVMCreateExecutionEngineForModule`. The exact engine type will be specified by family of function `LLVMLinkInEETYPE`, where `EETYPE` is an execution engine type, one of `Interpreter`, `MCJIT`, and `OrcMCJITReplacement`.

Since `MCJIT` is intended to generate machine code for some specific machine, we should also define which machine to use, e.g.: x86, x64, arm, and so on.

For the sake of simplicity we will generate the code for the host machine. In this case we don’t even have to now which CPU family we have. LLVM provides very useful shortcut, we could use `Native` when refer to a host machine.

`MCJIT` requires only information about a target and code generator for this specific target.

Here is final snippet for the execution engine:

```swift
LLVMLinkInMCJIT()
LLVMInitializeNativeTarget()
LLVMInitializeNativeAsmPrinter()

let engine = UnsafeMutablePointer<LLVMExecutionEngineRef>.alloc(alignof(LLVMExecutionEngineRef))
var error =  UnsafeMutablePointer<UnsafeMutablePointer<Int8>>.alloc(alignof(UnsafeMutablePointer<Int8>))

LLVMLinkInInterpreter()

if LLVMCreateExecutionEngineForModule(engine, module, error) != 0 {
  print("can't initialize engine: \(String.fromCString(error.memory)!)")
  // TODO: cleanup all allocated memory ;)
  exit(1)
}
```

### Function `main`

There is a small problem with `MCJIT`. Currently it can only run functions with signatures matching signatures of `main` C function, i.e. one of those:

```c
(int argc, char **argv, const char **envp)
(int argc, char **argv)
(int argc)
()
```

Return type of the function is also limited: only `int`. `double`, `float`, `void` and a pointer to something.

So how to call function with signature `(int a, int b)` and return type `int`?

The solution is simple: we just need to create a new function with return type `int` and without parameters. Then we could put call to the `sum` function into the body of our pseudo-main function.

Here is how it may look:

_Note: I put it into a function just to specify some scope_

_Note2: I do not cleanup memory in this snippet just to save some space_

```swift
func runFunction(a: Int, _ b: Int) -> Int {
  let functionType = LLVMFunctionType(returnType, nil, 0, 0)
  let wrapperFunction = LLVMAddFunction(module, "", functionType)

  let entryBlock = LLVMAppendBasicBlock(wrapperFunction, "entry")

  let builder = LLVMCreateBuilder()
  LLVMPositionBuilderAtEnd(builder, entryBlock)

  let argumentsCount = 2
  var argumentValues = [LLVMValueRef]()

  argumentValues.append(LLVMConstInt(int32, UInt64(a), 0))
  argumentValues.append(LLVMConstInt(int32, UInt64(b), 0))

  let argumentsPointer = UnsafeMutablePointer<LLVMValueRef>.alloc(strideof(LLVMValueRef) * argumentsCount)
  argumentsPointer.initializeFrom(argumentValues)

  let callTemp = LLVMBuildCall(builder,
                               sumFunction,
                               argumentsPointer,
                               UInt32(argumentsCount), "sum_temp")
  LLVMBuildRet(builder, callTemp)

  return 0
}

runFunction(5, 6)
```

Here is an output after executing this code:

```llvm
; ModuleID = 'Hello'

define i32 @sum(i32, i32) {
entry:
  %temp = add i32 %0, %1
  ret i32 %temp
}

define i32 @0() {
entry:
  %sum_temp = call i32 @sum(i32 5, i32 6)
  ret i32 %sum_temp
}
```

Our unnamed wrapper function has name `@0`. Since this function is just a helper we will need to remove it after we have done execution.

The way to run the function is the same as it was using interpreter:

```swift
func runFunction(a: Int, _ b: Int) -> Int {
  /// ...

  let executionEngine = UnsafeMutablePointer<LLVMExecutionEngineRef>.alloc(strideof(LLVMExecutionEngineRef))
  let error = UnsafeMutablePointer<UnsafeMutablePointer<Int8>>.alloc(strideof(UnsafeMutablePointer<Int8>))

  defer {
    error.dealloc(strideof(UnsafeMutablePointer<Int8>))
    executionEngine.dealloc(strideof(LLVMExecutionEngineRef))
  }

  let res = LLVMCreateExecutionEngineForModule(executionEngine, module, error)
  if res != 0 {
    let msg = String.fromCString(error.memory)
    print("\(msg)")
    exit(1)
  }

  let value = LLVMRunFunction(executionEngine.memory, wrapperFunction, 0, nil)
  let result = LLVMGenericValueToInt(value, 0)

  LLVMDeleteFunction(wrapperFunction)

  return Int(result)
}

print("\(runFunction(5, 6))")
print("\(runFunction(7, 142))")
print("\(runFunction(557, 1024))")
```

If we run this code we will actually see the result:

```
> ./hello_llvm
11
149
1581
```

### That’s it

I have updated the repository so you can look at it to see the whole code for the article:

[https://github.com/AlexDenisov/swift_llvm](https://github.com/AlexDenisov/swift_llvm)

Besides that, if you want to learn more about using LLVM with Swift and to see more practical examples, then I can recommend looking at LLVM’s [Kaleidoscope](http://llvm.org/docs/tutorial/index.html) implemented in Swift: [SwiftKaleidoscope](https://github.com/AlexDenisov/SwiftKaleidoscope)
