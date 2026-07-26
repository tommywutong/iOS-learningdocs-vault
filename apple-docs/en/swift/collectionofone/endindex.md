---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collectionofone/endindex
source_url: 'https://developer.apple.com/documentation/swift/collectionofone/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone/endindex.json'
content_hash: 'sha256:a0a6aae9c11fdf3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionOfOne](../collectionofone.md)

# endIndex

<sub>Instance Property</sub>

The “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: CollectionOfOne<Element>.Index { get }
```

## Discussion

In a `CollectionOfOne` instance, `endIndex` is always `1`.
