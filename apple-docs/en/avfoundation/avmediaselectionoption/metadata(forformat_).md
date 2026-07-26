---
title: 'metadata(forFormat:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediaselectionoption/metadata(forformat:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/metadata(forformat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/metadata%28forformat%3A%29.json'
content_hash: 'sha256:a027f382ffbc21cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# metadata(forFormat:)

<sub>Instance Method</sub>

Returns an array of metadata items—one for each metadata item in the container of a given format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func metadata(forFormat format: String) -> [AVMetadataItem]
```

## Parameters

- `format` — The metadata format for which items are requested.

## Return Value

An array of `AVMetadataItem` objects, one for each metadata item in the container of format, or `nil` if there is no metadata of the specified format.

## See Also

### Managing metadata

- [commonMetadata](commonmetadata.md) — An array of metadata items for each common metadata key for which a value is available.
- [availableMetadataFormats](availablemetadataformats.md) — The metadata formats that contain metadata associated with the option.
