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
doc_path: '/documentation/swift/range/init(_:in:)-612lr'
source_url: 'https://developer.apple.com/documentation/swift/range/init(_:in:)-612lr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/init%28_%3Ain%3A%29-612lr.json'
content_hash: 'sha256:ab1db784174868bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# init(_:in:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<R, S>(_ region: R, in attributedString: S) where R : RangeExpression, S : AttributedStringProtocol, R.Bound == String.Index
```
