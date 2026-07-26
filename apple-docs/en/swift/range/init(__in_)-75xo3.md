---
title: 'init(_:in:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/init(_:in:)-75xo3'
source_url: 'https://developer.apple.com/documentation/swift/range/init(_:in:)-75xo3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/init%28_%3Ain%3A%29-75xo3.json'
content_hash: 'sha256:11040847176e78b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# init(_:in:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<R, S>(_ region: R, in string: S) where R : RangeExpression, S : StringProtocol, R.Bound == AttributedString.Index
```
