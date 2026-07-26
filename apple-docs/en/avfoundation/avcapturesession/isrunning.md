---
title: isRunning
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/isrunning
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/isrunning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/isrunning.json'
content_hash: 'sha256:9d3b224b742ec64b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# isRunning

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture session is in a running state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isRunning: Bool { get }
```

## Discussion

This property is key-value observable.

## See Also

### Observing session state

- [interrupted](isinterrupted.md) — A Boolean value that indicates whether the capture session is in an interrupted state.
- [AVCaptureSessionDidStartRunningNotification](didstartrunningnotification.md) — A notification the system posts when a capture session starts.
- [AVCaptureSessionDidStopRunningNotification](didstoprunningnotification.md) — A notification the system posts when a capture session stops.
- [AVCaptureSessionWasInterruptedNotification](wasinterruptednotification.md) — A notification the system posts when it interrupts a capture session.
- [AVCaptureSessionInterruptionEndedNotification](interruptionendednotification.md) — A notification the system posts when an interruption to a capture session finishes.
- [AVCaptureSessionRuntimeErrorNotification](runtimeerrornotification.md) — A notification the system posts when an error occurs during a capture session.
