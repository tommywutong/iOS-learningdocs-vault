---
title: 'predicate(forBinauralAudio:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.5+, iPadOS 18.5+, Mac Catalyst 18.5+, macOS 15.5+, tvOS 18.5+, visionOS 2.5+, watchOS 11.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetvariantqualifier/predicate(forbinauralaudio:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(forbinauralaudio:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariantqualifier/predicate%28forbinauralaudio%3A%29.json'
content_hash: 'sha256:492a495d2499d997'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariantQualifier](../avassetvariantqualifier.md)

# predicate(forBinauralAudio:)

<sub>Type Method</sub>

Creates a NSPredicate for binaural which can be used with other NSPredicates to express variant preferences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func predicate(forBinauralAudio isBinauralAudio: Bool) -> NSPredicate
```

## See Also

### Building predicates

- [+ predicateForAudioSampleRate:mediaSelectionOption:operatorType:](<predicate(foraudiosamplerate_mediaselectionoption_operatortype_).md>) — Creates a predicate for audio sample rate.
- [+ predicateForAudioSampleRate:operatorType:](<predicate(foraudiosamplerate_operatortype_).md>) — Creates a NSPredicate for audio sample rate which can be used with other NSPredicates to express variant preferences.
- [+ predicateForBinauralAudio:mediaSelectionOption:](<predicate(forbinauralaudio_mediaselectionoption_).md>) — Creates a predicate for binaural audio.
- [+ predicateForChannelCount:mediaSelectionOption:operatorType:](<predicate(forchannelcount_mediaselectionoption_operatortype_).md>) — Creates a predicate with a channel count, media selection option, and operator type.
- [+ predicateForChannelCount:operatorType:](<predicate(forchannelcount_operatortype_).md>) — Creates a NSPredicate for audio channel count which can be used with other NSPredicates to express variant preferences.
- [+ predicateForDownmixAudio:](<predicate(fordownmixaudio_).md>) — Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [+ predicateForDownmixAudio:mediaSelectionOption:](<predicate(fordownmixaudio_mediaselectionoption_).md>) — Creates a predicate for downmix audio.
- [+ predicateForImmersiveAudio:](<predicate(forimmersiveaudio_).md>) — Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [+ predicateForImmersiveAudio:mediaSelectionOption:](<predicate(forimmersiveaudio_mediaselectionoption_).md>) — Creates a predicate for immersive audio.
- [+ predicateForPresentationHeight:operatorType:](<predicate(forpresentationheight_operatortype_).md>) — Creates a predicate with a height and operator type.
- [+ predicateForPresentationWidth:operatorType:](<predicate(forpresentationwidth_operatortype_).md>) — Creates a predicate with a width and operator type.
