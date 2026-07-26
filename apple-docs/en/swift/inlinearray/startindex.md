---
title: startIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/inlinearray/startindex
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/startindex.json'
content_hash: 'sha256:772b9b56ecf9e207'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a nonempty array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: InlineArray<count, Element>.Index { get }
```

## Discussion

If the array is empty, `startIndex` is equal to `endIndex`.

> [!abstract] Complexity
> O(1)
