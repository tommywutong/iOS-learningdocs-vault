---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/contains(_:)-680jp'
source_url: 'https://developer.apple.com/documentation/swift/range/contains(_:)-680jp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/contains%28_%3A%29-680jp.json'
content_hash: 'sha256:64ab7edf1a41cc91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the given closed range is contained within this range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ other: ClosedRange<Bound>) -> Bool
```

## Parameters

- `other` — A closed range to check for containment within this range.

## Return Value

`true` if `other` is wholly contained within this range; otherwise, `false`.

## Discussion

The given closed range is contained within this range if its bounds are contained within this range. If this range is empty, it cannot contain a closed range, since closed ranges by definition contain their boundaries.

```swift
let range = 0..<10
range.contains(2...5)        // true
range.contains(2...10)       // false
range.contains(2...12)       // false

let emptyRange = 3..<3
emptyRange.contains(3...3)   // false
```

> [!abstract] Complexity
> O(1)
