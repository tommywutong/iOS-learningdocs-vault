---
title: 'loadChapterMetadataGroups(bestMatchingPreferredLanguages:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasset/loadchaptermetadatagroups(bestmatchingpreferredlanguages:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/loadchaptermetadatagroups(bestmatchingpreferredlanguages:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/loadchaptermetadatagroups%28bestmatchingpreferredlanguages%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:c97979dcf22d22f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# loadChapterMetadataGroups(bestMatchingPreferredLanguages:completionHandler:)

<sub>Instance Method</sub>

Loads chapter metadata with a locale that best matches the list of preferred languages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadChapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String], completionHandler: @escaping @Sendable ([AVTimedMetadataGroup]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadChapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) async throws -> [AVTimedMetadataGroup]
```

## Parameters

- `preferredLanguages` — An array of language identifiers in order of preference, each of which is an IETF BCP 47 (RFC 4646) language identifier. Call  [preferredLanguages](../../foundation/locale/preferredlanguages.md) to retrieve the list of languates the user prefers.

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **metadataGroups** — An array of metadata groups, which may be empty if no groups exist for the specified languages. The value is `nil` if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## Discussion

This method returns an array of [AVTimedMetadataGroup](../avtimedmetadatagroup.md) objects asynchronously. Each object in the array contains an [AVMetadataItem](../avmetadataitem.md) that represents the chapter’s title, and the metadata group’s [timeRange](../avtimedmetadatagroup/timerange.md) value equals the time range of the chapter title item.

The metadata group contains all chapter metadata, including items with the common key [AVMetadataCommonKeyArtwork](../avmetadatakey/commonkeyartwork.md), if such items are present. The system adds an [AVMetadataItem](../avmetadataitem.md) with the specified common key to an existing [AVTimedMetadataGroup](../avtimedmetadatagroup.md) object if the time range (timestamp and duration) of the metadata item and the metadata group overlap. The locales of such items don’t need to match the locale of the chapter titles.

You can use the [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>) method to further filter the metadata items in each group. You can also filter the returned items based on locale using the [+ metadataItemsFromArray:withLocale:](<../avmetadataitem/metadataitems(from_with_).md>) method.

## See Also

### Loading chapter metadata

- [availableChapterLocales](../avpartialasyncproperty/availablechapterlocales.md) — The locales of an asset’s chapter metadata.
- [loadChapterMetadataGroups(withTitleLocale:containingItemsWithCommonKeys:)](<loadchaptermetadatagroups(withtitlelocale_containingitemswithcommonkeys_).md>) — Loads chapter metadata that contains the specified title locale and common keys.
