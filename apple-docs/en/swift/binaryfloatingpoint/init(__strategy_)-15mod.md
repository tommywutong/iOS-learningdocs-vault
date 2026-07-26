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
doc_path: '/documentation/swift/binaryfloatingpoint/init(_:strategy:)-15mod'
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(_:strategy:)-15mod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/init%28_%3Astrategy%3A%29-15mod.json'
content_hash: 'sha256:4bb8991480a167ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# init(_:strategy:)

<sub>Initializer</sub>

Initialize an instance by parsing `value` with the given `strategy`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ value: S.ParseInput, strategy: S) throws where Self == S.ParseOutput, S : ParseStrategy
```
