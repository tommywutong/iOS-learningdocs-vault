---
title: 'Specifying function execution contexts | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/specifying-execution-contexts.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:e9dc0ff34c9c4d4e'
translated: false
---

> 原文：[Specifying function execution contexts | Cocoa with Love](https://www.cocoawithlove.com/blog/specifying-execution-contexts.html)　·　Cocoa with Love (Matt Gallagher)

In asynchronous code, it is common to have callbacks and other functions that need to be run in a specific “execution context”.

Limited approaches for specifying execution context involve specifying a queue or thread on which to run the function but these only capture a small subset of possible traits that might fall under the banner of “execution context”. Technically, an “execution context” might include _any_ state on the stack, current thread, entire program or even the host environment outside the program.

Further complicating choice of execution contexts is the fact that in many cases, some negotiation between the caller and the callee is required. The callee might want asynchronous execution but the caller might need to block and wait for the callee to complete. The callee might specify synchronous invocation but the caller might require that the invocation be asynchronous to avoid re-entrancy. The caller might be expected to behave in a thread-safe manner but the callee might have provided a concurrent asynchronous context, undermining thread safety.

I’ll discuss how to specify execution contexts in a way that can handle a broad range of scenarios and allows both caller and callee some say in the final choice.

## Functions as parameters

Swift programs often involve _lots_ of cases where functions are passed around as data. The reasons why the number of cases of functions-as-data have increased relative to Objective-C are diverse:

- improved syntax (no more C-function declaration legacy)
- Swift’s ability to handle free functions, virtual functions, Objective-C message sending and closures with identical semantics
- different style established by Swift standard library versus Foundation
- broader industry trend towards functional composition instead of object oriented interfaces

The result is that a typical medium-sized Swift program might involve _thousands_ of cases where a function is passed as a parameter. Depending on programming style, tens of thousands of cases would not be excessive.

The overwhelming majority of functions passed as parameters – maybe 99% or more – are happy to be directly invoked in the callers execution context like this:

```swift
func someFunctionCaller(callee: () -> ()) {
   // Perform the function's logic
   
   // Directly invoke in the caller's execution context
   callee()

   // Perform any follow up work
}
```

In situations where the callee might need to perform its work in another execution context, the standard approach is to leave the transition to the callee.

```swift
// Embed the transition to the desired execution context in the closure,
// rather than requiring a separate parameter
someFunctionCaller { context.invoke(callee) }
```

## Piggybacking on the context transition

This article is about situations where “leaving it to the callee” is insufficient.

The primary example is when the caller needs to perform work in the same context where the callee runs.

```swift
func someFunctionCaller(context: ExecutionContext, callee: () -> ()) {
   // Perform the function's logic

   // Transition to the specified context
   context.invoke {
      // Perform any preceeding work that the caller needs to occur in the
      // callee context
      
      callee()
      
      // Perform any follow up work that the caller needs to occur in the
      // callee context
   }

   // Perform any follow up work that is independent of the callee
}
```

By letting the caller initiate the transition to the desired context, the caller can piggyback on the transition and perform work either side of the actual callee invocation.

The most common reason that this would be required is when the caller needs to release resources when the callee is done or when the caller needs to start another action after the callee is complete.

## Using a thread or queue as an execution context

The Cocoa APIs already provide examples of specifying the execution context for callback functions with a parameter. `NSNotificationCenter` is one of the most prominent example:

```swift
func addObserver(forName name: NSNotification.Name?, object obj: Any?, queue:
   OperationQueue?, using block: (Notification) -> Void) -> NSObjectProtocol
```

If the `queue` is non-`nil`, the `NSNotificationCenter` will ensure that the `OperationQueue` is used as the execution context for the `using` block.

The most obvious limitation with this approach is that it requires the target execution context be an `OperationQueue`. That’s fine for asynchronous invocation on the main thread or the global concurrent queue but it’s useless if you need to run code on a private `DispatchQueue`, `Thread` or `NSManagedObjectContext` or if your execution context isn’t a thread or queue but is simply a mutex.

With execution context being a very broad concept, restricting it to anything more specific than a protocol is a poor choice.

## An ExecutionContext protocol

So let’s look at what a a more general `ExecutionContext` protocol should declare:

```swift
public protocol ExecutionContext {
   /// A description about how functions will be invoked on an execution context.
   var type: ExecutionType { get }
   
   /// Run `execute` normally on the execution context
   func invoke(_ execute: @escaping () -> Void)
   
   /// Run `execute` asynchronously on the execution context
   func invokeAsync(_ execute: @escaping () -> Void)
   
   /// Run `execute` on the execution context but don't return from this function until the
   /// provided function is complete.
   func invokeAndWait(_ execute: @escaping () -> Void)
}
```

While the intention behind making `ExecutionContext` a protocol is to give additional flexibility to the callee to make arbitrary changes to the state before invocation, you’ll notice that we’re also giving additional flexibility to the caller with _three_ different functions for invoking: `invoke`, `invokeAsync` and `invokeAndWait`.

In part, this resembles `DispatchQueue`, where the caller can run work on the queue using `sync` or `async`. However, `DispatchQueue`s don’t have a “default preference” – as occurs here with `invoke`. In scenarios where the caller doesn’t care either way, this allows the callee to choose for itself. In scenarios where the caller _does_ care, `invokeAsync` forces asynchrony (to avoid blocking or re-entrancy) and `invokeAndWait` forces blocking until completion, when a result is needed synchronously.

Now the `ExecutionType` is an enum that describes the overall behavior of the execution context to the caller. It is defined as follows:

```swift
public enum ExecutionType {
   case immediate
   case mutex
   case serialAsync
   case concurrentAsync
   case conditionallyAsync(Bool)

   public var isImmediate: Bool
   public var isConcurrent: Bool
}
```

In this context, `immediate` means “guaranteed to complete before returning”. I deliberately avoid the term “synchronous” here (often used to mean a similar thing) since “synchronous” usually implies a serialized resource is acquired and in this enum `immediate` explicitly implies there is no mutex involved. It should be obvious that the separate case `mutex` is used for “guaranteed to complete before returning and guaranteed serialized” (which is closer to a true “synchronous”).

So `immediate` and `mutex` both return true for `isImmediate` and `immediate` and `concurrentAsync` both return true for `isConcurrent` (since neither serialize concurrent invocations).

The oddball is clearly `conditionallyAsync(Bool)`. This might be easiest to explain with the motivating example: running on the main thread. If you’re already on the main thread, you can immediately invoke the function. If you’re not on the main thread, you must asynchronously dispatch on the main thread. The `isConcurrent` property is always `false` for `conditionallyAsync(Bool)` and `isImmediate` will return the inverse of the associated `Bool` value.

## Optimizing the common cases

Earlier, I talked about how a program might contain thousands of functions used as parameters. In that case I was talking about lines of code, not the number of invocations per second. The invocations per second could be much, much higher.

Worth noting is that functions and callbacks like this are never the _work_ that you’re trying to perform; invocations are merely the glue between units of work. In my own code, I have examples where 10s of thousands of callbacks per second need to run and those callbacks need to take less than 10% of the CPU so that actual work can get done in the remaining time.

Accordingly, I have synthetic test cases where I run millions of invocations per second and bluntly: the code as written so far cannot handle those numbers.

You might think: “What code? All you’ve shown is a protocol interface.”

The protocol interface is the problem. An `@escaping` closure on an existential type (like a `protocol` when the explicit implementation is unknown at compile time) will almost always involve closure capture (a heap allocation) and a non-inlined dynamically resolved function call. While this could certainly satisfy tens of thousands of calls per second, it wouldn’t leave much time for other work. And it certainly can’t handle millions of calls per second.

For that reason, I don’t use `ExecutionContext` directly in my own programs. Instead, I use the following:

```swift
public enum Exec: ExecutionContext {
   /// Invoked directly from the caller's context
   case direct
   
   /// Invoked on the main thread, directly if the current thread is the main thread,
   /// otherwise asynchronously
   case main
   
   /// Invoked on the main thread, asynchronously, regardless of whether the current
   /// thread is the main thread
   case mainAsync
   
   /// Invoked asynchronously in the global queue with QOS_CLASS_USER_INTERACTIVE priority
   case interactive

   /// Invoked asynchronously in the global queue with QOS_CLASS_USER_INITIATED priority
   case user

   /// Invoked asynchronously in the global queue with QOS_CLASS_DEFAULT priority
   case `default`

   /// Invoked asynchronously in the global queue with QOS_CLASS_UTILITY priority
   case utility

   /// Invoked asynchronously in the global queue with QOS_CLASS_BACKGROUND priority
   case background

   /// Invoked using the wrapped ExecutionContext.
   case custom(ExecutionContext)

   public var type: ExecutionType
   public func invoke(_ execute: @escaping () -> Void)
   public func invokeAsync(_ execute: @escaping () -> Void)
   public func invokeAndWait(_ execute: @escaping () -> Void)
}
```

You should be able to see that this is really just a specialized implementation of `ExecutionContext` that implements all the common cases for an `ExecutionContext` – a `direct` case, two main thread cases and a case for all named `DispatchQueue`s – but can wrap any other `ExecutionContext` in the `custom` case.

The reason to use `Exec` in interfaces, instead of `ExecutionContext`, is that the compiler can implement far better optimizations for `Exec` because it can see the whole implementation. An `enum` is also really nice to use, syntactically:

```swift
someFunctionCaller(context: .main) { /* my callback work */ }
```

Using `Exec` also offers one additional optimization opportunity when you’re really trying to squeeze maximum performance out of your code:

```swift
func someFunctionCaller(context: Exec = .direct, callee: () -> ()) {
   switch context {
   case .direct:
      // Some setup code
      callee()
      // Some cleanup code
   default:
      context.invoke {
         // Some setup code
         callee()
         // Some cleanup code
      }
   }
}
```

When the `.direct` invocation case is the common case (which is a majority of the time - especially when it is specified as the “default” value, as it is here) you can further optimize by bypassing the `invoke` call entirely (since you know with certainly that it does nothing more than directly invoke the function). This avoids the closure capture and associated heap allocation that would otherwise be required for the setup and cleanup code.

## Usage

> The project containing the `Exec`, `ExecutionContext` and `ExecutionType` implementations is available on github: [mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils).

The [CwlExec.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlExec.swift?ts=3) file has a few dependences on other files in the same project, including the [CwlDispatch.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlDispatch.swift?ts=3) file and the [CwlMutex.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlMutex.swift?ts=3) file. It probably wouldn’t be difficult to grab these three files separately and add them to your project (if you prefer static linkage) but I recommend following the instructions in the [ReadMe.md file for the project](https://github.com/mattgallagher/CwlUtils/blob/master/README.md) and simply cloning the whole repository and adding the framework it produces to your own projects.

## Conclusion

All of this might seem a little abstract; inserting an additional layer between caller and callee, just to handle a basic function invocation. It’s primarily useful if you’re writing the caller side of an asynchronous workflow and you’re looking to better manage resources across multiple stages of the workflow or reduce boilerplate for the callee.

### Looking forward…

The CwlExec.swift file contains a number of features that I haven’t discussed here, including timers and timestamps. If you’re looking for an explanation about why these would be attached to the execution context, then please continue to the next article.
