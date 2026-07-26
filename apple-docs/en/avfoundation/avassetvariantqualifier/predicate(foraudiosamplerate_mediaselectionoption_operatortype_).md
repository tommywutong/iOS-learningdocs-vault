---
title: 'predicate(forAudioSampleRate:mediaSelectionOption:operatorType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetvariantqualifier/predicate(foraudiosamplerate:mediaselectionoption:operatortype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(foraudiosamplerate:mediaselectionoption:operatortype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariantqualifier/predicate%28foraudiosamplerate%3Amediaselectionoption%3Aoperatortype%3A%29.json'
content_hash: 'sha256:b9102bf3702cd041'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariantQualifier](../avassetvariantqualifier.md)

# predicate(forAudioSampleRate:mediaSelectionOption:operatorType:)

<sub>Type Method</sub>

Creates a predicate for audio sample rate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func predicate(forAudioSampleRate sampleRate: Double, mediaSelectionOption: AVMediaSelectionOption?, operatorType: NSComparisonPredicate.Operator) -> NSPredicate
```

## Parameters

- `sampleRate` — The specified sample rate to match.

- `mediaSelectionOption` — The audio media selection option under consideration.

- `operatorType` — The operator type.

## See Also

### Building predicates

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
- [+ predicateForPresentationWidth:operatorType:](<predicate(forpresentationwidth_operatortype_).md>) — Creates a predicate with a width and operator type.
