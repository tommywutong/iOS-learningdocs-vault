---
title: 'isDisjoint(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/isdisjoint(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/isdisjoint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/isdisjoint%28_%3A%29.json'
content_hash: 'sha256:0d58f4f0066762c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# isDisjoint(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether this range set set has no members in common with the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDisjoint(_ other: RangeSet<Bound>) -> Bool
```

## Parameters

- `other` — A range set to compare against.

## Return Value

`true` if this range set has no elements in common with `other`; otherwise, `false`.
