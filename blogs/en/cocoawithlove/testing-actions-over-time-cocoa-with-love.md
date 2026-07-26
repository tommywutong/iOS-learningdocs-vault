---
title: 'Testing actions over time | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/testing-actions-over-time.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:30a5b8296d286e55'
translated: false
---

> 原文：[Testing actions over time | Cocoa with Love](https://www.cocoawithlove.com/blog/testing-actions-over-time.html)　·　Cocoa with Love (Matt Gallagher)

Testing that actions are scheduled correctly over time is a pain. It’s common to have tests that “mostly” work but don’t confirm accuracy, run slowly, fail periodically and exceed wait times whenever a breakpoint is hit during testing.

One of the key reasons is that thread scheduling is imprecise. Tenths of a second inaccuracy are common and occasional spikes of much higher inaccuracy can occur. If we want to measure the timing of thread scheduled events, we end up needing events spaced over a long time to allow for significant windows of inaccuracy – this is not practical for large numbers of tests.

It is possible to mock the thread scheduler – so that we record the _attempts_ to schedule a task – but on its own, an empty mock might not be enough. If we need to test how scheduled events _interact_ then they still need to be performed, ideally as though they _precisely_ met their timing target.

I’ll show a way to test events scheduled over time, threads and other execution contexts with a `DebugContextCoordinator` that functions as a basic task scheduler but operates over a simulated version of time so that testing of invocation times and task interaction can be precise and free from changes due to host activity.

## A test case involving timing

Let’s imagine we want to test a class with the following interface:

```swift
class TimeoutService {
   init(work: @escaping WorkFunction)
   func start(timeout seconds: Double, handler: @escaping ResultHandler)
}
```

The class is constructed with an asynchronous “work” function and a handler that will receive the results. Each time the `start` function is called, the work function is invoked. The work function calls back to the service when it completes and the service forwards the result to the handler. If the service does not receive a timeout before the timeout time, then the handler is sent an error. Subsequent calls to `start` are permitted but if a subsequent work is started while a previous is still running, the previous is cancelled.

Thorough testing might involve a few possible scenarios:

1. is invoked succesfuly
2. is invoked with an error indicating timeout.
3. instance is released before success or timeout and the handler is never invoked.
4. after the first work completes or times out successfully run new work.
5. after the first work is started but before it completes or times out cancels work-in-progress in favor of the newly started work.

However, for this article, I want to focus exclusively on the second scenario: the timeout.

Basic testing with the `XCTest` framework might involve:

```swift
let expectation = expectation(description: "Waiting for timeout callback")
let service = TimeoutService(work: dummyAsyncWork) { r in
     XCTAssert(r.value == nil)
     expectation.fulfill()
}
service.run(timeout: 0.0) 

waitForExpectations(timeout: 10, handler: nil)
withExtendedLifetime(service) {}
```

While this tests that a timeout is _possible_, assuming `dummyAsyncWork` reliably takes longer than a zero second timeout timer, the test lacks any rigor. A zero second timer always takes a non-zero amount of time and depending on scheduling state on the host system, it’s technically possible for a non-zero duration success result to occur faster than a zero second timeout timer.

In addition, even if this test succeeds, we’re not actually testing that the timeout occurred at the correct time. The implementation could might apply the wrong timeout duration and this test might still succeed.

## Let’s fill in the TimeoutService implementation

Before we more forward and improve our testing, let’s step backward and fill in the definition of the `TimeoutService` so we can better define what we’re doing. Our `TimeoutService` is fairly simple. It takes an underlying `WorkFunction` an applies a timeout limit when waiting for a connection response.

The underlying `ConnectionFunction` can be swapped from the default `NetworkService.init` to an alternate implementation at construction time, allowing us to avoid network connections and get repeatable behavior when testing. Specifying alternate interfaces for any interally used external connections is also called [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection). I hope this isn’t news to anyone: it’s a fundamental aspect of isolating our code for testing.

> **NOTE**: This code example is quite large given that it’s just applying a time limit to an underlying action. I didn’t want to skimp on necessary steps so there’s a lot of work associated with managing lifetimes and ensuring everything cancels correctly when lifetimes elapse. I’ve tried to comment the code to explain some of these decisions. There are more syntactically efficient ways to manage lifetimes for asynchronous tasks (same steps but hidden behind simpler interfaces) but that’s a topic for another article.

```swift
class TimeoutService {
   struct Timeout: Error {}
   
   var currentAction: Lifetime? = nil
   
   // Define the interface for the underlying connection
   typealias ResultHandler = (Result<String>) -> Void
   typealias WorkFunction = (DispatchQueue, @escaping ResultHandler) -> Lifetime
   
   // This is the configurable connection to the underlying service
   let work: WorkFunction
   
   // Every action for this service should occur in in this queue
   let queue = DispatchQueue(label: "\(TimeoutService.self)")
   
   // Construction of the Service lets us specify the underlying service
   init(work: @escaping WorkFunction) {
      self.work = work
   }
   
   // This `TimeoutService` invokes the `underlyingConnect` and starts a timer
   func start(timeout seconds: Double, handler: @escaping ResultHandler) {
      var previousAction: Lifetime? = nil
      queue.sync {
         previousAction = self.currentAction
         
         let current = AggregateLifetime()
         
         // Run the underlying connection
         let underlyingAction = self.work(self.queue) { [weak current] result in
            // Cancel the timer if the success occurs first
            current?.cancel()
            handler(result)
         }
         
         // Run the timeout timer
         let timer = DispatchSource.singleTimer(interval: .interval(seconds), queue: self.queue) {
            [weak current] in
            // Cancel the connection if the timer fires first
            current?.cancel()
            handler(.failure(Timeout()))
         } as! DispatchSource
         
         current += timer
         current += underlyingAction
         self.currentAction = current
      }
      
      // Good rule of thumb: never release lifetime objects inside a mutex
      withExtendedLifetime(previousAction) {}
   }
}
```

The `DispatchSource.singleTimer` implementation, `Lifetime` and `AggregateLifetime` come from [CwlUtils](https://github.com/mattgallagher/CwlUtils). Everything else is standard Swift.

Assuming a valid implementation of `dummyAsyncWork` the previous tests would all likely succeed.

However, as previously stated: we are not correctly testing that the timeout occurs _when_ it should and we’re still connecting to the network which (in a real-world example) would connect to an external service like a website making testing prone to failures for range of difficult to control reasons.

## Let’s try testing using host time

Let’s start to test things better by providing a more specific function than `dummyAsyncWork` where we can control the exact time the service takes and isn’t dependent on anything outside our program.

```swift
let dummySuccessResponse = "Here's a string"
func dummyAsyncWork(duration: Double) -> TimeoutService.WorkFunction {
   return { exec, handler in
      exec.singleTimer(interval: .interval(duration)) {
         handler(.success(dummySuccessResponse))
      }
   }
}
```

Additionally, we need to start testing the actual time taken. Lets look at what that involves:

```swift
func testTimeoutServiceSuccessHostTime() {
   let expectation = expectation(description: "Waiting for timeout callback")
   
   // Use our debug `StringService`
   let service = TimeoutService(work: dummyAsyncWork(duration: 2.0))
   
   // Set up the time data we need
   let startTime = mach_absolute_time()
   let timeoutTime = 1.0
   let targetTime = UInt64(timeoutTime * Double(NSEC_PER_SEC))
   let leeway = UInt64(0.01 * Double(NSEC_PER_SEC))
   
   service.start(timeout: timeoutTime) { r in
      // Measure and test the time elapsed
      let endTime = mach_absolute_time()
      XCTAssert(endTime - startTime > targetTime - leeway)
      XCTAssert(endTime - startTime < targetTime + leeway)
         
      XCTAssert(r.value == nil)
      expectation.fulfill()
   }
   
   // Wait for all scheduled actions to occur
   waitForExpectations(timeout: 10, handler: nil)
}
```

This mostly works but as you can see:

- There’s a lot of boilerplate associated with getting and measuring host time and measuring both upper and lower bounds
- on my computer)
- In rare cases, this may still fail since heavy load or “stop the world” events on the host system (compressing memory, virtual memory thrashing, WindowServer crashes, sleep events) can cause many seconds delay.

## Injecting a scheduler like any other dependency

We already provide the `dummyAsyncWork` function; instead of a real underlying service like a network service, we provide synthetic, repeatable behavior.

The approach to making _time_ more testable is the same: instead of using real underlying host time, we can provide a service that provides synthetic, repeatable behavior.

In this `TimeoutService`, host time comes from libdispatch queues and timers. Unfortunately, libdispatch isn’t a single interface that we can swap out. In our code here, we’re using two separate interfaces, `DispatchQueue` and `DispatchSource`, so we’ll need to define a single new interface that unifies the functionality of both these interfaces.

We now get to why the CwlExec.swift file [I presented in the previous article for specifying execution contexts](https://www.cocoawithlove.com/blog/specifying-execution-contexts.html) also contains a range of timer and timestamp features – it is intended to be a unified interface for both these facets of libdispatch.

Lets rewrite the `TimeoutService` class to use `Exec` instead of libdispatch. We’ll need to pass an `Exec` parameter to the `init` function. This will replace the `queue` (which was previously a `DispatchQueue` used for synchronization) and will be used to start timers (instead of directly creating timers through `DispatchSource`).

```swift
class TimeoutService {
   struct Timeout: Error {}
   
   // This service performs one action at a time, lifetime tied to the service
   // The service retains the timeout timer which, in turn, returns the
   // underlying service
   var currentAction: Lifetime? = nil
   
   // Define the interface for the underlying connection
   typealias ResultHandler = (Result<String>) -> Void
   typealias WorkFunction = (Exec, @escaping ResultHandler) -> Lifetime

   // This is the configurable connection to the underlying service
   let work: WorkFunction

   // Every action for this service should occur in in this queue
   // **THIS LINE CHANGED**
   let context: Exec
   
   // Construction of the Service lets us specify the underlying service
   // **THIS LINE CHANGED**
   init(context: Exec = .global, work: @escaping WorkFunction = NetworkService.init) {
      self.work = work
      
      // **THIS LINE CHANGED**
      self.context = context.serialized()
   }

   // This `TimeoutService ` invokes the `underlyingConnect` and starts a timer
   func start(timeout seconds: Double, handler: @escaping ResultHandler) {
      var previousAction: Lifetime? = nil
      context.invokeAndWait {
         previousAction = self.currentAction

         let current = AggregateLifetime()
         
         // Run the underlying connection
         let underlyingAction = self.work(self.context) { [weak current] result in
            // Cancel the timer if the success occurs first
            current?.cancel()
            handler(result)
         }
         
         // Run the timeout timer
         // **THIS LINE CHANGED**
         let timer = self.context.singleTimer(interval: .interval(seconds)) { [weak current] in
            // Cancel the connection if the timer fires first
            current?.cancel()
            handler(.failure(Timeout()))
         }
         
         current += timer
         current += underlyingAction
         self.currentAction = current
      }
      
      // Good rule of thumb: never release lifetime objects inside a mutex
      withExtendedLifetime(previousAction) {}
   }
}
```

I have marked the four locations that actually changed in this example. The `Exec` type is intended to act as a low-friction abstration of `DispatchQueue`-like behavior.

As a further advantage, the `handler` callback for the `connect` function is now invoked in the `Exec` of the user’s choice (rather than the internally created `DispatchQueue`), so this change in interface offers all the same advantages discussed in the [previous article](https://www.cocoawithlove.com/blog/specifying-execution-contexts.html).

## Testing with DebugContextCoordinator

Now that libdispatch is replaced by the more flexible `Exec`, we can use the flexibility to schedule events with something other than libdispatch.

The new scheduler is named `DebugContextCoordinator`. This class runs tasks in an appropriate order but they will run according to a simulated, rather than real version of time, making everything testable and deterministic. With everything run in appropriate order, you should be able to simply substitute instances of `Exec.custom` created from a `DebugContextCoordinator` in place of the standard `Exec` cases and most common scheduling should continue to work, unchanged.

Let’s look at how our test for the timeout case would work:

```swift
func testTimeoutServiceTimeout() {
   let coordinator = DebugContextCoordinator()
   let context = coordinator.syncQueue

   // Construct the `TimeoutService` using our debug context
   let service = TimeoutService(context: context, work: dummyAsyncWork(duration: 2.0))

   // Run the `connect` function
   let timeoutTime = 1.0
   var result: Result<String>? = nil
   service.start(timeout: timeoutTime) { r in
      result = r
      XCTAssert(coordinator.currentTime == UInt64(timeoutTime * Double(NSEC_PER_SEC)))
      XCTAssert(coordinator.currentThread.matches(context))
   }

   // Perform all scheduled tasks immediately
   coordinator.runScheduledTasks()

   // Ensure we got the correct result
   XCTAssert(result?.error as? TimeoutService.Timeout != nil)

   withExtendedLifetime(service) {}
}
```

Some clear points to note here:

- and

  since all actions (even those nominally scheduled over time) are performed immediately when

  is called
- time (no more range required)
- We can also test that the callback thread matches our specified context

Less visible:

- it now takes less than a millisecond to run (versus 1.1 seconds, previously) since it doesn’t need to wait for any real-world time to elapse to simulate a second in the debug context.
- uses.

Downsides:

- ,

  or even just getting the current time), you won’t get the same resullts and in some cases, this will prevent your tests working. If possible, remove queries of the execution context or ask the

  instance for information about the execution context.
- runs single threaded, it won’t help you find threading bugs – thread testing will need to be done a different way.

## Usage

> The project containing the `DebugContextCoordinator`, along with all dependencies like `Exec` is available on github: [mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils).

The final `TimeoutService` is included in the the [CwlDebugContextTests.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Tests/CwlUtilsTests/CwlDebugContextTests.swift?ts=3) file, along with the `testTimeoutServiceSuccessHostTime` and `testTimeoutServiceSuccess` tests so you can play around with how the `DebugContextCoordinator` behaves at runtime.

The initial (`DispatchQueue` and `DispatchSource`) version of `TimeoutService` implementation appears on the TimeoutService page of the NonReactive playground in the [Cocoa with Love Playgrounds project](https://github.com/mattgallagher/CocoaWithLovePlaygrounds).

The [CwlDebugContext.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlDebugContext.swift?ts=3) file has a few dependences on other files in the same project, including [CwlExec.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlExec.swift?ts=3), [CwlDispatch.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlDispatch.swift?ts=3) and the [CwlMutex.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlMutex.swift?ts=3) file. It probably wouldn’t be difficult to grab these files separately and add them to your project (if you prefer static linkage) but I recommend following the instructions in the [ReadMe.md file for the project](https://github.com/mattgallagher/CwlUtils/blob/master/README.md) and simply cloning the whole repository and adding the framework it produces to your own projects.

## Conclusion

The `Exec` type presented in the [previous article](https://www.cocoawithlove.com/blog/specifying-execution-contexts.html) as a means of controlling callback execution context can also be used as a means of abstracting timing and scheduling too. The two ideas benefit from each other: when we added `Exec` to the `TimeoutService` class to abstract the timing, we automatically gained the ability to invoke the callback `handler` in an execution context of the user’s choosing.

The advantage with using a `DebugContext` and `DebugContextCoordinator` to handle timing is that you’re no longer dependent on the actual timing information from the host machine, leading to greater precision and greater reliablility in testing.

### Looking forward…

While not directly related to timing, I included a “NOTE” before a large code sample in this article: properly handling lifetimes for asynchronous tasks can make a simple composition of actions (like combining an action with a timeout) quite complicated. In the next article, I’ll begin looking at abstractions used for composing asychronous tasks with the aim of reducing this complexity.
