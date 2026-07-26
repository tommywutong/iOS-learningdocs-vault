---
title: AVCaptureAudioDataOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiodataoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiodataoutput.json'
content_hash: 'sha256:35cbfc303e5ae35b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureAudioDataOutput

<sub>Class</sub>

A capture output that records audio and provides access to audio sample buffers as they are recorded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureAudioDataOutput
```

## Relationships

- **Inherits From**: [AVCaptureOutput](avcaptureoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an audio capture output

- [- init](<avcaptureaudiodataoutput/init().md>) — Creates an instance of audio data output.

### Configuring audio capture

- [audioSettings](avcaptureaudiodataoutput/audiosettings.md) — The settings used to decode or re-encode audio before it’s output.
- [- recommendedAudioSettingsForAssetWriterWithOutputFileType:](<avcaptureaudiodataoutput/recommendedaudiosettingsforassetwriter(writingto_).md>) — Specifies the recommended settings for use with an `AVAssetWriterInput`.
- [spatialAudioChannelLayoutTag](avcaptureaudiodataoutput/spatialaudiochannellayouttag.md) — The audio channel layout tag of the audio sample buffers produced by the audio data output.

### Receiving captured audio data

- [- setSampleBufferDelegate:queue:](<avcaptureaudiodataoutput/setsamplebufferdelegate(__queue_).md>) — Sets the delegate that will accept captured buffers and the dispatch queue on which the delegate will be called.
- [sampleBufferDelegate](avcaptureaudiodataoutput/samplebufferdelegate.md) — The capture object’s delegate.
- [sampleBufferCallbackQueue](avcaptureaudiodataoutput/samplebuffercallbackqueue.md) — The queue on which delegate callbacks are invoked
- [AVCaptureAudioDataOutputSampleBufferDelegate](avcaptureaudiodataoutputsamplebufferdelegate.md) — Methods for receiving audio sample data from an audio capture.

## See Also

### Stream capture

- [Capturing Spatial Audio in your iOS app](capturing-spatial-audio-in-your-ios-app.md) — Enhance your app’s audio recording capabilities by supporting Spatial Audio capture.
- [AVCaptureVideoDataOutput](avcapturevideodataoutput.md) — A capture output that records video and provides access to video frames for processing.
- [AVCaptureSpatialAudioMetadataSampleGenerator](avcapturespatialaudiometadatasamplegenerator.md) — An interface for generating a spatial audio timed metadata sample.
