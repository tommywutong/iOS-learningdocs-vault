---
title: 'init(_:format:lenient:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryfloatingpoint/init(_:format:lenient:)-2p118'
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(_:format:lenient:)-2p118'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/init%28_%3Aformat%3Alenient%3A%29-2p118.json'
content_hash: 'sha256:b6d15dff68dc941c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# init(_:format:lenient:)

<sub>Initializer</sub>

Initialize an instance by parsing `value` with a `ParseStrategy` created with the given `format` and the `lenient` argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: String, format: FloatingPointFormatStyle<Self>, lenient: Bool = true) throws
```
