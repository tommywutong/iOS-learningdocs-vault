---
title: 'init(from:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/decodable/init(from:)-8cbq4'
source_url: 'https://developer.apple.com/documentation/swift/decodable/init(from:)-8cbq4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodable/init%28from%3A%29-8cbq4.json'
content_hash: 'sha256:78bd6028bcd752db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Decodable](../decodable.md)

# init(from:)

<sub>Initializer</sub>

Creates a new vector by decoding scalars from the given decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder` — The decoder to read data from.

## Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.
