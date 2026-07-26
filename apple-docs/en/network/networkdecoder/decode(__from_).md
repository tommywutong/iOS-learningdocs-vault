---
title: 'decode(_:from:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkdecoder/decode(_:from:)'
source_url: 'https://developer.apple.com/documentation/network/networkdecoder/decode(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkdecoder/decode%28_%3Afrom%3A%29.json'
content_hash: 'sha256:bf568124798e31ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkDecoder](../networkdecoder.md)

# decode(_:from:)

<sub>Instance Method</sub>

Decode a decodable object from Data

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T>(_ type: T.Type, from data: Data) throws -> T where T : Decodable
```

## Parameters

- `type` — The type to decode into.

- `data` — The data to use for decoding

## Return Value

An instance of type T or throws an error if unable to decode.
