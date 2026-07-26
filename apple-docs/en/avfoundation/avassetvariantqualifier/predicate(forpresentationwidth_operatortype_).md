---
title: 'predicate(forPresentationWidth:operatorType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetvariantqualifier/predicate(forpresentationwidth:operatortype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(forpresentationwidth:operatortype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariantqualifier/predicate%28forpresentationwidth%3Aoperatortype%3A%29.json'
content_hash: 'sha256:397fae489a272b2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariantQualifier](../avassetvariantqualifier.md)

# predicate(forPresentationWidth:operatorType:)

<sub>Type Method</sub>

Creates a predicate with a width and operator type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func predicate(forPresentationWidth width: CGFloat, operatorType: NSComparisonPredicate.Operator) -> NSPredicate
```

## Parameters

- `width` — The presentation width.

- `operatorType` — The predicate’s operator type.

## Return Value

A predicate object that you use to to create an [AVAssetVariantQualifier](../avassetvariantqualifier.md).

## See Also

### Building predicates

- [+ predicateForAudioSampleRate:mediaSelectionOption:operatorType:](<predicate(foraudiosamplerate_mediaselectionoption_operatortype_).md>) — Creates a predicate for audio sample rate.
- [+ predicateForAudioSampleRate:operatorType:](<predicate(foraudiosamplerate_operatortype_).md>) — Creates a NSPredicate for audio sample rate which can be used with other NSPredicates to express variant preferences.
- [+ predicateForBinauralAudio:](<predicate(forbinauralaudio_).md>) — Creates a NSPredicate for binaural which can be used with other NSPredicates to express variant preferences.
- [+ predicateForBinauralAudio:mediaSelectionOption:](<predicate(forbinauralaudio_mediaselectionoption_).md>) — Creates a predicate for binaural audio.
- [+ predicateForChannelCount:mediaSelectionOption:operatorType:](<predicate(forchannelcount_mediaselectionoption_operatortype_).md>) — Creates a predicate with a channel count, media selection option, and operator type.
- [+ predicateForChannelCount:operatorType:](<predicate(forchannelcount_operatortype_).md>) — Creates a NSPredicate for audio channel count which can be used with other NSPredicates to express variant preferences.
- [+ predicateForDownmixAudio:](<predicate(fordownmixaudio_).md>) — Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [+ predicateForDownmixAudio:mediaSelectionOption:](<predicate(fordownmixaudio_mediaselectionoption_).md>) — Creates a predicate for downmix audio.
- [+ predicateForImmersiveAudio:](<predicate(forimmersiveaudio_).md>) — Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [+ predicateForImmersiveAudio:mediaSelectionOption:](<predicate(forimmersiveaudio_mediaselectionoption_).md>) — Creates a predicate for immersive audio.
- [+ predicateForPresentationHeight:operatorType:](<predicate(forpresentationheight_operatortype_).md>) — Creates a predicate with a height and operator type.
