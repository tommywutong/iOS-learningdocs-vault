---
title: stopRunning()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/stoprunning()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/stoprunning()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/stoprunning%28%29.json'
content_hash: 'sha256:2d922ae18bd9a233'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# stopRunning()

<sub>Instance Method</sub>

Stops the flow of data through the capture pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func stopRunning()
```

## Discussion

Call this method to stop the flow of data from the inputs to the outputs connected to the capture session. This method is synchronous and blocks until the session stops running completely.

## See Also

### Managing the session life cycle

- [- startRunning](<startrunning().md>) — Starts the flow of data through the capture pipeline.
