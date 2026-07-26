---
title: interruptionEndedNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/interruptionendednotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionendednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/interruptionendednotification.json'
content_hash: 'sha256:fbd2faf719562980'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# interruptionEndedNotification

<sub>Type Property</sub>

A notification the system posts when an interruption to a capture session finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let interruptionEndedNotification: NSNotification.Name
```

## See Also

### Observing session state

- [running](isrunning.md) — A Boolean value that indicates whether the capture session is in a running state.
- [interrupted](isinterrupted.md) — A Boolean value that indicates whether the capture session is in an interrupted state.
- [AVCaptureSessionDidStartRunningNotification](didstartrunningnotification.md) — A notification the system posts when a capture session starts.
- [AVCaptureSessionDidStopRunningNotification](didstoprunningnotification.md) — A notification the system posts when a capture session stops.
- [AVCaptureSessionWasInterruptedNotification](wasinterruptednotification.md) — A notification the system posts when it interrupts a capture session.
- [AVCaptureSessionRuntimeErrorNotification](runtimeerrornotification.md) — A notification the system posts when an error occurs during a capture session.
