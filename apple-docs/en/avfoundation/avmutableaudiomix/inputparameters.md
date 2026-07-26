---
title: inputParameters
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutableaudiomix/inputparameters
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutableaudiomix/inputparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutableaudiomix/inputparameters.json'
content_hash: 'sha256:f13dfa542e8bff0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableAudioMix](../avmutableaudiomix.md)

# inputParameters

<sub>Instance Property</sub>

An array of input parameters for the mix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var inputParameters: [AVAudioMixInputParameters] { get set }
```

## Discussion

The array contains instances of [AVAudioMixInputParameters](../avaudiomixinputparameters.md). You don’t need an instance for each audio track that contributes to the mix. By default, the system processes audio for those tracks without an associated `AVAudioMixInputParameters` instance.

> [!warning] Warning
> Specifying multiple `AVAudioMixInputParameters` for the same track has undefined behavior. Use only one instance per track in an audio mix.
