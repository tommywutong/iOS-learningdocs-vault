---
title: 'index(after:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/ranges-swift.struct/index(after:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/ranges-swift.struct/index(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/ranges-swift.struct/index%28after%3A%29.json'
content_hash: 'sha256:ae6975cfe87660f9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [RangeSet](../../rangeset.md) · [Ranges](../ranges-swift.struct.md)

# index(after:)

<sub>Instance Method</sub>

Returns the position immediately after the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(after i: Self.Index) -> Self.Index
```

## Parameters

- `i` — A valid index of the collection. `i` must be less than `endIndex`.

## Return Value

The index value immediately after `i`.
