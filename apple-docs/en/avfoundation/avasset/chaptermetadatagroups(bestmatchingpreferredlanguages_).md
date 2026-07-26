---
title: 'chapterMetadataGroups(bestMatchingPreferredLanguages:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasset/chaptermetadatagroups(bestmatchingpreferredlanguages:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/chaptermetadatagroups(bestmatchingpreferredlanguages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/chaptermetadatagroups%28bestmatchingpreferredlanguages%3A%29.json'
content_hash: 'sha256:148d7f1c8c2d304d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# chapterMetadataGroups(bestMatchingPreferredLanguages:)

<sub>Instance Method</sub>

Returns an array of chapters with a locale that best matches the list of preferred languages.

> [!warning] Deprecated
> Use [- loadChapterMetadataGroupsBestMatchingPreferredLanguages:completionHandler:](<loadchaptermetadatagroups(bestmatchingpreferredlanguages_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

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

This method is callable without blocking the current thread after you’ve asynchronously loaded the [availableChapterLocales](availablechapterlocales.md) property.
