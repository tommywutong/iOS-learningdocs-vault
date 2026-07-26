---
title: 'Partial functions in Swift, Part 2: Catching precondition failures | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/02/02/partial-functions-part-two-catching-precondition-failures.html'
original_language: en
published: 2016-02-02
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:1156addf46a1d9ae'
translated: false
---

> 原文：[Partial functions in Swift, Part 2: Catching precondition failures | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/02/02/partial-functions-part-two-catching-precondition-failures.html)　·　Cocoa with Love (Matt Gallagher)

In the [previous post](https://www.cocoawithlove.com/blog/2016/01/25/partial-functions-part-one-avoidance.html), I discussed “partial functions” and advised against them. As stated in that article though, there are situations where partial functions are necessary or expected. If you’re going to write a partial function, you need to test it and that means testing a `precondition` failure occurs when the requirement is violated.

One problem: `precondition` failures crash the xctest harness making testing annoying. In this article, I’m going to show a Mach exception handler that catches these crashes and rewrites the thread’s state as though an Objective-C exception was raised instead, making `precondition` failures testable.

## Background

On ARM, a fatal error is implemented as a `brk` instruction which triggers an `EXC_BREAKPOINT` instead. We'll only test iOS code in the simulator, which is x86-64, so we won't worry about `EXC_BREAKPOINT`.

A `precondition` failure is implemented in the Swift standard library as a `Builtin.int_trap()` which is ultimately compiled as a `ud2` instruction on i386/x86-64 platforms. This instruction exists for the sole purpose of triggering an “invalid opcode” which will be caught by the operating system, leading to a Mach `EXC_BAD_INSTRUCTION` exception at runtime.

Using only Swift language and standard library features, there’s no way to recover from a `precondition` failure.

Traditional approaches to this type of situation involve running the code in a child process and monitoring crashes from the parent or using build configurations to swap the fatal error with something more catchable.

Mach exception handlers provide a different approach. With a Mach exception handler the operating system gives us a chance to respond to the Mach exception and we can use that chance to rewrite our application’s history as though the `ud2` instruction never happened.

## Tests first

What we need is a function named `catchBadInstruction` that satisfies the following test:

```swift
class CatchBadInstructionTests: XCTestCase {
   func testCatchBadInstruction() {
   #if arch(x86_64)
      // Test catching an assertion failure
      var reachedPoint1 = false
      var reachedPoint2 = false
      let exception1: BadInstructionException? = catchBadInstruction {
         // Must invoke this block
         reachedPoint1 = true
         
         // Fatal error raised
         precondition(false, "EXC_BAD_INSTRUCTION raised here")

         // Exception must be thrown so that this point is never reached
         reachedPoint2 = true
      }
      // We must get a valid BadInstructionException
      XCTAssert(exception1 != nil)
      XCTAssert(reachedPoint1)
      XCTAssert(!reachedPoint2)
      
      // Test without catching an assertion failure
      var reachedPoint3 = false
      let exception2: BadInstructionException? = catchBadInstruction {
         // Must invoke this block
         reachedPoint3 = true
      }
      // We must not get a BadInstructionException without an assertion
      XCTAssert(reachedPoint3)
      XCTAssert(exception2 == nil)
   #endif
   }
}
```

The `catchBadInstruction` function runs the closure passed to it. If any Mach `EXC_BAD_INSTRUCTION` exceptions occur, this function catches the Mach exception, creates an instance of `BadInstructionException` (a subclass of `NSException`), raises that exception at the point where the `EXC_BAD_INSTRUCTION` occurred and then catches the `BadInstructionException` outside the child closure. The `BadInstructionException` raised, if any, is returned.

This `catchBadInstruction` function will catch any of the Swift fatal error aborts, including `assert`, `assertionFailure`, `precondition`, `preconditionFailure`, `fatalError`. By catching these failures, we can test that functions required to raise assertions for particular combinations of inputs are being applied correctly.

This code will also catch other unrelated sources of Mach `EXC_BAD_INSTRUCTION` exceptions but they’re extremely rare unless your binary is corrupted (not a serious possibility in the testing scenarios to which this code should be limited).

## A list of serious caveats

> I have tagged this article with the tag ‘hacks’. I intend this tag to communicate that the code in this post does some clever things but the result is well outside the bounds of what safe, maintainable programs should do. Let me be clear: there’s no good reason to run this code in your deployment builds. **This code is intended for testing, exclusively**.

One of the simplest things this code does is also the least usable in a deployed program: throwing and catching an Objective-C exception over your Swift code. Even in Objective-C, exceptions are usually unsafe unless you’re extremely careful. The situation is worse in Swift since we can no longer ask the compiler to generate exception-safe automatic reference counting. A few memory leaks will almost certainly occur and other code may misbehave due to interrupted side effects or partial construction. It’s up to you to minimize these problems if they surround `precondition` failures that you need to test. Under test conditions, this is usually a manageable problem.

Installing multiple Mach exception handlers may create complications. I’ve not tested multiple, nested or otherwise conflicting Mach exception handlers and I’m not convinced the exception handler will play well with other handlers installed on the same thread. This is all outside the “testing, exclusively” use-case so just don’t do it.

There’s also something you might have noticed in the test code: it will only run on `arch(x86_64)`. The code will run in the iOS/watchOS/tvOS simulators and natively on the Mac but it will not run on iOS/watchOS/tvOS devices. This is because the API for catching Mach exceptions is not public in these SDKs. [Landon Fuller mentioned in 2013](https://mikeash.com/pyblog/friday-qa-2013-01-11-mach-exception-handlers.html) that he had filed a radar with Apple requesting the required interfaces on iOS but nothing has come of it. I can only assume this isn’t going to change.

If you’re using open source Swift on Linux, Mach exceptions and the Objective-C runtime aren’t available. See the “proof-of-concept” SIGILL handler, mentioned in the “Update” below.

## Trying to write a Mach exception handler

Writing this code was considerably harder for me than it ideally should have been. For whatever reason, Apple don’t document Mach exception handling. They don’t conceal its existence and the “mach_exc.defs” file is public API on OS X but there’s nothing in the Xcode documentation reference, man pages or on Apple’s website beyond the definitions file itself.

Making matters worse, the examples and documentation you can easily find on third-party web sites are usually for the 32-bit version of Mach exceptions which uses slightly different functions and requires slightly different parameters. When you do find examples of 64-bit Mach exception handling (like that in [plcrashreporter](https://www.plcrashreporter.org), lldb or gdb) it’s normally catching exceptions for the whole program rather than a specific thread or for catching from another process.

I eventually got through it with a basic trial-and-error approach but it was really slow going due to the ease of writing code that appeared to succeed but did nothing useful because the `mach_port_t` was configured using flags only valid in 32-bit.

Processing Mach exception messages uses technology that seems completely out-of-place in the modern world. Maybe that shouldn't be surprising, given a few of the files in this particular time-capsule are listed as "Author: Avadis Tevanian, Jr., Date: 1985".

There’s no simple C interface for processing Mach messages. Instead, you get a “MiG” (Mach Interface Generator) file and you’re expected to generate a C interface from that. Interface generators are normally used when it’s possible to generate interfaces for multiple languages. Okay, so can I generate a Swift interface? No, you can only generate a C interface. So why do I need to generate the interface at all? Why isn’t the implementation in a library with a basic C interface provided? I don’t know.

Then the generated interface expects to call into C functions in your code with specific type signatures. Here we run into a Swift limitation: Swift (as of version 2.1) can’t expose a function matching a C type signature. You can pass around `@convention(c)` pointers to your Swift functions but you can’t publicly expose headers to those same functions. The autogenerated “[ProductName]-Swift.h” file for letting Objective-C call into Swift only exposes your public Objective-C classes (free functions are not exposed). The end result is that it’s just easiest to call into Swift via Objective-C.

I wanted to write as much of the Mach message handling in Swift as possible but I’ve had to implement the actual callback interface in an Objective-C file and call the Swift handler function from there. There’s also some Objective-C code use to catch exceptions.

### Update: an alternative using a POSIX signal handler

I’ve had a few people ask “If a Mach Exception handler is so difficult, why not use a POSIX signal handler instead?” Both can do similar things. The reason I wanted to use a Mach exception handler is that despite requiring considerably more _boilerplate_, the resulting _behavior_ is far simpler.

I’ve added a “proof-of-concept” POSIX `SIGILL` signal handler to the code in the linked Github project so you can see what I mean. It’s a single Swift file (instead of the Mach exception handler’s 7 files scattered across Swift, Objective-C and MiG) but on platforms where Mach exceptions are available, it’s a clear step backwards.

The biggest problem is straightforward: it won’t run with lldb attached since lldb catches the `EXC_BAD_INSTRUCTION`, preventing the `SIGILL` from ever occurring (you must run without a debugger attached). For my typical “testing from within Xcode” usage scenario (where I always run with lldb attached) this point alone entirely rules out the signal handler version.

Additional problems in decreasing severity include:

- the signal handler is whole process (rather than correctly scoped to the thread where the “catch” occurs)
- the signal handler doesn’t deal with re-entrancy whereas the mach exception handler remains deterministic in the face of multiple fatal errors
- the signal handler overwrites the “[red zone](https://en.wikipedia.org/wiki/Red_zone_(computing))” which is technically frowned upon in signal handlers (although unlikely to cause problems here)

## The Mach exception handler: rewriting history

There’s a lot of different parts to the code but the core of it happens inside the Mach exception handler. The exception handler gives us the “state” (registers) for the thread where the exception occurs. We can return a modified version of this “state” and since the thread is suspended, we can also modify the stack. This is what we do:

```swift
// Read the old thread state
var state = old_state.withMemoryRebound(to: x86_thread_state64_t.self, capacity: 1) { return $0.pointee }

// 1. Decrement the stack pointer
state.__rsp -= __uint64_t(MemoryLayout<Int>.size)

// 2. Save the old Instruction Pointer to the stack.
if let pointer = UnsafeMutablePointer<__uint64_t>(bitPattern: UInt(state.__rsp)) {
   pointer.pointee = state.__rip
} else {
   return KERN_INVALID_ARGUMENT
}

// 3. Set the Instruction Pointer to the new function's address
var f: @convention(c) () -> Void = raiseBadInstructionException
withUnsafePointer(to: &f) {
   state.__rip = $0.withMemoryRebound(to: __uint64_t.self, capacity: 1) { return $0.pointee }
}

// Write the new thread state
new_state.withMemoryRebound(to: x86_thread_state64_t.self, capacity: 1) { $0.pointee = state }
new_stateCnt.pointee = x86_THREAD_STATE64_COUNT
```

The three numbered steps are the equivalent of an assembly language `call` instruction. We’ve changed the state of the thread to look like the last code run was not the `ud2` instruction that raised the `EXC_BAD_INSTRUCTION` but was instead a `call` to our `raiseBadInstructionException` function. Therefore, when the thread resumes it will run:

```swift
private func raiseBadInstructionException() {
   BadInstructionException().raise()
}
```

which is a straightforward throw of an `NSException` subclass.

## Setting up a Mach exception handler

The other code I wanted to highlight was the setup of the Mach exception handler. There are two reasons for this:

1. Documentation and useful examples for the required functions were really difficult to find, so I’d like to publish it here for visibility.
2. This was some of the first Swift 2 code I ever wrote and I went crazy with Swift’s `defer`, `try`, `guard`, `throw` and `catch`; I’m not sure if the result is brilliant or ridiculous but at least there’s no possibility of a `goto fail` error here.

I’ve commented each step in the code so you should just be able to read the comments to see what the code does. **Pay close attention to the order that the steps are numbered**, remember: `defer` statements are executed in the reverse order to their setup.

Here goes:

```swift
public func catchBadInstruction(in block: () -> Void) -> BadInstructionException? {
   var context = MachContext()
   var result: BadInstructionException? = nil
   do {
      var handlerThread: pthread_t? = nil
      defer {
         // 8. Wait for the thread to terminate *if* we actually made it to the creation
         // point. The mach port should be destroyed *before* calling pthread_join to avoid
         // a deadlock.
         if handlerThread != nil {
            pthread_join(handlerThread!, nil)
         }
      }
      
      try kernCheck {
         // 1. Create the mach port
         mach_port_allocate(mach_task_self_, MACH_PORT_RIGHT_RECEIVE,
            &context.currentExceptionPort)
      }
      defer {
         // 7. Cleanup the mach port
         mach_port_destroy(mach_task_self_, context.currentExceptionPort)
      }
      
      try kernCheck {
         // 2. Configure the mach port
         mach_port_insert_right(mach_task_self_, context.currentExceptionPort,
            context.currentExceptionPort, MACH_MSG_TYPE_MAKE_SEND)
      }
      
      try kernCheck { context.withUnsafeMutablePointers { masksPtr, portsPtr, behaviorsPtr,
         flavorsPtr in
         // 3. Apply the mach port as the handler for this thread
         thread_swap_exception_ports(mach_thread_self(), EXC_MASK_BAD_INSTRUCTION,
            context.currentExceptionPort, Int32(bitPattern: UInt32(EXCEPTION_STATE) |
            MACH_EXCEPTION_CODES), x86_THREAD_STATE64, masksPtr, &context.count, portsPtr,
            behaviorsPtr, flavorsPtr)
      } }
      
      defer { context.withUnsafeMutablePointers { masksPtr, portsPtr, behaviorsPtr,
         flavorsPtr in
         // 6. Unapply the mach port
         _ = thread_swap_exception_ports(mach_thread_self(), EXC_MASK_BAD_INSTRUCTION, 0,
            EXCEPTION_DEFAULT, THREAD_STATE_NONE, masksPtr, &context.count, portsPtr,
            behaviorsPtr, flavorsPtr)
      } }
      
      try withUnsafeMutablePointer(to: &context) { c throws in
         // 4. Create the thread
         let e = pthread_create(&handlerThread, nil, machMessageHandler, c)
         guard e == 0 else { throw PthreadError.code(e) }
         
         // 5. Run the block
         result = BadInstructionException.catchException(in: block)
      }
   } catch {
      // Should never be reached but this is testing code, don't try to recover, just abort
      fatalError("Mach port error: \(error)")
   }
   return result
}
```

The `kernCheck` function is just a little helper to grab the result code from a Mach function and if it’s an error, convert to a Swift `ErrorType` and `throw`. It’s equivalent to the sort of macro that might be used for this type of error code checking in C.

The `catchBadInstruction` function sets everything up but it’s the `machMessageHandler` function (spawned by the `pthread_create` call at step 4) that sits around and waits to see if a Mach message will be received. It looks like this:

```swift
private func machMessageHandler(_ arg: UnsafeMutableRawPointer) ->
   UnsafeMutableRawPointer? {
   let context = arg.assumingMemoryBound(to: MachContext.self).pointee
   var request = request_mach_exception_raise_t()
   var reply = reply_mach_exception_raise_state_t()
   
   var handledfirstException = false
   repeat { do {
      // Request the next mach message from the port
      request.Head.msgh_local_port = context.currentExceptionPort
      request.Head.msgh_size = UInt32(MemoryLayout<request_mach_exception_raise_t>.size)
      try kernCheck { request.withMsgHeaderPointer { requestPtr in
         mach_msg(requestPtr, MACH_RCV_MSG | MACH_RCV_INTERRUPT, 0, request.Head.msgh_size,
            context.currentExceptionPort, 0, UInt32(MACH_PORT_NULL))
      } }
      
      // Prepare the reply structure
      reply.Head.msgh_bits = MACH_MSGH_BITS(MACH_MSGH_BITS_REMOTE(request.Head.msgh_bits), 0)
      reply.Head.msgh_local_port = UInt32(MACH_PORT_NULL)
      reply.Head.msgh_remote_port = request.Head.msgh_remote_port
      reply.Head.msgh_size = UInt32(MemoryLayout<reply_mach_exception_raise_state_t>.size)
      reply.NDR = NDR_record
      
      if !handledfirstException {
         // Use the MiG generated server to invoke our handler for the request and fill in
         // the rest of the reply structure
         guard request.withMsgHeaderPointer(in: { requestPtr in
            reply.withMsgHeaderPointer { replyPtr in
            mach_exc_server(requestPtr, replyPtr)
         } }) != 0 else { throw MachExcServer.code(reply.RetCode) }
         
         handledfirstException = true
      } else {
         // If multiple fatal errors occur, don't handle subsquent errors (let the program
         // crash)
         reply.RetCode = KERN_FAILURE
      }
      
      // Send the reply
      try kernCheck { reply.withMsgHeaderPointer { replyPtr in
         mach_msg(replyPtr, MACH_SEND_MSG, reply.Head.msgh_size, 0, UInt32(MACH_PORT_NULL),
            0, UInt32(MACH_PORT_NULL))
      } }
   } catch let error as NSError where (error.domain == NSMachErrorDomain && (error.code ==
      Int(MACH_RCV_PORT_CHANGED) || error.code == Int(MACH_RCV_INVALID_NAME))) {
      // Port was already closed before we started or closed while we were listening.
      // This means the controlling thread shut down.
      return nil
   } catch {
      // Should never be reached but this is testing code, don't try to recover, just abort
      fatalError("Mach message error: \(error)")
   } } while true
}
```

## Usage

> The project containing this code is available on github: [mattgallagher/CwlPreconditionTesting](https://github.com/mattgallagher/CwlPreconditionTesting).

The [Readme.md file](https://github.com/mattgallagher/CwlPreconditionTesting/blob/master/README.md) file contains some additional usage instructions but the short version is:

1. `git clone https://github.com/mattgallagher/CwlPreconditionTesting.git`
2. drag the “CwlPreconditionTesting.xcodeproj” file into your project’s file tree in Xcode
3. go to your testing target’s Build Phase settings and under “Target Dependencies” press the “+” button and select the relevant “CwlPreconditionTesting” target ("_iOS" or “_OSX”, depending on your testing target’s SDK)
4. write `import CwlPreconditionTesting` at the top of any test file where you want to use `catchBadInstruction` (Swift should handle the linkage automatically when you do this)
5. use the `catchBadInstruction` function as shown in the [CwlCatchBadInstructionTests.swift tests file](https://github.com/mattgallagher/CwlPreconditionTesting/blob/master/Tests/CwlPreconditionTestingTests/CwlCatchBadInstructionTests.swift?ts=3)

## Conclusion

`CwlPreconditionTesting.catchBadInstruction` can catch Swift `precondition` failures so we can accurately test partial functions. I think it’s likely that the Mach exception handler shown in this article contains the highest percentage of Swift used in any Mach exception handler ever written (although I doubt there’s much Swift competition in this area).

This post completes my “Return to Cocoa with Love and Be Completely Self-Contradictory” trilogy:

- [Part 1: Move away from fun hacks on Cocoa with Love](https://www.cocoawithlove.com/blog/2016/01/25/a-new-era-for-cocoa-with-love.html)
- [Part 2: Don’t use partial functions](https://www.cocoawithlove.com/blog/2016/01/25/partial-functions-part-one-avoidance.html)
- [Part 3: Let’s test partial functions using fun hacks!](https://www.cocoawithlove.com/blog/2016/02/02/partial-functions-part-two-catching-precondition-failures.html)

I’m being flippant, of course, since this apparent contradiction only exists if we omit the context of the articles’ different problem domains: app implementation, API design and testing, respectively. It’s easy to forget the differences between these domains since we might use Swift, Xcode and other tools across all three. That doesn’t mean they’re the same. What’s good in test code may be bad in a deployed app – and vice versa.

An app needs to handle user unpredictability and endure revisions. An API needs to be efficient and reusable. None of this is strictly required for testing; if our tests are easy to write, easy to read and thorough, then everything else is optional.
