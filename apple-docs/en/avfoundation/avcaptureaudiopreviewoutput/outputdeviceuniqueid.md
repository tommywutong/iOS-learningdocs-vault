---
title: outputDeviceUniqueID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiopreviewoutput/outputdeviceuniqueid
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiopreviewoutput/outputdeviceuniqueid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiopreviewoutput/outputdeviceuniqueid.json'
content_hash: 'sha256:c1017445857eb76e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioPreviewOutput](../avcaptureaudiopreviewoutput.md)

# outputDeviceUniqueID

<sub>Instance Property</sub>

The unique identifier of the Core Audio output device to use for audio preview.

<sub>macOS</sub>

```swift
var outputDeviceUniqueID: String? { get set }
```

## Discussion

Set the value to the unique identifier of the audio output device, or `nil` to use default system output.

## See Also

### Configuring the output

- [volume](volume.md) — The output volume of the audio preview.
