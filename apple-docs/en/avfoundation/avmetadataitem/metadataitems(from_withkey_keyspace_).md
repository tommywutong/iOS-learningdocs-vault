---
title: 'metadataItems(from:withKey:keySpace:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/metadataitems(from:withkey:keyspace:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:withkey:keyspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/metadataitems%28from%3Awithkey%3Akeyspace%3A%29.json'
content_hash: 'sha256:9d0b7095841e769d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# metadataItems(from:withKey:keySpace:)

<sub>Type Method</sub>

Returns metadata items that match a specified key or key space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], withKey key: Any?, keySpace: AVMetadataKeySpace?) -> [AVMetadataItem]
```

## Parameters

- `metadataItems` — The metadata items to filter.

- `key` — The key of the metadata items to retrieve, or `nil` if you don’t want to filter by key.

- `keySpace` — The key space of the metadata items to retrieve, or `nil` if you don’t want to filter by key space.

## Return Value

An array of metadata items that match the specified key and key space.

## See Also

### Filtering arrays of metadata items

- [+ metadataItemsFromArray:filteredByIdentifier:](<metadataitems(from_filteredbyidentifier_).md>) — Returns metadata items for the specified identifier.
- [+ metadataItemsFromArray:withLocale:](<metadataitems(from_with_).md>) — Returns metadata items that match a specified locale.
- [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) — Returns metadata items whose locales match one of the specified language identifiers.
- [+ metadataItemsFromArray:filteredByMetadataItemFilter:](<metadataitems(from_filteredby_).md>) — Returns filtered metadata items.
