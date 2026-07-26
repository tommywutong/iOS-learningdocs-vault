---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/metadata.json'
content_hash: 'sha256:c5616c802da3655e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# metadata

<sub>Instance Property</sub>

An array of metadata items for all metadata identifiers that have a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var metadata: [AVMetadataItem] { get }
```

## Discussion

You can filter the array of metadata items according to language using the [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) method. Filter the results by identifier using the [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) method.

## See Also

### Accessing metadata

- [commonMetadata](commonmetadata.md) — An array of metadata items for all common metadata keys that have a value.
- [availableMetadataFormats](availablemetadataformats.md) — An array of metadata formats available for the track.
- [- metadataForFormat:](<metadata(forformat_).md>) — Returns metadata items that a track contains for the specified format.
