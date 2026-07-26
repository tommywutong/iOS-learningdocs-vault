---
title: 'CwlSignal, a library for reactive programming | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/cwlsignal.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:dc3249b04d4925f6'
translated: false
---

> 原文：[CwlSignal, a library for reactive programming | Cocoa with Love](https://www.cocoawithlove.com/blog/cwlsignal.html)　·　Cocoa with Love (Matt Gallagher)

In this article, I’m presenting [CwlSignal](https://github.com/mattgallagher/CwlSignal). It is the latest Swift iteration of a library that I’ve been using for reactive programming for the last few years. I consider it the fifth iteration although the first two iterations were in C++ and were quite different.

I don’t like releasing code that directly competes with existing solutions but I’m doing that here. I believe that the design of CwlSignal offers a number of significant features and advantages that make it worthy of consideration despite the existence of other options.

This article will focus on basic usage of the CwlSignal library itself. **I will not explain what reactive programming is or why you should use it, in this article.** If you’re unfamiliar with reactive programming, you might want to start with the next article, [What is reactive programming and why should I use it?](https://www.cocoawithlove.com/blog/reactive-programming-what-and-why.html)

## A one-way communication channel

The CwlSignal library is centered around the `Signal` type; a one-way communication channel:

```swift
// Create an input/output pair
let (input, signal) = Signal<Int>.create()

// Subscribe to listen to the values output by the channel
self.lifetimes += signal.subscribeValues { value in print(value) }

// Send values to the input end
input.send(value: 1)
input.send(value: 2)
input.send(value: 3)
```

<sub>"Basic channel" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

You can probably guess that this example will print:

```
1
2
3
```

The `SignalInput`/`Signal` types returned from `create` are the two ends of a communication channel and can be passed around your program to locations where values are emitted or where values are needed.

The `subscribeValues` function creates a `SignalOutput` which allows us to extract values from the channel. The output conforms to a protocol named `Lifetime` which means that holding onto it maintains a lifetime of a resources – in this case, the subscription and all processing in the channel are tied to the lifetime of the output and when it is released (or `cancel()` is invoked upon it), the subscription will be ended and all resources cleaned up.

The careful separation of “input” and “output” and the modelling of reactive programming as a channel is a distinguishing feature of CwlSignal. Other common implementations treat reactive programming as an implementation of the “Observer” pattern but this leads them to hide the input end of their channels or confusingly use types that are both input and output, when only an input interface is desired.

## Serial asynchronous compositions

Any number of `Signal` instances can be chained in series to form pipelines. This allows value transformations and other “stream processing” to be applied to values between the sender and the subscriber.

There are lots of different “operator” functions for chaining `Signal` instances together (including names like `map` and `flatMap` that you might recognize from `Sequence` and `Collection` processing in Swift) but most are implemented on top of the `transform` function which can be used like this:

```swift
let (i, o) = Signal<Int>.create()

// Transform into signal that emits a number of "Beep"s equal to the integer received
self.output = o.transform { result: Result<Int>, next: SignalNext<String> in
   switch result {
   case .success(let intValue): (0..<intValue).forEach { _ in next.send(value: "Beep") }
   case .failure(let error): next.send(error: error)
   }
}.subscribeValues { value in
   print(value)
}

i.send(value: 3)
```

<sub>"Serial pipelines - transform" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

Will output:

```
Beep
Beep
Beep
```

Unlike functional programming inspired transformation functions (e.g. `map`, `flatMap`), the fundamental `transform` in CwlSignal does not _return_ its result but `send`s it into the `SignalNext` (interface equivalent to `SignalInput` for sending to the next `Signal` in the chain). This design allows you to emit any number of values or an error.

There’s a hidden parameter here, `context`, an `Exec` type (I [presented and discussed `Exec`](https://www.cocoawithlove.com/blog/specifying-execution-contexts.html) in a previous article), which is left to its default `.direct` value (indicating this processing will be performed directly upon whatever context the value is sent). Providing a value for this parameter allows easy transfer between separate send and subscribe contexts or allowing processing work to occur on a worker thread.

As an example, the following code snippet uses `context` parameters in conjunction with the `map` function (a simplified one-to-one value transformer built on top of `transform`) to demonstrate sending a value in from the current context to the `.default` priority `Dispatch` global concurrent queue, before finally returning to the `.main` thread to report results.

```swift
// Create an input/output pair
let (input, output) = Signal<Int>.create()

// Create the processor
self.output = output.map(context: .default) { value in
   // Perform the background work
   return sqrt(Double(value))
}.subscribeValues(context: .main) { value in
   // Perform the main thread work
   print(value)
}

// Send values to the input end
input.send(value: 1)
input.send(value: 2)
input.send(value: 3)
```

<sub>"Serial pipelines - map" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

Which will output:

```
1.0
1.4142135623731
1.73205080756888
```

Note that despite transferring via a _concurrent_ global queue, `Signal` ensures serialized processing of values in the stream.

## Parallel asynchronous compositions

CwlSignal combines asynchronous signals as easily as it transforms signals serially. The `combine` function works in much the same way as the `transform` function, except that instead of processing a series of `Result<T>` values, it processes `EitherResult...` (an `enum` over two or more `Result` types, depending on how many input `Signal`s you are combining).

For example, if you wanted to put a 10 second limit on the total duration of a `Signal`, you could combine it with a timer `Signal` as follows:

```swift
let timer = Signal<()>.timer(interval: .seconds(10))
let signalWithTimeout = underlyingSignal.combine(second: timer) { eitherResult, next in
   switch eitherResult {
   case .result1(let r): next.send(result: r)
   case .result2: next.send(error: MyErrors.timeout)
   }
}
```

<sub>"Parallel composition - combine" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

I wanted to show the use of the `combine` function but you would normally apply a timeout using thebuilt-in function `timeout`. There are many built-in combining functions like `zip` and `combineLatest` that simplify applying `combine` transformations across multiple `Signal`s.

For example, combining the latest value of two dependencies for setting the `isEnabled` status of a button:

```swift
self.lifetimes += loginStatus.loggedInSignal
   .combineLatest(second: folderView.selectionSignal) { $0 && !$1.isEmpty }
   .subscribe(context: .main) { result in
      self.addToFavoritesButton.isEnabled = result.value ?? false
   }
```

<sub>"App scenario - dynamic view properties" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

Notice the `context: .main` to ensure that any final value is applied on the “main” thread (this `Exec` value checks to see if it is already on the “main” thread and directly invokes, otherwise invokes asynchronously on the `.main` thread).

## Three tricky scenarios

The examples I’ve shown so far have kept everything simple with regards to the timing of the signal construction and the sending of values. We didn’t start sending values until _after_ the subscriber connected, avoiding the question of what would happen to signals if they had nowhere to go.

Any reactive programming library usually needs to handle situations where the order of joining and disconnecting is less simple. The specific approach for handling of these types of scenario is usually a defining difference between reactive programming implementations.

### Instantaneous values

In some cases, discarding all values sent before a listener connects is the desired behavior. For example, if you created a signal that emitted a “tick” notification once per second, then discarding ticks when no one is listening is probably the right option.

If we send some values _before_ a subscriber is connected:

```swift
// Create an input/output pair
let (input, output) = Signal<Int>.create()

// Send values before a subscriber exists
input.send(value: 1)
input.send(value: 2)

// Subscribe to listen to the values output by the channel
self.lifetimes += output.subscribeValues { value in print(value) }

// Send a value after a subscriber exists
input.send(value: 3)
```

Ouput will be:

```
3
```

There’s more happening here than you can tell from this code sample and its output.

The first two calls to `send` will actually return a `SignalError.inactive` error to inform that the sent values have gone nowhere (the `Signal` _knows_ that there are no listeners). Note that this error is returned (rather than thrown) and has the `@discardableResult` attribute since it is expected that errors returned from an input will usually be ignored; ensuring the signal is connected appropriately is usually the signal constructor’s responsibility, not the sender’s responsibility.

A value of `nil` from one of the `send` functions indicates there is no error and the value was sent correctly.

### Continuous or playback values

Let’s consider a different scenario. Instead of a signal that emits “ticks”, we have a signal that emits the current hour, updated every hour. In this scenario, a receiver would probably want to receive the current hour immediately, even if it connected halfway between updates.

```swift
// Create an input/output pair, making the output continuous before returning
let (input, output) = Signal<Int>.create { signal in signal.continuous() }

// Send values before a subscriber exists
input.send(value: 1)
input.send(value: 2)

// Subscribe to listen to the values output by the channel
self.lifetimes += output.subscribeValues { value in print(value) }

// Send a value after a subscriber exists
input.send(value: 3)
```

<sub>"Advanced behaviors - continuous" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

Ouput will be:

```
2
3
```

Making the signal `continuous`, as in this example, causes it to re-emit the most recent value when a new subscriber connects. Other options include `playback` (for re-emitting _all_ values) or `buffer` (which lets you update a custom series of values each time a value is processed).

In the previous example, I applied the `continuous` function in a trailing closure provided to `create`. This trailing closure is just a syntactic convenience for transforming the _signal_ half of the returned tuple. I could also write:

```swift
let (input, signal) = Signal<Int>.create()
let output = signal.continuous()
```

to do the same thing.

### Lazy generation

In many cases, the signal sender should not be created until _after_ a subscriber connects. This allows for responding to whether a signal is needed, enabling patterns like lazy generation and cancellation.

```swift
// Create an output immediately but only create the input as needed
let output = Signal<Int>.generate { input in
   if let i = input {
      i.send(value: 1)
      i.send(value: 2)
      i.send(value: 3)
   }
}

// Subscribe to listen to the values output by the channel
self.lifetimes += output.subscribeValues { value in print(value) }
```

<sub>"Advanced behaviors - lazy generation" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

Output will be:

```
1
2
3
```

## Signal activation

> **A terminology note**: to this point, I’ve talked about `Signal` as being a simple “channel”, which implies single-input, single-output. Since I’ve already shown composing of parallel signals, it should be apparent that `Signal` structures get more complex than that. For the remainder of this section, I’ll talk about the `Signal` “graph” which is a potentially multiple input, potentially multiple output, directed, acyclic arrangement made by connecting `Signal`s together.

As I mentioned at the start of the previous section, these “key scenarios”, when handled at all, are handled very differently by different reactive programming implementions.

### Other implementations

The standard solution for lazy construction or continuous values in other frameworks is usually to have a two stage construction of the graph. The first stage constructs empty scaffolding and the second stage, which is deferred until a “subscribe” message is propagated, constructs the actual working graph.

This second construction stage can be run an arbitrary number of times to create multiple working versions of the graph for every subscriber. This is sometimes given names like a “cold observable” or “signal producing”.

This approach allows some degree of response to each subscriber but it also creates a situation where all work – at all nodes in the graph – is actually performed an additional time for every subscriber.

That’s not how CwlSignal operates.

### CwlSignal and “activation”

Instead of reconstructing parts of the graph, CwlSignal is designed around the concept of “activation”. On construction, a signal graph is “inactive”. When a `SignalOutput` is added to an inactive graph (by calling `subscribe`, or `subscribeValues`), every direct antecedent `Signal` becomes “active”. There’s a small handful of effects that may occur during activation but the most common are:

- value) are immediately emitted through the graph – propagating

  during the activation phase (even when their

  would normally be processed asynchronously)
- closures are invoked so lazily started signal emissions can begin

The important point to note, in contrast to other reactive programming solutions, is that activation happens per `Signal` in the graph, not per subscriber. A new subscriber activates only those `Signal`s that are _inactive_ between the new subscriber and any previously activated sections of the graph. This makes `Signal`s with multiple outputs a special consideration, since they must handle the activation of each of their outputs at separate times (See [Single-output by default](#single-output-by-default), below, for a discussion of the implications).

Activation allows some powerful solutions to problems that occur in imperative programs when trying to integrate reactive programming with non-reactive constructs.

Most prominent is “capturing”:

```swift
// Create an input/output pair, transforming the output before returning
let (input, output) = Signal<Int>.create { signal in signal.continuous() }

// The `continuous` signal will cache the most recently sent value
input.send(value: 1)
input.send(value: 2)

// Capture the "2" activation value cached by the `continuous` signal
let capture = output.capture()
let (values, error) = capture.activation()
print("Activation values: \(values)")

// Capturing blocks signal delivery so *both* of these will be queued for later
input.send(value: 3)
input.send(value: 4)

// Subscribing unblocks the signal so the "3" and the "4" will now be sent through.
self.lifetimes += capture.subscribeValues { value in print("Regular value: \(value)") }
```

<sub>"Advanced behaviors - capturing" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

Output will be:

```
Activation values: [2]
Regular value: 3
Regular value: 4
```

As you can see, `SignalCapture` allows activation values to be pulled _synchronously_ from a signal. This provides potential solutions to scenarios where code cannot proceed without being able to obtain an immediate value. Simply put: activation in CwlSignal provides pull-based synchronous behaviors, whereas typical reactive programming is push-based and potentially asynchronous.

### Closure state and deactivation

In _most_ cases, once a `Signal` has deactivated (due to an error sent through the `Signal` or the graph being disconnected from its output), it will not be used again. However, some constructs like `SignalJunction<T>` (which allows the breaking and joining of `Signal` connections) and `Signal<T>.generate` (which receives a new `SignalInput` every time the graph activates) may be used to allow a section of a signal graph to be connected to a new `SignalOutput` and start again.

This should be kept in mind if you’re using persistent state in transformation closures – state should always be cleared or reset on deactivation. To assist with this, most transformation closures offer a `withState` variant that provide a persistent state value to the closure every time it is invoked but automatically reset this state value to its initial value on deactivation.

Note that the `SignalInput` and `SignalOutput` classes are strictly single-use and once deactivated, will always _stay_ deactivated.

## Single-output by default

Another distinguishing trait of the `Signal` type in CwlSignal is that it is single-output. This is a difference compared to other reactive programming frameworks that allow multiple-observers by default.

If you try to do this:

```swift
let (input, signal) = Signal<Int>.create()
let output1 = signal.subscribe { r in print(r) }
let output2 = signal.subscribe { r in print(r) }
```

the second `subscribe` call will never actually connect to `signal` and will instead immediately receive a `SignalError.duplicate` error.

To validly connect multiple outputs, you must have an instance of the `Signal` subclass `SignalMulti` which you can obtain only by using a transformation that returns a `SignalMulti`. The `SignalMulti` subclass has no additional public methods and externally, merely serves to notify that a signal supports multiple outputs.

The reason you must obtain a `SignalMulti` is that it forces consideration of how to make the signal joinable mid-stream. Should the latest value be cached? Should all values be cached? Is a custom “bring me up to speed” value required? Is nothing required and a listener can simply join without any special behaviors?

`Signal` provides the `continuous`, `playback`, `buffer` and `multicast` functions. These `SignalMulti` returning functions provide the latest value, the entire sequence of values, a custom sequence of values, or no value at all to new subscribers, respectively.

As an example:

```swift
let (input, output) = Signal<Int>.create()

// Create a `SignalMulti<Int>` from the `Signal<Int>`
let continuousOutput = output.continuous(initial: 5)

let output1 = continuousOutput.subscribe { r in print(r) }
let output2 = continuousOutput.subscribe { r in print(r) }
```

Both outputs here will immediately receive the `continuous` value `5`.

### Usage implications of “single-output by default”

CwlSignal aims to be as foolproof as possible but along with “forgetting to retain the `SignalOutput`”, this is one of two clear situations where you can misuse a `Signal`. As with `SignalOutput` – whose behavior exists to _force_ you to tie a lifetime to a receiving scope – there is a purpose to “single-output by default”.

Single output forces you to choose the correct way to join subscribers _after_ the stream has started.

When multiple subscribers are implicitly permitted, the default behavior is typically equivalent to CwlSignal’s `multicast` (you get nothing new on subscribing and simply see the values sent _after_ subscribing). This is done because caching nothing is efficient but the problem is that it is less likely to be the desired behavior than `continuous` or other buffering patterns. A system that lets unplanned multiple observers subscribe to any arbitrary `Signal` is more likely to offer invalid behavior or hide a graph construction flaw than offer the correct solution.

### Interface implications of “single-output by default”

You should never expose a `Signal` instance member in a public interface.

A signal exposed by an interface should always be one of:

- , or
- on each access

If you receive a `Signal`, rather than a `SignalMulti` from another interface, subscribe or transform only once. If you need multiple subscribers, either append your own `SignalMulti` transform or call the other interface again to get a new `Signal`.

## Other details about CwlSignal

The CwlSignal library is around 5000 lines (not including code pulled from CwlUtils) of densely written code. There are a lot of details in there and I wanted to highlight a few additional points.

### Types

CwlSignal involves just a few public types:

- the downstream end of a channel (

  is the only subclass)
- the input end of a channel (the equivalent

  type is provided by transformation closures to fulfill the same sending role

  s)
- returned when subscribing to

  to extract values
- and

  , which I’ve

  detailed

  in

  previous articles
- ,

  ,

  ,

  ,

  which appear only if you’re doing specific things with the graph.

Seeing 14 type names all at once might seem a little complicated but in reactive programming, it’s very minimalist. All except the last three have already appeared in the code examples in this article – if you didn’t notice that they were there, then they have done their jobs.

### Result

While the examples in this article have focussed on values, `Signal`s actually send instances of `Result<T>` between each other (the `send(value:)` and `subscribeValues` functions in this article wrap and unwrap values automatically and use `send(result:)` and `subscribe` under-the-hood). In contrast to other reactive programming implementations, `Signal` uses no other event types – there’s no separate completed/interrupted/cancelled events, just `Result`. The first error sent causes an end of stream. A successful “end of stream” is usually a `SignalComplete.closed` and a close due to graph disconnection is usually a `SignalComplete.cancelled`.

### Lifetime management

A one-way communication channel has two ends: the sender and the receiver. Accordingly, the only two steps required for keeping a signal graph alive is that you must retain the `SignalInput` and the `SignalOutput`. Releasing the former indicates that there are no further values to come in the sequence and releasing the latter indicates that you no longer wish to receive updates.

The effects of releasing either are slightly different.

If a `SignalInput` is released, it will send a `SignalComplete.cancelled ` result. The `SignalInput` will never be able to send another error but whether the result closes the entire graph is dependent on the transformer closures in the graph; a transformer can choose to block or ignore an error, preventing its propagation. A `SignalInput` weakly references its `Signal` so releasing a `SignalInput` won’t necessarily release anything else in the graph.

If a `SignalOutput` is released, it will immediately deactivate its subgraph (`Signal`s that output to that `SignalOutput` and no others). There is no chance to block this change although `Signal<T>.generate` closures and transformation closures with managed state are offered a chance to clean up. A `SignalOutput` strongly retains the signal graph and when it deactivates, it immediately releases the graph. Any `Signal` deactivated when a `SignalOutput` is released will also be released unless strongly held elsewhere.

Both `SignalInput` and `SignalOutput` implement the `Lifetime` protocol to indicate that they keep alive a resource (either the input or output end of the signal channel) and you can directly invoke `cancel` on them if you need to immediately release them.

### Retaining outputs

If you don’t retain an output, the signal will be cancelled.

It is common for a class like a `UIViewController` to have a large number of `SignalOutput`s for setting properties on its views. You usually don’t care about the explicit type of the `SignalOutput`, you just need to keep it alive as long as the `UIViewController`. Accordingly, it’s common to have an `Array<Lifetime>` and just store the outputs there.

```swift
self.lifetimes += someSignal.subscribe { r in // do something }
```

That `+=` operator is provided by CwlSignal; it is simply a shortcut for `RangeReplaceableCollection.append`.

### Classes are just an implementation detail

While `SignalInput`, `Signal`, `SignalOutput` and other common types in CwlSignal are classes, using CwlSignal does not involve subclassing or implementing protocols. CwlSignal provides a sealed set of behaviors. Solving problems is achieved through composing signal graphs and applying transformation functions _between_ signals, rather than trying to subvert the signal machinery.

### Support for ReactiveX

CwlSignal implements the full range of [ReactiveX operators](http://reactivex.io/documentation/operators.html), minus those that are redundant with underlying functions or don’t make sense given CwlSignal’s “activation” behavior. If you read the comments in the “CwlSignalReactive.swift” file, I mention all prominent omitted ReactiveX operators, with an explanation for why they’re not applicable.

I’m not personally enthusiastic about the entire range of ReactiveX operators. While some operators like `combineLatest`, `map` and `timeout` are widely expected in reactive programming and make a lot of sense, many of the .NET LINQ inspired operators like `groupJoin` are so weird that you’re probably better off solving your problems another way. In any case, this support is provided to allow some degree of conceptual common ground between CwlSignal and other reactive programming implementations and to provide assurances that CwlSignal does offer the capability to support a full range of standard behaviors.

### Thread safety

CwlSignal is threadsafe and this safety should hold in a wider range circumstances than most APIs.

User-provided closures will never be invoked concurrently and will be invoked in your nominated context (if one is provided). Values sent simultaneously from multiple threads to the same `SignalInput` will be correctly serialized. It should not be possible to deadlock CwlSignal code under any combination of attempted graph cycles or re-entrancy (you can’t make a graph cycle and re-entrancy will be detected and serialized). Even changing the structure of the signal graph from one thread while values are being processed through the graph on another thread will result in nothing worse than the discarding of values in-transit over outdated graph connections.

### Mutable graph – even while active

You can continue changing the structure of a CwlSignal graph while it is active. CwlSignal remains threadsafe and will not deliver signals out-of-order, even if you are connecting and joining new subsections of the graph while values are processed.

This is helpful for having a model that runs in its own thread but a set of views running on the main thread that change which parts of the model they are observing, independently of the model.

## Limited out-of-the-box integration

I’m releasing CwlSignal primarily as a “back-end” technology. I’m not releasing a large number of out-of-the-box integration features for Cocoa or other APIs (although, [as I show in the next article](https://www.cocoawithlove.com/blog/reactive-programming-what-and-why.html), CwlSignal doesn’t need significant API integration to offer signficant code savings).

The “CwlSignalCocoa.swift” file in the library does include basic helpers for key-value-observing, key-value-setting, target-action handling and notifications but you won’t find built-in integration with `URLSession`/`URLConnection`, XPC or `NSTask` communication, CoreData or sqlite, any other Foundation or Cocoa delegate interface or any UIKit or AppKit views.

I will likely add additional helpers in future to simplify common tasks but I don’t expect that I will provide a set of shallow `Signal` hooks into UIKit or AppKit views. I do have a view framework involving reactive programming that I’m trying to get ready for sharing but it’s not a simple grafting of signals onto existing classes so it’s going to take a bit more time to tidy up.

## Usage

> The [CwlSignal framework](https://github.com/mattgallagher/CwlSignal) is available on GitHub.

To use [CwlSignal](https://github.com/mattgallagher/CwlSignal) in your own projects, follow the instructions in the [ReadMe.md file for the project](https://github.com/mattgallagher/CwlSignal/blob/master/README.md) to clone the repository and add the framework it produces to your own projects.

Note that the CwlSignal framework directly includes most of the files from the CwlUtils framework inside its own module so if you’re using CwlSignal, there’s no reason to also include CwlUtils (just use the same features via CwlSignal, instead). This manual inclusion of dependencies is certainly not ideal but is a workaround for an order of magnitude loss in performance due to Swift 3’s inability to specialize generics or inline functions between modules (and partly due to my desire to avoid reliance on package management until Swift Package Manager integrates with Xcode). I’m hopfeul that changes to Swift, Xcode and Swift Package Manager will allow a better solution in future.

## Conclusion

If you’ve seen other reactive programming code, I hope the simplicity of the examples in this article is apparent. There’s no nested sets of closures or confusingly named types just to construct a basic channel. In most contexts, you need only the `Signal` type name, rather than a landscape of types with nothing obviously in common. Inputs and outputs are clearly separated with no confusion between type names or roles. There’s no memory management or memory management containers that seem out-of-place in Swift and there are no names that reference .NET interfaces that don’t exist in Cocoa.

CwlSignal is simple, fast, threadsafe, full-featured and designed for Swift. It implements all common reactive programming operators while offering unique abilities like “activation” and “capturing”. [Download the project](https://github.com/mattgallagher/CwlSignal) and try out the code for yourself using the embedded CwlSignal.playground which features a number of the examples from this and the next article.

### Looking forward…

I’ve tried to give an overview of the basic usage of this library and its distinguishing features relative to other reactive programming implementations. In the next article, I’ll look at reactive programming in a more general sense and explain how it can be used to solve common problems that face application programmers.
