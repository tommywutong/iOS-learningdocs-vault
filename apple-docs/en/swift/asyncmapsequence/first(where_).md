---
title: 'first(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncmapsequence/first(where:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncmapsequence/first(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncmapsequence/first%28where%3A%29.json'
content_hash: 'sha256:f9aee218f3e8150a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncMapSequence](../asyncmapsequence.md)

# first(where:)

<sub>Instance Method</sub>

Returns the first element of the sequence that satisfies the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func first(where predicate: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?
```

## Parameters

- `predicate` — A closure that takes an element of the asynchronous sequence as its argument and returns a Boolean value that indicates whether the element is a match.

## Return Value

The first element of the sequence that satisfies `predicate`, or `nil` if there is no element that satisfies `predicate`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `first(where:)` method returns the first member of the sequence that’s evenly divisible by both `2` and `3`.

```swift
let divisibleBy2And3 = await Counter(howHigh: 10)
    .first { $0 % 2 == 0 && $0 % 3 == 0 }
print(divisibleBy2And3 ?? "none")
// Prints "6"
```

The predicate executes each time the asynchronous sequence produces an element, until either the predicate finds a match or the sequence ends.
