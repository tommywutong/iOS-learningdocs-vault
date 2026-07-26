---
title: audioMixInputParameters
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutableaudiomixinputparameters/audiomixinputparameters
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/audiomixinputparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutableaudiomixinputparameters/audiomixinputparameters.json'
content_hash: 'sha256:0f24eda5002c8506'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableAudioMixInputParameters](../avmutableaudiomixinputparameters.md)

# audioMixInputParameters

<sub>Type Method</sub>

Creates a mutable input parameters object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) audioMixInputParameters;
```

## Return Value

A mutable input parameters object with no volume ramps and [trackID](trackid.md) initialized to [kCMPersistentTrackID_Invalid](../../coremedia/kcmpersistenttrackid_invalid.md).

## See Also

### Creating input parameters

- [+ audioMixInputParametersWithTrack:](<init(track_).md>) — Creates a mutable input parameters object for a given track.
