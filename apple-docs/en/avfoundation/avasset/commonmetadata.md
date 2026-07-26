---
title: commonMetadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/commonmetadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/commonmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/commonmetadata.json'
content_hash: 'sha256:56d7ce5909f2896d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# commonMetadata

<sub>Instance Property</sub>

The metadata items an asset contains for common metadata identifiers that provide a value.

> [!warning] Deprecated
> Load the value of [commonMetadata](../avpartialasyncproperty/commonmetadata-3j3n4.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var commonMetadata: [AVMetadataItem] { get }
```

## Discussion

This property value is an array of metadata items, one for each metadata key from the common key space for which the asset has an available value. You can use the various class methods provided by [AVMetadataItem](../avmetadataitem.md), such as [+ metadataItemsFromArray:filteredByIdentifier:](<../avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) or [+ metadataItemsFromArray:withLocale:](<../avmetadataitem/metadataitems(from_with_).md>) to filter the array to the specific items of interest.
