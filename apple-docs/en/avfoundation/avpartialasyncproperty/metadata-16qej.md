---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/metadata-16qej
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/metadata-16qej'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/metadata-16qej.json'
content_hash: 'sha256:85372eb57a54c89b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# metadata

<sub>Type Property</sub>

The metadata items that an asset contains for all metadata identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var metadata: AVAsyncProperty<Root, [AVMetadataItem]> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

You can filter items in the array according to language by calling [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>), or by identifier by calling [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>).

## See Also

### Loading metadata

- [commonMetadata](commonmetadata-3j3n4.md) — The metadata items that an asset contains for common metadata identifiers.
- [availableMetadataFormats](availablemetadataformats-4yiq8.md) — The formats of metadata that an asset contains.
- [- loadMetadataForFormat:completionHandler:](<../avasset/loadmetadata(for_completionhandler_).md>) — Loads an array of metadata items that the asset contains for the specified format.
- [creationDate](creationdate.md) — A metadata item that indicates the creation date of an asset.
- [lyrics](lyrics.md) — The lyrics of the asset in a language suitable for the current locale.
