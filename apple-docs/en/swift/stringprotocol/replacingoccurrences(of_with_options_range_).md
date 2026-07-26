---
title: 'replacingOccurrences(of:with:options:range:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/replacingoccurrences(of:with:options:range:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/replacingoccurrences(of:with:options:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/replacingoccurrences%28of%3Awith%3Aoptions%3Arange%3A%29.json'
content_hash: 'sha256:6ffe8302ad29eeac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# replacingOccurrences(of:with:options:range:)

<sub>Instance Method</sub>

Returns a new string in which all occurrences of a target string in a specified range of the string are replaced by another given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacingOccurrences<Target, Replacement>(of target: Target, with replacement: Replacement, options: String.CompareOptions = [], range searchRange: Range<Self.Index>? = nil) -> String where Target : StringProtocol, Replacement : StringProtocol
```
