---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/utf8view/endindex
source_url: 'https://developer.apple.com/documentation/swift/string/utf8view/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/utf8view/endindex.json'
content_hash: 'sha256:1d78c21db72eb616'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UTF8View](../utf8view.md)

# endIndex

<sub>Instance Property</sub>

The “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: String.UTF8View.Index { get }
```

## Discussion

In an empty UTF-8 view, `endIndex` is equal to `startIndex`.
