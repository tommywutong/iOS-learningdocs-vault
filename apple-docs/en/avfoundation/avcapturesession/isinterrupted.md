---
title: isInterrupted
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/isinterrupted
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/isinterrupted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/isinterrupted.json'
content_hash: 'sha256:0e29852934c9556d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# isInterrupted

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture session is in an interrupted state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isInterrupted: Bool { get }
```

## Discussion

This property is key-value observable.

## See Also

### Observing session state

- [running](isrunning.md) — A Boolean value that indicates whether the capture session is in a running state.
- [AVCaptureSessionDidStartRunningNotification](didstartrunningnotification.md) — A notification the system posts when a capture session starts.
- [AVCaptureSessionDidStopRunningNotification](didstoprunningnotification.md) — A notification the system posts when a capture session stops.
- [AVCaptureSessionWasInterruptedNotification](wasinterruptednotification.md) — A notification the system posts when it interrupts a capture session.
- [AVCaptureSessionInterruptionEndedNotification](interruptionendednotification.md) — A notification the system posts when an interruption to a capture session finishes.
- [AVCaptureSessionRuntimeErrorNotification](runtimeerrornotification.md) — A notification the system posts when an error occurs during a capture session.
