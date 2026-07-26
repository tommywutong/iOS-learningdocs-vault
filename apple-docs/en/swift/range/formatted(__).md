---
title: 'formatted(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/swift/range/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/formatted%28_%3A%29.json'
content_hash: 'sha256:d741d496f0cf64b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# formatted(_:)

<sub>Instance Method</sub>

Formats the date range using the specified style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ style: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Range<Date>
```
