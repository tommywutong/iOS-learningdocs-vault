---
title: pauseRecording()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 10.7+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput/pauserecording()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/pauserecording()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/pauserecording%28%29.json'
content_hash: 'sha256:b7390f2fda7ac3e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# pauseRecording()

<sub>Instance Method</sub>

Pauses recording to the current output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func pauseRecording()
```

## Discussion

This method causes the receiver to stop writing captured samples to the current output file returned by [outputFileURL](outputfileurl.md), but leaves the file open so that samples can be written to it in the future, if [- resumeRecording](<resumerecording().md>) is called. This allows you to record multiple media segments that are not contiguous in time to a single file.

In macOS, if this method is called within the captureOutput:didOutputSampleBuffer:fromConnection: delegate method, the last samples written to the current file are guaranteed to be those that were output immediately before those in the sample buffer passed to that method.

## See Also

### Related Documentation

- [recordingPaused](isrecordingpaused.md) — Indicates whether recording to the current output file is paused.

### Managing recording

- [- startRecordingToOutputFileURL:recordingDelegate:](<startrecording(to_recordingdelegate_).md>) — Starts recording media to the specified output URL.
- [- stopRecording](<stoprecording().md>) — Tells the receiver to stop recording to the current file.
- [- resumeRecording](<resumerecording().md>) — Resumes recording to the current output file after it was previously paused using [- pauseRecording](<pauserecording().md>).
