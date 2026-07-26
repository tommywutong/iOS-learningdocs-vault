---
title: spatialAudioChannelLayoutTag
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiodataoutput/spatialaudiochannellayouttag
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/spatialaudiochannellayouttag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiodataoutput/spatialaudiochannellayouttag.json'
content_hash: 'sha256:8f2d93221ab29bf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md)

# spatialAudioChannelLayoutTag

<sub>Instance Property</sub>

The audio channel layout tag of the audio sample buffers produced by the audio data output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var spatialAudioChannelLayoutTag: AudioChannelLayoutTag { get set }
```

## Discussion

When you set your audio data output’s associated [multichannelAudioMode](../avcapturedeviceinput/multichannelaudiomode.md) property to `AVCaptureMultichannelAudioModeFirstOrderAmbisonics`, the [AVCaptureSession](../avcapturesession.md) allows up to two [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md) instances to be connected to the First-order Ambisonsics (FOA) input. If you connect a single [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md) instance, you must configure its [spatialAudioChannelLayoutTag](spatialaudiochannellayouttag.md) property to produce either four channels of FOA audio or two channels of Stereo audio. If you connect two [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md) instances, you must configure one to output four channels of FOA audio and the other to output two channels of Stereo audio.

Thus, when you set your associated [multichannelAudioMode](../avcapturedeviceinput/multichannelaudiomode.md) property to `AVCaptureMultichannelAudioModeFirstOrderAmbisonics`, you must set your connected [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md) instance’s [spatialAudioChannelLayoutTag](spatialaudiochannellayouttag.md) property to either `kAudioChannelLayoutTag_Stereo` for stereo, or `(kAudioChannelLayoutTag_HOA_ACN_SN3D | 4)` for FOA (see [AudioChannelLayoutTag](../../coreaudiotypes/audiochannellayouttag.md)). When you set your associated [multichannelAudioMode](../avcapturedeviceinput/multichannelaudiomode.md) to any other value, the [AVCaptureSession](../avcapturesession.md) only supports one [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md), and you may only set [spatialAudioChannelLayoutTag](spatialaudiochannellayouttag.md) to `kAudioChannelLayoutTag_Unknown` (the default value).

Your [AVCaptureSession](../avcapturesession.md) validates your app’s adherence to the the above rules when you call `AVCaptureSession/startRunning:` or [- commitConfiguration](<../avcapturesession/commitconfiguration().md>) and throws a `NSInvalidArgumentException` if necessary.

## See Also

### Configuring audio capture

- [audioSettings](audiosettings.md) — The settings used to decode or re-encode audio before it’s output.
- [- recommendedAudioSettingsForAssetWriterWithOutputFileType:](<recommendedaudiosettingsforassetwriter(writingto_).md>) — Specifies the recommended settings for use with an `AVAssetWriterInput`.
