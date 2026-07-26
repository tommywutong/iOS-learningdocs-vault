---
title: 'caseInsensitiveCompare(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/caseinsensitivecompare(_:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/caseinsensitivecompare(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/caseinsensitivecompare%28_%3A%29.json'
content_hash: 'sha256:ef66635cefe6f092'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# caseInsensitiveCompare(_:)

<sub>Instance Method</sub>

Returns the result of invoking `compare:options:` with `NSCaseInsensitiveSearch` as the only option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func caseInsensitiveCompare<T>(_ aString: T) -> ComparisonResult where T : StringProtocol
```
