---
title: isRecordingPaused
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 10.7+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput/isrecordingpaused
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/isrecordingpaused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/isrecordingpaused.json'
content_hash: 'sha256:d1fd0fe043c78d98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# isRecordingPaused

<sub>Instance Property</sub>

Indicates whether recording to the current output file is paused.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isRecordingPaused: Bool { get }
```

## Discussion

This property indicates recording to the file returned by [outputFileURL](outputfileurl.md) has been previously paused using the [- pauseRecording](<pauserecording().md>) method. When a recording is paused, captured samples are not written to the output file, but new samples can be written to the same file in the future by calling [- resumeRecording](<resumerecording().md>).

## See Also

### Related Documentation

- [- pauseRecording](<pauserecording().md>) — Pauses recording to the current output file.
- [- stopRecording](<stoprecording().md>) — Tells the receiver to stop recording to the current file.

### Setting file output properties

- [delegate](delegate.md) — The delegate object for the capture file output.
- [maxRecordedDuration](maxrecordedduration.md) — The longest duration allowed for the recording.
- [maxRecordedFileSize](maxrecordedfilesize.md) — The maximum size, in bytes, of the data that should be recorded by the receiver.
- [minFreeDiskSpaceLimit](minfreediskspacelimit.md) — The minimum amount of free space, in bytes, required for recording to continue on a given volume.
- [outputFileURL](outputfileurl.md) — The URL to which output is directed.
- [recordedDuration](recordedduration.md) — Indicates the duration of the media recorded to the current output file.
- [recordedFileSize](recordedfilesize.md) — Indicates the size, in bytes, of the data recorded to the current output file.
- [recording](isrecording.md) — Indicates whether recording is in progress.
