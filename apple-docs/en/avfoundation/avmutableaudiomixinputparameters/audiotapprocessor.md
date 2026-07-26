---
title: audioTapProcessor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutableaudiomixinputparameters/audiotapprocessor
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/audiotapprocessor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutableaudiomixinputparameters/audiotapprocessor.json'
content_hash: 'sha256:d78aa4a808b6ade9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableAudioMixInputParameters](../avmutableaudiomixinputparameters.md)

# audioTapProcessor

<sub>Instance Property</sub>

The audio processing tap associated with the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var audioTapProcessor: MTAudioProcessingTap? { get set }
```

## Discussion

You can use this property to associate an audio tap with the audio track. You can use the audio tap to access the audio data before it is played, read, or exported.
