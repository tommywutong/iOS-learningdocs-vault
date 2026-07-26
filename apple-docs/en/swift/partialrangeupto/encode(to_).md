---
title: 'encode(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/partialrangeupto/encode(to:)'
source_url: 'https://developer.apple.com/documentation/swift/partialrangeupto/encode(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/partialrangeupto/encode%28to%3A%29.json'
content_hash: 'sha256:d86a237d10f4c6e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [PartialRangeUpTo](../partialrangeupto.md)

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
