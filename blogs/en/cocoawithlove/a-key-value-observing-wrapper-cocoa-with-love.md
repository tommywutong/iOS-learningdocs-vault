---
title: 'A key-value observing wrapper | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/key-value-observing-wrapper.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:9ef2c0a58b85fe47'
translated: false
---

> 原文：[A key-value observing wrapper | Cocoa with Love](https://www.cocoawithlove.com/blog/key-value-observing-wrapper.html)　·　Cocoa with Love (Matt Gallagher)

In this article, I’ll show you a helper type named `KeyValueObserver` that improves syntax and addresses some core problems in key-value observing. This class is used by the [CwlSignal project](https://github.com/mattgallagher/CwlSignal) to adapt key-value observing into a reactive programming pattern but the class depends only on the `OnDelete` class from [CwlUtils](https://github.com/mattgallagher/CwlUtils) so you can just copy these two files and use it without reactive programming, to improve the experience of working with key-value observing.

There are other wrappers for key-value observing that apply type-safety or synchronize notifications or similar abstractions around key-value observing. This isn’t one of those; instead it largely keeps the same “change dictionary” output and thread-safety implications of the underlying key-value observing, assuming that your application will want to apply its own logic to process the change dictionary or ensure thread safety. I’ll show how CwlSignal applies both of these things over the top of `KeyValueObserver`.

The purpose of the `KeyValueObserver` class – other than a dramatic improvement in syntax – is to address deeper problems in the key-value observing machinery such as lack of reporting about where changes occurred on a key path, failure to observe weak properties correctly and eliminating the dreaded `NSInternalInconsistencyException` if the observed object deallocates while observers are registered.

> **Update for Swift 4**: Since I released this code, Swift added type-safe key-paths and the associated `observe(_:, options:, changeHandler:)`. While it doesn’t offer all the same capabilities as the code in this article, the type-safety is enough of a reason to use that observe function instead of this stringly-typed approach.

## A little history

Key-value observing first appeared in Mac OS X 10.3. At the time, I was astounded by the “magic” of it. Many classes appeared to automatically support key-value observing for simple properties. It started a fascination for me where I tried to achieve other tricks with the Objective-C messaging system. Ultimately, this fascination waned – years before Swift arrived – due to the many kinds of maintenance headache that dynamic messaging can cause.

If you ever relied on implicitly supported key-value observing (observing a value where the documentation didn’t explicitly advertise the value as key-value observable), you doubtless saw one of the effects of relying on tricks; it was unreliable. It wasn’t unreliable due to any flaw in the key-value observing machinery itself but simply due to the fact that unless a class carefully chooses to support key-value observing for a particular property, it’s likely to occasionally update that property in different ways that simply don’t trigger key-value observing notifications.

So despite being apparently “magic”, key-value observing still required the same methodical design at the emitting end as other notification systems.

On its own, that’s not really a problem; it negates some of the “magic” but it doesn’t negate the worthiness of the entire key-value observing API. However, the system does take a turn for the worse when we start to look at the observing end.

Proper implementations across `addObserver`, `observeValue` and `removeObserver` are large, complex and fraught with a number of risks that are not always apparent at first glance: failing to call super in the `observeValue` method, failing to keep observations unique, failing to correctly process the `change` dictionary, failing to remove the observation when done.

Even once you’ve implemented everything and your code appears to mostly work, if the observed object is somehow released before the observation is removed – due to a code path you hadn’t fully tested – the whole program crashes:

```
2016-12-31 09:16:14.476134 MyApp[63688:8417160] *** Terminating app due to uncaught
exception 'NSInternalInconsistencyException', reason: 'An instance 0x100a072c0 of class
SomeModule.SomeClass was deallocated while key value observers were still registered
with it. Current observation info: <NSKeyValueObservationInfo 0x100a09e30> (
```

In my experience, these types of lifecycle ordering glitches do happen from time to time; not frequently but often enough that a better approach than crashing is strongly desired.

## Key-value observing in Swift

Newly written programs should use reactive programming or other more modern change management approaches instead of key-value observing but when deadling with existing APIs, we often don’t have a choice.

So let’s look at what’s involved in key-value observing in Swift. There are dozens of ways to implement the observing end – each with different drawbacks and costs. It’s not a system that feels like it’s “on rails”, instead you’re really designing your own system each time. I’m going to give an example of what I consider to be “good” handling of key-value observing but keep in mind that it still has its own costs and drawbacks relative to other approaches. If you want, you can compare this approach to another that [I demonstrated in a previous article](https://www.cocoawithlove.com/blog/reactive-programming-what-and-why.html#a-button-dependent-on-two-state-values).

Remember, _all_ of the following code is simply to handle the observing of a _single_ key-value observing property.

```swift
class MyClass: NSObject {
   var observations = Dictionary<UnsafeMutableRawPointer, (NSObject, String)>()
   
   // Set up the observations in some function (constructor/viewDidLoad/awakeFromNib)
   func startObserving(observedObject: TargetType) {
      // Implementing addObserver properly requires a context object to keep the
      // observation unique. We can make this a wrapper or specialized handling class but
      // the simplest scenario is a dummy allocation; little more than a unique key.
      let context = UnsafeMutableRawPointer.allocate(bytes: 1, alignedTo: 0)

      // We need to store the context object so it persists and we can test against it
      // later. It's usually a good idea to retain the observedObject too, to avoid
      // exceptions.
      self.observations[context] = (observedObject, #keyPath(TargetType.targetProperty))

      // Finally, we can add the observer
      observedObject.addObserver(self, forKeyPath: #keyPath(TargetType.targetProperty),
         options: NSKeyValueObservingOptions.new.union(NSKeyValueObservingOptions.initial),
            context: context)
   }
   
   // Implement the observeValue function
   override func observeValue(forKeyPath keyPath: String?, of object: Any?,
      change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {
      // We need to make *multiple* checks before we can continue
      if let c = context, let (target, _) = self.observations[c] as? TargetType, let
         newValue = change?[.newKey] as? TargetPropertyType {
         // If the context object is a specialied handling class, then it likely knows
         // what keyPath to which this observation relates. However, we're not using a
         // customized handler class, we still need to switch here on the keyPath since
         // our class may need to handle multiple different types of property.
         switch keyPath {
         case .some(#keyPath(TargetType.targetProperty)):
            // Do something to `self` in response to `newValue`
         default: break
         }
      } else {
         // Need to invoke super
         super.observeValue(forKeyPath: keyPath, of: object, change: change,
            context: context)
      }
   }
   
   deinit {
      // Remember to remove all of the observations we're holding and release the context
      for (context, (target, keyPath)) in observations {
         target.removeObserver(self, forKeyPath: keyPath, context: context)
         context.deallocate(bytes: 1, alignedTo: 0)
      }
   }
}
```

The large number of comments make this code look bigger than it really is but the reality remains: this is a lot of code.

Notice that the code comments repeatedly refer to “a specialized handling class” that would act as the “context” for the observation. Obviously, that’s where we’re going.

## A wrapper class

The `KeyValueObserver` wrapper class that I’m presenting in this article reduces the above code down to the following:

```swift
class MyClass: NSObject {
   var observers = [KeyValueObserver]()
   
   func startObserving(observedObject: TargetType) {
      // Construct the observation
      let observer = KeyValueObserver(source: observedObject, keyPath:
         #keyPath(TargetType.targetProperty)) { [weak self] change, reason in
         
         // Safely get strong ref to self and the new value from the change dict
         guard let s = self, let newValue = change[.newKey] as?
            TargetPropertyType else { return }
         
         // Do something to `s` (aka `self`) in response to `newValue`
      }
      
      // Retain the observation
      observers.append(observer)
   }
}
```

This is not a case where I’m aiming for maximum syntactic efficiency. The work required still involves a little boilerplate, mostly because `KeyValueObserver` isn’t trying to re-invent the wheel.

Some verbosity remains due to the following three points:

- is not generic over the observed type (you need to dynamically downcast observed values)
- dictionary is the same as that used by key value observing (although it’s guaranteed to be non-nil)
- can be used with

  (although the default value of

  +

  is used implicitly, here)

The advantage to keeping these minor complexities is that this `KeyValueObserver` should be able to replace _any_ usage of Cocoa key-value observing. However, if you want maximum syntactic efficiency, you’ll still want an additional layer that further adapts the output (e.g. CwlSignal or simply a subclass of `KeyValueObserver` that applies a transformation to the `callback` applied to the `init` method).

For example, [CwlSignal](https://github.com/mattgallagher/CwlSignal) includes a wrapper around `KeyValueObserver` that offers built-in handling for the first two bullet points (and locks the third point to either `new` or `new` + `initial`), resulting in the following code:

```swift
class MyClass: NSObject {
   var endpoints = [Cancellable]()
   
   func startObserving(observedObject: TargetType) {
      endpoints += Signal<TargetPropertyType>.keyValueObserving(observedObject, keyPath:
         #keyPath(TargetType.targetProperty)).subscribeValues { [weak self] newValue in
         // Do something to `self` in response to `newValue`
      }
   }
}
```

The `Signal<T>.keyValueObserving` function is just a static function around `signalKeyValueObserving` that dynamically downcasts the `Any` results typically emitted from key-value observing to the value type `T`, discarding values of the wrong type. You can see how these functions are implemented in the [CwlSignalCocoa.swift file in the CwlSignal project](https://github.com/mattgallagher/CwlSignal/blob/master/CwlSignal/CwlSignalCocoa.swift?ts=3).

## Advantages of `KeyValueObserver`

Most of the code savings with `KeyValueObserver` come from automatically providing a “specialized handling class” context object, to which I referred in the code comments from the example in the [Key-value observing in Swift](#key-value-observing-in-swift) section. There’s also some savings due to using a trailing closure instead of relying on method overloads.

However, the advantages go deeper than syntactic advantages. If you look closely, you’ll also notice that the `observeValue` example retained `observedObject` in the dictionary, along with the `context` and `keyPath` whereas in the `KeyValueObserver` example the `observedObject` is _not_ retained at all (it is assumed to be kept alive elsewhere).

The `observeValue` example _needed_ to retain the `observedObject` due to the risks associated with the observed object getting released while being observed and triggering an exception. Meanwhile, with `KeyValueObserver`, letting the observed object release while we are observing it is well defined - on release of the observed object, the observing closure will be invoked with the `reason` value set to `.sourceDeleted` (the `change` dictionary will be empty).

The `reason` parameter can also provide further information about _where_ the change occurred, including `.valueChanged` (if the end value changes) and `.pathChanged` (if a change occurs between the observed object and the end of the key path).

## How does `KeyValueObserver` work?

The whole class is fairly straightforward Swift – unlike some other key-value wrappers, it doesn’t need to dip down to Objective-C or engage in any runtime antics like swizzling. The class does use the Objective-C runtime functions to learn if the observed property is `weak` and to set associated objects (used for detecting when the observed object is released) but that’s about as complicated as it gets.

The largest code contribution in the `KeyValueObserver` class is to handle any actual _path_ observing itself. Normally with Cocoa key-value observing, you can pass a “key path” and the intermediate observations along the path are all handled automatically. With `KeyValueObserver`, the key path is parsed and each step in the path is individually observed. This gives greater flexibility and allows more information about _where_ the change occurred but it is responsible for about half the code in the class as these steps need to be deleted and recreated when the path changes. If you look at the class and see anything involving the `tailPath` that you can’t understand – it’s probably just tracking and updating these intermediate key path steps.

There’s one use of `tailPath` that isn’t a key path as you might expect: weak properties. Weak properties don’t always send key value changed notifications for the property. To avoid this problem, `KeyValueObserver` may also include a `tailPath` observer on `self`. This is used because changing weak properties will trigger a change notification from `self`, even when they don’t trigger a change notification on the property itself. `KeyValueObserver` uses this dummy key path to correctly notify the weak property itself.

A final interesting point: I mentioned that this class does not actually change the thread safety of key-value observing (that notifications could still occur concurrently from separate threads). This is true, however, the class _does_ include a mutex. The mutex is used to protect the class’ two mutable state values – it does not deliberately change the serialization of callbacks. If serialization is needed, it should be applied by a layer on top of `KeyValueObserver` (e.g. CwlSignal’s usage of `KeyValueObserver` serializes everything through the `Signal` class).

If you really want to see how it works, I recommend you [look at the code, directly](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlKeyValueObserver.swift?ts=3). I’ve documented most of the functions and variables and discussed a number of other aspects of the code in comments – including why the `source` needs to be tracked as `Unmanaged<NSObject>` instead of `weak` or `unowned`.

## Usage

> The project containing `KeyValueObserver` is available on github: [mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils).

The [CwlKeyValueObserver.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlKeyValueObserver.swift?ts=3) file depends only on the [CwlOnDelete.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlOnDelete.swift?ts=3) file in the same project so you can just copy these two files if that’s all you need.

Otherwise, the [ReadMe.md file for the project](https://github.com/mattgallagher/CwlUtils/blob/master/README.md) contains detailed information on cloning the whole repository and adding the framework it produces to your own projects.

This file is also part of the [CwlSignal framework](https://www.cocoawithlove.com/blog/cwlsignal.html). If you’re already using CwlSignal, then it is already available to you. As a [reactive programming framework](https://www.cocoawithlove.com/blog/reactive-programming-what-and-why.html), CwlSignal offers significantly more options for processing, transforming and handling observations.

## Conclusion

Less code, providing more information and fewer possible problems; `KeyValueObserver` makes the observing end of a key-value observing relationship significantly better. It doesn’t totally smooth out _all_ the rough edges when dealing with key-value observing but it provides a foundation upon which you can add further application-specific filtering.

### Looking forward…

It’s New Year’s Eve 2016 as I write this. Catch you all in 2017!
