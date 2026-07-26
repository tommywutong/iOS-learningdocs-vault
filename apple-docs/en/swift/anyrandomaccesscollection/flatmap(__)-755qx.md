---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.1 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/anyrandomaccesscollection/flatmap(_:)-755qx'
source_url: 'https://developer.apple.com/documentation/swift/anyrandomaccesscollection/flatmap(_:)-755qx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyrandomaccesscollection/flatmap%28_%3A%29-755qx.json'
content_hash: 'sha256:c4434d7a53df9361'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRandomAccessCollection](../anyrandomaccesscollection.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```
