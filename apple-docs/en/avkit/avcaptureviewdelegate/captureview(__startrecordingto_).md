---
title: 'captureView(_:startRecordingTo:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcaptureviewdelegate/captureview(_:startrecordingto:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureviewdelegate/captureview(_:startrecordingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureviewdelegate/captureview%28_%3Astartrecordingto%3A%29.json'
content_hash: 'sha256:3425da014dc816e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureViewDelegate](../avcaptureviewdelegate.md)

# captureView(_:startRecordingTo:)

<sub>Instance Method</sub>

Tells the delegate that the user has made a request to start a new recording.

<sub>macOS</sub>

```swift
func captureView(_ captureView: AVCaptureView, startRecordingTo fileOutput: AVCaptureFileOutput)
```

## Parameters

- `captureView` — The capture view.

- `fileOutput` — The capture file output.

## Discussion

If the capture file output is an instance of [AVCaptureMovieFileOutput](../../avfoundation/avcapturemoviefileoutput.md), you start recording by calling [startRecording(to:recordingDelegate:)](<../../avfoundation/avcapturefileoutput/startrecording(to_recordingdelegate_).md>) on the capture file output.
