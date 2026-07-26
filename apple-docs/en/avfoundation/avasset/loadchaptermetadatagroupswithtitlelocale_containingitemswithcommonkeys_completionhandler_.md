---
title: 'loadChapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:completionHandler:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasset/loadchaptermetadatagroupswithtitlelocale:containingitemswithcommonkeys:completionhandler:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/loadchaptermetadatagroupswithtitlelocale:containingitemswithcommonkeys:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/loadchaptermetadatagroupswithtitlelocale%3Acontainingitemswithcommonkeys%3Acompletionhandler%3A.json'
content_hash: 'sha256:52199c0bfdd18c29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# loadChapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:completionHandler:

<sub>Instance Method</sub>

Loads chapter metadata that contains the specified title locale and common keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) loadChapterMetadataGroupsWithTitleLocale:(NSLocale *) locale containingItemsWithCommonKeys:(NSArray<NSString *> *) commonKeys completionHandler:(void (^)(NSArray<AVTimedMetadataGroup *> *, NSError *)) completionHandler;
```

## Parameters

- `locale` — The locale of the chapter metadata to load.

- `commonKeys` — An array of common keys of [AVMetadataItem](../avmetadataitem.md) to include in the returned array. The framework currently only supports the [AVMetadataCommonKeyArtwork](../avmetadatakey/commonkeyartwork.md) key.

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **metadataGroups** — An array of metadata groups, which may be empty if no groups exist for the locale. The value is `nil` if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading chapter metadata

- [- loadChapterMetadataGroupsBestMatchingPreferredLanguages:completionHandler:](<loadchaptermetadatagroups(bestmatchingpreferredlanguages_completionhandler_).md>) — Loads chapter metadata with a locale that best matches the list of preferred languages.
