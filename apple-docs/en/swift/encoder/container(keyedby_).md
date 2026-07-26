---
title: 'container(keyedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/encoder/container(keyedby:)'
source_url: 'https://developer.apple.com/documentation/swift/encoder/container(keyedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/encoder/container%28keyedby%3A%29.json'
content_hash: 'sha256:157191689ee9f557'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Encoder](../encoder.md)

# container(keyedBy:)

<sub>Instance Method</sub>

Returns an encoding container appropriate for holding multiple values keyed by the given key type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func container<Key>(keyedBy type: Key.Type) -> KeyedEncodingContainer<Key> where Key : CodingKey
```

## Parameters

- `type` — The key type to use for the container.

## Return Value

A new keyed encoding container.

## Discussion

You must use only one kind of top-level encoding container. This method must not be called after a call to `unkeyedContainer()` or after encoding a value through a call to `singleValueContainer()`
