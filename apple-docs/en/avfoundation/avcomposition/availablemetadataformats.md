---
title: availableMetadataFormats
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/availablemetadataformats
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/availablemetadataformats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/availablemetadataformats.json'
content_hash: 'sha256:b925f798f9a02f64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# availableMetadataFormats

<sub>Instance Property</sub>

The metadata formats this asset contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var availableMetadataFormats: [AVMetadataFormat] { get }
```

## Discussion

Metadata formats may include ID3, iTunes metadata, and so on.

## See Also

### Accessing metadata

- [metadata](metadata.md) — An array of metadata items for all metadata identifiers for which a value is available.
- [commonMetadata](commonmetadata.md) — The metadata items an asset contains for common metadata identifiers that provide a value.
- [- metadataForFormat:](<metadata(forformat_).md>) — Returns an array of metadata items from the container with the specified format.
- [creationDate](creationdate.md) — A metadata item that indicates the asset’s creation date.
- [lyrics](lyrics.md) — The lyrics of the asset in a language suitable for the current locale.
