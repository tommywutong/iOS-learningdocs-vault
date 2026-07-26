---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/subscript(_:)-358vm'
source_url: 'https://developer.apple.com/documentation/swift/range/subscript(_:)-358vm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/subscript%28_%3A%29-358vm.json'
content_hash: 'sha256:13989293395e1fa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the subsequence bounded by the given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(bounds: Range<Range<Bound>.Index>) -> Range<Bound> { get }
```

## Parameters

- `bounds` — A range of the range’s indices. The upper and lower bounds of the `bounds` range must be valid indices of the collection.
