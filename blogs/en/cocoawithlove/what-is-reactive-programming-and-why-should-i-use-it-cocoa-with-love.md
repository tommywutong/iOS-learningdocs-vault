---
title: 'What is reactive programming and why should I use it? | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/reactive-programming-what-and-why.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:5f3a002a24a51bf6'
translated: false
---

> 原文：[What is reactive programming and why should I use it? | Cocoa with Love](https://www.cocoawithlove.com/blog/reactive-programming-what-and-why.html)　·　Cocoa with Love (Matt Gallagher)

A good reactive programming library takes a huge maintenance burden off some of the most commonly written, bug-prone code in applications.

In the previous article [I presented my own library for reactive programming, CwlSignal](https://www.cocoawithlove.com/blog/cwlsignal.html), but simple syntax examples don’t really demonstrate how to use reactive programming to solve problems.

In this article, I’ll explain why I consider reactive programming to be one of the most important design patterns for application programming by looking at three scenarios that are common in application development, yet are a drain on development time, lead to frequent bugs and make design and refactoring hard. I’ll show how reactive programming addresses the verbosity, eliminates the unsafety and restructures the code to aid maintainability.

The specific scenarios I’ll examine will be:

- A button whose `isEnabled` status is dependent on two different state values
- A thread-safe storage type
- An asynchronous task with a timeout

## A description of reactive programming

Reactive programming addresses the following problem:

> Any “getter” for mutable state causes problems because it gives you the _current value_ without ensuring you respond to the _changes_.

by suggesting the following solution:

> Never store mutable state on your types. Instead, when you generate a new value in response to a change, send the value into a channel. Any part of the program that relies upon that value must subscribe to the channel.

The idea is that we remove state from exposed parts of our program and encapsulate it inside channels instead. Channels clearly show data dependencies and effects, make changes easy to reason about and easy to maintain and otherwise simplify how we modify application state.

Reactive programming supports this underlying principle with an approach that centers on serial and parallel compositions of channels to transform streams of data as they are emitted and merge changes that may occur concurrently or in otherwise intersecting patterns.

Simply put: reactive programming manages asynchronous data flows between sources of data and components that need to _react_ to that data.

## A button dependent on two state values

Let’s start with a fundamental task in application programming: setting the `isEnabled` status of a button.

Imagine your app as a screen to upload files to a server. To do this, you have an “Upload” button. The “Upload” button should be enabled if (and only if) both of the following are true:

1. the app is connected to a server
2. the selection is non-empty

Let’s include two complicating factors:

1. the connection status is typically updated on a background thread
2. either the server connection or selection objects could completely change or even be set to nil while we’re observing them

Assuming updates for relevant values are sent using Key-Value-Observing then our view controller might contain the following code:

```swift
serverObs = sharedServer.observe(\.currentServer, options: .initial) {
   [uploadButton, serverStatusButton] object, change in
   uploadButton.isEnabled =
      object.currentServer != nil && sharedSelection.currentSelection?.selection.isEmpty == false
}
   
selectionObs = sharedSelection.observe(\.currentSelection, options: .initial) {
   [filesSelectedLabel, uploadButton, weak self] object, change in
   if let s = object.currentSelection {
      self?.selectionNameObs = s.observe(\.selection, options: .initial) {
         [filesSelectedLabel, uploadButton] object, change in
         uploadButton.isEnabled =
            sharedServer.currentServer != nil && object.selection.isEmpty == false
      }
   } else {
      uploadButton.isEnabled = false
   }
}
```

<sub>The complete code for this view controller appears on the ViewStateObserving page of the NonReactive playground in the [Cocoa with Love Playgrounds project](https://github.com/mattgallagher/CocoaWithLovePlaygrounds).</sub>

It’s exhausting just to look at. The logic around updating three controls takes 18 lines of densely written code. The `isEnabled` flag on the `uploadButton` is updated in three different locations with subtly different logic in each location. And it’s still not enough to do things properly.

This code includes a few subtle but common mistakes that occur, not because we’re bad programmers but because we code for the path of least resistance. We fix problems if they’re immediately apparent but if the code _mostly_ works – as this code does – it’s likely to get through testing.

What problems are in this code that could cause headaches later?

1. **Thread unsafe**: with the server connection updating on a background thread, its closure is called on the background thread, resulting in unsafe access to the `uploadButton`.
2. **Not transactional**: both observation methods need to access the value reported by the _other_ observation method, meaning that you might process a change twice or you might process changes in an inconsistent order

There are some other issue that are not bugs but are maintenance risks:

1. **It’s difficult to refactor**: We update the `uploadButton.isEnabled` value in 3 different places. If another dependency were added to this value, we would need to remember to update all three locations.
2. **We access values directly**: Since this approach requires accessing changing values directly when _other_ values change, it is possible to forget to observe some values at all, leading to change propagation failure.
3. **Nested observations**: When the current selection changes, we need to observe the new selection. Handling observations inside observations is really clumsy and easy to get wrong.

In reactive programming, assuming all state values send their changes through reactive programming channels, rather than Key-Value-Observing, you’d only need the following:

```swift
let latestSelection = FileSelection.currentSelection
   .flatMapLatest { curSel in curSel?.selection.map(Optional.some) ?? .just(nil) }
lifetimes += Server.currentServer
   .combineLatest(latestSelection) { server, selection in server != nil && selection?.isEmpty == false }
   .subscribeValues(context: .main) { [uploadButton] canUpload in uploadButton.isEnabled = canUpload }
```

<sub>"App scenario - dynamic view properties" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

The above problems are fixed:

1. this code is completely threadsafe
2. all notifications are issued in sequence without repeated processing of values
3. no repeated logic
4. no values accessed outside observation
5. nested observation is handled through the dedicated `flatMapLatest` function which handles the clumsy aspects

## Maintaining a threadsafe dictionary of values

That was a look at the “subscriber” end of a dependency. Let’s look at the “sender” end by taking a look at a threadsafe dictionary of values.

You might use a dictionary as the “model” in a trivial app. Even if more sophisticated storage than a dictionary is required, the pattern of updating and notifying shown here should be the same in _any_ well written app.

Solving the problem with standard Cocoa classes `DispatchQueue` and `NotificationCenter` might look like the following:

```swift
class DocumentValues {
   typealias Dict = Dictionary<AnyHashable, Any>
   typealias Tuple = (AnyHashable, Any?)

   static let changed = Notification.Name("com.mycompany.mymodule.documentvalues.changed")
   
   // Underlying storage protected by a `DispatchQueue` mutex
   private var storage = Dict()
   private let mutex = DispatchQueue(label: "")

   init() {}
   
   // Access to the storage involves copying out of the mutex
   var values: Dict {
      return mutex.sync {
         return storage
      }
   }
   
   // Remove a value and send a change notification
   func removeValue(forKey key: AnyHashable) {
      let latest = mutex.sync { () -> Dict in
         storage.removeValue(forKey: key)
         return storage
      }
      NotificationCenter.default.post(name: DocumentValues.changed, object: self,
         userInfo: latest)
   }

   // Create/change a value and send a change notification
   func setValue(_ value: Any, forKey key: AnyHashable) {
      let latest = mutex.sync { () -> Dict in
         storage[key] = value
         return storage
      }
      NotificationCenter.default.post(name: DocumentValues.changed, object: self,
         userInfo: latest)
   }
}
```

<sub>The complete code for this view controller appears on the NotfyingDictionary page of the NonReactive playground in the [Cocoa with Love Playgrounds project](https://github.com/mattgallagher/CocoaWithLovePlaygrounds).</sub>

I have been carefully copying values in and out of the mutex and it is memory safe in all cases. The class uses notifications so that other interfaces can receive updates.

What’s the problem?

Let’s look at the key failings, again:

1. **Bad behavior is encouraged**: It is easy for another interface to access the current `values` property but it is additional work to properly observe the `DocumentValues.changed` notification, so you’re encouraging dependent interfaces to _forget_ to properly observe changes and fall out-of-sync.
2. **There is no safe way to initialize and subscribe**: If you get the `values` then start observing notifications, it’s possible that a change could occur _between_ these two actions (causing you to lose a notification). If you observe notifications first, then get the `values`, you might get a first notification before you’ve properly initialized. `NSKeyValueObservingOptions.initial` could fix the problem for KVO but with `Notification`s, you’d need some clever coding to work around this problem.
3. **Prone to deadlocks**: The `removeValue` function on `storage` deletes an arbitrary value inside a mutex. If there is a `deinit` on this deleted value and the `deinit` tries to change the `DocumentValues` (re-entering the mutex), you’ve created a deadlock.
4. **It’s difficult to refactor**: There’s no single point that all changes to the `storage` go through. If you need to add functionality in future – like writing `DocumentValues` to a file on each change – you’d have to carefully integrate this change into multiple places.
5. **No lifecycle notifications**: If the `DocumentValues` object is deleted, it doesn’t notify this, by default.

Many of these are the same or similar problems to the previous example. As before, these problems can be solved through additional careful coding but as before, each solution would require additional code and additional complexity and more than that: you’d need to first realize that the problem exists; due to the subtlety of all of these problems, you might not notice any issues during testing.

An implementation using reactive programming would replace the `values` property with a channel that emits the current value, followed by future updates, as a stream.

```swift
class DocumentValues {
   typealias Dict = Dictionary<AnyHashable, Any>
   typealias Tuple = (AnyHashable, Any?)
   
   private let input: SignalInput<Tuple>
   
   // Access to the data is via the signal.
   public let signal: SignalMulti<Dict>

   init() {
      // Actual values storage is encapsulated within the signal
      (self.input, self.signal) = Signal<Tuple>.channel()
         // All updates pass through this single, common function.
         .map(initialState: [:]) { (state: inout Dict, update: Tuple) in
            switch update {
            case (let key, .some(let value)): state[key] = value
            case (let key, .none): state.removeValue(forKey: key)
            }
            return state
         }
         // Convert single `Signal` into multi-subscribable `SignalMulti` with `continuous`
         .continuous(initialValue: [:]).tuple
   }
   
   func removeValue(forKey key: AnyHashable) {
      input.send((key, nil))
   }
   
   func setValue(_ value: Any, forKey key: AnyHashable) {
      input.send((key, value))
   }
}
```

<sub>"App scenario - threadsafe key-value storage" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

The code size is not significantly different (27 non-blank, non-comment lines before versus 23 after) but in this case, every problem mentioned above is solved implicitly.

1. The same work is involved in accessing a value once or subscribing properly so good behavior is encouraged.
2. If separate handling of initial value and subsequent values is required (e.g. using a `capture` and `subscribe` sequence as described in the previous article) the stream is correctly paused so you can’t miss a notification.
3. Everything is threadsafe (the `map` closure will never be concurrently invoked and re-entrancy is not possible)
4. All changes go through the `map` function and can be coordinated there.
5. A `SignalError.cancelled` message is automatically sent to subscribers if `input` is released.

Associated with being “threadsafe”, notice that there are no longer any mutable variables in the class; state is encapsulated inside the `Signal`.

Not only is this less code than the previous class but there are far fewer implementation mistakes you could make; code is more declarative and contained and there’s no mutex to carefully administer and work around.

## An asynchronous task with a timeout

I originally gave the following code in a previous article, [Testing Actions over Time](https://www.cocoawithlove.com/blog/testing-actions-over-time.html#let-s-fill-in-the-service-implementation). The code contains a class with a `start` function that does two things:

1. Invokes a `work` function, which takes a callback and invokes it on completion
2. Starts a timer, which, if it fires _before_ the `work` function invokes its completion handler, cancels the `work` function.

I’ve made the class a little complicated by allowing the user to call `start` multiple times on the `Service` class – possibly while a previous call to `start` still has asynchronous tasks outstanding.

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
   
   // This `Service` invokes the `underlyingConnect` and starts a timer
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

<sub>The complete code for this view controller appears on the TimeoutService page of the NonReactive playground in the [Cocoa with Love Playgrounds project](https://github.com/mattgallagher/CocoaWithLovePlaygrounds).</sub>

Now, this code works and as far as I’m aware, there are no bugs. But it’s _**gigantic**_ given that all it is doing is applying a timeout to an underlying function.

Most of the size is due to careful coding to avoid problems. After the `start` function starts the `work` and the `timer`, it needs to aggregate the lifetimes of both and store in the `currentAction`. There’s some careful handling of the `previousAction` which is released outside the `queue.sync` (to prevent re-entrancy deadlock problems). Both the `underlyingAction`’s handler closure and the `timer`’s handler closure need to access the `current` lifetime (to cancel things properly) and since this lifetime retains the closures themselves, there’s some weak reference juggling going on too.

We shouldn’t need to carefully code around so many issues. We want the code smaller. We want it simpler.

Let’s try the whole thing with reactive programming.

```swift
struct TimeoutService {
   let startWithTimeout: SignalMultiInput<DispatchTimeInterval>
   let signal: SignalMulti<Result<String>>
   
   init(asynchronousWork: @escaping () -> Signal<String>) {
      (startWithTimeout, signal) = Signal<DispatchTimeInterval>.multiChannel()
         .map { seconds in
            asynchronousWork()
               .timeout(interval: seconds)
               .materialize()
         }
         .switchLatest()
         .multicast()
         .tuple
   }
}
```

<sub>"Parallel composition - operators" appears in the [CwlSignal.playground](https://github.com/mattgallagher/CwlSignal).</sub>

The difference is astounding; it doesn’t even _resemble_ the original class. However, this class does the same thing, just over reactive programming channels, rather than over callbacks with state and mutexes. With reactive programming, all of the threading and lifetime management that caused a huge burden for the previous implementation are implicit – they’re still _there_ but they’re just handled internally.

The two implementations aren’t _identical_. In this implementation, inputs and outputs follow reactive conventions. Instead of calling a `start` function, the asynchronous work is started by sending a timeout time to the `startWithTimeout` input. Instead of passing a callback function to the `start` function to receive completion, we can subscribe to the `signal`.

Getting comfortable with common reactive programming conventions and operators like `switchLatest` and `materialize` can take a little time but these functions follow the behavior of typical [ReactiveX implementations](http://reactivex.io/documentation/operators.html) so you can also consult that documentation to gain additional insight.

In case you think using a built-in function for the `timeout` is cheating in this comparison, it is simple to replace the `asynchronousWork().timeout(interval: seconds).materialize()` code with:

```swift
let timer = Signal<()>.timer(interval: .seconds(10))
return asynchronousWork().combine(second: timer) { eitherSignal, next in
   switch eitherSignal {
   case .result1(let r): next.send(result: r)
   case .result2: next.send(error: MyErrors.timeout)
   }
}.materialize()
```

It’s a little more verbose but still not complicated.

## Conclusion

Reactive programming changes how data is stored, how it flows through your program and how the elements of your program are connected. The result is significant improvement across the following categories:

- Thread safety
- Coordinating concurrent asynchronous tasks
- Loose coupling of components
- Data dependencies

The biggest advantage comes when you realize that in applying a solution to just one of these problems, you’ve gained a solution to the other three for free.

For situations where the code already addresses these issues properly, reactive programming can deliver _significant_ lines-of-code savings.

The end result is code that is easier to write and easier to maintain.

### Looking forward…

There’s a lot of carefully written code in the [CwlSignal](https://github.com/mattgallagher/CwlSignal) library. Even if – despite all the discussion in this article – you’re not interested in reactive programming, there’s lots to learn about how CwlSignal solves problems internally like avoiding re-entrancy and integrating with Key-Value-Observing.

## Appendix: A little bit of history

Even though the terms “reactive” and “reactive systems” have been in use in programming at least since Alan Kay’s 1969 paper [The Reactive Engine](http://www.mprove.de/diplom/gui/kay69.html), modern use of the term “reactive programming” really refers to ideas started in [Conal Elliot](http://conal.net) and Paul Hudak’s 1997 paper [Function Reactive Animation](http://conal.net/papers/icfp97/).

Functional reactive animation, later called functional reactive programming (FRP) is about “behaviors” (continuous, time-dependent equations like those describing the position of a moving object) and how they change and interact with “events” (one-off occurrences at an instantaneous time).

All of this might have been irrelevant to imperative programming languages since pull-driven, lazily evaluated “behaviors” (the primary output of functional reactive programming) are uninteresting for most imperative programming which can use push-driven stateful calculations to produce the same results in a simpler way.

It turns out, however, that the patterns that functional reactive programming provides for handling, transforming and responding to “events” (side effects that functional reactive programming tries to minimize) easily carry across to imperative languages and remain similarly useful for managing and responding to streams of discrete events – even when those streams are predominantly _push_ driven, as in imperative programming, rather than lazily evaluated _pull_ driven, as is typical in functional languages.

Thus we get “reactive programming” (note the absence of “functional”) which focuses on emitting, transforming and subscribing to streams of events.

The biggest difference between functional reactive and imperative reactive is ultimately “time”. In functional reactive programming, time is a parameter passed into each calculation. In imperative reactive programming, time may be pulled from the context but the actual time is usually less important than the order in which relevant mutexes are acquired. This means that functional reactive programming operates a bit more like a simulation (“if two objects should happen to interact in this way at this time…”) whereas reactive programming is more like a simple ordering of blocks into a sequence by the order that they happen to be processed. One of the effect of this is that functional reactive programming can handle two events that are literally simultaneous whereas imperative reactive programming has no such notion of simultaneity.

While there may have been prior implementations of reactive programming in an imperative languages, the first popular implementation is the [Reactive Extensions (Rx) for .NET](https://github.com/Reactive-Extensions/Rx.NET) which was [first released in late 2009](https://blogs.msdn.microsoft.com/rxteam/2009/11/17/announcing-reactive-extensions-rx-for-net-silverlight/).

The Reactive Extensions largely mimic the .NET framework’s `IObservable` as the primary metaphor. Along with integration of `IDisposable` and ideas from `IEnumerable` and LINQ. Many implementations of reactive programming on imperative platforms continue to employ terminology like “Observable” and “Disposable” for the core communication and lifetime protocols, respectively, revealing their lineage from the Reactive Extensions.
