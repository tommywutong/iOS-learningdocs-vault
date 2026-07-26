---
title: 'chapterMetadataGroups(withTitleLocale:containingItemsWithCommonKeys:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcomposition/chaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/chaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/chaptermetadatagroups%28withtitlelocale%3Acontainingitemswithcommonkeys%3A%29.json'
content_hash: 'sha256:a7430a3a9cf7358f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# chapterMetadataGroups(withTitleLocale:containingItemsWithCommonKeys:)

<sub>Instance Method</sub>

Returns an array of chapters that contain the specified title locale and common keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func chapterMetadataGroups(withTitleLocale locale: Locale, containingItemsWithCommonKeys commonKeys: [AVMetadataKey]?) -> [AVTimedMetadataGroup]
```

## Parameters

- `locale` — The locale of the metadata items carrying chapter titles.

- `commonKeys` — An array of common keys of [AVMetadataItem](../avmetadataitem.md) to include in the returned array. The framework currently only supports the [AVMetadataCommonKeyArtwork](../avmetadatakey/commonkeyartwork.md) key.

## Return Value

An array of [AVTimedMetadataGroup](../avtimedmetadatagroup.md) objects.

## Discussion

A metadata group contains an [AVMetadataItem](../avmetadataitem.md) object that represents the chapter title, and a time range equal to the time range of the chapter title item.

The system adds a metadata item with the specified common key to an existing [AVTimedMetadataGroup](../avtimedmetadatagroup.md) object if the time range (timestamp and duration) of the metadata item and the metadata group overlap.

The locale of items that don’t contain chapter titles doesn’t need to match the specified locale parameter. You can filter the returned items based on locale using [+ metadataItemsFromArray:withLocale:](<../avmetadataitem/metadataitems(from_with_).md>).

## See Also

### Accessing chapter metadata

- [availableChapterLocales](availablechapterlocales.md) — The locales of the asset’s chapter metadata.
- [- chapterMetadataGroupsBestMatchingPreferredLanguages:](<chaptermetadatagroups(bestmatchingpreferredlanguages_).md>) — Returns an array of chapters with a locale that best matches the list of preferred languages.
