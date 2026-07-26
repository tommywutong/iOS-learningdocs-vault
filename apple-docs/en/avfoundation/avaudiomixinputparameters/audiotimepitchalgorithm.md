---
title: audioTimePitchAlgorithm
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avaudiomixinputparameters/audiotimepitchalgorithm
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/audiotimepitchalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiomixinputparameters/audiotimepitchalgorithm.json'
content_hash: 'sha256:c70e75785aec7538'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAudioMixInputParameters](../avaudiomixinputparameters.md)

# audioTimePitchAlgorithm

<sub>Instance Property</sub>

The processing algorithm used to manage audio pitch for scaled audio edits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm? { get }
```

## Discussion

The supported constants are defined in Time Pitch Algorithm Settings. An [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) will be raised if this property is set to a value other than the defined constants.

## See Also

### Getting the time pitch algorithm setting

- [AVAudioTimePitchAlgorithm](../avaudiotimepitchalgorithm.md) — An algorithm used to set the audio pitch as the rate changes.
