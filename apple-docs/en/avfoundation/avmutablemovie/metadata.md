---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/metadata.json'
content_hash: 'sha256:2123e8e37276a675'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# metadata

<sub>Instance Property</sub>

An array of metadata items for all metadata identifiers for which a value is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var metadata: [AVMetadataItem] { get set }
```

## Discussion

You can filter the metadata items by language using the [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) method, or by identifier with the [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) method.

## See Also

### Accessing metadata

- [commonMetadata](commonmetadata.md) — The metadata items an asset contains for common metadata identifiers that provide a value.
- [availableMetadataFormats](availablemetadataformats.md) — The metadata formats this asset contains.
- [- metadataForFormat:](<metadata(forformat_).md>) — Returns an array of metadata items from the container with the specified format.
- [creationDate](creationdate.md) — A metadata item that indicates the asset’s creation date.
- [lyrics](lyrics.md) — The lyrics of the asset in a language suitable for the current locale.
