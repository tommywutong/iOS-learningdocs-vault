---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/contains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/contains%28_%3A%29.json'
content_hash: 'sha256:e4ad12118ac36331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the given value is contained by the ranges in the range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ value: Bound) -> Bool
```

## Parameters

- `value` — The value to look for in the range set.

## Return Value

`true` if `value` is contained by a range in the range set; otherwise, `false`.

## Discussion

> [!abstract] Complexity
> O(log _n_), where _n_ is the number of ranges in the range set.
