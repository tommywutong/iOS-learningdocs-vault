---
title: commonMetadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/commonmetadata-73m58
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/commonmetadata-73m58'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/commonmetadata-73m58.json'
content_hash: 'sha256:6423801404335de4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# commonMetadata

<sub>Type Property</sub>

An array of metadata items for all common metadata keys that have a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

You can filter the array of metadata items according to language using the [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) method. Filter the results by identifier using the [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) method.

## See Also

### Loading metadata

- [metadata](metadata-6e14c.md) — An array of metadata items for all metadata identifiers that have a value.
- [availableMetadataFormats](availablemetadataformats-5p9xg.md) — An array of metadata formats available for the track.
- [- loadMetadataForFormat:completionHandler:](<../avassettrack/loadmetadata(for_completionhandler_).md>) — Loads metadata items that a track contains for the specified format.
