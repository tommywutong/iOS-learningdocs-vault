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
doc_path: '/documentation/swift/mutablerawspan/init(unsafeelements:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/init(unsafeelements:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/init%28unsafeelements%3A%29.json'
content_hash: 'sha256:fc3a19cf9f5ae455'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# init(unsafeElements:)

<sub>Initializer</sub>

Unsafely convert a typed span to a raw span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Element>(unsafeElements elements: consuming MutableSpan<Element>)
```

## Parameters

- `elements` — An existing `MutableSpan<Element>`, from which this `MutableRawSpan` will inherit its lifetime.

## Discussion

Creates a `MutableRawSpan` over the memory represented by a `MutableSpan<Element>`.
