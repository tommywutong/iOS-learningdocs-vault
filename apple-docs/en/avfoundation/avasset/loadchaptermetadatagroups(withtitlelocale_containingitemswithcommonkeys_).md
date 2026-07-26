---
title: 'loadChapterMetadataGroups(withTitleLocale:containingItemsWithCommonKeys:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasset/loadchaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/loadchaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/loadchaptermetadatagroups%28withtitlelocale%3Acontainingitemswithcommonkeys%3A%29.json'
content_hash: 'sha256:9d9dc68f37140685'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# loadChapterMetadataGroups(withTitleLocale:containingItemsWithCommonKeys:)

<sub>Instance Method</sub>

Loads chapter metadata that contains the specified title locale and common keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadChapterMetadataGroups(withTitleLocale locale: Locale, containingItemsWithCommonKeys commonKeys: [AVMetadataKey] = []) async throws -> [AVTimedMetadataGroup]
```

## Parameters

- `locale` — The locale of the chapter metadata to load.

- `commonKeys` — An array of common [AVMetadataKey](../avmetadatakey.md) values to include in the returned array. The framework currently only supports the [AVMetadataCommonKeyArtwork](../avmetadatakey/commonkeyartwork.md) key.

## Return Value

An array of chapter metadata items for a locale.

## Discussion

This method returns an array of [AVTimedMetadataGroup](../avtimedmetadatagroup.md) objects asynchronously. Each object in the array contains an [AVMetadataItem](../avmetadataitem.md) that represents the chapter’s title, and the metadata group’s [timeRange](../avtimedmetadatagroup/timerange.md) value equals the time range of the chapter title item.

The metadata group contains all chapter metadata, including items with the common key [AVMetadataCommonKeyArtwork](../avmetadatakey/commonkeyartwork.md), if such items are present. The system adds an [AVMetadataItem](../avmetadataitem.md) with the specified common key to an existing [AVTimedMetadataGroup](../avtimedmetadatagroup.md) object if the time range (timestamp and duration) of the metadata item and the metadata group overlap. The locales of such items don’t need to match the locale of the chapter titles.

You can use the [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) method to further filter the metadata items in each group. You can also filter the returned items based on locale using the [+ metadataItemsFromArray:withLocale:](<../avmetadataitem/metadataitems(from_with_).md>) method.

## See Also

### Loading chapter metadata

- [availableChapterLocales](../avpartialasyncproperty/availablechapterlocales.md) — The locales of an asset’s chapter metadata.
- [- loadChapterMetadataGroupsBestMatchingPreferredLanguages:completionHandler:](<loadchaptermetadatagroups(bestmatchingpreferredlanguages_completionhandler_).md>) — Loads chapter metadata with a locale that best matches the list of preferred languages.
