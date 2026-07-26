---
title: 'fileOutput(_:didStartRecordingTo:from:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didstartrecordingto:from:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didstartrecordingto:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput%28_%3Adidstartrecordingto%3Afrom%3A%29.json'
content_hash: 'sha256:0ef4e821d9e83628'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutputRecordingDelegate](../avcapturefileoutputrecordingdelegate.md)

# fileOutput(_:didStartRecordingTo:from:)

<sub>Instance Method</sub>

Informs the delegate when the output has started writing to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func fileOutput(_ output: AVCaptureFileOutput, didStartRecordingTo fileURL: URL, from connections: [AVCaptureConnection])
```

## Parameters

- `output` — The capture file output that started writing the file.

- `fileURL` — The file URL of the file that is being written.

- `connections` — An array of [AVCaptureConnection](../avcaptureconnection.md) objects attached to the file output that provided the data that is being written to the file.

## Discussion

If an error condition prevents any data from being written, this method may not be called. [- captureOutput:willFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__willfinishrecordingto_from_error_).md>) and [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__didfinishrecordingto_from_error_).md>) are always called, even if no data is written.

You should not assume that this method will be called on a specific thread, and should make this method as efficient as possible.

## See Also

### Delegate methods

- [- captureOutput:didStartRecordingToOutputFileAtURL:startPTS:fromConnections:](<fileoutput(__didstartrecordingto_startpts_from_).md>)
- [- captureOutput:willFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__willfinishrecordingto_from_error_).md>) — Informs the delegate when the output will stop writing new samples to a file.
- [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__didfinishrecordingto_from_error_).md>) — Informs the delegate when all pending data has been written to an output file.
- [- captureOutput:didPauseRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didpauserecordingto_from_).md>) — Called whenever the output is recording to a file and successfully pauses the recording at the request of a client.
- [- captureOutput:didResumeRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didresumerecordingto_from_).md>) — Called whenever the output, at the request of the client, successfully resumes a file recording that was paused.
