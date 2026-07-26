---
title: '22 short tests of combine – Part 2: Sharing | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-2.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:988c3373c88ad66e'
translated: false
---

> 原文：[22 short tests of combine – Part 2: Sharing | Cocoa with Love](https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-2.html)　·　Cocoa with Love (Matt Gallagher)

I wrote some experiments around Combine, Apple’s reactive programming framework, to gain insight into how Combine handles edge cases that have caused problems for me in other reactive programming frameworks.

Looking at everything in one article got much too long so I broke it into three parts:

1. re-implementing the core protocols of Combine
2. shared computation, shared reference lifetimes and sharing subscribers
3. asynchrony, threading and performance

This article will be the middle third, an investigation spanning a trio of topics with “shared” in the name: shared computation, shared reference lifetimes and sharing subscribers.

> **Download**: The code for this series, [CombineExploration, is available on github](https://github.com/mattgallagher/CombineExploration).

> **Warning**: This is not a tutorial for Combine. I won’t be using Combine in anything resembling a conventional manner. This is going to be a look at some edge cases in Combine, testing behaviors that aren’t really documented and may therefore change in future.

## Hot and cold publishers

In [the previous article](https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-1.html), I focussed on Combine’s largely hidden `Subscription` type and the fact that Combine creates a new graph of `Subscription` types for every new subscriber. Using this independent subscription graph allows Combine to follow the “cold publisher” model:

> A **cold publisher** is one where the emitted sequence of values is lazily constructed and traversed when requested by a downstream subscriber. Asynchronous tasks begin on subscription, not construction of the publisher. The graph may not change structure for the entire duration of the sequence.

The terms "cold publisher" and "hot publisher" are usually "cold observable" and "hot observable" in other Rx frameworks. I've changed the terminology to match Combine's terms but the ideas are equivalent.

In a “cold publisher” graph, you don’t need to cache values because a value exists only at the moment it is requested by a subscriber and immediately handed over. A subscriber cannot re-request old values and any request for values made by a new subscriber is really a request to calculate the values again. Caching values emitted from a “cold publisher” graph doesn’t make sense.

However, this model isn’t practical outside of strict functional programming languages. Aside from the fact that we don’t want to waste time calculating the same values, there is also the problem of network data, the filesystem, host time, user interactions and other side effects that may start before our program is ready and run independent of any Combine graph we may have created and will never play nicely with a “cold publisher” model.

In imperative programming, we need “hot publishers”.

> A **hot publisher** may produce values at any time and at any rate, regardless of the demand from downstream subscribers. The graph may continue to change in structure during the sequence. Publishers must encode rules about what to do with values that exceed downstream demand or how to handle new subscribers joining an existing value sequence.

In almost all cases, a “hot publisher” in Combine will use a `Subject` (either externally or internally). `Subject`s play an important role in “hot” graphs because a `Subject` is a publisher with a single shared identity (most publishers create a new independent identity for each downstream subscription).

## Sharing via multicast

The essential part of working with a graph that contains “hot publishers” is that you must be able to handle new subscribers joining in the middle of a sequence.

In the previous article, I discussed the idea that there were 5 different kinds of approach to handling multiple subscribers:

1. multicast
2. caching
3. latest value
4. custom caching
5. resubscribe

but I looked only at resubscribe because this is the “cold publisher” favored option in Combine.

In my `testOverlappingABCD` example showing “resubscribe” behavior, I used `Deferred` to simulate a “cold publisher” while still offering the ability to manually send values into each subscription. Let’s change this example to remove the independent `PassthroughSubject`s created inside a `Deferred` closure and instead use a single, shared `PassthroughSubject` (without `Deferred`).

```swift
func testSharedSubjectABCD() {
   let subjectA = PassthroughSubject<Int, Never>()
   let scanB = subjectA.scan(10) { state, next in state + next }

   var receivedC = [Subscribers.Event<Int, Never>]()
   let sinkC = scanB.sink(event: { e in receivedC.append(e) })
   subjectA.send(sequence: 1...2, completion: nil)
   
   var receivedD = [Subscribers.Event<Int, Never>]()
   let sinkD = scanB.sink(event: { e in receivedD.append(e) })
   subjectA.send(sequence: 3...4, completion: .finished)
   
   XCTAssertEqual(receivedC, [11, 13, 16, 20].asEvents(completion: .finished))
   XCTAssertEqual(receivedD, [13, 17].asEvents(completion: .finished))
   
   sinkC.cancel()
   sinkD.cancel()
}
```

This no longer behaves like “resubscribe”. Now, `D` receives only 2 values – related to the two values sent after it connected.

This is almost what we’d expect in a “multicast” scenario except that `D` doesn’t receive the same `16, 20` that `C` receives. Instead, it receives `13, 17`. What happened?

This graph has two conflicting ideas:

1. is a shared “hot” publisher
2. is a “cold” publisher and a separate value of the

  is created for each subscriber

While the `PassthroughSubject` is shared between `C` and `D`, there are two separate `Subscription` instances created for the `scan` (with different values of `state`) so we get different outputs.

This is an example of hot publishers and stateful cold publishers playing poorly together. To eliminate this strangeness, we need to entirely enclose the `scan` publisher in “hot” endpoints so that only one `scan` subscription is ever created.

We can do this by putting a `Publishers.Multicast` after the `scan` publisher:

```swift
func testMulticastABCD() {
   let subjectA = PassthroughSubject<Int, Never>()
   let multicastB = subjectA
      .scan(10) { state, next in state + next }
      .multicast { PassthroughSubject() }
   let cancelB = multicastB.connect()
   
   var receivedC = [Subscribers.Event<Int, Never>]()
   let sinkC = multicastB.sink(event: { e in receivedC.append(e) })
   subjectA.send(sequence: 1...2, completion: nil)
   
   var receivedD = [Subscribers.Event<Int, Never>]()
   let sinkD = multicastB.sink(event: { e in receivedD.append(e) })
   subjectA.send(sequence: 3...4, completion: .finished)
   
   XCTAssertEqual(receivedC, [11, 13, 16, 20].asEvents(completion: .finished))
   XCTAssertEqual(receivedD, [16, 20].asEvents(completion: .finished))
   
   sinkC.cancel()
   sinkD.cancel()
   cancelB.cancel()
}
```

We now have `C` and `D` correctly receiving a “multicast” version of the same stream. `D` receives the same `16, 20` values that `C` receives after it subscribes.

## Caching computation

The other forms of “shared computation” that I mentioned (“caching”, “latest value” and “custom caching”) are all forms of holding onto recently emitted values.

Combine offers just one built-in way of doing this: `CurrentValueSubject`, which offers “latest value” caching. We can use this by replacing the `PassthroughSubject<Int, Never>()` in the previous test with `CurrentValueSubject<Int, Never>(0)`. Running the test in this way confirms the following values:

```swift
XCTAssertEqual(receivedC, [0, 11, 13, 16, 20].asEvents(completion: .finished))
XCTAssertEqual(receivedD, [11, 13, 17].asEvents(completion: .finished))
```

A `CurrentValueSubject` is great for user-interfaces that always need a value and need only the latest “state” from an publisher or service.

Beyond user-interfaces though, we often need more of the stream than the latest value.

You might think that the `Publishers.Buffer` operator in Combine could help with this, however, this operator is actually for managing demand between a hot publisher and a downstream subscriber and doesn’t apply to buffering between downstream subscriber. The `Record` publisher also doesn’t seem quite right as it doesn’t really stream values from an upstream publisher. Unless I’m missing something, there _isn’t_ a way to multicast with a playback buffer greater than one value in Combine.

What would be needed is a `Subject`, like `CurrentValueSubject`, that can buffer more than just the latest value (and doesn’t force an initial value, if none has yet been received).

I’ve implemented a custom subject to handle this scenario: `BufferSubject`. Dropping `BufferSubject(limit: Int.max)` in place of the subject constructor in the last test confirms the following values:

```swift
XCTAssertEqual(receivedC, [11, 13, 16, 20].asEvents(completion: .finished))
XCTAssertEqual(receivedD, [11, 13, 16, 20].asEvents(completion: .finished))
```

This is a completely cached, “playback” sequence, shared between `C` and `D`. Values pass through `scan` and are sent immediately to `C` but buffered and replayed for `D` when it subscribes.

## Reference lifetimes

In the previous test cases, I’ve been carefully calling `cancel()` on the `Subscribers.Sink` and the `connect()` results. This behavior is not because I wanted to cancel these values but instead because I wanted to guarantee that I was keeping their references alive so their associated subscriptions don’t get cancelled until the end of the function.

Is carefully keeping references alive strictly necessary?

The answer is complicated to test for two reasons:

1. In Release builds, Swift may release references in the middle of a scope (like a function) but in Debug builds, Swift usually won’t release until the end of the scope.
2. is a reference that calls

  automatically on

  . Other types of

  will usually not but might (you never know).

Neither of these rules make accurate analysis easy. Let’s start with some examples that use `AnyCancellable` (avoiding complications with point 2) and deliberately create our own dummy scopes (which will avoid most complications with point 1).

This is how `AnyCancellable` behaves:

```swift
func testAnyCancellable() {
   let subject = PassthroughSubject<Int, Never>()
   var received = [Subscribers.Event<Int, Never>]()

   weak var weakCancellable: AnyCancellable?
   do {
      let anyCancellable = subject.sink(event: { e in received.append(e) } )
      weakCancellable = anyCancellable
      subject.send(1)
   }
   XCTAssertNil(weakCancellable)
   
   subject.send(2)
   XCTAssertEqual(received, [1].asEvents(completion: nil))
}
```

The `anyCancellable` falls out of scope at the end of the `do {}`, cancelling the subscription so sending the second value (`send(2)`) has no effect.

This is probably the behavior that is most in-line with expectations but let’s look instead at raw use of `Subscribers.Sink`, which conforms to `Cancellable` but does not offer the same “auto-cancel when released” guarantee:

```swift
func testSinkCancellation() {
   let subject = PassthroughSubject<Int, Never>()
   var received = [Subscribers.Event<Int, Never>]()
   
   weak var weakSink: Subscribers.Sink<Int, Never>?
   do {
      let sink = Subscribers.Sink<Int, Never>(
         receiveCompletion: { received.append(.complete($0)) },
         receiveValue: { received.append(.value($0)) }
      )
      weakSink = sink
      subject.subscribe(sink)
      
      subject.send(1)
   }
   XCTAssertNotNil(weakSink)
   
   subject.send(2)
   weakSink?.cancel()
   subject.send(3)
   XCTAssertEqual(received, [1, 2].asEvents(completion: nil))
}
```

The `Sink` is not strongly referenced outside the `do {}` but is still alive when the `send(2)` value reaches the `received` array. It is only when we _explicitly_ call `cancel()` that further values stop being delivered.

If we drop all our strong references to `Sink`, it can continue to receive values while there is an active subscription. In fact, we can drop our `PassthroughSubject`, too:

```swift
func testOwnership() {
   var received = [Subscribers.Event<Int, Never>]()

   weak var weakSubject: PassthroughSubject<Int, Never>?
   weak var weakSink: Subscribers.Sink<Int, Never>?
   do {
      let subject = PassthroughSubject<Int, Never>()
      weakSubject = subject
      let sink = Subscribers.Sink<Int, Never>(
         receiveCompletion: { received.append(.complete($0)) },
         receiveValue: { received.append(.value($0)) }
      )
      weakSink = sink
      subject.subscribe(sink)
   }
   XCTAssertNotNil(weakSubject)
   XCTAssertNotNil(weakSink)

   weakSubject?.send(1)
   weakSubject?.send(completion: .finished)

   XCTAssertNil(weakSubject)
   XCTAssertNil(weakSink)
   XCTAssertEqual(received, [1].asEvents(completion: .finished))
}
```

We don’t have to hold _any_ references to the graph. It continues to stay alive, all on its own, until the current subscription completes.

This is a dangerous scenario. In short, to have sane memory management with Combine, you _must_ ensure there is at least one `AnyCancellable` connected to your graph.

## Multiple subscriptions

Many of these test cases have focussed on what happens when there are multiple `Subscriber`s connected to the same `Publisher`.

What happens if you do the inverse: take a single `Subscribers.Sink` and subscribe it to multiple `Publisher`s?

```swift
func testMultipleSubscribe() {
   let subject1 = PassthroughSubject<Int, Never>()
   let subject2 = PassthroughSubject<Int, Never>()
   var received = [Subscribers.Event<Int, Never>]()
   let sink = Subscribers.Sink<Int, Never>(
      receiveCompletion: { received.append(.complete($0)) },
      receiveValue: { received.append(.value($0)) }
   )
   subject1.subscribe(sink)
   subject2.subscribe(sink)

   subject1.send(sequence: 1...2, completion: .finished)
   subject2.send(sequence: 3...4, completion: .finished)
   
   XCTAssertEqual(received, (1...2).asEvents(completion: .finished))
}
```

Short answer: the `Sink` remains subscribed to the first subject and ignores everything from the second. However, it’s not an error of any kind, just a silent failure. It seems like sharing a `Subscriber` isn’t something you should ever do.

This test isn’t just abstract interface abuse. I want something that offers the ability to subscribe multiple times to different upstream subscriptions with this kind of simplicity. For the first subscription to a `Publisher`, the downstream `Subscriber` will own the subscription and will `cancel` it if the downstream nodes are cancelled. It’s elegant and self-contained but handles just one subscription.

The only multi-subscribable interface in Combine, by default, is `Subject`:

```swift
func testMultiSubjectSubscribe() {
   let subject1 = PassthroughSubject<Int, Never>()
   let subject2 = PassthroughSubject<Int, Never>()
   let multiInputSubject = PassthroughSubject<Int, Never>()
   let cancellable1 = subject1.subscribe(multiInputSubject)
   let cancellable2 = subject2.subscribe(multiInputSubject)
   var received = [Subscribers.Event<Int, Never>]()
   let multiInputCancellable = multiInputSubject.sink(
      receiveCompletion: { received.append(.complete($0)) },
      receiveValue: { received.append(.value($0)) }
   )
   
   subject1.send(sequence: 1...2, completion: nil)
   subject2.send(sequence: 3...4, completion: .finished)
   
   XCTAssertEqual(received, [1, 2, 3, 4].asEvents(completion: .finished))

   cancellable1.cancel()
   cancellable2.cancel()
   multiInputCancellable.cancel()
}
```

This works – the `multiInputCancellable` receives from both `subject` and `subject2` – but you must hold onto each `AnyCancellable` and there’s no implicit cancellation of upstream subscriptions the subject falls out of scope.

Fortunately, it’s very easy to set up a better approach where these upstream `Cancellable`s are held internally and automatically cancelled when the downstream is cancelled. It involves little more than a combination of the subjects and sinks from the previous test, hidden behind a clean interface:

```swift
func testMergeSink() {
   var received = [Subscribers.Event<Int, Never>]()
   let subject1 = PassthroughSubject<Int, Never>()
   let subject2 = PassthroughSubject<Int, Never>()
   let input = MergeInput<Int>()
   subject1.merge(into: input)
   subject2.merge(into: input)
   let cancellable = input.sink(receiveValue: { received.append(.value($0)) })

   subject1.send(sequence: 1...2, completion: .finished)
   subject2.send(sequence: 3...4, completion: .finished)
   
   XCTAssertEqual(received, [1, 2, 3, 4].asEvents(completion: nil))

   cancellable.cancel()
}
```

This `MergeInput` interface does not receive completion from upstream publishers. This is an intentional choice: for this type of multi-input scenario, you generally don’t want one input to close the `MergeInput` and cut off all other inputs.

The previous tests revealed that a `Subscriber` will not accept new subscriptions while it already has an active subscription. A related question is: what happens if you subscribe to a second `Publisher` after the first subscription completes? Can you “reactivate” a completed subscriber?

```swift
func testSinkReactivation() {
   var received = [Subscribers.Event<Int, Never>]()
   let sink = Subscribers.Sink<Int, Never>(
      receiveCompletion: { received.append(.complete($0)) },
      receiveValue: { received.append(.value($0)) }
   )
   
   weak var weakSubject: PassthroughSubject<Int, Never>?
   do {
      let subject = PassthroughSubject<Int, Never>()
      weakSubject = subject
      subject.subscribe(sink)
      
      subject.send(1)
   }
   XCTAssertNotNil(weakSubject)
   
   weakSubject?.send(completion: .finished)
   
   // At this point, the first subscription to sink is finished
   XCTAssertNil(weakSubject)
   XCTAssertEqual(received, [1].asEvents(completion: .finished))
   
   // Try to start a new one
   let subject2 = PassthroughSubject<Int, Never>()
   subject2.subscribe(sink)
   subject2.send(2)
   
   #if false
      // Prior to macOS 10.15 beta 6...
      XCTAssertEqual(received,
         [1].asEvents(completion: .finished) + [2].asEvents(completion: nil)
      )
   #else
      // In macOS 10.15 beta 6...
      XCTAssertEqual(received,
         [1].asEvents(completion: .finished)
      )
   #endif
}
```

This is an example of behavior that changed while I was writing this series on Combine. Until macOS 10.15 beta 7, it was possible to reuse a subscriber, once any previous subscription completed.

Apparently, that changed in beta 7. Now, a `Subscriber` is strictly a non-shareable object. It lives for the duration of a subscription and subsequently declines to do anything more.

## Conclusion

> **Download**: The code for this series, [CombineExploration, is available on github](https://github.com/mattgallagher/CombineExploration).

I don’t personally like cold publishers. I think they are a counter-intuitive solution to some edge cases that can create problems in some common cases. Any interaction between hot publishers and stateful cold publishers needs to be carefully managed to achieve consistent outputs.

Combine offers no built-in way to cache more than a single value. Fortunately, I’ve shown that it isn’t particularly difficult to buffer additional values by creating a custom `BufferSubject` that you can use with `Multicast`.

The subscriber graph in Combine maintains a reference counted loop while a subscription is active. If you’re using `.sink` (or a handful of other convenience methods) as part of your graph, this won’t matter, since the returned `AnyCancellable` will break the loop. However, more manual constructions – like using `Subscribers.Sink` – don’t offer the same convenience so be careful to wrap types in `AnyCancellable` as appropriate to avoid memory leaks.

Tests reveal `Subscribers.Sink` will not trigger any kind of error if you subscribe it multiple times but it will not listen to new subscriptions.

If you want a sink that handle multiple inputs, you must use a `Subject`. The default `Publisher.subscribe(Subject)` is a little fussy (requiring you hold onto additional `Cancellable` instances) so I provided a convenience `merge(into:)` for the purpose.

### Looking forward…

Given the tested behavior showing `Subscriber` ignores subsequent subscriptions and attempts at reuse after completion, you might expect that `Subscriber` will never emit values once it reaches the end of a sequence or is cancelled.

You’d be wrong.

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

This test shows us cancelling a sink, at which point we have received no values. Later a value arrives on our cancelled sink.

There’s a possibility that this behavior is Combine “behaving as expected” but realistically there is no scenario where this is a good outcome. Combine has some serious rough edges around anything asynchronous and this is not the only scenario that causes problems.

In the final part of this series, I’ll look at why this behavior occurs and some possible workarounds until Combine fixes its design to eliminate these problems.
