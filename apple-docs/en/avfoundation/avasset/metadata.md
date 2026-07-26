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
doc_path: /documentation/avfoundation/avasset/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/metadata.json'
content_hash: 'sha256:7894e785cc74a940'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# metadata

<sub>Instance Property</sub>

An array of metadata items for all metadata identifiers for which a value is available.

> [!warning] Deprecated
> Load the value of [metadata](../avpartialasyncproperty/metadata-16qej.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var metadata: [AVMetadataItem] { get }
```

## Discussion

You can filter the metadata items by language using the [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) method, or by identifier with the [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) method.
