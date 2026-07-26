---
title: API Pollution in Swift Modules
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/swift-api-pollution/'
original_language: en
published: 2019-02-18
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:35133f341949d581'
translated: false
---

> 原文：[API Pollution in Swift Modules](https://nshipster.com/swift-api-pollution/)　·　NSHipster (Mattt)

# [API Pollution in Swift Modules](https://nshipster.com/swift-api-pollution/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  February 18^th, 2019

When you import a module into Swift code, you expect the result to be entirely additive. That is to say: the potential for new functionality comes at no expense (other than, say, a modest increase in the size of your app bundle).

Import the `NaturalLanguage` framework, and _***boom***_ your app can [determine the language of text](https://nshipster.com/nllanguagerecognizer/); import `CoreMotion`, and _***whoosh***_ your app can [respond to changes in device orientation](https://nshipster.com/cmdevicemotion/). But it’d be surprising if, say, the ability to distinguish between French and Japanese interfered with your app’s ability to tell which way was magnetic north.

Although this particular example isn’t real (to the relief of Francophones in Hokkaido), there are situations in which a Swift dependency can change how your app behaves — _even if you don’t use it directly_.

In this week’s article, we’ll look at a few ways that imported modules can silently change the behavior of existing code, and offer suggestions for how to prevent this from happening as an API provider and mitigate the effects of this as an API consumer.

## Module Pollution

It’s a story as old as `<time.h>`: two things are called `Foo`, and the compiler has to decide what to do.

Pretty much every language with a mechanism for code reuse has to deal with naming collisions one way or another. In the case of Swift, you can use fully-qualified names to distinguish between the `Foo` type declared in module `A` (`A.Foo`) from the `Foo` type in module `B` (`B.Foo`). However, Swift has some unique characteristics that cause other ambiguities to go unnoticed by the compiler, which may result in a change to existing behavior when modules are imported.

### Operator Overloading

In Swift, the `+` operator denotes concatenation when its operands are arrays. One array plus another results in an array with the elements of the former array followed by those of the latter.

```
let oneTwoThree: [Int] = [1, 2, 3]
let fourFiveSix: [Int] = [4, 5, 6]
oneTwoThree + fourFiveSix // [1, 2, 3, 4, 5, 6]
```

If we look at the operator’s [declaration in the standard library](https://github.com/apple/swift/blob/master/stdlib/public/core/Array.swift#L1318-L1324), we see that it’s provided in an unqualified extension on `Array`:

```
extension Array {
  @inlinable public static func + (lhs: Array, rhs: Array) -> Array {}
}
```

The Swift compiler is responsible for resolving API calls to their corresponding implementations. If an invocation matches more than one declaration, the compiler selects the most specific one available.

To illustrate this point, consider the following conditional extension on `Array`, which defines the `+` operator to perform member-wise addition for arrays whose elements conform to `Numeric`:

```
extension Array where Element: Numeric {
    public static func + (lhs: Array, rhs: Array) -> Array {
        return Array(zip(lhs, rhs).map {$0 + $1})
    }
}

oneTwoThree + fourFiveSix // [5, 7, 9] 😕
```

Because the requirement of `Element: Numeric` is more specific than the unqualified declaration in the standard library, the Swift compiler resolves `+` to this function instead.

Now, these new semantics may be perfectly acceptable — indeed preferable. But only if you’re aware of them. The problem is that if you so much as _import_ a module containing such a declaration you can change the behavior of your entire app without even knowing it.

This problem isn’t limited to matters of semantics; it can also come about as a result of ergonomic affordances.

### Function Shadowing

In Swift, function declarations can specify default arguments for trailing parameters, making them optional (though not necessarily `Optional`) for callers. For example, the top-level function [`dump(_:name:indent:maxDepth:maxItems:)`](https://developer.apple.com/documentation/swift/1539127-dump) has an intimidating number of parameters:

```
@discardableResult func dump<T>(_ value: T, name: String? = nil, indent: Int = 0, maxDepth: Int = .max, maxItems: Int = .max) -> T
```

But thanks to default arguments, you need only specify the first one to call it:

```
dump("🏭💨") // "🏭💨"
```

Alas, this source of convenience can become a point of confusion when method signatures overlap.

Imagine a hypothetical module that — not being familiar with the built-in `dump` function — defines a `dump(_:)` that prints the UTF-8 code units of a string.

```
public func dump(_ string: String) {
    print(string.utf8.map {$0})
}
```

The `dump` function declared in the Swift standard library takes an unqualified generic `T` argument in its first parameter (which is effectively `Any`). Because `String` is a more specific type, the Swift compiler will choose the imported `dump(_:)` method when it’s available.

```
dump("🏭💨") // [240, 159, 143, 173, 240, 159, 146, 168]
```

Unlike the previous example, it’s not entirely clear that there’s any ambiguity in the competing declarations. After all, what reason would a developer have to think that their `dump(_:)` method could in any way be confused for `dump(_:name:indent:maxDepth:maxItems:)`?

Which leads us to our final example, which is perhaps the most confusing of all…

### String Interpolation Pollution

In Swift, you can combine two strings by interpolation in a string literal as an alternative to concatenation.

```
let name = "Swift"
let greeting = "Hello, \(name)!" // "Hello, Swift!"
```

This has been true from the first release of Swift. However, with the new [`ExpressibleByStringInterpolation`](https://nshipster.com/expressiblebystringinterpolation) protocol in Swift 5, this behavior can no longer be taken for granted.

Consider the following extension on the default interpolation type for `String`:

```
extension DefaultStringInterpolation {
    public mutating func appendInterpolation<T>(_ value: T) where T: StringProtocol {
        self.appendInterpolation(value.uppercased() as TextOutputStreamable)
    }
}
```

`StringProtocol` inherits, [among other things](https://swiftdoc.org/v4.2/protocol/stringprotocol/) the `TextOutputStreamable` and `CustomStringConvertible` protocols, making it more specific than the [`appendInterpolation` method declared by `DefaultStringInterpolation`](https://github.com/apple/swift/blob/master/stdlib/public/core/StringInterpolation.swift#L63) that would otherwise be invoked when interpolating `String` values.

```
public struct DefaultStringInterpolation: StringInterpolationProtocol {
    @inlinable public mutating func appendInterpolation<T>(_ value: T)
        where T: TextOutputStreamable, T: CustomStringConvertible {}
}
```

Once again, the Swift compiler’s notion of specificity causes behavior to go from expected to unexpected.

If the previous declaration is made accessible by any module in your app, it would change the behavior of all interpolated string values.

```
let greeting = "Hello, \(name)!" // "Hello, SWIFT!"
```

---

Given the rapid and upward trajectory of the language, it’s not unreasonable to expect that these problems will be solved at some point in the future.

But what are we to do in the meantime? Here are some suggestions for managing this behavior both as an API consumer and as an API provider.

---

## Strategies for API Consumers

As an API consumer, you are — in many ways — beholden to the constraints imposed by imported dependencies. It really _shouldn’t_ be your problem to solve, but at least there are some remedies available to you.

### Add Hints to the Compiler

Often, the most effective way to get the compiler to do what you want is to explicitly cast an argument down to a type that matches the method you want to call.

Take our example of the `dump(_:)` method from before: by downcasting to `CustomStringConvertible` from `String`, we can get the compiler to resolve the call to use the standard library function instead.

```
dump("🏭💨") // [240, 159, 143, 173, 240, 159, 146, 168]
dump("🏭💨" as CustomStringConvertible) // "🏭💨"
```

### ~~Scoped Import Declarations~~

### Fork Dependencies

If all else fails, you can always solve the problem by taking it into your own hands.

If you don’t like something that a third-party dependency is doing, simply fork the source code, get rid of the stuff you don’t want, and use that instead. (You could even try to get them to upstream the change.)

## Strategies for API Provider

As someone developing an API, it’s ultimately your responsibility to be deliberate and considerate in your design decisions. As you think about the greater consequences of your actions, here are some things to keep in mind:

### Be More Discerning with Generic Constraints

Unqualified `<T>` generic constraints are the same as `Any`. If it makes sense to do so, consider making your constraints more specific to reduce the chance of overlap with unrelated declarations.

### Isolate Core Functionality from Convenience

As a general rule, code should be organized into modules such that module is responsible for a single responsibility.

If it makes sense to do so, consider packaging functionality provided by types and methods in a module that is separate from any extensions you provide to built-in types to improve their usability. Until it’s possible to pick and choose which behavior we want from a module, the best option is to give consumers the choice to opt-in to features if there’s a chance that they might cause problems downstream.

### Avoid Collisions Altogether

Of course, it’d be great if you could knowingly avoid collisions to begin with… but that gets into the whole _[“unknown unknowns”](https://en.wikipedia.org/wiki/There_are_known_knowns)_ thing, and we don’t have time to get into epistemology now.

So for now, let’s just say that if you’re aware of something _maybe_ being a conflict, a good option might be to avoid it altogether.

For example, if you’re worried that someone might get huffy about changing the semantics of fundamental arithmetic operators, you could choose a different one instead, like `.+`:

```
infix operator .+: AdditionPrecedence

extension Array where Element: Numeric {
    static func .+ (lhs: Array, rhs: Array) -> Array {
        return Array(zip(lhs, rhs).map {$0 + $1})
    }
}

oneTwoThree + fourFiveSix // [1, 2, 3, 4, 5, 6]
oneTwoThree .+ fourFiveSix // [5, 7, 9]
```

---

As developers, we’re perhaps less accustomed to considering the wider impact of our decisions. Code is invisible and weightless, so it’s easy to forget that it even exists after we ship it.

But in Swift, our decisions have impacts beyond what’s immediately understood so it’s important to be considerate about how we exercise our responsibilities as stewards of our APIs.
