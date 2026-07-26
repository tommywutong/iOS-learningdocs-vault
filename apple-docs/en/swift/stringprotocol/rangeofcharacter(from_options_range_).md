---
title: 'rangeOfCharacter(from:options:range:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/rangeofcharacter(from:options:range:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/rangeofcharacter(from:options:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/rangeofcharacter%28from%3Aoptions%3Arange%3A%29.json'
content_hash: 'sha256:c8785d257a56c8f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# rangeOfCharacter(from:options:range:)

<sub>Instance Method</sub>

Finds and returns the range in the `String` of the first character from a given character set found in a given range with given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rangeOfCharacter(from aSet: CharacterSet, options mask: String.CompareOptions = [], range aRange: Range<Self.Index>? = nil) -> Range<Self.Index>?
```
