---
title: 'metadataItems(from:with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/metadataitems(from:with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/metadataitems%28from%3Awith%3A%29.json'
content_hash: 'sha256:f3c32809f2633ceb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# metadataItems(from:with:)

<sub>Type Method</sub>

Returns metadata items that match a specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], with locale: Locale) -> [AVMetadataItem]
```

## Parameters

- `metadataItems` — The metadata items to filter.

- `locale` — The locale of the metadata items to retrieve.

## Return Value

An array of metadata items that match the specified key and key space.

## See Also

### Filtering arrays of metadata items

- [+ metadataItemsFromArray:filteredByIdentifier:](<metadataitems(from_filteredbyidentifier_).md>) — Returns metadata items for the specified identifier.
- [+ metadataItemsFromArray:withKey:keySpace:](<metadataitems(from_withkey_keyspace_).md>) — Returns metadata items that match a specified key or key space.
- [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) — Returns metadata items whose locales match one of the specified language identifiers.
- [+ metadataItemsFromArray:filteredByMetadataItemFilter:](<metadataitems(from_filteredby_).md>) — Returns filtered metadata items.
