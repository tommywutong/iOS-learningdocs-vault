---
title: wasInterruptedNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/wasinterruptednotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/wasinterruptednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/wasinterruptednotification.json'
content_hash: 'sha256:6284fc7f987ef0bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# wasInterruptedNotification

<sub>Type Property</sub>

A notification the system posts when it interrupts a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let wasInterruptedNotification: NSNotification.Name
```

## Discussion

Retrieve the underlying error from the notification’s user information dictionary using the key [AVCaptureSessionInterruptionReasonKey](../avcapturesessioninterruptionreasonkey.md).

## Topics

### User-infomation keys

- [AVCaptureSessionInterruptionSystemPressureStateKey](../avcapturesessioninterruptionsystempressurestatekey.md) — A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
- [AVCaptureSessionInterruptionReasonKey](../avcapturesessioninterruptionreasonkey.md) — Key to retrieve information about a capture interruption from a [AVCaptureSessionWasInterruptedNotification](wasinterruptednotification.md) user info dictionary.
- [InterruptionReason](interruptionreason.md) — Constants identifying the reason a capture session was interrupted, found in an [AVCaptureSessionWasInterruptedNotification](wasinterruptednotification.md) user info dictionary.

## See Also

### Observing session state

- [running](isrunning.md) — A Boolean value that indicates whether the capture session is in a running state.
- [interrupted](isinterrupted.md) — A Boolean value that indicates whether the capture session is in an interrupted state.
- [AVCaptureSessionDidStartRunningNotification](didstartrunningnotification.md) — A notification the system posts when a capture session starts.
- [AVCaptureSessionDidStopRunningNotification](didstoprunningnotification.md) — A notification the system posts when a capture session stops.
- [AVCaptureSessionInterruptionEndedNotification](interruptionendednotification.md) — A notification the system posts when an interruption to a capture session finishes.
- [AVCaptureSessionRuntimeErrorNotification](runtimeerrornotification.md) — A notification the system posts when an error occurs during a capture session.
