---
title: AVCaptureSession.InterruptionReason.audioDeviceInUseByAnotherClient
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/interruptionreason/audiodeviceinusebyanotherclient
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/audiodeviceinusebyanotherclient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/interruptionreason/audiodeviceinusebyanotherclient.json'
content_hash: 'sha256:db4657ac3051e244'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureSession](../../avcapturesession.md) · [InterruptionReason](../interruptionreason.md)

# AVCaptureSession.InterruptionReason.audioDeviceInUseByAnotherClient

<sub>Case</sub>

An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case audioDeviceInUseByAnotherClient
```

## See Also

### Constants

- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableInBackground](videodevicenotavailableinbackground.md) — An interruption caused by the app being sent to the background while using a camera.
- [AVCaptureSessionInterruptionReasonVideoDeviceInUseByAnotherClient](videodeviceinusebyanotherclient.md) — An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableWithMultipleForegroundApps](videodevicenotavailablewithmultipleforegroundapps.md) — An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableDueToSystemPressure](videodevicenotavailableduetosystempressure.md) — An interruption due to system pressure, such as thermal duress.
- [AVCaptureSessionInterruptionReasonSensitiveContentMitigationActivated](sensitivecontentmitigationactivated.md) — An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [AVCaptureDeviceInput](../../avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.
