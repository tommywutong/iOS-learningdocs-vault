---
title: min()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingprefixwhilesequence/min()
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingprefixwhilesequence/min()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingprefixwhilesequence/min%28%29.json'
content_hash: 'sha256:f37f1401bc68a646'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingPrefixWhileSequence](../asyncthrowingprefixwhilesequence.md)

# min()

<sub>Instance Method</sub>

Returns the minimum element in an asynchronous sequence of comparable elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@warn_unqualified_access func min() async rethrows -> Self.Element?
```

## Return Value

The sequence’s minimum element. If the sequence has no elements, returns `nil`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `min()` method returns the minimum value of the sequence.

```swift
let min = await Counter(howHigh: 10)
    .min()
print(min ?? "none")
// Prints "1"
```
