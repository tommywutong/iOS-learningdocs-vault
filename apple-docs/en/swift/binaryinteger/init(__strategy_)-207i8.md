---
title: 'init(_:strategy:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryinteger/init(_:strategy:)-207i8'
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/init(_:strategy:)-207i8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/init%28_%3Astrategy%3A%29-207i8.json'
content_hash: 'sha256:6f9a7736d186f385'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

# init(_:strategy:)

<sub>Initializer</sub>

Initialize an instance by parsing `value` with the given `strategy`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ value: S.ParseInput, strategy: S) throws where S : ParseStrategy, S.ParseOutput : BinaryInteger
```
