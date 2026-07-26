---
title: AVCaptureSpatialAudioMetadataSampleGenerator
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator.json'
content_hash: 'sha256:5f08ec9dc7b89df9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSpatialAudioMetadataSampleGenerator

<sub>Class</sub>

An interface for generating a spatial audio timed metadata sample.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class AVCaptureSpatialAudioMetadataSampleGenerator
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Analyzing audio samples

- [- analyzeAudioSample:](<avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(__).md>) — Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [- newTimedMetadataSampleBufferAndResetAnalyzer](<avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer().md>) — Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [timedMetadataSampleBufferFormatDescription](avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription.md) — Returns the format description of the sample buffer returned from the [- newTimedMetadataSampleBufferAndResetAnalyzer](<avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer().md>) method.
- [- resetAnalyzer](<avcapturespatialaudiometadatasamplegenerator/resetanalyzer().md>) — Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.

## See Also

### Stream capture

- [Capturing Spatial Audio in your iOS app](capturing-spatial-audio-in-your-ios-app.md) — Enhance your app’s audio recording capabilities by supporting Spatial Audio capture.
- [AVCaptureVideoDataOutput](avcapturevideodataoutput.md) — A capture output that records video and provides access to video frames for processing.
- [AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md) — A capture output that records audio and provides access to audio sample buffers as they are recorded.
