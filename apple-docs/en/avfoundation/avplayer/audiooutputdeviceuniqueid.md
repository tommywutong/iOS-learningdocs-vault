---
title: audioOutputDeviceUniqueID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/audiooutputdeviceuniqueid
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/audiooutputdeviceuniqueid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/audiooutputdeviceuniqueid.json'
content_hash: 'sha256:58f4ec55913fa4c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# audioOutputDeviceUniqueID

<sub>Instance Property</sub>

Specifies the unique ID of the Core Audio output device used to play audio.

<sub>macOS</sub>

```swift
nonisolated var audioOutputDeviceUniqueID: String? { get set }
```

## Discussion

The default value of this property is `nil`, indicating that the default audio output device is used. Otherwise the value of this property is a string containing the unique ID of the Core Audio output device to be used for audio output.

Core Audio’s [kAudioDevicePropertyDeviceUID](../../coreaudio/kaudiodevicepropertydeviceuid.md) is a suitable source of audio output device unique IDs.

## See Also

### Configuring audio and video devices

- [preferredVideoDecoderGPURegistryID](preferredvideodecodergpuregistryid.md) — The registry identifier for the GPU used for video decoding.
