---
title: 'isSubset(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/issubset(of:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/issubset(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/issubset%28of%3A%29.json'
content_hash: 'sha256:b428428c2556c782'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# isSubset(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether this range set is a subset of the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isSubset(of other: RangeSet<Bound>) -> Bool
```

## Parameters

- `other` — A range set to compare against.

## Return Value

`true` if this range set is a subset of `other`; otherwise, `false`.
