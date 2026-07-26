---
title: AVAssetVariantQualifier
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariantqualifier
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariantqualifier.json'
content_hash: 'sha256:f43d5ff862736d2c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetVariantQualifier

<sub>Class</sub>

An object that represents an HTTP Live Streaming asset variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAssetVariantQualifier
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a variant qualifier

- [+ assetVariantQualifierWithVariant:](<avassetvariantqualifier/init(variant_).md>) — Creates a variant qualifier with an asset variant.
- [AVAssetVariant](avassetvariant.md) — An object that represents a bit rate variant.
- [+ assetVariantQualifierWithPredicate:](<avassetvariantqualifier/init(predicate_).md>) — Creates a variant qualifier with a predicate.

### Building predicates

- [+ predicateForAudioSampleRate:mediaSelectionOption:operatorType:](<avassetvariantqualifier/predicate(foraudiosamplerate_mediaselectionoption_operatortype_).md>) — Creates a predicate for audio sample rate.
- [+ predicateForAudioSampleRate:operatorType:](<avassetvariantqualifier/predicate(foraudiosamplerate_operatortype_).md>) — Creates a NSPredicate for audio sample rate which can be used with other NSPredicates to express variant preferences.
- [+ predicateForBinauralAudio:](<avassetvariantqualifier/predicate(forbinauralaudio_).md>) — Creates a NSPredicate for binaural which can be used with other NSPredicates to express variant preferences.
- [+ predicateForBinauralAudio:mediaSelectionOption:](<avassetvariantqualifier/predicate(forbinauralaudio_mediaselectionoption_).md>) — Creates a predicate for binaural audio.
- [+ predicateForChannelCount:mediaSelectionOption:operatorType:](<avassetvariantqualifier/predicate(forchannelcount_mediaselectionoption_operatortype_).md>) — Creates a predicate with a channel count, media selection option, and operator type.
- [+ predicateForChannelCount:operatorType:](<avassetvariantqualifier/predicate(forchannelcount_operatortype_).md>) — Creates a NSPredicate for audio channel count which can be used with other NSPredicates to express variant preferences.
- [+ predicateForDownmixAudio:](<avassetvariantqualifier/predicate(fordownmixaudio_).md>) — Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [+ predicateForDownmixAudio:mediaSelectionOption:](<avassetvariantqualifier/predicate(fordownmixaudio_mediaselectionoption_).md>) — Creates a predicate for downmix audio.
- [+ predicateForImmersiveAudio:](<avassetvariantqualifier/predicate(forimmersiveaudio_).md>) — Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [+ predicateForImmersiveAudio:mediaSelectionOption:](<avassetvariantqualifier/predicate(forimmersiveaudio_mediaselectionoption_).md>) — Creates a predicate for immersive audio.
- [+ predicateForPresentationHeight:operatorType:](<avassetvariantqualifier/predicate(forpresentationheight_operatortype_).md>) — Creates a predicate with a height and operator type.
- [+ predicateForPresentationWidth:operatorType:](<avassetvariantqualifier/predicate(forpresentationwidth_operatortype_).md>) — Creates a predicate with a width and operator type.

## See Also

### Accessing configuration details

- [variantQualifiers](avassetdownloadcontentconfiguration/variantqualifiers.md) — The variant qualifiers for this configuration.
- [mediaSelections](avassetdownloadcontentconfiguration/mediaselections.md) — The media selections of an asset that a task downloads.
