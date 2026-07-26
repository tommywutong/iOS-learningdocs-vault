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
doc_path: /documentation/avfoundation/avaudiomixinputparameters/audiotapprocessor
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/audiotapprocessor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiomixinputparameters/audiotapprocessor.json'
content_hash: 'sha256:af1063fe50db202c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAudioMixInputParameters](../avaudiomixinputparameters.md)

# audioTapProcessor

<sub>Instance Property</sub>

The audio processing tap associated with the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var audioTapProcessor: MTAudioProcessingTap? { get }
```

## Discussion

You can use the audio tap to access the track’s audio data before it is played, read, or exported. This property is `nil` by default.

The process of setting up a tap requires the configuration of an instance of [AVMutableAudioMixInputParameters](../avmutableaudiomixinputparameters.md). If an instance of [AVMutableAudioMixInputParameters](../avmutableaudiomixinputparameters.md) is present in the [inputParameters](../avaudiomix/inputparameters.md) array of an [AVAudioMix](../avaudiomix.md), the results of mutating the [AVMutableAudioMixInputParameters](../avmutableaudiomixinputparameters.md) while the audio mix is in use are undefined
