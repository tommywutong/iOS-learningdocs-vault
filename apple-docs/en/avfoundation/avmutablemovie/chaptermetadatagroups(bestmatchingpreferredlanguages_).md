---
title: 'chapterMetadataGroups(bestMatchingPreferredLanguages:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/chaptermetadatagroups(bestmatchingpreferredlanguages:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/chaptermetadatagroups(bestmatchingpreferredlanguages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/chaptermetadatagroups%28bestmatchingpreferredlanguages%3A%29.json'
content_hash: 'sha256:60b9f7bf316a14f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# chapterMetadataGroups(bestMatchingPreferredLanguages:)

<sub>Instance Method</sub>

Returns an array of chapters with a locale that best matches the list of preferred languages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func chapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) -> [AVTimedMetadataGroup]
```

## Parameters

- `preferredLanguages` — An array of BCP 47 language identifier strings. The order of the identifiers in the array reflects the preferred language order, with the most preferred language being first in the array. Typically, you pass the user’s preferred languages by retrieving this array from the [preferredLanguages](../../foundation/nslocale/preferredlanguages.md) class method of [NSLocale](../../foundation/nslocale.md).

## Return Value

An array of [AVTimedMetadataGroup](../avtimedmetadatagroup.md) objects.

## Discussion

Each object in the returned array contains an [AVMetadataItem](../avmetadataitem.md) object representing the chapter title. The time range property of the [AVTimedMetadataGroup](../avtimedmetadatagroup.md) object is equal to the time range of the chapter title item.

The metadata group contains all chapter metadata, including items with the common key [AVMetadataCommonKeyArtwork](../avmetadatakey/commonkeyartwork.md), if such items are present. The system adds an [AVMetadataItem](../avmetadataitem.md) with the specified common key to an existing [AVTimedMetadataGroup](../avtimedmetadatagroup.md) object if the time range (timestamp and duration) of the metadata item and the metadata group overlap. The locale of such items don’t need to match the locale of the chapter titles.

You can use the [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) method to further filter the metadata items in each group. You can also filter the returned items based on locale using the [+ metadataItemsFromArray:withLocale:](<../avmetadataitem/metadataitems(from_with_).md>) method.

This method is callable without blocking the current thread after you’ve asynchronously loaded the [availableChapterLocales](../avasset/availablechapterlocales.md) property.

## See Also

### Accessing chapter metadata

- [availableChapterLocales](availablechapterlocales.md) — The locales of the asset’s chapter metadata.
- [- chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](<chaptermetadatagroups(withtitlelocale_containingitemswithcommonkeys_).md>) — Returns an array of chapters that contain the specified title locale and common keys.
