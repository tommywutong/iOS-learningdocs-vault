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
doc_path: '/documentation/swift/binaryfloatingpoint/formatted(_:)-4ksqj'
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/formatted(_:)-4ksqj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/formatted%28_%3A%29-4ksqj.json'
content_hash: 'sha256:af64111325a54a55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# formatted(_:)

<sub>Instance Method</sub>

Format `self` with the given format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ format: S) -> S.FormatOutput where Self == S.FormatInput, S : FormatStyle
```
