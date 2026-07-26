---
title: 'commonPrefix(with:options:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/commonprefix(with:options:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/commonprefix(with:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/commonprefix%28with%3Aoptions%3A%29.json'
content_hash: 'sha256:ff66f3cbda0e951b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# commonPrefix(with:options:)

<sub>Instance Method</sub>

Returns a string containing characters this string and the given string have in common, starting from the beginning of each up to the first characters that aren’t equivalent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func commonPrefix<T>(with aString: T, options: String.CompareOptions = []) -> String where T : StringProtocol
```
