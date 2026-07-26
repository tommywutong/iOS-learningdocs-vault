---
title: 'encode(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int128/encode(to:)'
source_url: 'https://developer.apple.com/documentation/swift/int128/encode(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/encode%28to%3A%29.json'
content_hash: 'sha256:42212281f101d7ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

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

This function throws an error if any values are invalid for the given encoder’s format.
