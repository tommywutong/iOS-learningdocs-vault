---
title: startRunning()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/startrunning()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/startrunning()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/startrunning%28%29.json'
content_hash: 'sha256:53a82c1127dbfb68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# startRunning()

<sub>Instance Method</sub>

Starts the flow of data through the capture pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startRunning()
```

## Discussion

Call this method to start the flow of data from the capture session’s inputs to its outputs. This method is synchronous and blocks until the session starts running or it fails, which it reports by posting an [AVCaptureSessionRuntimeErrorNotification](runtimeerrornotification.md) notification.

## See Also

### Managing the session life cycle

- [- stopRunning](<stoprunning().md>) — Stops the flow of data through the capture pipeline.
