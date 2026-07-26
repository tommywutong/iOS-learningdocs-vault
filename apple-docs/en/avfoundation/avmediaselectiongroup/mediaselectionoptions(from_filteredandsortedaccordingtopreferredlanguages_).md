---
title: 'mediaSelectionOptions(from:filteredAndSortedAccordingToPreferredLanguages:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediaselectiongroup/mediaselectionoptions(from:filteredandsortedaccordingtopreferredlanguages:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/mediaselectionoptions(from:filteredandsortedaccordingtopreferredlanguages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectiongroup/mediaselectionoptions%28from%3Afilteredandsortedaccordingtopreferredlanguages%3A%29.json'
content_hash: 'sha256:536425b4da7b53f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionGroup](../avmediaselectiongroup.md)

# mediaSelectionOptions(from:filteredAndSortedAccordingToPreferredLanguages:)

<sub>Type Method</sub>

Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMediaSelectionOption]
```

## Parameters

- `mediaSelectionOptions` — An array of [AVMediaSelectionOption](../avmediaselectionoption.md) objects to be filtered and sorted.

- `preferredLanguages` — An array of [NSString](../../foundation/nsstring.md) objects, each of which contains a canonicalized IETF BCP 47 language identifier. The strings should be sorted in order of preference, with the string corresponding to the most preferred language as the first element in the array. Typically, you retrieve these strings using the [preferredLanguages](../../foundation/nslocale/preferredlanguages.md) class method of the [NSLocale](../../foundation/nslocale.md) class.

## Return Value

An array of [AVMediaSelectionOption](../avmediaselectionoption.md) objects that match one of the languages in the `preferredLanguages` parameter. The objects in this array are sorted based on the language each one matches, with objects matching the most preferred language first in the array.

## See Also

### Filtering selection options

- [+ playableMediaSelectionOptionsFromArray:](<playablemediaselectionoptions(from_).md>) — Returns an array containing the media selection options from a given array that are playable.
- [+ mediaSelectionOptionsFromArray:withLocale:](<mediaselectionoptions(from_with_).md>) — Returns an array containing the media selection options from a given array that match the specified locale.
- [+ mediaSelectionOptionsFromArray:withMediaCharacteristics:](<mediaselectionoptions(from_withmediacharacteristics_).md>) — Returns an array containing the media selection options from a given array that match given media characteristics.
- [+ mediaSelectionOptionsFromArray:withoutMediaCharacteristics:](<mediaselectionoptions(from_withoutmediacharacteristics_).md>) — Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [customMediaSelectionScheme](custommediaselectionscheme.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
