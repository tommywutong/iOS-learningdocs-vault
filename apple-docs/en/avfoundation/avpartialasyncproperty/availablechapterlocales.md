---
title: availableChapterLocales
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/availablechapterlocales
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availablechapterlocales'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/availablechapterlocales.json'
content_hash: 'sha256:f8409aff7f13f80b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# availableChapterLocales

<sub>Type Property</sub>

The locales of an asset’s chapter metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var availableChapterLocales: AVAsyncProperty<Root, [Locale]> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading chapter metadata

- [loadChapterMetadataGroups(withTitleLocale:containingItemsWithCommonKeys:)](<../avasset/loadchaptermetadatagroups(withtitlelocale_containingitemswithcommonkeys_).md>) — Loads chapter metadata that contains the specified title locale and common keys.
- [- loadChapterMetadataGroupsBestMatchingPreferredLanguages:completionHandler:](<../avasset/loadchaptermetadatagroups(bestmatchingpreferredlanguages_completionhandler_).md>) — Loads chapter metadata with a locale that best matches the list of preferred languages.
