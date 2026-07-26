---
title: startIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/unicodescalarview/startindex
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/startindex.json'
content_hash: 'sha256:b2af9b075d9be3c5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# startIndex

<sub>Instance Property</sub>

The position of the first Unicode scalar value if the string is nonempty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: String.UnicodeScalarView.Index { get }
```

## Discussion

If the string is empty, `startIndex` is equal to `endIndex`.
