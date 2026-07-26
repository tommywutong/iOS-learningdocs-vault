---
title: '22 short tests of combine – Part 3: Asynchrony | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-3.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:266bfea99f6159ee'
translated: false
---

> 原文：[22 short tests of combine – Part 3: Asynchrony | Cocoa with Love](https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-3.html)　·　Cocoa with Love (Matt Gallagher)

I wrote some experiments around Combine, Apple’s reactive programming framework, to gain insight into how Combine handles edge cases that have caused problems for me in other reactive programming frameworks.

Looking at everything in one article got much too long so I broke it into three parts:

1. [re-implementing the core protocols of Combine](https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-1.html)
2. [a trio of topics: shared computation, shared reference lifetimes and sharing subscribers](https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-2.html)
3. asynchrony, threading and performance

This final part will look at asynchronous delivery scenarios. What happens in Combine when the next value arrives while the previous is being processed; in what ways is Combine thread-safe? Can values arrive out-of-order? Can delivered values overwhelm the subscriber? I’ll finish up with a quick look at Combine’s performance.

> **Download**: The code for this series, [CombineExploration, is available on github](https://github.com/mattgallagher/CombineExploration).

> **Warning**: This is not a tutorial for Combine. I won’t be using Combine in anything resembling a conventional manner. This is going to be a look at some edge cases in Combine, testing behaviors that aren’t really documented and may therefore change in future.

## Asynchronous problems

Asynchronous problems are those that process events that occur over time. Most programming languages have no representation of time so we’re reliant on operating-system mediated trickery (blocking, threads and event queues) to let our programming languages handle asynchrony.

Reactive programming offers abstractions over a number of different time-related operating system features but you can primarily treat reactive programming like an event queue, since the events passing through your pipelines will usually be triggered by events from an operating system event queue.

What are the problems that affect event queues?

1. events which overwhelm their consumers
2. consumers which block other processing while waiting on events
3. events on multiple threads triggering memory races
4. events on multiple threads triggering logical races

These problems are what I’ll focus on in this article.

Reactive programming generally takes a “non-blocking” approach to its API so I won’t consider point (2). While a “non-blocking” approach largely eliminates blocking as a source of problems, it means that rendezvous-based synchronization is not possible as a means of addressing point (1) (see Go’s CSP channels for an example of rendezvous-based synchronization).

## Supply and demand

I’m going to start by looking at how Combine handles events which overwhelm their consumers. It’s a weird place to start because Swift’s primary audience (iOS app developers) rarely ever encounter this problem. In front-end application development, the primary source of events is user-interaction and this event stream is usually slow compared to the application’s ability to process it. I’ve chosen this as a starting point though because Combine has a lot of quirks around its design to handle supply and demand scenarios. In this case, I consider a quirk to be a feature that’s more surprising and difficult to manage than it is helpful.

Combine uses a concept called “demand” (an implementation of what is elsewhere called “backpressure”) to determine how many values a downstream subscriber will accept. When an upstream event source generates more values than the subscriber will accept, Combine throws the values away.

In the first part of this series, I implemented the following `receive` function (a per-subscription function that passes values to the downstream `Subscriber` function with the same name) like this:

```swift
func receive(_ input: Input) -> Subscribers.Demand {
   if demand > 0 {
      let newDemand = downstream.receive(input)
      demand = newDemand + (demand - 1)
      return newDemand
   }
   return Subscribers.Demand.none
}
```

You can see that if the current known downstream `demand` is zero, any received `input` is simply discarded. All subscriptions are expected to behave this way: if they don’t _know_ that the downstream subscriber wants a value, they must discard it.

In synchronous scenarios, it’s uncommon to see this causing a problem because most subscribers will immediately request `Demand.unlimited`. To see this happening in a controlled scenario, I’ve created a special `Sink` implementation that allows a custom demand value and subsequent custom increases in demand.

```swift
func testDemand() {
   var received = [Subscribers.Event<Int, Never>]()
   let subject = PassthroughSubject<Int, Never>()
   let sink = CustomDemandSink<Int, Never>(
      demand: 2,
      receiveCompletion: { received.append(.complete($0)) },
      receiveValue: { received.append(.value($0)) }
   )
   subject.subscribe(sink)
   
   subject.send(sequence: 1...3, completion: nil)
   sink.increaseDemand(2)
   subject.send(sequence: 4...6, completion: .finished)
   sink.increaseDemand(2)
   
   XCTAssertEqual(received, [1, 2, 4, 5].asEvents(completion: .finished))
}
```

The initial demand is for 2 values (i.e. the `1, 2` in the received array). The `3` value sent in the first sequence exceeds that demand and is discarded. The demand is increased by 2, 3 more values are sent and again, the last value is discarded.

### Is discarding values ever a good idea?

As a quick look at demand shows: Combine handles inputs overwhelming consumers by discarding inputs. The problem here is that the discarding of data is not accompanied by an error response indicating “server/queue busy” or anything to that effect. It’s a silent failure.

There are very few situations where throwing away data without some kind of special handling of the discarded data is a good idea. The two scenarios where it would make sense to me are when:

1. we want only the “most recent update” to be handled
2. we can respond to the sender with a “server busy error”

If you carefully construct your Combine graph, you can handle the first scenario:

```swift
func testDemandWithBuffer() {
   let subject = PassthroughSubject<Int, Never>()
   var received = [Subscribers.Event<Int, Never>]()
   let sink = CustomDemandSink<Int, Never>(
      demand: 1,
      receiveCompletion: { received.append(.complete($0)) },
      receiveValue: { received.append(.value($0)) }
   )
   subject.buffer(size: 1, prefetch: .byRequest, whenFull: .dropOldest).subscribe(sink)
   
   subject.send(sequence: 1...3, completion: nil)
   sink.increaseDemand(1)
   subject.send(sequence: 4...6, completion: .finished)
   sink.increaseDemand(1)
   
   XCTAssertEqual(received, [1, 3, 6].asEvents(completion: nil))
}
```

Bizarrely, as indicated by the `.asEvents(completion: nil)` at the end, the `.buffer` prevents completion being emitted when used with `.dropOldest` (which seems like a bug). The completion is emitted when `.dropNewest` is used.

The `buffer` lets us ensure “scenario 1” (“most recent update”) is correctly handled.

However, “scenario 2” (responding with a “server busy error”) is much harder. Yes, `buffer` supports a `.customError` case for the `whenFull` parameter but that causes the entire pipeline (the “server”) to fail, rather than the request. Sending errors to the upstream requester would require giving every value in the input a sequence number and triggering a side-effect when values in the sequence are omitted – a careful task that you’d need to manually handle.

In summary, discarding values due to supply exceeding demand can work but you need to carefully build your reactive pipeline appropriately. It’s far more likely that you want to build pipelines that, by design, will _never_ discard values.

### Accidentally discarded asynchronous values

The purpose of this article is to look at asynchronous problems but I haven’t written any asynchronous code. I will, I promise, but let’s look at one last synchronous test case, to establish a baseline:

```swift
func testReceiveOnImmediate() {
   let e = expectation(description: "")
   let subject = PassthroughSubject<Int, Never>()
   var received = [Subscribers.Event<Int, Never>]()
   let c = subject
      .receive(on: ImmediateScheduler.shared)
      .sink(
         receiveCompletion: { 
            received.append(.complete($0))
            e.fulfill()
         },
         receiveValue: { received.append(.value($0)) }
      )
   
   subject.send(1)
   subject.send(completion: .finished)
   wait(for: [e], timeout: 5.0)

   XCTAssertEqual(received, [1].asEvents(completion: .finished))

   c.cancel()
}
```

This is close to the original Combine test I showed in the first part of this series. It sends a value (`1`) and completes. The test calls `.receive(on: ImmediateScheduler.shared)` and waits on an expectation that is fulfilled at the completion of the signal but these steps do practically nothing here because everything completes synchronously.

Let’s try to use `receive(on:)` to perform this work on a background thread:

```swift
func testReceiveOnFailure() {
   let queue = DispatchQueue(label: "test")
   let e = expectation(description: "")
   let subject = PassthroughSubject<Int, Never>()
   var received = [Subscribers.Event<Int, Never>]()
   let c = subject
      .receive(on: queue)
      .sink(
         receiveCompletion: { 
            received.append(.complete($0))
            e.fulfill()
         },
         receiveValue: { received.append(.value($0)) }
      )
   
   subject.send(1)
   queue.async { subject.send(completion: .finished) }
   wait(for: [e], timeout: 5.0)

   XCTAssertEqual(received, [].asEvents(completion: .finished))
   
   c.cancel()
}
```

I’ve added a custom `DispatchQueue`, used by the `.receive(on: queue)` line and I’m sending the completion on this same queue.

The important result to notice is that the `received` array in the `XCTAssertEqual` contains the `completion: .finished` but the value (`1`) has disappeared. If I hadn’t changed the completion to be sent asynchronously on the `queue`, then even the completion would fail to be received.

What happened to the value we sent? Why does trying to send values asynchronously in Combine cause them to fail?

The answer gets back to “demand”, again.

Earlier in this article, I showed “demand” being sent synchronously via the `receive(_ input: Input) -> Subscribers.Demand` function. However, when values are asynchronously received, the demand is communicated asynchronously, via the separate `request(_ demand: Subscribers.Demand)` function on the specified queue.

This is the cause of our lost values: the `request(_ demand: Subscribers.Demand)` function had not run on the background `queue` by the time we called `subject.send(1)`, so the “demand” known to the `PassthroughSubject` is at a default of zero and it simply discarded our value.

Let’s look at this in detail with the `.debug()` publisher:

```swift
func testReceiveWithLogging() {
   let subject = PassthroughSubject<Int, Never>()

   print("Start...")
   var received = [Subscribers.Event<Int, Never>]()
   let cancellable = subject
      .debug()
      .receive(on: DispatchQueue.main)
      .sink(receiveValue: { received.append(.value($0)) })
   
   print("Phase 1...")
   subject.send(1)
   XCTAssertEqual(received, [].asEvents(completion: nil))
   
   print("Phase 2...")
   RunLoop.current.run(until: Date(timeIntervalSinceNow: 0.001))
   XCTAssertEqual(received, [].asEvents(completion: nil))
   
   print("Phase 3...")
   subject.send(2)
   XCTAssertEqual(received, [].asEvents(completion: nil))
   
   print("Phase 4...")
   RunLoop.current.run(until: Date(timeIntervalSinceNow: 0.001))
   XCTAssertEqual(received, [2].asEvents(completion: nil))
   
   cancellable.cancel()
}
```

Instead of running on a background `DispatchQueue`, I’m running everything on the main thread so I can run the `RunLoop` at controlled points.

The `debug()` line here logs each lifecycle event through it so we can see what happens at each point:

```
Start...
testReceiveWithLogging(), line 163: subscription PassthroughSubject
Phase 1...
Phase 2...
testReceiveWithLogging(), line 163: request unlimited
Phase 3...
testReceiveWithLogging(), line 163: output 2
Phase 4...
testReceiveWithLogging(), line 163: cancelled
```

The subscription occurs immediately but the `request` for unlimited values happens only after we let the main scheduler run. Until that point, values we might expect to be sent are completely lost.

This behavior of `receive(on:)` in Combine is dangerously bad to the point where I don’t think `receive(on:)` should ever be used in isolation in its current state. When you create a pipeline of publishers and subscribers, you should be able to immediately send values.

### Safe use of receive(on:)

Bluntly, I think that `receive(on:)` should _always_ include `.buffer` behavior. Here’s a construction that lets `receive(on:)` work as I would expect it to work:

```swift
func testBufferedReceiveOn() {
   let subject = PassthroughSubject<Int, Never>()
   let e = expectation(description: "")
   var received = [Subscribers.Event<Int, Never>]()
   let c = subject
      .buffer(size: Int.max, prefetch: .byRequest, whenFull: .dropNewest)
      .receive(on: DispatchQueue(label: "test"))
      .sink(
         receiveCompletion: {
            received.append(.complete($0))
            e.fulfill()
         },
         receiveValue: { received.append(.value($0)) }
      )
   
   subject.send(1)
   subject.send(completion: .finished)
   wait(for: [e], timeout: 5.0)

   XCTAssertEqual(received, [1].asEvents(completion: .finished))

   c.cancel()
}
```

## Thread safety

Now that we see how “demand” and asynchronous receiving work, we can see that the `testReceiveOnFailure` test case was really an example of a race condition. There was no **memory race** (multiple threads accessing the same memory at the same time) but there was a **logical race** (where steps were not performed in the expected order due to thread timing). We fixed this race by including a buffer (which establishes demand synchronously) but this does raise the question: what actions are thread-safe in Combine? Are any actions explicitly thread unsafe?

It’s difficult to know what thread safety guarantees exist in Combine because the documentation is surprisingly empty of thread safety discussion. A web search across the Combine documentation reveals only: “Canceling a Subscription must be thread-safe” on the description of the `Subscription` protocol.

Let’s try some crazy things and see if we can get some thread-unsafety.

### Is cancelling a subscription thread-safe?

As I showed at the end of the [previous article](https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-2.html#looking-forward), cancelling a subscription is not asynchronously safe:

```swift
func testSinkCancellationPlusAsyncDelivery() {
   var received = [Subscribers.Event<Int, Never>]()
   let sink = Just(1)
      .receive(on: DispatchQueue.main)
      .sink(event: { e in received.append(e) })

   sink.cancel()
   XCTAssertEqual(received, [].asEvents(completion: nil))

   RunLoop.main.run(until: Date(timeIntervalSinceNow: 0.001))
   XCTAssertEqual(received, [1].asEvents(completion: .finished))
}
```

This test shows us cancelling a sink, at which point we have received no values. Later a value arrives, even though we our cancelled sink.

This isn’t a memory race between threads (the narrowest definition of thread-safety) but this is a failure to preserve semantics when threads act in a valid but unexpected order could be considered thread-unsafe broader definitions. Certainly, the problem is likely to cause headaches in a number of threaded and asynchronous scenarios.

This is probably just a bug but it speaks of a lack of testing in Combine around asynchronous scenarios. The problem itself is easily fixed once you’re aware that the problem can occur. I’ve implemented one possible solution (by checking for a `subscribed` state when receiving) in my `CustomSink`, so the test will pass when swapping `customSink` in place of `sink`:

```swift
   func testSinkCancellationPlusImmediateAsyncDelivery() {
      var received = [Subscribers.Event<Int, Never>]()
      let sequence = Just(1)
         .receive(on: DispatchQueue.main)
         .customSink(
            receiveCompletion: { c in received.append(.complete(c)) },
            receiveValue: { v in received.append(.value(v)) }
         )
      
      sequence.cancel()
      XCTAssertEqual(received, [].asEvents(completion: nil))
      
      RunLoop.main.run(until: Date(timeIntervalSinceNow: 0.001))
      XCTAssertEqual(received, [].asEvents(completion: nil))
   }
```

### Mutual exclusion

Let’s simulate a possible cause of memory races by trying to run a closure simultaneously on multiple threads.

What happens if we simultaneously send a value to a `Subject`/`Subscriber` pair from a hundred different threads at the same time? Will our `Subscriber`’s handler closure be concurrently invoked, causing thread safety problems?

```swift
func testSubjectOrder() {
   let sequenceLength = 100
   let subject = PassthroughSubject<Int, Never>()
   let semaphore = DispatchSemaphore(value: 0)
   
   let total = AtomicBox<Int>(0)
   var collision = false
   let c = subject
      .sink(receiveValue: { value in
         if total.isMutating {
            // Check to see if this closure is concurrently invoked
            collision = true
         }
         total.mutate { total in
            // Make sure we're in the handler for enough time to get a concurrent invocation
            Thread.sleep(forTimeInterval: 0.001)
            total += value
            if total == sequenceLength {
               semaphore.signal()
            }
         }
      })
   
   // Try to send from a hundred different threads at once
   for _ in 1...sequenceLength {
      DispatchQueue.global().async {
         subject.send(1)
      }
   }
   
   semaphore.wait()
   c.cancel()
   XCTAssertEqual(total.value, sequenceLength)
   XCTAssertFalse(collision)
}
```

This test confirms the `receiveValue` closure is never invoked simultaneously on multiple threads.

Inspecting the call to `receiveValue` in the debugger reveals that the `PassthroughSubject.Conduit.offer` function appears to block in an `os_unfair_lock` if another thread is sending through the `PassthroughSubject`.

Short answer: Combine does appear to be thread-safe due to mutexes applied by `Subject`s.

### Sequence ordering

What happens if we do something thread unsafe in the middle of a pipeline?

Instead of sending values from 100 threads at one pipeline, lets send 100 values down one pipeline via a concurrent (and therefore non-ordered) scheduler.

```swift
func testDeliveryOrder() {
   var received = [Subscribers.Event<Int, Never>]()
   let sequence = Publishers.Sequence<ClosedRange<Int>, Never>(sequence: 1...10)
   let e = expectation(description: "")
   let c = sequence
      .receive(on: DispatchQueue.global())
      .receive(on: DispatchQueue.main)
      .sink(
         receiveCompletion: {
            received.append(.complete($0))
            e.fulfill()
         },
         receiveValue: { received.append(.value($0)) }
      )
   withExtendedLifetime(c) { wait(for: [e], timeout: 5.0) }
   XCTAssertNotEqual(received, (1...10).asEvents(completion: .finished))
}
```

If you use a concurrent queue, you lose your sequence ordering. I guess that makes sense but it’s worth keeping in mind that if ordering is important, then don’t use `DispatchQueue.global()`.

### Re-entrancy

Does Combine allow same-thread re-entrancy?

```swift
func testReentrancy() {
   let subject = PassthroughSubject<Int, Never>()
   var received = [Subscribers.Event<Int, Never>]()
   let subscriber = Subscribers.Sink<Int, Never>(
      receiveCompletion: { received.append(.complete($0)) },
      receiveValue: { v in
         if v < 3 {
            subject.send(v + 1)
         }
         received.append(.value(v))
      }
   )
   subject.subscribe(subscriber)
   
   subject.send(sequence: 1...1, completion: .finished)
   XCTAssertEqual(received, [3, 2, 1].asEvents(completion: .finished))
   
   subscriber.cancel()
}
```

Yes, it does. Despite using an `os_unfair_lock` (usually non-reentrant) as its mutex, `PassthroughSubject` allows same-thread re-entrancy. This operates as classic functional recursion and has the expected consequences (here, the values are appended in the reverse order to which they arrive).

For comparison, here’s another test that attempts re-entrancy via a second thread (attempting a send from the main thread onto a background thread for a `Subject` that is already sending):

```swift
#if false
// NOTE: this test deadlocks
func testDeadlock() {
   let subject = PassthroughSubject<Int, Never>()
   let semaphore = DispatchSemaphore(value: 0)
   
   let sequenceLength = 100
   var total = 0
   let t = mach_absolute_time()
   let c = subject
      .sink(receiveValue: { value in
         total += value
         if total < sequenceLength {
            DispatchQueue.main.sync { subject.send(1) }
         }
      })
   DispatchQueue.global().async { subject.send(1) }
   while total < sequenceLength {
      RunLoop.current.run(until: Date(timeIntervalSinceNow: 0.001))
   }
   c.cancel()
   
   XCTAssertEqual(total, sequenceLength)
}
#endif
```

As you’d expect, given a recursive mutex, it deadlocks.

## Performance

Do you need maximum performance in your reactive programming framework? Probably not.

For the reactive programming framework to cause performance problems, you need to be sending a _lot_ of messages between components. Tens thousand messages per second is the point where you might start to care about the speed of the reactive programming framework, rather than the code it invokes. In these cases, it would be possible for a poorly implemented message transport mechanism to become a bottleneck.

This is _not_ common when using reactive programming for bindings in user-applications. User-initiated events rarely exceed hundreds per second. However, if you’re using reactive programming as part of a processing queue then it becomes easily possible.

Even with a poorly performing reactive programming framework, you can usually avoid bottlenecks in your transport mechanism by aggregating inter-component messages. However, it’s nice to know that your transport is high performance so you can wait longer before needing to take optimizing steps and you won’t have to make decisions that trade latency for throughput.

### A few scenarios

I ran a three-way performance test between Combine, RxSwift and CwlSignal.

|  | Combine | RxSwift | CwlSignal |
|---|---|---|---|
| Subject send | **5.021** | 3.826 | 4.495 |
| Sequence send | **1.154** | 0.288 | 1.052 |
| Async send | 0.200 | 0.359 | **1.280** |
| Deep pipeline | **2.624** | 1.814 | 0.176 |

<sub>Performance on macOS 10.15 beta 6 in millions of values sent per second (higher is better)</sub>

What do these numbers tell us? Frankly, none of these numbers are too bad.

The “async send” number (critical for most operations queues where performance really matters) is a little low for Combine. Part of this slow performance is because I put a `.buffer` in the pipeline ahead of the `receive(on:)` (without this `.buffer` the number would be closer to 0.5 than 0.2 but that’s still a little slow).

Annoying workarounds and async issues notwithstanding, Combine is a good, high performance framework. While modern CPUs can perform billions of operations per second, it is _difficult_ to reach 5 million iterations per second in code involving generics and mutexes, so Combine has done well.

These figures are from macOS 10.15 beta 6, running on my Mac Book Pro 2018. In beta 4, the Combine numbers looked like this:

|  | Combine | RxSwift | CwlSignal |
|---|---|---|---|
| Subject send | 0.891 | 3.782 | **4.512** |
| Sequence send | **1.011** | 0.277 | 0.998 |
| Async send | 0.140 | 0.359 | **1.112** |
| Deep pipeline | 0.954 | **1.888** | 0.180 |

<sub>Performance on macOS 10.15 beta 4 in millions of values sent per second (higher is better)</sub>

You can see that since beta 4, Combine has dramatically improved on most tests. However, these numbers have been bouncing around from beta to beta (in macOS 10.15 beta 5, Combine briefly peaked at 7 million values per second on the “Subject send” test and has since dropped down to 5 million).

## Conclusion

> **Download**: The code for this series, [CombineExploration, is available on github](https://github.com/mattgallagher/CombineExploration).

I’ve been hard on Combine in these three articles. I don’t think Combine is a bad framework but in its current state, I think there are a few critical areas where it works badly. I think these problem areas are going to cause reliability issues for many developers until they are addressed.

To me, the most important improvements Combine should make are:

1. `Subscription` and other “black boxes” should be fully documented (we shouldn’t be guessing about thread safety and graph lifecycles)
2. support buffered subjects and other ways of sharing cached computations
3. support scenarios where demand must never be zero
4. `receive(on:)` should synchronously establish initial demand (only `subscribe(on:)` should asynchronously complete construction)

I’ve shown that we can work around these problems but proper fixes will need to occur in Combine itself.

It’s apparent that Combine has kept to many of the overall goals of the [Reactive Streams initiative](https://www.reactive-streams.org). This initiative is promoted by groups that work with networked, multi-client, server-limited processing. The strict mandates for subscriptions and asynchronous backpressure support that use case but in my use cases (view-bindings and single-client operation queues), I’ve found the entire concepts of backpressure and subscriptions to be a hinderance and a source of spurious failures and design challenges.

What I want from Combine is to better support scenarios where multi-subscribing and demand are effectively disabled (have no measurable effect) and to focus more on caching sequences emitted by hot publishers for sharing between dynamically changing subscribers because this is the natural way to program in an imperative programming language.
