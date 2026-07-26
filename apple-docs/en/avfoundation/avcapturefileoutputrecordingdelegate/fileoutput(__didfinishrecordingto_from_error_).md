---
title: 'fileOutput(_:didFinishRecordingTo:from:error:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didfinishrecordingto:from:error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didfinishrecordingto:from:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput%28_%3Adidfinishrecordingto%3Afrom%3Aerror%3A%29.json'
content_hash: 'sha256:5b231240e46c5c84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutputRecordingDelegate](../avcapturefileoutputrecordingdelegate.md)

# fileOutput(_:didFinishRecordingTo:from:error:)

<sub>Instance Method</sub>

Informs the delegate when all pending data has been written to an output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func fileOutput(_ output: AVCaptureFileOutput, didFinishRecordingTo outputFileURL: URL, from connections: [AVCaptureConnection], error: (any Error)?)
```

## Parameters

- `output` — The capture file output that has finished writing the file.

- `outputFileURL` — The file URL of the file that is being written.

- `connections` — An array of [AVCaptureConnection](../avcaptureconnection.md) objects attached to the file output that provided the data that is being written to the file.

- `error` — If the file was not written successfully, an error object that describes the problem; otherwise `nil`.

## Discussion

This method is called whenever a file is finished. If the file was forced to be finished due to an error, the error is described in the error parameter—otherwise, the error parameter is `nil`.

This method is called when the file output has finished writing all data to a file whose recording was stopped, either because [- startRecordingToOutputFileURL:recordingDelegate:](<../avcapturefileoutput/startrecording(to_recordingdelegate_).md>) or [- stopRecording](<../avcapturefileoutput/stoprecording().md>) were called, or because an error (described by the error parameter) occurred (if no error occurred, the error parameter is `nil`).

This method is always called for each recording request, even if no data is successfully written to the file.

You should not assume that this method will be called on a specific thread.

## See Also

### Delegate methods

- [- captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didstartrecordingto_from_).md>) — Informs the delegate when the output has started writing to a file.
- [- captureOutput:didStartRecordingToOutputFileAtURL:startPTS:fromConnections:](<fileoutput(__didstartrecordingto_startpts_from_).md>)
- [- captureOutput:willFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__willfinishrecordingto_from_error_).md>) — Informs the delegate when the output will stop writing new samples to a file.
- [- captureOutput:didPauseRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didpauserecordingto_from_).md>) — Called whenever the output is recording to a file and successfully pauses the recording at the request of a client.
- [- captureOutput:didResumeRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didresumerecordingto_from_).md>) — Called whenever the output, at the request of the client, successfully resumes a file recording that was paused.
