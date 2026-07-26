---
title: stopRecording()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput/stoprecording()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/stoprecording()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/stoprecording%28%29.json'
content_hash: 'sha256:2cdfec5cfcb7afe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# stopRecording()

<sub>Instance Method</sub>

Tells the receiver to stop recording to the current file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func stopRecording()
```

## Discussion

You can call this method when they want to stop recording new samples to the current file, and do not want to continue recording to another file. If you want to switch from one file to another, you should not call this method. Instead you should simply call [- startRecordingToOutputFileURL:recordingDelegate:](<startrecording(to_recordingdelegate_).md>) with the new file URL.

When recording is stopped either by calling this method, by changing files using [- startRecordingToOutputFileURL:recordingDelegate:](<startrecording(to_recordingdelegate_).md>), or because of an error, the remaining data that needs to be included to the file will be written in the background. Therefore, before using the file, you must wait until the delegate that was specified in [- startRecordingToOutputFileURL:recordingDelegate:](<startrecording(to_recordingdelegate_).md>) is notified when all data has been written to the file using the [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<../avcapturefileoutputrecordingdelegate/fileoutput(__didfinishrecordingto_from_error_).md>) method.

In macOS, if this method is called within the captureOutput:didOutputSampleBuffer:fromConnection: delegate method, the last samples written to the current file are guaranteed to be those that were output immediately before those in the sample buffer passed to that method.

## See Also

### Related Documentation

- [recording](isrecording.md) — Indicates whether recording is in progress.

### Managing recording

- [- startRecordingToOutputFileURL:recordingDelegate:](<startrecording(to_recordingdelegate_).md>) — Starts recording media to the specified output URL.
- [- pauseRecording](<pauserecording().md>) — Pauses recording to the current output file.
- [- resumeRecording](<resumerecording().md>) — Resumes recording to the current output file after it was previously paused using [- pauseRecording](<pauserecording().md>).
