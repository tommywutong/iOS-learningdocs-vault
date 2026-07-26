---
title: audioSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiofileoutput/audiosettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput/audiosettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiofileoutput/audiosettings.json'
content_hash: 'sha256:b142510673e5360a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioFileOutput](../avcaptureaudiofileoutput.md)

# audioSettings

<sub>Instance Property</sub>

The settings used to decode or re-encode audio before it is output by the receiver.

<sub>macOS</sub>

```swift
var audioSettings: [String : Any]? { get set }
```

## Discussion

The value of this property is a dictionary containing values for audio settings keys defined in `AVAudioSettings.h`. If you set the value of this property to `nil`, the output vends samples in their device native format.

## See Also

### Configuring output

- [metadata](metadata.md) — A collection of metadata to be written to the receiver’s output files.
