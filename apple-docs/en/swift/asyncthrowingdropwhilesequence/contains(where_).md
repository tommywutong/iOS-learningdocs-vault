---
title: 'contains(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingdropwhilesequence/contains(where:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingdropwhilesequence/contains(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingdropwhilesequence/contains%28where%3A%29.json'
content_hash: 'sha256:82c6eb60a1683373'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingDropWhileSequence](../asyncthrowingdropwhilesequence.md)

# contains(where:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(where predicate: (Self.Element) async throws -> Bool) async rethrows -> Bool
```

## Parameters

- `predicate` — A closure that takes an element of the asynchronous sequence as its argument and returns a Boolean value that indicates whether the passed element represents a match.

## Return Value

`true` if the sequence contains an element that satisfies predicate; otherwise, `false`.

## Discussion

You can use the predicate to check for an element of a type that doesn’t conform to the `Equatable` protocol, or to find an element that satisfies a general condition.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `contains(where:)` method checks to see whether the sequence produces a value divisible by `3`:

```swift
let containsDivisibleByThree = await Counter(howHigh: 10)
    .contains { $0 % 3 == 0 }
print(containsDivisibleByThree)
// Prints "true"
```

The predicate executes each time the asynchronous sequence produces an element, until either the predicate finds a match or the sequence ends.
