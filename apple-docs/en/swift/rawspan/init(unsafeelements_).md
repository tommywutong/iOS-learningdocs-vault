---
title: 'init(unsafeElements:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawspan/init(unsafeelements:)'
source_url: 'https://developer.apple.com/documentation/swift/rawspan/init(unsafeelements:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/init%28unsafeelements%3A%29.json'
content_hash: 'sha256:d34f5e0bb2f3802e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# init(unsafeElements:)

<sub>Initializer</sub>

Unsafely view a typed span as a raw span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Element>(unsafeElements span: Span<Element>)
```

## Discussion

Creates a `RawSpan` over the memory represented by a `Span<Element>`
