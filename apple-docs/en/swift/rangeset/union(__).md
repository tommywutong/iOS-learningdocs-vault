---
title: 'union(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/union(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/union(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/union%28_%3A%29.json'
content_hash: 'sha256:d2da7b52b7cd262d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# union(_:)

<sub>Instance Method</sub>

Returns a new range set containing the contents of both this set and the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func union(_ other: RangeSet<Bound>) -> RangeSet<Bound>
```

## Parameters

- `other` — The range set to merge with this one.

## Return Value

A new range set.
