---
title: 'init(from:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/never/init(from:)'
source_url: 'https://developer.apple.com/documentation/swift/never/init(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/never/init%28from%3A%29.json'
content_hash: 'sha256:e87cc76921f8f135'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Never](../never.md)

# init(from:)

<sub>Initializer</sub>

Creates a new instance by decoding from the given decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder` — The decoder to read data from.

## Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.
