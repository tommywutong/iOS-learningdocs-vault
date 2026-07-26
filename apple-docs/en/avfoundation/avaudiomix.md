---
title: AVAudioMix
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avaudiomix
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiomix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiomix.json'
content_hash: 'sha256:c863269d25947ef3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAudioMix

<sub>Class</sub>

An object that manages the input parameters for mixing audio tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAudioMix
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMutableAudioMix](avmutableaudiomix.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Retrieving input parameters

- [inputParameters](avaudiomix/inputparameters.md) — An array of input parameters for the mix.

## See Also

### Mixing

- [AVAudioMixInputParameters](avaudiomixinputparameters.md) — An object that represents the parameters that you apply when adding an audio track to a mix.
- [AVAudioMixInputParametersTrackID](avaudiomixinputparameterstrackid.md) — Special value for the trackID property of AVAudioMixInputParameters. _(beta)_
- [AVMutableAudioMix](avmutableaudiomix.md) — An object that manages the input parameters for mixing audio tracks.
- [AVMutableAudioMixInputParameters](avmutableaudiomixinputparameters.md) — The parameters you use when adding an audio track to a mix.
