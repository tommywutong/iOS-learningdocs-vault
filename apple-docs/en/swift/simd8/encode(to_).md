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
doc_path: '/documentation/swift/simd8/encode(to:)'
source_url: 'https://developer.apple.com/documentation/swift/simd8/encode(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd8/encode%28to%3A%29.json'
content_hash: 'sha256:ebed8a7ecf119914'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD8](../simd8.md)

# encode(to:)

<sub>Instance Method</sub>

Encodes the scalars of this vector into the given encoder in an unkeyed container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder) throws
```

## Parameters

- `encoder` — The encoder to write data to.

## Discussion

This function throws an error if any values are invalid for the given encoder’s format.
