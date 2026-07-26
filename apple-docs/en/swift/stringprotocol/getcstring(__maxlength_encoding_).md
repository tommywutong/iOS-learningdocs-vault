---
title: 'getCString(_:maxLength:encoding:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/getcstring(_:maxlength:encoding:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/getcstring(_:maxlength:encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/getcstring%28_%3Amaxlength%3Aencoding%3A%29.json'
content_hash: 'sha256:d67c1d34701a52c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# getCString(_:maxLength:encoding:)

<sub>Instance Method</sub>

Converts the `String`’s content to a given encoding and stores them in a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getCString(_ buffer: inout [CChar], maxLength: Int, encoding: String.Encoding) -> Bool
```

## Discussion

> [!note] Note
> Will store a maximum of `min(buffer.count, maxLength)` bytes.
