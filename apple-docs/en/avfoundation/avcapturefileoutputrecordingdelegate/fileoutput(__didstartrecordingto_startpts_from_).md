---
title: 'fileOutput(_:didStartRecordingTo:startPTS:from:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, macOS 15.2+, tvOS 18.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didstartrecordingto:startpts:from:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didstartrecordingto:startpts:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput%28_%3Adidstartrecordingto%3Astartpts%3Afrom%3A%29.json'
content_hash: 'sha256:b40e201da5e40f2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutputRecordingDelegate](../avcapturefileoutputrecordingdelegate.md)

# fileOutput(_:didStartRecordingTo:startPTS:from:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func fileOutput(_ output: AVCaptureFileOutput, didStartRecordingTo fileURL: URL, startPTS: CMTime, from connections: [AVCaptureConnection])
```

## Parameters

- `output` — The capture file output that started writing the file.

- `fileURL` — The file URL of the file that is being written.

- `startPTS` — The timestamp of the first buffer written to the file, synced with AVCaptureSession.synchronizationClock

- `connections` — An array of AVCaptureConnection objects attached to the file output that provided the data that is being written to the file.

## Discussion

Informs the delegate when the output has started writing to a file.

This method is called when the file output has started writing data to a file. If an error condition prevents any data from being written, this method may not be called. captureOutput:willFinishRecordingToOutputFileAtURL:fromConnections:error: and captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error: will always be called, even if no data is written.

If this method is implemented, the alternative delegate callback -captureOutput:didStartRecordingToOutputFileAtURL:fromConnections will not be called.

Clients should not assume that this method will be called on a specific thread, and should also try to make this method as efficient as possible.

## See Also

### Delegate methods

- [- captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didstartrecordingto_from_).md>) — Informs the delegate when the output has started writing to a file.
- [- captureOutput:willFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__willfinishrecordingto_from_error_).md>) — Informs the delegate when the output will stop writing new samples to a file.
- [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<fileoutput(__didfinishrecordingto_from_error_).md>) — Informs the delegate when all pending data has been written to an output file.
- [- captureOutput:didPauseRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didpauserecordingto_from_).md>) — Called whenever the output is recording to a file and successfully pauses the recording at the request of a client.
- [- captureOutput:didResumeRecordingToOutputFileAtURL:fromConnections:](<fileoutput(__didresumerecordingto_from_).md>) — Called whenever the output, at the request of the client, successfully resumes a file recording that was paused.
