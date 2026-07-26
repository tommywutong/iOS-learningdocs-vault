---
title: 'encode(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/encode(to:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/encode(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/encode%28to%3A%29.json'
content_hash: 'sha256:f389d30b8416c3f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# encode(to:)

<sub>Instance Method</sub>

Encodes this value into the given encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder) throws
```

## Parameters

- `encoder` — The encoder to write data to.

## Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container in its place.

This function throws an error if any values are invalid for the given encoder’s format.
