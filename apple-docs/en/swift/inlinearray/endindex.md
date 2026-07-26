---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/inlinearray/endindex
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/endindex.json'
content_hash: 'sha256:dae504e0e0ee9479'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# endIndex

<sub>Instance Property</sub>

The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: InlineArray<count, Element>.Index { get }
```

## Discussion

If the array is empty, `endIndex` is equal to `startIndex`.

> [!abstract] Complexity
> O(1)
