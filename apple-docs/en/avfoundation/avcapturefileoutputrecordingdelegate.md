---
title: AVCaptureFileOutputRecordingDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutputrecordingdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutputrecordingdelegate.json'
content_hash: 'sha256:ddaf22156e922896'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureFileOutputRecordingDelegate

<sub>Protocol</sub>

Methods for responding to events that occur while recording captured media to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVCaptureFileOutputRecordingDelegate : NSObjectProtocol
```

## Overview

Defines an interface for delegates of [AVCaptureFileOutput](avcapturefileoutput.md) to respond to events that occur in the process of recording a single file.

The delegate of an `AVCaptureFileOutput` object must adopt the `AVCaptureFileOutputRecordingDelegate` protocol.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Delegate methods

- [- captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:](<avcapturefileoutputrecordingdelegate/fileoutput(__didstartrecordingto_from_).md>) — Informs the delegate when the output has started writing to a file.
- [- captureOutput:didStartRecordingToOutputFileAtURL:startPTS:fromConnections:](<avcapturefileoutputrecordingdelegate/fileoutput(__didstartrecordingto_startpts_from_).md>)
- [- captureOutput:willFinishRecordingToOutputFileAtURL:fromConnections:error:](<avcapturefileoutputrecordingdelegate/fileoutput(__willfinishrecordingto_from_error_).md>) — Informs the delegate when the output will stop writing new samples to a file.
- [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<avcapturefileoutputrecordingdelegate/fileoutput(__didfinishrecordingto_from_error_).md>) — Informs the delegate when all pending data has been written to an output file.
- [- captureOutput:didPauseRecordingToOutputFileAtURL:fromConnections:](<avcapturefileoutputrecordingdelegate/fileoutput(__didpauserecordingto_from_).md>) — Called whenever the output is recording to a file and successfully pauses the recording at the request of a client.
- [- captureOutput:didResumeRecordingToOutputFileAtURL:fromConnections:](<avcapturefileoutputrecordingdelegate/fileoutput(__didresumerecordingto_from_).md>) — Called whenever the output, at the request of the client, successfully resumes a file recording that was paused.

## See Also

### File capture

- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md) — Change the default format for capturing movie files.
- [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) — A capture output that records video and audio to a QuickTime movie file.
- [AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md) — A capture output that records audio and saves the recorded audio to a file.
- [AVCaptureFileOutput](avcapturefileoutput.md) — The abstract superclass for capture outputs that can record captured data to a file.
- [AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md) — Methods for monitoring or controlling the output of a media file capture.
