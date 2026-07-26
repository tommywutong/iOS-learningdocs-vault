---
title: 'metadataItems(from:filteredByIdentifier:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredbyidentifier:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredbyidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/metadataitems%28from%3Afilteredbyidentifier%3A%29.json'
content_hash: 'sha256:b1c1938206469b55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# metadataItems(from:filteredByIdentifier:)

<sub>Type Method</sub>

Returns metadata items for the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], filteredByIdentifier identifier: AVMetadataIdentifier) -> [AVMetadataItem]
```

## Parameters

- `metadataItems` — The metadata items to filter.

- `identifier` — The identifier of the metadata items to retrieve.

## Return Value

An array of metadata items that match the specified identifier.

## See Also

### Filtering arrays of metadata items

- [+ metadataItemsFromArray:withKey:keySpace:](<metadataitems(from_withkey_keyspace_).md>) — Returns metadata items that match a specified key or key space.
- [+ metadataItemsFromArray:withLocale:](<metadataitems(from_with_).md>) — Returns metadata items that match a specified locale.
- [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) — Returns metadata items whose locales match one of the specified language identifiers.
- [+ metadataItemsFromArray:filteredByMetadataItemFilter:](<metadataitems(from_filteredby_).md>) — Returns filtered metadata items.
