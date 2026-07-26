---
title: singleValueContainer()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/encoder/singlevaluecontainer()
source_url: 'https://developer.apple.com/documentation/swift/encoder/singlevaluecontainer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/encoder/singlevaluecontainer%28%29.json'
content_hash: 'sha256:8affeac7d6052380'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Encoder](../encoder.md)

# singleValueContainer()

<sub>Instance Method</sub>

Returns an encoding container appropriate for holding a single primitive value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func singleValueContainer() -> any SingleValueEncodingContainer
```

## Return Value

A new empty single value container.

## Discussion

You must use only one kind of top-level encoding container. This method must not be called after a call to `unkeyedContainer()` or `container(keyedBy:)`, or after encoding a value through a call to `singleValueContainer()`
