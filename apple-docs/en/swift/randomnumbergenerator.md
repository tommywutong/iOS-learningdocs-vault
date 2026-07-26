---
title: RandomNumberGenerator
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/randomnumbergenerator
source_url: 'https://developer.apple.com/documentation/swift/randomnumbergenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/randomnumbergenerator.json'
content_hash: 'sha256:0ae46b1b11f28fc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# RandomNumberGenerator

<sub>Protocol</sub>

A type that provides uniformly distributed random data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol RandomNumberGenerator
```

## Overview

When you call methods that use random data, such as creating new random values or shuffling a collection, you can pass a `RandomNumberGenerator` type to be used as the source for randomness. When you don’t pass a generator, the default `SystemRandomNumberGenerator` type is used.

When providing new APIs that use randomness, provide a version that accepts a generator conforming to the `RandomNumberGenerator` protocol as well as a version that uses the default system generator. For example, this `Weekday` enumeration provides static methods that return a random day of the week:

```swift
enum Weekday: CaseIterable {
    case sunday, monday, tuesday, wednesday, thursday, friday, saturday

    static func random<G: RandomNumberGenerator>(using generator: inout G) -> Weekday {
        return Weekday.allCases.randomElement(using: &generator)!
    }

    static func random() -> Weekday {
        var g = SystemRandomNumberGenerator()
        return Weekday.random(using: &g)
    }
}
```

## Conforming to the RandomNumberGenerator Protocol

A custom `RandomNumberGenerator` type can have different characteristics than the default `SystemRandomNumberGenerator` type. For example, a seedable generator can be used to generate a repeatable sequence of random values for testing purposes.

To make a custom type conform to the `RandomNumberGenerator` protocol, implement the required `next()` method. Each call to `next()` must produce a uniform and independent random value.

Types that conform to `RandomNumberGenerator` should specifically document the thread safety and quality of the generator.

## Relationships

- **Conforming Types**: [SystemRandomNumberGenerator](systemrandomnumbergenerator.md)

## Topics

### Generating Random Binary Data

- [next()](<randomnumbergenerator/next().md>) — Returns a value from a uniform, independent distribution of binary data.
- [next(upperBound:)](<randomnumbergenerator/next(upperbound_).md>) — Returns a random value that is less than the given upper bound.

## See Also

### Random Number Generators

- [SystemRandomNumberGenerator](systemrandomnumbergenerator.md) — The system’s default source of random data.
