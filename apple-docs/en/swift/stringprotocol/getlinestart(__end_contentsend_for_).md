---
title: 'getLineStart(_:end:contentsEnd:for:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/getlinestart(_:end:contentsend:for:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/getlinestart(_:end:contentsend:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/getlinestart%28_%3Aend%3Acontentsend%3Afor%3A%29.json'
content_hash: 'sha256:414f3a62ed21dfc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# getLineStart(_:end:contentsEnd:for:)

<sub>Instance Method</sub>

Returns by reference the beginning of the first line and the end of the last line touched by the given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getLineStart(_ start: UnsafeMutablePointer<Self.Index>, end: UnsafeMutablePointer<Self.Index>, contentsEnd: UnsafeMutablePointer<Self.Index>, for range: some RangeExpression<String.Index>)
```
