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
doc_path: '/documentation/avfoundation/avcomposition/metadata(forformat:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/metadata(forformat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/metadata%28forformat%3A%29.json'
content_hash: 'sha256:2fbbc90259c02eda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# metadata(forFormat:)

<sub>Instance Method</sub>

Returns an array of metadata items from the container with the specified format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func metadata(forFormat format: AVMetadataFormat) -> [AVMetadataItem]
```

## Parameters

- `format` — The metadata format for which you want items.

## Return Value

An array of [AVMetadataItem](../avmetadataitem.md) objects, one for each metadata item in the container of the specified format, or an empty array if there is no metadata for the specified format.

## Discussion

You can filter the array to the specific items of interest using the class methods provided by [AVMetadataItem](../avmetadataitem.md), like [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) or [+ metadataItemsFromArray:withLocale:](<../avmetadataitem/metadataitems(from_with_).md>).

You can call this method without blocking the current thread after you’ve asynchronously loaded the [availableMetadataFormats](../avasset/availablemetadataformats.md) property.

## See Also

### Accessing metadata

- [metadata](metadata.md) — An array of metadata items for all metadata identifiers for which a value is available.
- [commonMetadata](commonmetadata.md) — The metadata items an asset contains for common metadata identifiers that provide a value.
- [availableMetadataFormats](availablemetadataformats.md) — The metadata formats this asset contains.
- [creationDate](creationdate.md) — A metadata item that indicates the asset’s creation date.
- [lyrics](lyrics.md) — The lyrics of the asset in a language suitable for the current locale.
