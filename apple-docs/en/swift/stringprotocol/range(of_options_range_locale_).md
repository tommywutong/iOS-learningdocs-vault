---
title: 'range(of:options:range:locale:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/range(of:options:range:locale:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/range(of:options:range:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/range%28of%3Aoptions%3Arange%3Alocale%3A%29.json'
content_hash: 'sha256:ad4f71e7f05e01e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# range(of:options:range:locale:)

<sub>Instance Method</sub>

Finds and returns the range of the first occurrence of a given string within a given range of the `String`, subject to given options, using the specified locale, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range<T>(of aString: T, options mask: String.CompareOptions = [], range searchRange: Range<Self.Index>? = nil, locale: Locale? = nil) -> Range<Self.Index>? where T : StringProtocol
```
