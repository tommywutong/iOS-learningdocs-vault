---
title: 'captureOutput(_:didOutput:from:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate/captureoutput%28_%3Adidoutput%3Afrom%3A%29.json'
content_hash: 'sha256:d918cd58c29dae3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioDataOutputSampleBufferDelegate](../avcaptureaudiodataoutputsamplebufferdelegate.md)

# captureOutput(_:didOutput:from:)

<sub>Instance Method</sub>

Notifies the delegate that a sample buffer was written.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection)
```

## Parameters

- `output` — The capture output object.

- `sampleBuffer` — The sample buffer that was output.

- `connection` — The connection.
