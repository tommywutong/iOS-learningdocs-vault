---
title: 'fileOutput(_:didPauseRecordingTo:from:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 10.7+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didpauserecordingto:from:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didpauserecordingto:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput%28_%3Adidpauserecordingto%3Afrom%3A%29.json'
content_hash: 'sha256:f80415392dc4bb3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutputRecordingDelegate](../avcapturefileoutputrecordingdelegate.md)

# fileOutput(_:didPauseRecordingTo:from:)

<sub>Instance Method</sub>

Called whenever the output is recording to a file and successfully pauses the recording at the request of a client.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func fileOutput(_ output: AVCaptureFileOutput, didPauseRecordingTo fileURL: URL, from connections: [AVCaptureConnection])
```

## Parameters

- `output` — The capture file output that has paused its file recording.

- `fileURL` — The file URL of the file that is being written.

- `connections` — An array of [AVCaptureConnection](../avcaptureconnection.md) objects attached to the file output that provided the data that is being written to the file.

## Discussion

This method is called whenever a request to pause recording is actually respected.

It is safe for delegates to change what the file output is currently doing (starting a new file, for example) from within this method. If recording to a file is stopped, either manually or due to an error, this method is not guaranteed to be called, even if a previous call to `pauseRecording` was made.

You should not assume that this method will be called on a specific thread, and should make this method as efficient as possible.

## See Also

### Delegate methods

- [- captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didstartrecordingto_from_).md>) — Informs the delegate when the output has started writing to a file.
- [- captureOutput:didStartRecordingToOutputFileAtURL:startPTS:fromConnections:](<fileoutput(__didstartrecordingto_startpts_from_).md>)
- [- captureOutput:willFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__willfinishrecordingto_from_error_).md>) — Informs the delegate when the output will stop writing new samples to a file.
- [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__didfinishrecordingto_from_error_).md>) — Informs the delegate when all pending data has been written to an output file.
- [- captureOutput:didResumeRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didresumerecordingto_from_).md>) — Called whenever the output, at the request of the client, successfully resumes a file recording that was paused.
