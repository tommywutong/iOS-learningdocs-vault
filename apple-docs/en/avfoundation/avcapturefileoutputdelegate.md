---
title: AVCaptureFileOutputDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutputdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutputdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutputdelegate.json'
content_hash: 'sha256:e682d7a1afb83bc6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureFileOutputDelegate

<sub>Protocol</sub>

Methods for monitoring or controlling the output of a media file capture.

<sub>macOS</sub>

```swift
protocol AVCaptureFileOutputDelegate : NSObjectProtocol
```

## Overview

The `AVCaptureFileOutputDelegate` protocol defines an interface for delegates of an [AVCaptureFileOutput](avcapturefileoutput.md) object to monitor and control recordings along exact sample boundaries.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Sample processing

- [- captureOutputShouldProvideSampleAccurateRecordingStart:](<avcapturefileoutputdelegate/fileoutputshouldprovidesampleaccuraterecordingstart(__).md>) — Allows a client to opt in to frame accurate recording in [- captureOutput:didOutputSampleBuffer:fromConnection:](<avcapturefileoutputdelegate/fileoutput(__didoutputsamplebuffer_from_).md>).
- [- captureOutput:didOutputSampleBuffer:fromConnection:](<avcapturefileoutputdelegate/fileoutput(__didoutputsamplebuffer_from_).md>) — Gives the delegate the opportunity to inspect samples as they are received by the output and start and stop recording at exact times.

## See Also

### File capture

- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md) — Change the default format for capturing movie files.
- [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) — A capture output that records video and audio to a QuickTime movie file.
- [AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md) — A capture output that records audio and saves the recorded audio to a file.
- [AVCaptureFileOutput](avcapturefileoutput.md) — The abstract superclass for capture outputs that can record captured data to a file.
- [AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md) — Methods for responding to events that occur while recording captured media to a file.
