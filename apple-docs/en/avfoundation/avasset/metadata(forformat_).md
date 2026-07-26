---
title: 'metadata(forFormat:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasset/metadata(forformat:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/metadata(forformat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/metadata%28forformat%3A%29.json'
content_hash: 'sha256:49ac7854052c717c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# metadata(forFormat:)

<sub>Instance Method</sub>

Returns an array of metadata items from the container with the specified format.

> [!warning] Deprecated
> Use [- loadMetadataForFormat:completionHandler:](<loadmetadata(for_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func metadata(forFormat format: AVMetadataFormat) -> [AVMetadataItem]
```

## Parameters

- `format` — The metadata format for which you want items.

## Return Value

An array of [AVMetadataItem](../avmetadataitem.md) objects, one for each metadata item in the container of the specified format, or an empty array if there is no metadata for the specified format.

## Discussion

You can filter the array to the specific items of interest using the class methods provided by [AVMetadataItem](../avmetadataitem.md), like [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) or [+ metadataItemsFromArray:withLocale:](<../avmetadataitem/metadataitems(from_with_).md>).

You can call this method without blocking the current thread after you’ve asynchronously loaded the [availableMetadataFormats](availablemetadataformats.md) property.
