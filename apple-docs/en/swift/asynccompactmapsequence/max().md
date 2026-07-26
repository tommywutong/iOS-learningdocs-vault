---
title: max()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asynccompactmapsequence/max()
source_url: 'https://developer.apple.com/documentation/swift/asynccompactmapsequence/max()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asynccompactmapsequence/max%28%29.json'
content_hash: 'sha256:e503487891d23d54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncCompactMapSequence](../asynccompactmapsequence.md)

# max()

<sub>Instance Method</sub>

Returns the maximum element in an asynchronous sequence of comparable elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@warn_unqualified_access func max() async rethrows -> Self.Element?
```

## Return Value

The sequence’s maximum element. If the sequence has no elements, returns `nil`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `max()` method returns the max value of the sequence.

```swift
let max = await Counter(howHigh: 10)
    .max()
print(max ?? "none")
// Prints "10"
```
