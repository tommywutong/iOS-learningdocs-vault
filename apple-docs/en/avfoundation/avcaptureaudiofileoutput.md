---
title: AVCaptureAudioFileOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiofileoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiofileoutput.json'
content_hash: 'sha256:a93a9e0c285d50b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureAudioFileOutput

<sub>Class</sub>

A capture output that records audio and saves the recorded audio to a file.

<sub>macOS</sub>

```swift
class AVCaptureAudioFileOutput
```

## Overview

`AVCaptureAudioFileOutput` implements the complete file recording interface declared by [AVCaptureFileOutput](avcapturefileoutput.md) for writing media data to audio files. In addition, you can configure options specific to the audio file formats, including writing metadata collections to each file and specifying audio encoding options. `AVCaptureAudioFileOutput` does not, however, support [- startRecordingToOutputFileURL:recordingDelegate:](<avcapturefileoutput/startrecording(to_recordingdelegate_).md>)—use [- startRecordingToOutputFileURL:outputFileType:recordingDelegate:](<avcaptureaudiofileoutput/startrecording(to_outputfiletype_recordingdelegate_).md>) instead.

## Relationships

- **Inherits From**: [AVCaptureFileOutput](avcapturefileoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Discovering supported types

- [+ availableOutputFileTypes](<avcaptureaudiofileoutput/availableoutputfiletypes().md>) — Returns an array containing UTIs identifying the file types `AVCaptureAudioFileOutput` can write.

### Starting a recording

- [- startRecordingToOutputFileURL:outputFileType:recordingDelegate:](<avcaptureaudiofileoutput/startrecording(to_outputfiletype_recordingdelegate_).md>) — Tells the receiver to start recording to a new file of the specified format, and specifies a delegate that will be notified when recording is finished.

### Configuring output

- [audioSettings](avcaptureaudiofileoutput/audiosettings.md) — The settings used to decode or re-encode audio before it is output by the receiver.
- [metadata](avcaptureaudiofileoutput/metadata.md) — A collection of metadata to be written to the receiver’s output files.

### Creating output

- [- init](<avcaptureaudiofileoutput/init().md>) — Creates a new audio file output.

## See Also

### File capture

- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md) — Change the default format for capturing movie files.
- [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) — A capture output that records video and audio to a QuickTime movie file.
- [AVCaptureFileOutput](avcapturefileoutput.md) — The abstract superclass for capture outputs that can record captured data to a file.
- [AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md) — Methods for monitoring or controlling the output of a media file capture.
- [AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md) — Methods for responding to events that occur while recording captured media to a file.
