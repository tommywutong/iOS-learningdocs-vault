---
title: 'Tracking tasks with stack traces in Swift | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/02/28/stack-traces-in-swift.html'
original_language: en
published: 2016-02-28
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:594cce39a87205e6'
translated: false
---

> 原文：[Tracking tasks with stack traces in Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/02/28/stack-traces-in-swift.html)　·　Cocoa with Love (Matt Gallagher)

Debugging tasks with complex or asynchronous control flow can be difficult since it renders useless one of the most important debugging tools we have: the debugger stack trace. To overcome this, we can have our tasks capture their own stack traces in debug builds to aid debugging by reconstructing the path that long-running task objects take through the program.

This article will also share my own custom code for creating and symbolicating stack traces that’s a little faster and more flexible than the existing code for doing this in Swift.

## Introduction

One of the best ways to analyze a program for the source of an error is a debugger stack trace.

Imagine we create a task object in function (1), then we pass the task object into another function (2), which then passes the task object into a third function (3) which represents the end of the task. In this example, path the object takes through the program and the call stack are the same thing:

![a linear, three node graph](https://www.cocoawithlove.com/assets/blog/three_node_graph.svg)

If, by the end of function (3), we don’t have the expected result, we can set a breakpoint at the end of function (3) and the stack trace in the debugger will show functions (2) and (1) ahead of function (3) on the stack. We’ll know the path our task took through functions between creation and completion. If the task is processed purely as a series of nested calls, then the debugger stack trace at the deepest point will capture the entire history of the task and reconstructing the control flow is as simple as reading this stack trace.

Unfortunately, many tasks are not so simple. Objects are not just passed into functions but also returned from functions, eliminating their source frames from the call stack in the process. Objects are also passed between threads, eliminating all prior steps in their lifetime from the call stack.

Imagine our simple three step path for the object instead looked like this:

![a non-linear, three node graph](https://www.cocoawithlove.com/assets/blog/three_layer_graph.svg)

In this diagram, function (2) calls function (1) where the task object is created. Function (1) then returns the task object to function (2) which then asynchronously passes the object to function (3).

Function (1) is lost from the stack trace as soon as it returns to function (2) then function (2) is also lost from the stack trace when function (3) is invoked asynchronously. When we find a problem at the end of function (3), we’ve lost the history of control flow for the object through our program.

How can we maintain enough information about our computation to perform useful reactive analysis at step (3) under these circumstances?

## We could use a log file

Traditionally, we address this type of control flow tracking problem with a log file. We log the construction of the task object, we log when we hand the object from one thread to another and we log its conclusion. By reading through the log file, we can see what events occurred and when.

The biggest problem with a log file though is controlling the amount of information it contains. A log file is usually program-wide and records events from all tasks in a single location. If multiple tasks are occurring simultaneously, they will be interleaved in the log file. If you have many tasks in your program, the log can become unreasonably difficult to read.

Another problem with log files is that they’re only as helpful as the information you choose to write – they don’t implicitly gather information. Good logging requires a non-zero amount of time to write a good log message.

Finally, logging only captures information from the current scope. This makes logging information far less helpful in reusable code where you’re more likely to be interested in the call site than the reusable callee.

## A journal of stack traces instead

Instead of using log files to track asynchronous tasks, I prefer to use a structure that I call a “task journal”. It’s not a complicated data structure. Here’s an example:

```swift
#if DEBUG
   var taskJournal: [[UInt]] = [callStackReturnAddresses()]
#endif
```

Its an array of stack traces, where a stack trace is simply an array of return addresses (`UInt`) that we can use to reconstruct functions and offsets within those functions at a later time.

Relative to a log file for tracking control flow, this task journal has the following advantages:

1. it stays out of the way until you need it (it’s not blasted into a common location)
2. it’s unique for the task (remains readable, even when multiple tasks are occurring at once)
3. it captures information about callers, making it useful in _reusable_ classes

The initial stack trace (as captured by `callStackReturnAddresses`) is added on initialization of the `taskJournal` and when your task reaches an interesting sequence point (conditional branch, interface boundary or other handover point), you append a stack trace.

Log files have many other purposes outside of tracking control flow; I'm not proposing stack traces as a replacement for log files. Log files remain the best solution for tracking progress across an aggregation of multiple tasks. Log files can also be persistent and user-readable, allowing them to be useful outside of simple debug analysis.

Coming from a log files, it’s natural to think you might need to include a message with the stack trace but the message is usually “I am here”, something that is already implicit in the stack trace.

This doesn’t mean you shouldn’t store additional metadata with tasks – information like “this task was created with parameters X, Y and Z” or “task received error message E” is very helpful – but it should usually be stored in a custom format for your task context. The key purpose of the task journal is to have metadata that doesn’t require any custom formatting, structures or messages – you just add sequence points when you want.

## Wait… why are we doing this at all?

Since Xcode 6, Xcode can automatically record backtraces when queueing blocks asynchronously using dispatch queues so you can follow a call stack across multiple asynchronous calls. You can watch this in action in [Debugging in Xcode 6 from WWDC2014](https://developer.apple.com/videos/play/wwdc2014/413/).

Do we still need to do stack trace capturing for ourselves?

Xcode will only record backtraces when queuing on a dispatch queue. You’re not in control of these backtraces so you can’t request them in other situations. There are therefore lots of examples of important control flow behaviors that this doesn’t capture:

1. Ongoing tasks that don’t use dispatch, including common tasks like network connections and user input
2. Operations on a single thread like basic function calls or taking one branch instead of another

Even when the control flow you want to track is asynchronous invocation of blocks on dispatch queues, recorded backtraces in Xcode relies on implicit behavior. Sometimes it works and sometimes it doesn’t and you get no feedback when the backtrace simply doesn’t appear. For example: in Xcode 7.2.1, Xcode’s recorded backtraces don’t appear to work at all for me in xctest targets. I don’t know if it’s a “known limitation” or a bug but it leaves me needing an alternative.

## Capturing the stack trace

Now, I’ve written `callStackReturnAddresses` in the examples above to capture the current stack trace. There isn’t a free function with that name in Swift or Cocoa.

There is a class function with that name on `NSThread`, so we could write:

```swift
var taskJournal: [[UInt]] = [Thread.callStackReturnAddresses()]
```

Unfortunately, neither `NSThread`, nor any other class in Foundation, exposes a way to easily convert addresses to symbols at a later time when needed.

There is an alternative function on `NSThread`:

```swift
let trace = NSThread.callStackSymbols()
```

which immediately converts the return addresses to symbols but that’s really too time consuming to attach to our main task machinery (we only want to convert to symbols after an error occurs, not on our critical path where we may need to capture hundreds or thousands of stack traces per second).

For performance reasons then, we need to stick to basic return addresses and we’ll need to convert them to symbols ourselves with the C function `dladdr`. At a minimum: `NSThread.callStackReturnAddresses` isn’t going to be a complete solution.

But I have another issue with the `NSThread` implementation: you can’t skip over the top couple of stack frames and you can’t limit the number of captured frames. With `NSThread.callStackReturnAddresses`, you must always capture the whole stack and then crop the result down to the information you actually need – which forces reallocates and wastes time.

We’d have a bit more flexibility if we could use the C function `backtrace` but in Swift, we can’t. The `backtrace` function comes from the “execinfo.h” header and is implemented as part of libSystem on OS X and iOS (which all Swift programs link against) but for whatever reason, the “execinfo.h” contents are not exposed to Swift programs.

## Rolling my own

While the functionality of `NSThread.callStackReturnAddresses` is probably enough for most people, I was dissatisfied enough that I bothered to re-implement it in Swift with the features I wanted:

```swift
/// Traverses the frames on current stack and gathers the return addresses for traversed
/// stack frames as an array of UInt.
/// - parameter skip: number of stack frames to skip over before copying return addresses
///   to the result array.
/// - parameter maximumAddresses: limit on the number of return addresses to return
///   (default is `Int.max`)
/// - returns: The array of return addresses on the current stack within the
///   skip/maximumAddresses bounds.
@inline(never)
public func callStackReturnAddresses(skip: UInt = 0, maximumAddresses: Int = Int.max) ->
   [UInt]
```

To support the function, I also wrote:

```swift
/// When applied to the output of callStackReturnAddresses, produces identical output to
/// the execinfo function "backtrace_symbols" or Thread.callStackSymbols
/// - parameter addresses: an array of memory addresses, generally as produced by
///   `callStackReturnAddresses`
/// - returns: an array of formatted, symbolicated stack frame descriptions.
public func symbolsForCallStack(addresses: [UInt]) -> [String]
```

which can take the `[UInt]` and produce call stack symbols in an identical format to `Thread.callStackSymbols()` but in an on-demand fashion.

## A simple example using these functions

I have a class that I sometimes use called `DeferredWork`. This object wraps a closure that is deferred to run at a later date. The class has a strict usage requirement: the work _must_ be run at some point before the `DeferredWork` object is deleted but it is not automatically run; it must be done manually.

A simplified version of the class looks like this (NOTE: this code assumes `DEBUG` is defined in debug builds):

```swift
class DeferredWork {
   let work: () -> Void

#if DEBUG
   // The task journal captures the stack trace on construction
   var taskJournal: [[UInt]] = [callStackReturnAddresses()]
   var didRun = false
#endif

   init(work: () -> Void) {
      self.work = work
   }
   
   func run() {
      work()
#if DEBUG
      didRun = true
#endif
   }

   func recordHandover() {
#if DEBUG
      // We can append additional stack traces whenever we wish.
      // For DeferredWork, this is intended to be done on ownership changes.
      taskJournal.append(callStackReturnAddresses())
#endif
   }
   
#if DEBUG
   deinit {
      if !didRun {
         // A "didn't run" condition at this point constitutes a failure.
         // We symbolicate and format the stack traces and trigger a fatal error.
         let traces = taskJournal.map {
            symbolsForCallStackAddresses($0).joinWithSeparator("\n")
         }
         preconditionFailure("Failed to perform work deferred at location:\n" +
            traces.joinWithSeparator("\n\nWith handover at:\n"))
      }
   }
#endif
}
```

To explain how this works: when the `DeferredWork` class is created, it takes ownership of the `work` closure and agrees to run this closure at a later time. The location of the construction is saved as the first element in the `taskJournal`.

If the `DeferredWork` is handed over to another owner, the `recordHandover` function can be manually invoked, recording the change in ownership.

Ultimately, if there is a problem – for this class a “problem” is a failure to invoke `run` before `deinit` – we know where the `work` closure came from we know the chain of custody that brought it to the current location and we can rapidly track down the precise location where the failure to run occurred.

Let’s look at how this solves the problematic three-step control flow I showed above:

![a non-linear, three node graph](https://www.cocoawithlove.com/assets/blog/three_layer_graph.svg)

`DeferredWork.init` is function (1). The `recordHandover` function should be called immediately before the asynchronous call at the end of function (2). The `deinit` function is invoked at the end of function (3) when the `DeferredWork` object falls out of scope. If the `run` function is not called at any time during function (2) or function (3) then we can immediately see the path the object took through our program and decide where we’ve made our mistake.

## Implementation of callStackReturnAddresses

As with all code, I’d prefer to implement everything in Swift but Swift lacks an equivalent of to the gcc/clang builtin function `__builtin_frame_address` which is critical for locating the current stack frame. I’ve written a C function named `frame_address` that returns `__builtin_frame_address(1)` and exposed this function to Swift in the bridging header.

Using this function, the internals of `callStackReturnAddresses` are very simple. I store the result from `frame_address` in a struct named `StackFrame` (which is nothing more than few functions wrapped around a `uintptr_t` that stores the result from `frame_address`)

```swift
let frame = StackFrame(address: frame_address())
```

Traversing through a stack is as simple as dereferencing the frame pointer (since the value at the frame pointer is the address of the previous frame):

```swift
let nextFrameAddress = UnsafeMutablePointer<UInt>(bitPattern: address)?.pointee
```

Getting return addresses from each frame is also easy since it is stored immediately after the frame pointer in each frame:

```swift
let returnAddress = UnsafeMutablePointer<UInt>(bitPattern: address)!.advanced(by: FP_LINK_OFFSET).pointee
```

So we just do this repeatedly through the stack until we exceed the stack bounds.

The resulting `callStackReturnAddresses` function is about twice as fast as `NSThread.callStackReturnAddresses` on the basic tests I’ve tried (roughly 2 million invocations per second per core on my Mac versus 1 million invocations per second for `Thread.callStackReturnAddresses`). It’s easily fast enough to gather lots of data in Debug builds – even for fairly intensive computational paths.

## Usage

> The project containing this code is available on github: [mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils).

1. In a subdirectory of your project’s directory, run `git clone https://github.com/mattgallagher/CwlUtils.git`
2. Drag the “CwlUtils.xcodeproj” file into your own project’s file tree in Xcode
3. Click on your project in the file tree to access project settings and click on the target to which you want to add CwlUtils.
4. Click on the “Build Phases” tab and under “Target Dependencies” click “+” and add the CwlUtils_OSX or CwlUtils_iOS target as appropriate for your target’s platform.
5. Still on “Build Phases”, if you don’t already have a “Copy Files” build phase with a “Destination: Frameworks”, add one. In this build phase, add “CwlUtils.framework”. NOTE: there will be _two_ frameworks in the list with the same name (one is OS X and the other is iOS). The “CwlUtils.framework” will appear above the corresponding CwlUtils OS X or iOS testing target.

Note about step (1): it is not required to create the checkout inside your project’s directory but if you check the code out in a shared location and then open it in multiple parent projects simultaneously, Xcode will complain – it’s usually easier to create a new copy inside each of your projects.

### Packaging note

This and the next few code posts I write are going to be part of a single framework, CwlUtils. To be blunt, I’m not really happy with this monolithic framework approach. Ideally, much of the code I’m hoping to produce would be separate, isolated classes that would be pulled together, on-demand, by a dependency manager. However, the existing third-party solutions for dependency management in Swift don’t work elegantly in this scenario (not entirely their fault since static linking and transparent Xcode integration are not possible).

I’ll definitely revisit this when the official Swift Package Manager is shipped as part of Xcode but at the moment, a dependency-free, monolithic framework is it. If you’re only interested in a small piece of code that I’ve written, you’ll need to extract it for yourself.

## Conclusion

I’ve talked about ease and benefits of recording stack traces for ongoing tasks to aid debugging. Tracking down why a result is incorrect after asynchronous invocations or other complex control flows can be completely impractical without this information so it’s a good technique to keep in mind.
