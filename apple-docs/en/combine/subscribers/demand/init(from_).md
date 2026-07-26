---
title: 'init(from:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscribers/demand/init(from:)'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/demand/init(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/demand/init%28from%3A%29.json'
content_hash: 'sha256:e0c2c7cf2b6944b6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Demand](../demand.md)

# init(from:)

<sub>Initializer</sub>

Creates a demand instance from a decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder` — The decoder of a previously-encoded [Demand](../demand.md) instance.

## See Also

### Encoding and decoding

- [encode(to:)](<encode(to_).md>) — Encodes the demand to the provide encoder.
