---
title: Enumerating enum cases in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/06/enumerating-enum-cases/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5f4bbadff7f388a6'
translated: false
---

> 原文：[Enumerating enum cases in Swift](https://oleb.net/blog/2018/06/enumerating-enum-cases/)　·　Ole Begemann

# Enumerating enum cases in Swift

New in Swift 4.2, the compiler can generate a collection of an enum’s cases, relieving you from the error-prone task of maintaining such a list yourself. The Swift Evolution proposal that introduced this feature is [SE-0194](https://github.com/apple/swift-evolution/blob/master/proposals/0194-derived-collection-of-enum-cases.md).

# The `CaseIterable` protocol

For plain enums without associated values, all you have to do is conform your enum to the new [`CaseIterable`](https://developer.apple.com/documentation/swift/caseiterable) protocol. The compiler will then generate a static [`allCases`](https://developer.apple.com/documentation/swift/caseiterable/2994869-allcases) property for you. This is the example from the standard library documentation:

```
enum CompassDirection: CaseIterable {
    case north
    case south
    case east
    case west
}

CompassDirection.allCases // → [north, south, east, west]
CompassDirection.allCases.count // → 4
```

`allCases` is a [collection](https://developer.apple.com/documentation/swift/collection), so it has all the usual properties and capabilities, like `count`, `map`, and so on:

```
let caseList = CompassDirection.allCases
    .map { "\($0)" }
    .joined(separator: ", ")
// → "north, south, east, west"
```

# Example: Table view sections

Let’s look at another example. When working with [iOS table views](https://developer.apple.com/documentation/uikit/uitableview) that have multiple sections, it’s a common pattern to introduce an enum to represent the sections:

```
enum TableSection: Int {
    /// The section for the search field
    case search = 0
    /// Featured content
    case featured = 1
    /// Regular content cells
    case standard = 2
}
```

Then, in the table view [data source](https://developer.apple.com/documentation/uikit/uitableviewdatasource) and [delegate](https://developer.apple.com/documentation/uikit/uitableviewdelegate) methods, we can switch over the `section` parameter and perform the appropriate action for the section in question.

_(Side note: I don’t want to turn this article into a debate about the pros and cons of this approach. It definitely has its limits as the table becomes more complex and your `switch` statements grow, but it works well enough for a small example. So let’s run with it.)_

Now, you’ll find that we need to return the number of cases in your enum as the number of sections in the table view:

```
func numberOfSections(in tableView: UITableView) -> Int {
    return ... // number of cases. How?
}
```

The traditional solution was to either hardcode the count or to add another case named `sectionCount` (or similar) to the end of the enum. This final case’s raw value would then be magically equal to the number of “real” cases. Neither approach is satisfactory.

`CaseIterable` makes this much cleaner. Just adopt the protocol, no implementation needed:

```
extension TableSection: CaseIterable {}
```

Now we can `return TableSection.allCases.count` in the data source method.

## Cases appear in declaration order

SE-0194 does not prescribe a specific order of the values in the `allCases` collection, but the [documentation for `CaseIterable` guarantees it](https://developer.apple.com/documentation/swift/caseiterable):

> The synthesized `allCases` collection provides the cases in order of their declaration.

This means we can safely remove the raw-value integer backing from the `TableSection` enum and use a case’s position in the `allCases` collection for mapping between section indices and enum cases:

```
override func tableView(_ tableView: UITableView,
    cellForRowAt indexPath: IndexPath) -> UITableViewCell
{
    let section = TableSection.allCases[indexPath.section]
    switch section {
    case .search: ...
    case .featured: ...
    case .standard: ...
    }
}
```

# Synthesis only works in the same file

Like other compiler-synthesized conformances ([`Equatable`, `Hashable`](https://github.com/apple/swift-evolution/blob/master/proposals/0185-synthesize-equatable-hashable.md), [`Encodable`, `Decodable`](https://github.com/apple/swift-evolution/blob/master/proposals/0166-swift-archival-serialization.md) — the list keeps growing)[1](#fn:1), the automatic code generation only works when you declare the conformance in the same file where the type is defined (either on the type definition itself or, new in Swift 4.2, in a same-file extension).

The automatic code synthesis is really a feature for _owners_ of a type, not to make retroactive conformances easier.

# Retroactive conformance

Of course, you can always declare the conformance retroactively and provide a manual implementation, but that also means you’re responsible for maintaining it if new cases get added.

As a rule of thumb, think twice before adopting `CaseIterable` (and other system protocols) for types you don’t own, especially when it comes to types from Apple frameworks. Your code may break in one of two ways in the future:

- when the original owner of the type adds the conformance themselves in a future release,
- or when the original type changes in a way that breaks your conformance, e.g. when a new case gets added to the type. If you’re lucky, the breakage will manifest in a compile-time error on your side, but it’s entirely possible that it will break silently and you’ll have a hard time finding the bug.

# Manual conformance

We’ve seen that the automatic synthesis only works for enums without associated values. This makes sense because adding associated values to an enum makes the number of possible values the enum can have potentially infinite.

Ignoring the utility of having access to an infinite sequence of a type’s possible values for a moment, an infinite list is not representable in the confines of `CaseIterable` anyway: the protocol requires `allCases` to return a [`Collection`](https://developer.apple.com/documentation/swift/collection), and collections must be finite (although this could change in the future[2](#fn:2)).

But as long as the list of all possible values is finite, we can always implement the protocol manually for enums with associated values.

## Example

Here’s an example with two enums, where one plain enum is used in the associated values of another:

```
enum Intensity: CaseIterable {
    case light
    case medium
    case hard
}

enum Workout {
    case resting
    case running(Intensity)
    case cycling(Intensity)
}
```

(I know “resting” isn’t a real workout type, but bear with me. I wanted an example where not all cases have the same associated value.)

The compiler can synthesize a `CaseIterable` conformance for `Intensity` but not for `Workout`. Let’s write one. We build an array of all possible `Workout` values by starting with `.resting` and applying each possible associated value to the other two cases:

```
extension Workout: CaseIterable {
    static var allCases: [Workout] {
        return [.resting]
            + Intensity.allCases.map(Workout.running)
            + Intensity.allCases.map(Workout.cycling)
    }
}
```

If you find the [`map`](https://developer.apple.com/documentation/swift/sequence/2965520-map) invocations hard to parse, observe that a “naked” enum case without its associated values is equivalent to a constructor function for that particular case. In other words, the type of `Workout.running` is `(Intensity) -> Workout`, i.e. a function that produces a `Workout` value if you give it the desired `Intensity`. We pass these constructor functions to `map` and get arrays of `Workout` back.

This is the result:

```
Workout.allCases.count // → 7
Workout.allCases
// → [resting, running(light), running(medium), running(hard),
//    cycling(light), cycling (medium), cycling(hard)]
```

## Manual maintenance required

The manual implementation is easy enough to write, but it has a major downside compared to compiler-generated code: we now have to remember to keep it up to date. If we later add another workout type to our enum, the compiler won’t alert us that our `allCases` implementation is no longer correct. It will just silently return the wrong result.

The only workaround I can think of is a little ugly, but it solves this problem in a really interesting way. Let’s add a local dummy function inside the `allCases` body. This function’s only purpose is to switch exhaustively over our enum so that the compiler will complain at this source location when we later add another workout type. We can mark the function [as unavailable](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html#ID348) and give it a parameter of type [`Never`](https://developer.apple.com/documentation/swift/never) to document we never intend to call it (since you can’t create a value of type `Never`, a function that takes a `Never` cannot be called).

```
extension Workout: CaseIterable {
    static var allCases: [Workout] {
        /// Dummy function whose only purpose is to produce
        /// an error when a new case is added to Workout. Never call!
        @available(*, unavailable, message: "Only for exhaustiveness checking, don't call")
        func _assertExhaustiveness(of workout: Workout, never: Never) {
            switch workout {
            case .resting,
                 .running(.light), .running(.medium), .running(.hard),
                 .cycling(.light), .cycling(.medium), .cycling(.hard):
                break
            }
        }

        return [.resting]
            + Intensity.allCases.map(Workout.running)
            + Intensity.allCases.map(Workout.cycling)
    }
}
```

Observe what happens now when we add another case to the `Workout` enum:

![Compile-time error at almost the desired source location after adding a new enum case](https://oleb.net/media/swift-caseiterable-assertexhaustiveness-error-v2-1712px.png)

<sub>Swift showing a compile-time error at almost the desired source location after adding a new enum case.</sub>

It’s like an inline unit test that runs at compile-time! You still have to remember to fix the actual `allCases` implementation though, not just the dummy `switch` statement.

# Beyond enums

The names `CaseIterable` and `allCases` imply that this feature is specifically intended for enums. However, that doesn’t mean other types can’t adopt the protocol. In fact, this is how [the documentation describes `CaseIterable`](https://developer.apple.com/documentation/swift/caseiterable):

> A type that provides a collection of all of its values.

This clearly states that any type that has a finite number of values can conform. During the [discussion of SE-0194 on Swift Evolution](https://forums.swift.org/t/se-0194-derived-collection-of-enum-cases/7377), many people favored names like `ValueEnumerable` and `allValues` to reflect this broader scope in the name. In the end, the [decision was made](https://forums.swift.org/t/accepted-se-0194-derived-collection-of-enum-cases/10723) to derive the name from the primary use case:

> The core team felt that these names reflect the primary use case of this protocol, promoting better clarity for most code that iterates over all of the cases.

## Making other types `CaseIterable`

Regardless, let’s conform some non-enum types to `CaseIterable`. The simplest example is [`Bool`](https://developer.apple.com/documentation/swift/bool)[3](#fn:3):

```
extension Bool: CaseIterable {
    public static var allCases: [Bool] {
        return [false, true]
    }
}

Bool.allCases // → [false, true]
```

Some integer types are also a good match. Note that the return type of `allCases` doesn’t have to be an array — it can be any `Collection`. It’d be quite wasteful to generate an array of every possible integer when a range is enough:

```
extension UInt8: CaseIterable {
    public static var allCases: ClosedRange<UInt8> {
        return .min ... .max
    }
}

UInt8.allCases.count // → 256
```

If your custom type has a finite number of values but the values are expensive to generate, consider returning a [lazy collection](https://developer.apple.com/documentation/swift/lazycollectionprotocol) so as not to perform unnecessary work upfront.

## Potential `Collection.count` overflow

If we continue to conform the integer types to `CaseIterable`, we’ll eventually reach the limits of Swift’s `Collection` protocol. The [`count`](https://developer.apple.com/documentation/swift/collection/2950091-count) of a `Collection` is defined to be an [`Int`](https://developer.apple.com/documentation/swift/int), which will overflow as we reach types with more than `Int.max` inhabitants (i.e. `Int`/`UInt` and larger).

You can still create collections that nominally have more elements, so this is fine:

```
let hugeRange = UInt64.min ... .max
// → ClosedRange<UInt64>
//   {lowerBound 0, upperBound 9223372036854775807}
```

But as soon as you ask this collection for its `count` (or more generally, as you compute a distance between two indices that overflows `Int.max`), things will not end well.[4](#fn:4)

## Applications

You might ask, when is it useful to have a collection of a type’s inhabitants? We’ve seen a classic use case above in the table view example: the type represents a finite list of options and we want to represent these options in another domain, e.g. as buttons in the UI.

Another application is the need to generate arbitrary values of a certain type. [Property-based testing](http://blog.jessitron.com/2013/04/property-based-testing-what-is-it.html) frameworks generate test cases by feeding “random” data into your code and asserting that certain conditions hold. (Often the data isn’t really random but machine-generated following specific rules.)

The [SwiftCheck](https://github.com/typelift/SwiftCheck) testing framework is based on a [protocol named `Arbitrary`](https://github.com/typelift/SwiftCheck#custom-types), which defines an API for types to generate random data. In principle, this is very similar to `CaseIterable`, although `Arbitrary` has different requirements: it also works for infinitely big types such as strings, and it defines how a value can be _shrunk_. Once SwiftCheck has found a failing test case, it tries to reduce the value to the simplest form that still fails the test by shrinking it repeatedly.

# `CaseIterable` and conditional conformance

Many generic types can adopt `CaseIterable` by taking advantage of [conditional conformance](https://swift.org/blog/conditional-conformance/), i.e. the ability to conform a type to a protocol when its generic parameters satify certain requirements (introduced in Swift 4.1).

For example, any [`Optional`](https://developer.apple.com/documentation/swift/optional) can be `CaseIterable` as long as the optional’s generic type is itself `CaseIterable`. In code this looks like this (the explicit typealias shouldn’t be necessary, but without it this doesn’t compile in the current Swift 4.2 beta):

```
extension Optional: CaseIterable where Wrapped: CaseIterable {
    public typealias AllCases = [Wrapped?]
    public static var allCases: AllCases {
        return [nil] + Wrapped.allCases.map { $0 }
    }
}
```

The implementation of `allCases` starts with `nil` and appends the `Wrapped.allCases` collection to it (the mapping step is necessary to convert the elements from `Wrapped` to `Wrapped?`). I decided to put `nil` at the front to follow the `CaseIterable` convention of listing values in declaration order — [`.none` comes before `.some`](https://github.com/apple/swift/blob/7f158a5c3c2b7cfd8293e0296fd3fa257b760dca/stdlib/public/core/Optional.swift#L122-L133) in the standard library source.

`Optional` adds one more possible value (namely, `.none` or `nil`) to the underlying type’s inhabitants. In other words, `Optional<Wrapped>.allCases.count` will always be equal to `Wrapped.allCases.count + 1`:

```
CompassDirection.allCases // → [north, south, east, west]
CompassDirection.allCases.count // → 4
CompassDirection?.allCases // → [nil, north, south, east, west]
CompassDirection?.allCases.count // → 5
```

Notice that although `CompassDirection?.allCases` looks like [optional chaining syntax](https://docs.swift.org/swift-book/LanguageGuide/OptionalChaining.html), it isn’t! We’re accessing a static member on the type named `CompassDirection?`. Alternatively, we could’ve written `Optional<CompassDirection>.allCases`.

How useful is it to extend `Optional` like this? I’m not sure. It probably doesn’t hurt, but I can’t think of any situation where I’d need this. The Swift core team [seems to agree](https://twitter.com/dgregor79/status/1004027177283620864):

> The core team discussed this when `CaseIterable` was introduced, and concluded that it wasn’t clearly useful.

1. The compiler also synthesizes [`RawRepresentable`](https://developer.apple.com/documentation/swift/rawrepresentable) conformance in some cases, but that has slightly different semantics (you don’t have to explicitly conform to the protocol). [↩︎](#fnref:1)
2. Dave Abrahams [argues for a remake](https://forums.swift.org/t/pitch-make-collection-super-convenient-and-retire-sequence/12103) of the [`Sequence`](https://developer.apple.com/documentation/swift/sequence)/[`Collection`](https://developer.apple.com/documentation/swift/collection) hierarchy in the standard library. Among many other things, he proposes to lift the current restriction for collections to be finite.

  [Xiaodi Wu points out](https://forums.swift.org/t/se-0194-derived-collection-of-enum-cases/7377/12) that if [`CaseIterable.AllValues`](https://developer.apple.com/documentation/swift/caseiterable/2994868-allcases) were constrained to `Sequence`,

  > then even types that have an infinite number of possible values could conform to [`CaseIterable`]. Here’s the rub: the definition of a type, or at least one of them, _is_ precisely the set of all possible values of a variable. If unconstrained by finiteness, then _all types_ would meet the semantic requirements of [`CaseIterable`].

  [↩︎](#fnref:2)
3. I guess technically, [`Never`](https://developer.apple.com/documentation/swift/never) would be [an even simpler example](https://twitter.com/olebegemann/status/1005492033484713984). [`Void`](https://developer.apple.com/documentation/swift/void) too, but `Void` is just a typealias for the empty tuple, and tuples can’t be conformed to protocols. [↩︎](#fnref:3)
4. In Swift 4.1.2 and the current beta of Swift 4.2, `(UInt64.min ... .max).count` actually returns `0`, i.e. a wrong result. It really should be a fatal error. [I filed a bug, SR-7984](https://bugs.swift.org/browse/SR-7948). [↩︎](#fnref:4)
