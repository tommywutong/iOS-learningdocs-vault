---
title: runtimeErrorNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/runtimeerrornotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/runtimeerrornotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/runtimeerrornotification.json'
content_hash: 'sha256:509ae3ac3033415f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# runtimeErrorNotification

<sub>Type Property</sub>

A notification the system posts when an error occurs during a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let runtimeErrorNotification: NSNotification.Name
```

## Discussion

Retrieve the underlying error from the notification’s user information dictionary using the key [AVCaptureSessionErrorKey](../avcapturesessionerrorkey.md).

## Topics

### User info keys

- [AVCaptureSessionErrorKey](../avcapturesessionerrorkey.md) — Key to retrieve the error object from a [AVCaptureSessionRuntimeErrorNotification](runtimeerrornotification.md) user info dictionary.

## See Also

### Observing session state

- [running](isrunning.md) — A Boolean value that indicates whether the capture session is in a running state.
- [interrupted](isinterrupted.md) — A Boolean value that indicates whether the capture session is in an interrupted state.
- [AVCaptureSessionDidStartRunningNotification](didstartrunningnotification.md) — A notification the system posts when a capture session starts.
- [AVCaptureSessionDidStopRunningNotification](didstoprunningnotification.md) — A notification the system posts when a capture session stops.
- [AVCaptureSessionWasInterruptedNotification](wasinterruptednotification.md) — A notification the system posts when it interrupts a capture session.
- [AVCaptureSessionInterruptionEndedNotification](interruptionendednotification.md) — A notification the system posts when an interruption to a capture session finishes.
