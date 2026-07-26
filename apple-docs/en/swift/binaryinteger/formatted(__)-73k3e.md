---
title: 'formatted(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryinteger/formatted(_:)-73k3e'
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/formatted(_:)-73k3e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/formatted%28_%3A%29-73k3e.json'
content_hash: 'sha256:6792592cf2f88c4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

# formatted(_:)

<sub>Instance Method</sub>

Format `self` with the given format. `self` is first converted to `S.FormatInput` type, then format with the given format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ format: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput : BinaryInteger
```
