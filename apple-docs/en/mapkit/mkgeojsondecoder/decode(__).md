---
title: 'decode(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkgeojsondecoder/decode(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeojsondecoder/decode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeojsondecoder/decode%28_%3A%29.json'
content_hash: 'sha256:404b3a3f7a262583'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeoJSONDecoder](../mkgeojsondecoder.md)

# decode(_:)

<sub>Instance Method</sub>

Decodes the provided data into native MapKit types that a map can display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode(_ data: Data) throws -> [any MKGeoJSONObject]
```

## Parameters

- `data` — An [NSData](../../foundation/nsdata.md) object that contains the JSON to decode.

## Return Value

An array of [MKGeoJSONObject](../mkgeojsonobject.md) objects, or an error if the decoder encounters an issue.
