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
doc_path: /documentation/avfoundation/avaudiomix/inputparameters
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiomix/inputparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiomix/inputparameters.json'
content_hash: 'sha256:89dcea30ff362f0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAudioMix](../avaudiomix.md)

# inputParameters

<sub>Instance Property</sub>

An array of input parameters for the mix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var inputParameters: [AVAudioMixInputParameters] { get }
```

## Discussion

The array contains instances of [AVAudioMixInputParameters](../avaudiomixinputparameters.md).

> [!note] Note
> An instance of [AVAudioMixInputParameters](../avaudiomixinputparameters.md) isn’t required for each audio track that contributes to the mix. Audio for those without associated `AVAudioMixInputParameters` objects are included in the mix and processed according to the default behavior.
