---
title: didStopRunningNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/didstoprunningnotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/didstoprunningnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/didstoprunningnotification.json'
content_hash: 'sha256:09047ca5ebf603ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# didStopRunningNotification

<sub>Type Property</sub>

A notification the system posts when a capture session stops.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let didStopRunningNotification: NSNotification.Name
```

## See Also

### Observing session state

- [running](isrunning.md) — A Boolean value that indicates whether the capture session is in a running state.
- [interrupted](isinterrupted.md) — A Boolean value that indicates whether the capture session is in an interrupted state.
- [AVCaptureSessionDidStartRunningNotification](didstartrunningnotification.md) — A notification the system posts when a capture session starts.
- [AVCaptureSessionWasInterruptedNotification](wasinterruptednotification.md) — A notification the system posts when it interrupts a capture session.
- [AVCaptureSessionInterruptionEndedNotification](interruptionendednotification.md) — A notification the system posts when an interruption to a capture session finishes.
- [AVCaptureSessionRuntimeErrorNotification](runtimeerrornotification.md) — A notification the system posts when an error occurs during a capture session.
