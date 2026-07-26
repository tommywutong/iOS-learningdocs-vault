---
title: 'predicate(forBinauralAudio:mediaSelectionOption:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetvariantqualifier/predicate(forbinauralaudio:mediaselectionoption:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(forbinauralaudio:mediaselectionoption:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariantqualifier/predicate%28forbinauralaudio%3Amediaselectionoption%3A%29.json'
content_hash: 'sha256:3fc75684c8fc3b4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariantQualifier](../avassetvariantqualifier.md)

# predicate(forBinauralAudio:mediaSelectionOption:)

<sub>Type Method</sub>

Creates a predicate for binaural audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func predicate(forBinauralAudio isBinauralAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate
```

## Parameters

- `isBinauralAudio` — A Boolean value that indicates the binaural state to use in the predicate equation.

- `mediaSelectionOption` — The media selection option for the variant.

## Return Value

A predicate object that you use to to create an [AVAssetVariantQualifier](../avassetvariantqualifier.md).

## Discussion

Use the returned value, along with other predicates, to express variant preferences.

## See Also

### Building predicates

- [+ predicateForAudioSampleRate:mediaSelectionOption:operatorType:](<predicate(foraudiosamplerate_mediaselectionoption_operatortype_).md>) — Creates a predicate for audio sample rate.
- [+ predicateForAudioSampleRate:operatorType:](<predicate(foraudiosamplerate_operatortype_).md>) — Creates a NSPredicate for audio sample rate which can be used with other NSPredicates to express variant preferences.
- [+ predicateForBinauralAudio:](<predicate(forbinauralaudio_).md>) — Creates a NSPredicate for binaural which can be used with other NSPredicates to express variant preferences.
- [+ predicateForChannelCount:mediaSelectionOption:operatorType:](<predicate(forchannelcount_mediaselectionoption_operatortype_).md>) — Creates a predicate with a channel count, media selection option, and operator type.
- [+ predicateForChannelCount:operatorType:](<predicate(forchannelcount_operatortype_).md>) — Creates a NSPredicate for audio channel count which can be used with other NSPredicates to express variant preferences.
- [+ predicateForDownmixAudio:](<predicate(fordownmixaudio_).md>) — Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [+ predicateForDownmixAudio:mediaSelectionOption:](<predicate(fordownmixaudio_mediaselectionoption_).md>) — Creates a predicate for downmix audio.
- [+ predicateForImmersiveAudio:](<predicate(forimmersiveaudio_).md>) — Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [+ predicateForImmersiveAudio:mediaSelectionOption:](<predicate(forimmersiveaudio_mediaselectionoption_).md>) — Creates a predicate for immersive audio.
- [+ predicateForPresentationHeight:operatorType:](<predicate(forpresentationheight_operatortype_).md>) — Creates a predicate with a height and operator type.
- [+ predicateForPresentationWidth:operatorType:](<predicate(forpresentationwidth_operatortype_).md>) — Creates a predicate with a width and operator type.
