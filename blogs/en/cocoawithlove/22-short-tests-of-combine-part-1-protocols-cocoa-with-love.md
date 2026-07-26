---
title: '22 short tests of Combine – Part 1: Protocols | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-1.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:539f37f4ea9a73b5'
translated: false
---

> 原文：[22 short tests of Combine – Part 1: Protocols | Cocoa with Love](https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-1.html)　·　Cocoa with Love (Matt Gallagher)

I wrote some experiments around Combine, Apple’s reactive programming framework, to gain insight into how Combine handles edge cases that have caused problems for me in other reactive programming frameworks. How do subscriptions work? How do I cache computations? When are publishers and subscribers released? Under what circumstances is Combine thread-safe? Is re-entrancy possible? Does Combine guarantee delivery-order? How does Combine’s performance compare to pre-existing reactive frameworks?

Looking at everything in one article got much too long so I broke it into three parts:

1. re-implementing the core protocols of Combine
2. [a trio of topics: shared computation, shared reference lifetimes and sharing subscribers](https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-2.html)
3. [asynchrony, threading and performance](https://www.cocoawithlove.com/blog/twenty-two-short-tests-of-combine-part-3.html)

This article will be the first third of my investigation, covering an effort to re-implement the three key protocols of Combine: `Publisher`, `Subscriber` and `Subscription`.

> **Download**: The code for this series, [CombineExploration, is available on github](https://github.com/mattgallagher/CombineExploration).

> **Warning**: This is not a tutorial for Combine. I won’t be using Combine in anything resembling a conventional manner. This is going to be a look at some edge cases in Combine, testing behaviors that aren’t really documented and may therefore change in future.

Apple’s Combine is built around two key protocols, `Publisher` and `Subscriber`.

> **The naïve intepretation of Combine** is that a `Publisher` emits a sequence of values.

This common interpretation is not accurate but the distinction between this “naïve” interpretation and an “accurate” interpretation is rare enough that we often ignore the difference.

`Publisher` is defined as:

```swift
protocol Publisher {
   associatedtype Output
   associatedtype Failure : Error
   func receive<S>(subscriber: S) where S : Subscriber, Self.Failure == S.Failure, Self.Output == S.Input
}
```

According to the protocol, a `Publisher` does not emit values but receives `Subscriber`s. Of course, depending on what a `Subscriber` is, the `Publisher` might still directly emit values into these `Subscriber`s that it receives.

So let’s look at the `Subscriber` protocol for a clearer picture:

```swift
protocol Subscriber : CustomCombineIdentifierConvertible {
   associatedtype Input
   associatedtype Failure : Error
   func receive(_ input: Self.Input) -> Subscribers.Demand
   func receive(completion: Subscribers.Completion<Self.Failure>)
   func receive(subscription: Subscription)
}
```

Ignoring that last function for now, the other functions here on `Subscriber` appear to support the “naïve” interpretation: the `Publisher` receives `Subscriber`s and can send `Input` values or `Completion` events directly to all known `Subscriber`s.

Let’s establish a “control case” to which we can compare other tests, starting with a fairly standard test of the `Publisher` and `Subscriber` model where a `Subscribers.Sink` (a typical `Subscriber`) is subscribed to a `PassthroughSubject` (not exactly a typical `Publisher` but helpful in tests since it lets us inject values easily from outside) and we record the values that pass from the subject to the sink.

```swift
func testSubjectSink() {
   let subject = PassthroughSubject<Int, Never>()
   var received = [Subscribers.Event<Int, Never>]()
   let sink = Subscribers.Sink<Int, Never>(
      receiveCompletion: { received.append(.complete($0)) },
      receiveValue: { received.append(.value($0)) }
   )
   
   subject.subscribe(sink)
   subject.send(sequence: 1...3, completion: .finished)
      
   XCTAssertEqual(received, (1...3).asEvents(completion: .finished))
}
```

This test includes a few of my own additions to make the tests easier:

- `Subscribers.Event` is just an “either” over the `Value` and `Completion` types of a Combine sequence
- `send(sequence:completion:)` sends all values in the sequence and the completion
- `asEvents` creates an array of `Subscribers.Event` from an array of `Value` and a `Completion`.

This test conforms to the “naïve” interpretation: values are sent to the subject are received by the closure we passed to the sink.

## Graph mutations over time

Imagine a basic subject, `A`, that generates values over time (e.g. a network connection), followed by a stateful transforming node `B` (e.g. a `scan` or similar streaming processor), followed by an observer `C` (e.g. a `Sink`):

![](https://www.cocoawithlove.com/assets/blog/combine1.svg)

```swift
func testScan() {
   let subjectA = PassthroughSubject<Int, Never>()
   let scanB = Publishers.Scan(upstream: subjectA, initialResult: 10) { state, next in state + next }
   var receivedC = [Subscribers.Event<Int, Never>]()
   let sinkC = Subscribers.Sink<Int, Never>(
      receiveCompletion: { receivedC.append(.complete($0)) },
      receiveValue: { receivedC.append(.value($0)) }
   )

   scanB.subscribe(sinkC)
   subjectA.send(sequence: 1...4, completion: .finished)
   
   XCTAssertEqual(receivedC, [11, 13, 16, 20].asEvents(completion: .finished))
}
```

There’s an extra transformation line (the `scanB` line) but relative to the original control case it’s not much different.

Now, what happens when, halfway through `A` streaming its data, a new observer `D` subscribes to `B`, totally unaware that `B` is already in the middle of its output?

![](https://www.cocoawithlove.com/assets/blog/combine2.svg)

Should the new listener `D` get half the data it expected, even though it doesn’t know about `C` and the fact that the connection is already started?

The answer is complicated. Depending on your program’s logic, you may want _any_ of the following options:

1. **multicast** – `D` receives the second half of the values that `C` receives
2. **caching** – the first half is buffered and `D` immediately receives the first half of the message upon joining and new values like multicast
3. **latest value** – `D` receives the last emitted value immediately and new values like multicast
4. **custom caching** – `D` receives only as much as needed (e.g. since the last keyframe or resume point) and new values like multicast
5. **resubscribe** – `D` should trigger all upstream nodes to restart their work, go all the way back to the network and re-request all data, performing all calculations, again

In this article, I will focus only on the last of these options since it is, arguably, the default behavior in Combine. In the next article, I’ll look at the other approaches.

For now though, here’s an example of resubscribe behavior:

```swift
func testSequenceABCD() {
   let sequenceA = Publishers.Sequence<ClosedRange<Int>, Never>(sequence: 1...4)
   let scanB = Publishers.Scan(upstream: sequenceA, initialResult: 10) { state, next in state + next }
   var receivedC = [Subscribers.Event<Int, Never>]()
   let sinkC = Subscribers.Sink<Int, Never>(
      receiveCompletion: { receivedC.append(.complete($0)) },
      receiveValue: { receivedC.append(.value($0)) }
   )
   var receivedD = [Subscribers.Event<Int, Never>]()
   let sinkD = Subscribers.Sink<Int, Never>(
      receiveCompletion: { receivedD.append(.complete($0)) },
      receiveValue: { receivedD.append(.value($0)) }
   )

   scanB.subscribe(sinkC)
   scanB.subscribe(sinkD)
   
   XCTAssertEqual(receivedC, [11, 13, 16, 20].asEvents(completion: .finished))
   XCTAssertEqual(receivedD, [11, 13, 16, 20].asEvents(completion: .finished))
}
```

None of the nodes here are recreated and most importantly, the `B` node – the stateful `scan` processor – is shared between subscriptions, yet each of `C` and `D` receive an independent version of the values.

In case you think something weird is happening because the sequences don’t actually overlap in time, here’s an equivalent test where the sequences values are manually delivered in an overlapping fashion:

```swift
func testOverlappingABCD() {
   var subjects = [PassthroughSubject<Int, Never>]()
   let deferred = Deferred { () -> PassthroughSubject<Int, Never> in
      let request = PassthroughSubject<Int, Never>()
      subjects.append(request)
      return request
   }
   let scanB = Publishers.Scan(upstream: deferred, initialResult: 10) { state, next in state + next }
   var receivedC = [Subscribers.Event<Int, Never>]()
   let sinkC = Subscribers.Sink<Int, Never>(
      receiveCompletion: { receivedC.append(.complete($0)) },
      receiveValue: { receivedC.append(.value($0)) }
   )
   var receivedD = [Subscribers.Event<Int, Never>]()
   let sinkD = Subscribers.Sink<Int, Never>(
      receiveCompletion: { receivedD.append(.complete($0)) },
      receiveValue: { receivedD.append(.value($0)) }
   )

   scanB.subscribe(sinkC)
   subjects[0].send(sequence: 1...2, completion: nil)
   scanB.subscribe(sinkD)
   subjects[0].send(sequence: 3...4, completion: .finished)
   subjects[1].send(sequence: 1...4, completion: .finished)
   
   XCTAssertEqual(receivedC, [11, 13, 16, 20].asEvents(completion: .finished))
   XCTAssertEqual(receivedD, [11, 13, 16, 20].asEvents(completion: .finished))
}
```

This test case shows that the “naïve” interpretation of Combine cannot properly describe how Combine works in all cases. While there are two `PassthroughSubject`s, two `Subscriber.Sink`s, there is only one `scanB` node in the `Publisher` graph, yet it behaves like two completely different nodes – one for the `sinkC` and one for the `sinkD`.

## Subscription, the mostly-hidden type

How does this work?

Despite the programmer creating a single graph of `Publisher`s, there is a shadow graph of other instances that really performs the value processing and sending. We can see this shadow graph in the last function in `Subscriber` protocol.

```swift
func receive(subscription: Subscription)
```

Every `Publisher` in your graph is shadowed by one instance of `Subscription` per active `Subscriber`.

We didn’t see the effects of this shadow `Subscription` graph in the first `testScan` example because the shared `PassthroughSubject` tied all the subscriptions together but when we moved to using `Deferred`, the graphs become untied and independent and we could see the effects of multiple `Subscription`s at the `scan` node.

> **The accurate interpretation of Combine** is that values are sent and processed through a graph of `Subscription` instances, lazily constructed by `Publisher` instances on a per-subscribe basis.

We don’t usually interact with `Subscription` instances. `Subscription` instances are created automatically by `Publisher`s when a `Subscriber` subscribes. The graph of `Subscription` instances mirrors the graph of `Publisher`s.

You can see why the distinction between the `Publisher` graph and the `Subscriber` graph (the distinction between the “naïve” and “accurate” interpretations) can be confusing. Further adding to the confusion is that there are no usable public implementations of `Subscription` (I’m ignoring `Subscriptions.empty` which is a placeholder that ignores everything).

The subscription concept was introduced by the Reactive Extensions for .NET, attempting to make each mutation of the graph behave like a completely separate, unrelated graph – as it might appear in a strict functional programming language. However, strict functional programming languages cache function results, so redundant recalculation of upstream values is avoided. In Swift, if we don’t cache it ourselves, everything is repeated.

If I wanted to repeat all the processing, I would have recreated the publisher graph.

When I wrote my own reactive programming framework, CwlSignal, the main `Signal` instances were the delivery graph – the “naïve” interpretation was the same as the “accurate” interpretation. I handled the problem with multiple subscribers a different way: `Signal` nodes allowed only a single child to observe. For those specific cases where you need multiple listeners, CwlSignal offered a special `SignalMulti` node that encoded choices like “multicast”, “continuous” (cache latest), “playback” (cache all). But a re-subscribe option deliberately wasn’t offered.

In any case, let’s look under the hood at the definition of `Subscription`:

```swift
public protocol Subscription : Cancellable, CustomCombineIdentifierConvertible {
    func request(_ demand: Subscribers.Demand)
}
```

It’s pretty terse. If this is the entire definition of the shadow value sending graph, it’s not revealing much.

## Custom implementations

Fortunately, `Subscription` isn’t impossible to understand. It generally just performs all the roles of the `Publisher` and `Subscriber` in the “naïve” interpretation: it receives values, processes them and passes them down the line.

A `Subscription` should replicate everything important from its associated `Publisher`, copying any closures and state from the initial values stored in the `Publisher`. In this way, the `Subscription` is independent and has everything needed to handle the processing, without further assistance from the `Publisher`.

The trickiest part is working out when to create a `Subscriber` from a `Publisher` and getting everything to piece together. I arrived at the following steps, centered on `Publisher.receive`, after a little experimentation:

> **NOTE**: the words `Subscriber` and `Subscription` are very similar. I’m sure this is going to get confusing (it was confusing to write).

1. You invoke Combine’s `subscribe` function on your `Publisher`, passing your `Subscriber`.
2. This will call through to your `Publisher`’s `receive` function passing the `Subscriber` you provided to the `subscribe` function
3. In the `receive` function `Publisher` creates a custom `Subscription` instance, which should also conform to `Subscriber` and should hold a reference to the downstream `Subscriber`.
4. Your `Publisher` calls `subscribe` on its upstream `Publisher` (if any) passing the custom `Subscription` (this is why it should conform to `Subscriber`).
5. The upstream `Publisher` calls `receive` on your custom `Subscription`, passing its own subscription instance.
6. Your `Subscriber` should call `receive` on its downstream `Subscriber`
7. The downstream `Subscriber` will invoke `request` on your `Subscription` and your `Subscription` should invoke `request` on its upstream `Subscription`.

The exact steps tend to vary based on whether your `Publisher` has an upstream `Publisher` or is a `Subject`.

Let’s focus on a transforming `Publisher` with an upstream `Publisher`, since that’s the canonical case. Such a `Publisher` would have a `receive` function that looks like this:

```swift
public func receive<S>(subscriber: S) where S: Subscriber, Failure == S.Failure, Output == S.Input {
   let downstream = AnySubscriber(subscriber)
   let behavior = CustomTransformer.Behavior(
      downstream: downstream,
      processor: processor,
      state: initialState)
   let subscription = CustomSubscription(behavior: behavior)
   upstreamPublisher.subscribe(subscription)
}
```

There’s a very important trick here: even though we are a downstream node (and could implement `Subscriber` for ourselves), we don’t pass ourselves to the `upstreamPublisher`. Instead we pass the newly constructed `Subscription` instance instead. This is why `Subscription` implementations are often `Subscriber` implementations too. The `Subscription` instances are their own, independent delivery graph, connected only to other `Subscription` instances.

I chose to design my custom subscription in two parts: a wrapper (to apply mutex behaviors) and a behavior protocol (used to apply `Publisher` specific behaviors inside the mutex). The mutex wrapper is therefore implemented just once and the behavior content is simpler.

Here’s the wrapper interface:

```swift
public struct CustomSubscription<Content: SubscriptionBehavior>: Subscriber, Subscription {
   public typealias Input = Content.Input
   public typealias Failure = Content.Failure
   
   public var combineIdentifier: CombineIdentifier { return content.combineIdentifier }
   let recursiveMutex = NSRecursiveLock()
   let content: Content
}
```

and the `SubscriptionBehavior` inside it looks like this:

```swift
public protocol SubscriptionBehavior: class, Cancellable, CustomCombineIdentifierConvertible {
   associatedtype Input
   associatedtype Failure: Error
   associatedtype Output
   associatedtype OutputFailure: Error

   var demand: Subscribers.Demand { get set }
   var upstream: Subscription? { get set }
   var downstream: AnySubscriber<Output, OutputFailure> { get }
   
   func request(_ d: Subscribers.Demand)
   func receive(_ input: Input) -> Subscribers.Demand
   func receive(completion: Subscribers.Completion<Failure>)
}
```

The implementations are then straightforward: values arrive via the `receive` functions and are processed as appropriate for the publisher that created the instance and emitted to the downstream `AnySubscriber`.

You can see the full implementation of `CustomSubject`, `CustomScan`, `CustomSubscription` and `CustomSink` [in the CombineExploration repository](https://github.com/mattgallagher/CombineExploration).

Is this how the implemention of `Subscription` looks in Combine? Almost certainly not. As far as I can tell, Combine uses a type called `Conduit` which applies its mutex once at the start, rather than once for every `Publisher` stage in the pipeline. `Conduit` does use a recursive mutex implementation (more on that in part 3 of this series) but it appears to be implemented on top of `os_unfair_lock` (which is usually a non-recursive mutex).

However, these implementations do appear to behave correctly and interoperate correctly with the official Combine implementations.

Here’s the previous `testOverlappingABCD` rewritten with these implementations, showing that they function as drop-in replacements for the default implementations:

```swift
func testCustomABCD() {
   var subjects = [CustomSubject<Int, Never>]()
   let deferred = Deferred { () -> CustomSubject<Int, Never> in
      let request = CustomSubject<Int, Never>()
      subjects.append(request)
      return request
   }
   let scanB = CustomScan(upstream: deferred, initialResult: 10) { state, next in state + next }
   var receivedC = [Subscribers.Event<Int, Never>]()
   let sinkC = CustomSink<Int, Never>(
      receiveCompletion: { receivedC.append(.complete($0)) },
      receiveValue: { receivedC.append(.value($0)) }
   )
   var receivedD = [Subscribers.Event<Int, Never>]()
   let sinkD = CustomSink<Int, Never>(
      receiveCompletion: { receivedD.append(.complete($0)) },
      receiveValue: { receivedD.append(.value($0)) }
   )

   scanB.subscribe(sinkC)
   subjects[0].send(sequence: 1...2, completion: nil)
   scanB.subscribe(sinkD)
   subjects[0].send(sequence: 3...4, completion: .finished)
   subjects[1].send(sequence: 1...4, completion: .finished)
   
   XCTAssertEqual(receivedC, [11, 13, 16, 20].asEvents(completion: .finished))
   XCTAssertEqual(receivedD, [11, 13, 16, 20].asEvents(completion: .finished))
}
```

## Conclusion

> **Download**: The code for this series, [CombineExploration, is available on github](https://github.com/mattgallagher/CombineExploration).

We frequently talk about our `Publisher` graphs as though they perform a calculation and emit values but this isn’t really true. Values in Combine are sent by the `Subscription` graph and the calculation is repeated for each `Subscription` graph.

The distinction between `Publisher` and `Subscription` graphs exists to prevent separate subscribers from interferring with each other. For this to work, _all_ stream processing state you set up in a custom `Publisher` must be copied into a `Subscription` and mutated there, exclusively.

### Looking forward…

In most cases, we don’t want redundant calculations. Where possible, we want values calculated once per `Publisher` graph and we want the latest value _shared_ between all subscribers.

How do we avoid “resubscription” in Combine? How do we get multicast or cached results? Will we need to use `connect` or hold redundant `subscribe` cancellables as we do in RxSwift? For that matter, what is needed, in general, to keep Combine subscriptions alive? What are the rules by which Combine keeps anything (`Publishers`, `Subscribers` or `Subscriptions`) alive?

This is what I’ll look at in the next article: sharing.
