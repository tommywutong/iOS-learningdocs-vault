---
title: Optionals and String Interpolation
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/12/optionals-string-interpolation/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:82b8849195ce7ddb'
translated: false
---

> 原文：[Optionals and String Interpolation](https://oleb.net/blog/2016/12/optionals-string-interpolation/)　·　Ole Begemann

# Optionals and String Interpolation

Do you know this problem? You want to display an optional value in the UI or log it to the console for debugging, but you don’t like the default string conversion for optionals, which results in either `"Optional(…)"` or `"nil"`. For example:

```
var someValue: Int? = 5
print("The value is \(someValue)")
// → "The value is Optional(5)"
someValue = nil
print("The value is \(someValue)")
// → "The value is nil"
```

# Using optionals in string interpolation can yield unexpected results

Swift 3.1 will actually actually raise [a warning when you use an optional in string interpolation](https://github.com/apple/swift/pull/5110) like this because this behavior may be surprising. Here’s Julio Carrettoni, Harlan Haskins, and Robert Widmann’s [argument on swift-evolution](https://forums.swift.org/t/proposal-draft-disallow-optionals-in-string-interpolation-segments/4172):

> Given that the `Optional` type is never fit for display to the end user, and can often be a surprising find in the console, we propose that requesting an `Optional`’s debug description be an explicit act. This proposal now requires a warning when using an expression of `Optional` type within a string interpolation segment.

The warning is already implemented in the latest Swift development snapshot (2016-12-01):

![Xcode warning about using an optional value in a string interpolation segment in the latest Swift snapshot](https://oleb.net/media/xcode-warning-string-interpolation-optional-as-any.png)

<sub>Xcode warning about using an optional value in a string interpolation segment in the latest Swift snapshot.</sub>

You have several options to silence the warning:

1. .
2. .
3. .

I don’t particularly like any of these in most cases, but it’s the best the compiler can offer. The problem with the third option is that the [nil-coalescing operator](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/BasicOperators.html#//apple_ref/doc/uid/TP40014097-CH6-ID72) `??` requires matching types — if the left operand is a `T?`, the right operand must be a `T`. Applied to the example above, this means I can provide another `Int` as a default value, but not a string — which is what I’d like to do in this situation.

# A custom optional-string-coalescing operator

I solved this by defining my own custom optional-string-coalescing operator. I decided to name it `???` because of its obvious connection to the nil-coalescing operator.[1](#fn:1) The `???` operator takes any `Optional` on its left side and a default string value on the right, returning a string. If the optional value is non-`nil`, it unwraps it and returns its string description, otherwise it returns the default value. Here’s the implementation:

```
infix operator ???: NilCoalescingPrecedence

public func ???<T>(optional: T?, defaultValue: @autoclosure () -> String) -> String {
    switch optional {
    case let value?: return String(describing: value)
    case nil: return defaultValue()
    }
}
```

[The `@autoclosure` construct](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html#//apple_ref/doc/uid/TP40014097-CH11-ID543) ensures that the right operand is only evaluated when needed, i.e. when the optional is `nil`. This allows you to pass an expression that is expensive or has side effects and only incur the performance cost in the rare case. I don’t think it’s too important to support this for this use case, but it mirrors [the definition of the `??` operator](http://swiftdoc.org/v3.0/operator/qmqm/#func-qmqm-t_-t-defaultvalue_-autoclosure-throws-t) in the standard library. (I decided to leave out the `throws`/[`rethrows`](http://robnapier.net/re-throws) dance the standard library version does, though.)

Alternatively, you could implement the operator with a one-liner using [`Optional.map`](https://developer.apple.com/reference/swift/optional/1539476-map), like so:

```
public func ???<T>(optional: T?, defaultValue: @autoclosure () -> String) -> String {
    return optional.map { String(describing: $0) } ?? defaultValue()
}
```

This is completely equivalent to the first implementation. Which version you prefer is a matter of taste and what coding style you’re used to. I don’t think either is significantly clearer than the other.

One last thing I’d like to note is that you have to make a choice whether you want to use [`String(describing:)`](https://developer.apple.com/reference/swift/string/2427941-init) (i.e. preferring the value’s `description` or [`String(reflecting:)`](https://developer.apple.com/reference/swift/string/1541282-init) (preferring `debugDescription`) to convert the value. The former is better suited for formatting a value for UI display, whereas the latter may be the better choice for logging. Alternatively, you could define another operator (say, `????`) for the usually longer debug description output.

# In action

Let’s rewrite the example from the beginning of this article with the `???` operator:

```
var someValue: Int? = 5
print("The value is \(someValue ??? "unknown")")
// → "The value is 5"
someValue = nil
print("The value is \(someValue ??? "unknown")")
// → "The value is unknown"
```

It’s a small thing, but I really like this.

1. I initially thought it a good idea to overload the nil-coalescing operator, i.e. define a version of `??` that has the type `(T?, String) -> String`. I liked this because I think my implementation captures the meaning of the nil-coalescing operator very well, but it would have meant giving up some type safety in other contexts, since an expression like `someOptional ?? "someString"` would now always compile. [↩︎](#fnref:1)
