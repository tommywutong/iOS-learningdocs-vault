---
title: 'mediaSelectionOptions(from:with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediaselectiongroup/mediaselectionoptions(from:with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/mediaselectionoptions(from:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectiongroup/mediaselectionoptions%28from%3Awith%3A%29.json'
content_hash: 'sha256:355308cad7a819e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionGroup](../avmediaselectiongroup.md)

# mediaSelectionOptions(from:with:)

<sub>Type Method</sub>

Returns an array containing the media selection options from a given array that match the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], with locale: Locale) -> [AVMediaSelectionOption]
```

## Parameters

- `mediaSelectionOptions` — An array of [AVMediaSelectionOption](../avmediaselectionoption.md) objects to be filtered.

- `locale` — The locale that must be matched for a media selection option to be copied to the output array.

## Return Value

An array containing the media selection options from `array` that match the `locale`.

## See Also

### Filtering selection options

- [+ playableMediaSelectionOptionsFromArray:](<playablemediaselectionoptions(from_).md>) — Returns an array containing the media selection options from a given array that are playable.
- [+ mediaSelectionOptionsFromArray:withMediaCharacteristics:](<mediaselectionoptions(from_withmediacharacteristics_).md>) — Returns an array containing the media selection options from a given array that match given media characteristics.
- [+ mediaSelectionOptionsFromArray:withoutMediaCharacteristics:](<mediaselectionoptions(from_withoutmediacharacteristics_).md>) — Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [+ mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<mediaselectionoptions(from_filteredandsortedaccordingtopreferredlanguages_).md>) — Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.
- [customMediaSelectionScheme](custommediaselectionscheme.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
