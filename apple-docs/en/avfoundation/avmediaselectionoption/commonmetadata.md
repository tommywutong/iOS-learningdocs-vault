---
title: commonMetadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption/commonmetadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/commonmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/commonmetadata.json'
content_hash: 'sha256:320660dc3c112bbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# commonMetadata

<sub>Instance Property</sub>

An array of metadata items for each common metadata key for which a value is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var commonMetadata: [AVMetadataItem] { get }
```

## Discussion

You can filter the array of [AVMetadataItem](../avmetadataitem.md) objects according to locale using [+ metadataItemsFromArray:withLocale:](<../avmetadataitem/metadataitems(from_with_).md>), key using [+ metadataItemsFromArray:withKey:keySpace:](<../avmetadataitem/metadataitems(from_withkey_keyspace_).md>), or language using [+ metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<../avmetadataitem/metadataitems(from_filteredandsortedaccordingtopreferredlanguages_).md>).

Clients that are filtering media selection options by language should be prepared to handle cases in which the [extendedLanguageTag](extendedlanguagetag.md) property value is `nil`. Further, they should be prepared to handle cases in which an `extendedLanguageTag` is present but indicates that the language is “undetermined” (a language value of @“und”, as defined in ISO 639-2).

## See Also

### Managing metadata

- [availableMetadataFormats](availablemetadataformats.md) — The metadata formats that contain metadata associated with the option.
- [- metadataForFormat:](<metadata(forformat_).md>) — Returns an array of metadata items—one for each metadata item in the container of a given format.
