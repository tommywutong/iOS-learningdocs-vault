---
title: 'replacingCharacters(in:with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/replacingcharacters(in:with:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/replacingcharacters(in:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/replacingcharacters%28in%3Awith%3A%29.json'
content_hash: 'sha256:9c39a5863b15e6f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# replacingCharacters(in:with:)

<sub>Instance Method</sub>

Returns a new string in which the characters in a specified range of the `String` are replaced by a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacingCharacters<T, R>(in range: R, with replacement: T) -> String where T : StringProtocol, R : RangeExpression, R.Bound == String.Index
```
