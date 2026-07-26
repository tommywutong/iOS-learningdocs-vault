---
title: 'decode(_:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsondecoder/decode(_:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/decode(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/decode%28_%3Afrom%3A%29.json'
content_hash: 'sha256:9dfbe6637016e8de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# decode(_:from:)

<sub>Instance Method</sub>

Returns a value of the type you specify, decoded from a JSON object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T>(_ type: T.Type, from data: Data) throws -> T where T : Decodable
```

## Parameters

- `type` — The type of the value to decode from the supplied JSON object.

- `data` — The JSON object to decode.

## Return Value

A value of the specified type, if the decoder can parse the data.

## Discussion

If the data isn’t valid JSON, this method throws the [DecodingError.dataCorrupted(_:)](<../../swift/decodingerror/datacorrupted(__).md>) error. If a value within the JSON fails to decode, this method throws the corresponding error.
