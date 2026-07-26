---
title: resumeRecording()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 10.7+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput/resumerecording()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/resumerecording()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/resumerecording%28%29.json'
content_hash: 'sha256:1a0cda5873c4eef6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# resumeRecording()

<sub>Instance Method</sub>

Resumes recording to the current output file after it was previously paused using [- pauseRecording](<pauserecording().md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func resumeRecording()
```

## Discussion

This method causes the receiver to resume writing captured samples to the current output file returned by [outputFileURL](outputfileurl.md), after recording was previously paused using [- pauseRecording](<pauserecording().md>). This allows you to record multiple media segments that are not contiguous in time to a single file.

In macOS, if this method is called within the captureOutput:didOutputSampleBuffer:fromConnection: delegate method, the first samples written to the current file are guaranteed to be those contained in the sample buffer passed to        that method.

## See Also

### Related Documentation

- [recordingPaused](isrecordingpaused.md) — Indicates whether recording to the current output file is paused.

### Managing recording

- [- startRecordingToOutputFileURL:recordingDelegate:](<startrecording(to_recordingdelegate_).md>) — Starts recording media to the specified output URL.
- [- stopRecording](<stoprecording().md>) — Tells the receiver to stop recording to the current file.
- [- pauseRecording](<pauserecording().md>) — Pauses recording to the current output file.
