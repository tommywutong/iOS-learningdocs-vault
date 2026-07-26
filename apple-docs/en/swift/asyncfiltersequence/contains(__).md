---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncfiltersequence/contains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncfiltersequence/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncfiltersequence/contains%28_%3A%29.json'
content_hash: 'sha256:d92ec541b27152f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncFilterSequence](../asyncfiltersequence.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ search: Self.Element) async rethrows -> Bool
```

## Parameters

- `search` — The element to find in the asynchronous sequence.

## Return Value

`true` if the method found the element in the asynchronous sequence; otherwise, `false`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `contains(_:)` method checks to see whether the sequence produces the value `5`:

```swift
let containsFive = await Counter(howHigh: 10)
    .contains(5)
print(containsFive)
// Prints "true"
```
