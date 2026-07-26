---
title: 'fileOutput(_:willFinishRecordingTo:from:error:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:willfinishrecordingto:from:error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:willfinishrecordingto:from:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput%28_%3Awillfinishrecordingto%3Afrom%3Aerror%3A%29.json'
content_hash: 'sha256:e690b9144abef301'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutputRecordingDelegate](../avcapturefileoutputrecordingdelegate.md)

# fileOutput(_:willFinishRecordingTo:from:error:)

<sub>Instance Method</sub>

Informs the delegate when the output will stop writing new samples to a file.

<sub>macOS</sub>

```swift
optional func fileOutput(_ output: AVCaptureFileOutput, willFinishRecordingTo fileURL: URL, from connections: [AVCaptureConnection], error: (any Error)?)
```

## Parameters

- `output` — The capture file output that will finish writing the file.

- `fileURL` — The file URL of the file that is being written.

- `connections` — An array of [AVCaptureConnection](../avcaptureconnection.md) objects attached to the file output that provided the data that is being written to the file.

- `error` — An error describing what caused the file to stop recording, or `nil` if there was no error.

## Discussion

This method is called when the file output will stop recording new samples to the file at [outputFileURL](../avcapturefileoutput/outputfileurl.md), either because [- startRecordingToOutputFileURL:recordingDelegate:](<../avcapturefileoutput/startrecording(to_recordingdelegate_).md>) or [- stopRecording](<../avcapturefileoutput/stoprecording().md>) was called, or because an error (described by the error parameter) occurred (if no error occurred, the error parameter is `nil`).

This method is always called for each recording request, even if no data is successfully written to the file.

You should not assume that this method will be called on a specific thread, and should make this method as efficient as possible.

## See Also

### Delegate methods

- [- captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didstartrecordingto_from_).md>) — Informs the delegate when the output has started writing to a file.
- [- captureOutput:didStartRecordingToOutputFileAtURL:startPTS:fromConnections:](<fileoutput(__didstartrecordingto_startpts_from_).md>)
- [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__didfinishrecordingto_from_error_).md>) — Informs the delegate when all pending data has been written to an output file.
- [- captureOutput:didPauseRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didpauserecordingto_from_).md>) — Called whenever the output is recording to a file and successfully pauses the recording at the request of a client.
- [- captureOutput:didResumeRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didresumerecordingto_from_).md>) — Called whenever the output, at the request of the client, successfully resumes a file recording that was paused.
