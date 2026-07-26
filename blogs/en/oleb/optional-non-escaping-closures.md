---
title: Optional Non-Escaping Closures
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/10/optional-non-escaping-closures/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:33b136b6ed072caa'
translated: false
---

> 原文：[Optional Non-Escaping Closures](https://oleb.net/blog/2016/10/optional-non-escaping-closures/)　·　Ole Begemann

# Optional Non-Escaping Closures

Swift differentiates between _escaping_ and _non-escaping_ closures. An [escaping closure](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html) is one that is (potentially) called _after_ the function the closure is passed to returns — that is, the closure _escapes_ the scope of the function it is passed to as an argument.

Escaping closures are often associated with asynchronous control flow, like in the following examples:

- A function starts a background task and returns immediately, reporting the result of the background task via a completion handler.
- A view class stores a closure in a property as an event handler for a button tap event. The class calls the closure every time the user taps the button. The closure escapes the property setter.
- `DispatchQueue.async`

  . The task closure outlives the call to

  .

Contrast this with [`DispatchQueue.sync`](https://developer.apple.com/reference/dispatch/dispatchqueue/2016081-sync), which waits until the task closure has finished executing before it returns — the closure never escapes. The same is true for [`map`](https://developer.apple.com/reference/swift/sequence/1641748-map) and the other common sequence and collection algorithms in the standard library.

# Why is differentiating between escaping and non-escaping closures important?

In short, memory management. A closure keeps a strong reference to every object the closure captures — and that includes `self` if you access any property or instance method of `self` inside the closure, because all of these carry an implicit `self` parameter.

It’s very easy to accidentally introduce [reference cycles](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/AutomaticReferenceCounting.html#//apple_ref/doc/uid/TP40014097-CH20-ID56) in this way, which is why the compiler requires you to explicitly refer to `self` inside closures. This forces you to think about potential reference cycles and manually resolve them [using capture lists](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/AutomaticReferenceCounting.html#//apple_ref/doc/uid/TP40014097-CH20-ID56).

However, it’s impossible to create a reference cycle with a non-escaping closure — the compiler can guarantee that the closure will have released all objects it captured by the time the function returns. For this reason, the compiler only requires explicit references to `self` for _escaping_ closures. This makes non-escaping closures significantly more pleasant to use.

Another benefit of non-escaping closures is that the compiler can apply more aggressive performance optimizations. For example, the compiler can omit some retain and release calls when the lifetime of the closure is known. In addition, the memory for a closure’s context can be kept on the stack instead of the heap if the closure is non-escaping — though I don’t know if the Swift compiler currently performs this optimization (an [open March 2016 bug report](https://bugs.swift.org/browse/SR-904) suggests that it doesn’t).

# Closures are non-escaping by default …

Beginning in Swift 3, non-escaping closures [are now the default](https://github.com/apple/swift-evolution/blob/master/proposals/0103-make-noescape-default.md). If you want to allow a closure parameter to escape, you need to add the `@escaping` annotation to the type. For instance, here are the declarations for `DispatchQueue.async` (escaping) and `DispatchQueue.sync` (non-escaping):

```
class DispatchQueue {
    ...
    func async(/* other params omitted */, execute work: @escaping () -> Void)
    func sync<T>(execute work: () throws -> T) rethrows -> T
}
```

Before Swift 3, it was the other way around: escaping was the default, and you’d add `@noescape` to override. The new behavior is better because it’s safe by default: a function argument now must be explicitly annotated to signal the potential for reference cycles. Thus, the `@escaping` annotation serves as a warning to the developer using the function.

# … but only as immediate function parameters

There’s a catch to the non-escaping-by-default rule: it only applies to closures in _immediate function parameter position_, i.e. any function argument that has a function type. All other closures are escaping.

## What does immediate parameter position mean?

Let’s look at some examples. The simplest case is something like `map`: a function that takes an immediate closure parameter. As we’ve seen, the closure is non-escaping (I omitted some details from the real signature of `map` that are not important for this discussion):

```
func map<T>(_ transform: (Iterator.Element) -> T) -> [T]
```

### Variables of function type are always escaping

Contrast this with a variable or property that has a function type. It is automatically escaping, even without explicit annotation (in fact, adding an explicit `@escaping` is an error). This makes sense, because assigning a value to a variable implicitly lets the value escape to the variable’s scope, which shouldn’t be permitted for non-escaping closures. It can be confusing, however, that the a bare, unannotated function type has a different meaning in a parameter list than anywhere else.

### Optional closures are always escaping

More surprisingly, closures that _are_ used as parameters, but are wrapped in some other type (such as a tuple, an enum case, or an optional), are also escaping. Since the closure is no longer an _immediate_ parameter in this case, it automatically becomes escaping. As a consequence, in Swift 3.0 you can’t write a function that takes a function argument where the parameter is both optional and non-escaping. Consider the following contrived example: the `transform` function takes an integer `n` and an optional transformation function `f`. It returns `f(n)`, or `n` if `f` is `nil`:

```
/// Applies `f` to `n` and returns the result.
/// Returns `n` unchanged if `f` is nil.
func transform(_ n: Int, with f: ((Int) -> Int)?) -> Int {
    guard let f = f else { return n }
    return f(n)
}
```

Here, the function `f` is escaping because `((Int) -> Int)?` is shorthand for `Optional<(Int) -> Int>`, i.e. the function type is not in _immediate_ parameter position. This is undesirable because there’s no reason `f` shouldn’t be non-escaping here.

### Replace optional parameter with default implementation

The Swift team is [aware of this limitation](https://bugs.swift.org/browse/SR-2444) and plans to fix it in a future release. Until then, it is important to be aware of it. There’s currently no way to force an optional closure to be non-escaping, but in many situations, you can probably avoid making the argument optional by providing a default value for the closure. In our example, the default value is the identity function, which simply returns the argument unchanged:

```
/// Uses a default implementation for `f` if omitted
func transform(_ n: Int, with f: (Int) -> Int = { $0 }) -> Int {
    return f(n)
}
```

### Use overloading to provide an optional and a non-escaping variant

If providing a default value is not possible, Michael Ilseman suggests to [use overloading as a workaround](https://forums.swift.org/t/escaping-may-only-be-applied-to-parameters-of-function-type/4017/9) — you can write two variants of the function, one with an optional (escaping) function parameter and one with a non-optional, non-escaping parameter:

```
// Overload 1: optional, escaping
func transform(_ n: Int, with f: ((Int) -> Int)?) -> Int {
    print("Using optional overload")
    guard let f = f else { return n }
    return f(n)
}

// Overload 2: non-optional, non-escaping
func transform(_ input: Int, with f: (Int) -> Int) -> Int {
    print("Using non-optional overload")
    return f(input)
}
```

I added some print statements to demonstrate which function gets called. Let’s test this with various arguments. Unsurprisingly, if you pass `nil`, the type checker selects the first overload because it’s the only one that’s compatible with the input:

```
transform(10, with: nil) // → 10
// Using optional overload
```

The same is true if you pass a variable that has an optional function type:

```
let f: ((Int) -> Int)? = { $0 * 2 }
transform(10, with: f) // → 20
// Using optional overload
```

Even if the variable has a non-optional type, Swift will still select the first overload. This is because the function stored in the variable is automatically escaping and is therefore not compatible with the second overload, which expects a non-escaping argument:

```
let g: (Int) -> Int = { $0 * 2 }
transform(10, with: g) // → 20
// Using optional overload
```

But things change when you pass a closure expression, i.e. a function literal in place. Now the second, non-escaping overload gets selected:

```
transform(10) { $0 * 2 } // → 20
// Using non-optional overload
```

Since it is very common to call higher-order functions with literal closure expressions, this lets you take the happy path (i.e. non-escaping, without having to think about reference cycles) in the majority of situations while still giving you the option to pass `nil`. If you decide to go this route, make sure to document why you need the two overloads.

### Typealiases are always escaping

One final thing to be aware of is that you can’t add escaping or non-escaping annotations to typealiases in Swift 3.0. And if you use a typealias for a function type in a function declaration, that parameter is always considered escaping. A fix for [this bug](https://bugs.swift.org/browse/SR-2316) is already in master and should be part of the next release.
