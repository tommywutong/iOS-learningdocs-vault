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
doc_path: /documentation/avfoundation/avcaptureaudiodataoutput/audiosettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/audiosettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiodataoutput/audiosettings.json'
content_hash: 'sha256:106a917b08883a7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md)

# audioSettings

<sub>Instance Property</sub>

The settings used to decode or re-encode audio before it’s output.

<sub>macOS</sub>

```swift
var audioSettings: [String : Any]! { get set }
```

## Discussion

The value of this property is a dictionary containing values for audio settings keys defined in [Audio settings](../audio-settings.md).

If the value of this property is `nil`, samples are output in their device native format.

## See Also

### Configuring audio capture

- [- recommendedAudioSettingsForAssetWriterWithOutputFileType:](<recommendedaudiosettingsforassetwriter(writingto_).md>) — Specifies the recommended settings for use with an `AVAssetWriterInput`.
- [spatialAudioChannelLayoutTag](spatialaudiochannellayouttag.md) — The audio channel layout tag of the audio sample buffers produced by the audio data output.
