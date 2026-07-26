---
title: availableMetadataFormats
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/availablemetadataformats
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/availablemetadataformats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/availablemetadataformats.json'
content_hash: 'sha256:a8d6cab29ac11b78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# availableMetadataFormats

<sub>Instance Property</sub>

The metadata formats this asset contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

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
