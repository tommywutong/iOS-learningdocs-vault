---
title: commonMetadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/commonmetadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/commonmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/commonmetadata.json'
content_hash: 'sha256:c35d8315d134ccc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# commonMetadata

<sub>Instance Property</sub>

The metadata items an asset contains for common metadata identifiers that provide a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var commonMetadata: [AVMetadataItem] { get }
```

## Discussion

This property value is an array of metadata items, one for each metadata key from the common key space for which the asset has an available value. You can use the various class methods provided by [AVMetadataItem](../avmetadataitem.md), such as [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) or [+ metadataItemsFromArray:withLocale:](<../avmetadataitem/metadataitems(from_with_).md>) to filter the array to the specific items of interest.

## See Also

### Accessing metadata

- [metadata](metadata.md) — An array of metadata items for all metadata identifiers for which a value is available.
- [availableMetadataFormats](availablemetadataformats.md) — The metadata formats this asset contains.
- [- metadataForFormat:](<metadata(forformat_).md>) — Returns an array of metadata items from the container with the specified format.
- [creationDate](creationdate.md) — A metadata item that indicates the asset’s creation date.
- [lyrics](lyrics.md) — The lyrics of the asset in a language suitable for the current locale.
