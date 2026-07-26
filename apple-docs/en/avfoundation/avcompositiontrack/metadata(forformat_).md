---
title: 'metadata(forFormat:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcompositiontrack/metadata(forformat:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/metadata(forformat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/metadata%28forformat%3A%29.json'
content_hash: 'sha256:a2895404f5f479c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# metadata(forFormat:)

<sub>Instance Method</sub>

Returns metadata items that a track contains for the specified format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func metadata(forFormat format: AVMetadataFormat) -> [AVMetadataItem]
```

## Parameters

- `format` — The format of the metadata items to retrieve.

## Return Value

An array of metadata items matching the specified format, or an empty array if none are found.

## See Also

### Accessing metadata

- [metadata](metadata.md) — An array of metadata items for all metadata identifiers that have a value.
- [commonMetadata](commonmetadata.md) — An array of metadata items for all common metadata keys that have a value.
- [availableMetadataFormats](availablemetadataformats.md) — An array of metadata formats available for the track.
