---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.10+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/metadata.json'
content_hash: 'sha256:863600c9f15939cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# metadata

<sub>Instance Property</sub>

An array of metadata items for all metadata identifiers that have a value.

> [!warning] Deprecated
> Load the value of [metadata](../avpartialasyncproperty/metadata-6e14c.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var metadata: [AVMetadataItem] { get }
```

## Discussion

You can filter the array of metadata items according to language using the [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) method. Filter the results by identifier using the [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) method.
