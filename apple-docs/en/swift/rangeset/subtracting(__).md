---
title: 'subtracting(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/subtracting(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/subtracting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/subtracting%28_%3A%29.json'
content_hash: 'sha256:f21a237d71710c63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# subtracting(_:)

<sub>Instance Method</sub>

Returns a new set containing the contents of this range set that are not also in the given range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subtracting(_ other: RangeSet<Bound>) -> RangeSet<Bound>
```

## Parameters

- `other` — The range set to subtract.

## Return Value

A new range set.
