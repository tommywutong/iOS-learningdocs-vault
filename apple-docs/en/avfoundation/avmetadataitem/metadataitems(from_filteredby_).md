---
title: 'metadataItems(from:filteredBy:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredby:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/metadataitems%28from%3Afilteredby%3A%29.json'
content_hash: 'sha256:494505a67dfc932c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# metadataItems(from:filteredBy:)

<sub>Type Method</sub>

Returns filtered metadata items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], filteredBy metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem]
```

## Parameters

- `metadataItems` — The metadata items to filter.

- `metadataItemFilter` — The metadata item filter to apply.

## Return Value

The filtered array of metadata items.

## See Also

### Filtering arrays of metadata items

- [+ metadataItemsFromArray:filteredByIdentifier:](<metadataitems(from_filteredbyidentifier_).md>) — Returns metadata items for the specified identifier.
- [+ metadataItemsFromArray:withKey:keySpace:](<metadataitems(from_withkey_keyspace_).md>) — Returns metadata items that match a specified key or key space.
- [+ metadataItemsFromArray:withLocale:](<metadataitems(from_with_).md>) — Returns metadata items that match a specified locale.
- [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) — Returns metadata items whose locales match one of the specified language identifiers.
