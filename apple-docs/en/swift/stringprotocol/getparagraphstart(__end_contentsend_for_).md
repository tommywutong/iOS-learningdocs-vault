---
title: 'getParagraphStart(_:end:contentsEnd:for:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/getparagraphstart(_:end:contentsend:for:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/getparagraphstart(_:end:contentsend:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/getparagraphstart%28_%3Aend%3Acontentsend%3Afor%3A%29.json'
content_hash: 'sha256:13564bd5252f1723'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# getParagraphStart(_:end:contentsEnd:for:)

<sub>Instance Method</sub>

Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getParagraphStart(_ start: UnsafeMutablePointer<Self.Index>, end: UnsafeMutablePointer<Self.Index>, contentsEnd: UnsafeMutablePointer<Self.Index>, for range: some RangeExpression<String.Index>)
```
