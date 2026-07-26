---
title: AVCaptureSession.InterruptionReason
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/interruptionreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/interruptionreason.json'
content_hash: 'sha256:7026b00d3695ba32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# AVCaptureSession.InterruptionReason

<sub>Enumeration</sub>

Constants identifying the reason a capture session was interrupted, found in an [AVCaptureSessionWasInterruptedNotification](wasinterruptednotification.md) user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum InterruptionReason
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableInBackground](interruptionreason/videodevicenotavailableinbackground.md) — An interruption caused by the app being sent to the background while using a camera.
- [AVCaptureSessionInterruptionReasonAudioDeviceInUseByAnotherClient](interruptionreason/audiodeviceinusebyanotherclient.md) — An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSessionInterruptionReasonVideoDeviceInUseByAnotherClient](interruptionreason/videodeviceinusebyanotherclient.md) — An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableWithMultipleForegroundApps](interruptionreason/videodevicenotavailablewithmultipleforegroundapps.md) — An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableDueToSystemPressure](interruptionreason/videodevicenotavailableduetosystempressure.md) — An interruption due to system pressure, such as thermal duress.
- [AVCaptureSessionInterruptionReasonSensitiveContentMitigationActivated](interruptionreason/sensitivecontentmitigationactivated.md) — An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [AVCaptureDeviceInput](../avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.

### Initializers

- [init(rawValue:)](<interruptionreason/init(rawvalue_).md>)

## See Also

### User-infomation keys

- [AVCaptureSessionInterruptionSystemPressureStateKey](../avcapturesessioninterruptionsystempressurestatekey.md) — A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
- [AVCaptureSessionInterruptionReasonKey](../avcapturesessioninterruptionreasonkey.md) — Key to retrieve information about a capture interruption from a [AVCaptureSessionWasInterruptedNotification](wasinterruptednotification.md) user info dictionary.
