---
title: 'startRecording(to:recordingDelegate:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturefileoutput/startrecording(to:recordingdelegate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/startrecording(to:recordingdelegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/startrecording%28to%3Arecordingdelegate%3A%29.json'
content_hash: 'sha256:0840e3f98c6ae93c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# startRecording(to:recordingDelegate:)

<sub>Instance Method</sub>

Starts recording media to the specified output URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func startRecording(to outputFileURL: URL, recordingDelegate delegate: any AVCaptureFileOutputRecordingDelegate)
```

## Parameters

- `outputFileURL` — An object specifying the output file URL. This method raises an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if the argument isn’t a valid file URL.

- `delegate` — A delegate object that’s notified of changes to the recording state.

## Discussion

A failure occurs if you attempt to record to a URL where a file exists. To overwrite the content, delete the old file before calling this method.

In macOS, calling this method from within the [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) method guarantees that the first samples written to the new file are those passed to the delegate method.

When you stop recording by calling [- stopRecording](<stoprecording().md>), by changing files using this method, or because of an error, the framework writes any remaining file data in the background. Therefore, for the system to notify you upon completion, you must adopt the [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<../avcapturefileoutputrecordingdelegate/fileoutput(__didfinishrecordingto_from_error_).md>) delegate method. The recording delegate can also optionally implement methods that inform it when the output object starts writing data, when it pauses or resumes recording, and when it’s about to finish recording.

In macOS, you don’t need to call [- stopRecording](<stoprecording().md>) before calling this method while another recording is in progress. If you call this method while the output object is recording, the framework preserves media samples between the old file and the new file. In iOS, to avoid any errors, you must call [- stopRecording](<stoprecording().md>) before calling this method again.

> [!note] Note
> Don’t call this method when capturing audio using [AVCaptureAudioFileOutput](../avcaptureaudiofileoutput.md). Use the [- startRecordingToOutputFileURL:outputFileType:recordingDelegate:](<../avcaptureaudiofileoutput/startrecording(to_outputfiletype_recordingdelegate_).md>) method instead.

## See Also

### Managing recording

- [- stopRecording](<stoprecording().md>) — Tells the receiver to stop recording to the current file.
- [- pauseRecording](<pauserecording().md>) — Pauses recording to the current output file.
- [- resumeRecording](<resumerecording().md>) — Resumes recording to the current output file after it was previously paused using [- pauseRecording](<pauserecording().md>).
