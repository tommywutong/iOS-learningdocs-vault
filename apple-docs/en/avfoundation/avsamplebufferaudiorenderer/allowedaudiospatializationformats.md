---
title: allowedAudioSpatializationFormats
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/allowedaudiospatializationformats
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/allowedaudiospatializationformats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/allowedaudiospatializationformats.json'
content_hash: 'sha256:dbc89c390c07154d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md)

# allowedAudioSpatializationFormats

<sub>Instance Property</sub>

The source audio channel layouts the audio renderer supports for spatialization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allowedAudioSpatializationFormats: AVAudioSpatializationFormats { get set }
```

## Discussion

The default property value is [AVAudioSpatializationFormatMultichannel](../avaudiospatializationformats/multichannel.md), which tells the player to spatialize any decodable multichannel layout. Setting the value to [AVAudioSpatializationFormatMonoStereoAndMultichannel](../avaudiospatializationformats/monostereoandmultichannel.md) tells the player to spatialize any decodable mono, stereo, or multichannel layout. When this property value is [AVAudioSpatializationFormatMonoAndStereo](../avaudiospatializationformats/monoandstereo.md) the player attempts to spatialize content tagged with a stereo channel layout (two-channel content with no layout specified as well as mono).

This property isn’t key-value observable.

> [!important] Important
> It’s incorrect to render binaural recordings with spatialization. Content tagged with a binaural channel layout ignores this property value.
