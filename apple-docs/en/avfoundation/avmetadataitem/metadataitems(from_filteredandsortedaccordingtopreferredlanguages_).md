---
title: 'metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/metadataitems%28from%3Afilteredandsortedaccordingtopreferredlanguages%3A%29.json'
content_hash: 'sha256:8a849fe655ae7ec4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)

<sub>Type Method</sub>

Returns metadata items whose locales match one of the specified language identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem]
```

## Parameters

- `metadataItems` — The metadata items to filter.

- `preferredLanguages` — An array of [NSString](../../foundation/nsstring.md) objects, each of which contains a canonicalized IETF BCP 47 language identifier. The order of the identifiers in the array reflects the preferred language order, with the most preferred language being first in the array. Typically, you pass the user’s preferred languages by retrieving this array from the [preferredLanguages](../../foundation/nslocale/preferredlanguages.md) class method of [NSLocale](../../foundation/nslocale.md).

## Return Value

An array of metadata items that match the specified languages.

## See Also

### Filtering arrays of metadata items

- [+ metadataItemsFromArray:filteredByIdentifier:](<metadataitems(from_filteredbyidentifier_).md>) — Returns metadata items for the specified identifier.
- [+ metadataItemsFromArray:withKey:keySpace:](<metadataitems(from_withkey_keyspace_).md>) — Returns metadata items that match a specified key or key space.
- [+ metadataItemsFromArray:withLocale:](<metadataitems(from_with_).md>) — Returns metadata items that match a specified locale.
- [+ metadataItemsFromArray:filteredByMetadataItemFilter:](<metadataitems(from_filteredby_).md>) — Returns filtered metadata items.
