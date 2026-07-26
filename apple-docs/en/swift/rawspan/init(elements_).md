---
title: 'init(elements:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawspan/init(elements:)'
source_url: 'https://developer.apple.com/documentation/swift/rawspan/init(elements:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/init%28elements%3A%29.json'
content_hash: 'sha256:5922d6d65cb61f81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# init(elements:)

<sub>Initializer</sub>

View a typed span as a raw span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Element>(elements span: Span<Element>) where Element : ConvertibleToBytes
```

## Discussion

Creates a `RawSpan` over the memory represented by a `Span<Element>`.
