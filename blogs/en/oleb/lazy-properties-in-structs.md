---
title: Lazy Properties in Structs
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/12/lazy-properties-in-structs-swift/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:629718bc01990be6'
translated: false
---

> 原文：[Lazy Properties in Structs](https://oleb.net/blog/2015/12/lazy-properties-in-structs-swift/)　·　Ole Begemann

# Lazy Properties in Structs

Swift’s [`lazy` keyword](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Properties.html#//apple_ref/doc/uid/TP40014097-CH14-ID257) allows you to define a property whose initial value is computed when it is first accessed. As an example, imagine a struct to represent an image. The image’s metadata dictionary might be expensive to create, and we want to defer this cost until the data is needed. We can declare a `lazy var` like this:

```
struct Image {
    lazy var metadata: [String:Any] = {
        // Load image file and parse metadata
        // (expensive)
        ...
        return ...
    }()
}
```

Note that we have to use `var` in the property declaration. `let` constants must always have a value before instance initialization is complete, and this is not guaranteed for lazy variables.

Accessing the lazy property is a mutating operation because the property’s initial value is set on the first access. When a struct (which is a value type) contains a lazy property, any owner of the struct that accesses the lazy property must therefore declare the struct as a variable, too, because accessing the property means potentially mutating its container. So this is not allowed:

```
let image = Image()
print(image.metadata)
// error: Cannot use mutating getter on immutable
// value: 'image' is a 'let' constant.
```

We could force users of our `Image` type to use `var`, but that could be inconvenient (for example, if it is used [as a function parameter](https://github.com/apple/swift-evolution/blob/master/proposals/0003-remove-var-parameters-patterns.md)) or confusing (because getters are usually not mutating).

# Box all the things

Another option is to wrap the lazy value in a class, similar to the often-used [`Box` type](https://github.com/robrix/Box). Because classes are reference types, a struct can contain a `let` constant to a class instance and still be immutable even if the referenced object itself is mutated.

Let’s first define an enum, called `LazyValue`, to represent a value of type `T` that can be computed lazily. It has two possible states: either the computation has yet to be performed, or the value has already been computed. In the former case, it stores the function that performs the computation. In the latter case, it stores the computed value:

```
private enum LazyValue<T> {
    case notYetComputed(() -> T)
    case computed(T)
}
```

Now we wrap this enum in a class, called `LazyBox`, so that we can mutate it independently of its container. The owner of the `LazyBox` instance can remain immutable. The implementation could look like this:

```
final class LazyBox<T> {
    init(computation: @escaping () -> T) {
        _value = .notYetComputed(computation)
    }

    private var _value: LazyValue<T>

    var value: T {
        switch self._value {
        case .notYetComputed(let computation):
            let result = computation()
            self._value = .computed(result)
            return result
        case .computed(let result):
            return result
        }
    }
}
```

The class is initialized with the function it should use to compute the value. We store this function in a private `LazyValue` property until we need it. The public interface of the class is the read-only `value` property. In the getter we check if we have already computed the value, and return it if we have. If not, we evaluate the computation function and cache the value for subsequent reads.

We can use `LazyBox` like this, and verify that the computation function is indeed only evaluated once:

```
var counter = 0
let box = LazyBox<Int> {
    counter += 1;
    return counter * 10
}
assert(box.value == 10)
assert(box.value == 10)
assert(counter == 1)
```

This approach has the benefit that it can be used with constant structs. In other aspects it’s a little less convenient to use than a plain `lazy` variable would be because clients have to use the `value` property to access the value. If that’s not good enough, we could hide the implementation by exposing another computed property that returns `LazyBox.value` and making the `LazyBox` property private.

```
struct Image {
    // Lazy storage
    private let _metadata = LazyBox<[String:Any]> {
        // Load image file and parse metadata
        // (expensive)
        ...
        return ...
    }
    var metadata: [String:Any] {
        return _metadata.value
    }
}

let image = Image()
print(image.metadata) // no error
```

And the containing struct retains its value semantics. It’s a common pattern to use reference types internally inside a value type and implement it in a way that guarantees value semantics. The standard library uses it for many of the collection types.

# Concurrency

There’s one final potential issue with this implementation, and that is concurrency. If `LazyBox.value` is accessed simultaneously from multiple threads before it has computed the value, it could evaluate the computation function multiple times. This is something you may want to avoid if the computation function has side effects or is expensive.

We can guarantee that the function is only evaluated once by routing all reads and writes of the internal `_value` property through a private serial queue. Here is the new implementation:

```
import Dispatch

final class LazyBox<T> {
    init(computation: @escaping () -> T) {
        _value = .notYetComputed(computation)
    }

    private var _value: LazyValue<T>

    /// All reads and writes of `_value` must
    /// happen on this queue.
    private let queue = DispatchQueue(label: "LazyBox._value")

    var value: T {
        var returnValue: T? = nil
        queue.sync {
            switch self._value {
            case .notYetComputed(let computation):
                let result = computation()
                self._value = .computed(result)
                returnValue = result
            case .computed(let result):
                returnValue = result
            }
        }
        assert(returnValue != nil)
        return returnValue!
    }
}
```

The downside is a small performance hit on every access of `value`, and possible contention if many threads read the value simultaneously because they all have to go through the same serial queue. Given that very little work is performed on the queue after the cached value has been computed once, this latter aspect should be negligible in the vast majority of cases.

It’s worth noting that Swift doesn’t make this guarantee for the `lazy` keyword. [Apple says this in the Swift book](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Properties.html#//apple_ref/doc/uid/TP40014097-CH14-ID257):

> Note: If a property marked with the `lazy` modifier is accessed by multiple threads simultaneously and the property has not yet been initialized, there is no guarantee that the property will be initialized only once.

# Using instance data inside the lazy computation

**Update November 12, 2017:** Added this section.

The common use case for our `LazyBox` type is as an immutable property on some type. This only works if the `LazyBox` value can be fully initialized when its parent type is initialized, as we showed above for the `Image` struct. Unfortunately, this is a pretty big limitation: it means that the lazy evaluation function can’t access other instance properties of the parent type, because we’re not allowed to access `self` until initialization is complete.

To make this work, we’d need to pass `self` as an argument into the evaluation function so that the function can use the value without capturing it. We can do this by adding another generic parameter to `LazyValue` and `LazyBox` that represents the input for the evaluation function.

Here’s the new `LazyValue` implementation:

```
private enum LazyValue<Input, Value> {
    case notYetComputed((Input) -> Value)
    case computed(Value)
}
```

`LazyBox` receives a similar change to its initializer to accomodate the new parameter. More importantly, notice that I changed the `value` property to a function named `value(input:)` that takes the input argument and passes it on to the evaluation function (if the value hasn’t been computed yet; if it has, the argument is ignored):

```
final class LazyBox<Input, Result> {
    init(computation: @escaping (Input) -> Result) {
        _value = .notYetComputed(computation)
    }

    private var _value: LazyValue<Input, Result>

    /// All reads and writes of `_value` must
    /// happen on this queue.
    private let queue = DispatchQueue(label: "LazyBox._value")

    func value(input: Input) -> Result {
        var returnValue: Result? = nil
        queue.sync {
            switch self._value {
            case .notYetComputed(let computation):
                let result = computation(input)
                self._value = .computed(result)
                returnValue = result
            case .computed(let result):
                returnValue = result
            }
        }
        assert(returnValue != nil)
        return returnValue!
    }
}
```

The usage example would look like this now:

```
struct Image {
    // Lazy storage
    private let _metadata =
        LazyBox<Image, [String:Any]> { image in
        // Use image to access the instance's
        // state here
    }
    var metadata: [String:Any] {
        return _metadata.value(input: self)
    }
}
```

# Property behaviors

**Update a few minutes after posting:** An hour before I published this, [Joe Groff](https://twitter.com/jckarter) posted a far-reaching [proposal for property behaviors](https://forums.swift.org/t/proposal-property-behaviors/594) to the Swift evolution mailing list that, if adopted, would make the things I discuss in this post (and a lot more) implementable in a much more natural way. I encourage you to take a look.
