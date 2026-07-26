---
title: AVCaptureFileOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput.json'
content_hash: 'sha256:2d936565acbada7d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureFileOutput

<sub>Class</sub>

The abstract superclass for capture outputs that can record captured data to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureFileOutput
```

## Relationships

- **Inherits From**: [AVCaptureOutput](avcaptureoutput.md)

- **Inherited By**: [AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md), [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting file output properties

- [delegate](avcapturefileoutput/delegate.md) — The delegate object for the capture file output.
- [maxRecordedDuration](avcapturefileoutput/maxrecordedduration.md) — The longest duration allowed for the recording.
- [maxRecordedFileSize](avcapturefileoutput/maxrecordedfilesize.md) — The maximum size, in bytes, of the data that should be recorded by the receiver.
- [minFreeDiskSpaceLimit](avcapturefileoutput/minfreediskspacelimit.md) — The minimum amount of free space, in bytes, required for recording to continue on a given volume.
- [outputFileURL](avcapturefileoutput/outputfileurl.md) — The URL to which output is directed.
- [recordedDuration](avcapturefileoutput/recordedduration.md) — Indicates the duration of the media recorded to the current output file.
- [recordedFileSize](avcapturefileoutput/recordedfilesize.md) — Indicates the size, in bytes, of the data recorded to the current output file.
- [recording](avcapturefileoutput/isrecording.md) — Indicates whether recording is in progress.
- [recordingPaused](avcapturefileoutput/isrecordingpaused.md) — Indicates whether recording to the current output file is paused.

### Managing recording

- [- startRecordingToOutputFileURL:recordingDelegate:](<avcapturefileoutput/startrecording(to_recordingdelegate_).md>) — Starts recording media to the specified output URL.
- [- stopRecording](<avcapturefileoutput/stoprecording().md>) — Tells the receiver to stop recording to the current file.
- [- pauseRecording](<avcapturefileoutput/pauserecording().md>) — Pauses recording to the current output file.
- [- resumeRecording](<avcapturefileoutput/resumerecording().md>) — Resumes recording to the current output file after it was previously paused using [- pauseRecording](<avcapturefileoutput/pauserecording().md>).

## See Also

### File capture

- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md) — Change the default format for capturing movie files.
- [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) — A capture output that records video and audio to a QuickTime movie file.
- [AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md) — A capture output that records audio and saves the recorded audio to a file.
- [AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md) — Methods for monitoring or controlling the output of a media file capture.
- [AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md) — Methods for responding to events that occur while recording captured media to a file.
