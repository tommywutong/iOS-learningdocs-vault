---
title: volume
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiopreviewoutput/volume
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiopreviewoutput/volume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiopreviewoutput/volume.json'
content_hash: 'sha256:f18e7e1f5a067818'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioPreviewOutput](../avcaptureaudiopreviewoutput.md)

# volume

<sub>Instance Property</sub>

The output volume of the audio preview.

<sub>macOS</sub>

```swift
var volume: Float { get set }
```

## Discussion

A value of `1.0` indicates maximum volume, and a value of `0.0` mutes the audio preview.

## See Also

### Configuring the output

- [outputDeviceUniqueID](outputdeviceuniqueid.md) — The unique identifier of the Core Audio output device to use for audio preview.
