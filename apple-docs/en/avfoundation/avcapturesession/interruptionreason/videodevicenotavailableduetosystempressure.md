---
title: AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 11.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableduetosystempressure
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableduetosystempressure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableduetosystempressure.json'
content_hash: 'sha256:004d083a3f2563bc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureSession](../../avcapturesession.md) · [InterruptionReason](../interruptionreason.md)

# AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure

<sub>Case</sub>

An interruption due to system pressure, such as thermal duress.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case videoDeviceNotAvailableDueToSystemPressure
```

## See Also

### Constants

- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableInBackground](videodevicenotavailableinbackground.md) — An interruption caused by the app being sent to the background while using a camera.
- [AVCaptureSessionInterruptionReasonAudioDeviceInUseByAnotherClient](audiodeviceinusebyanotherclient.md) — An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSessionInterruptionReasonVideoDeviceInUseByAnotherClient](videodeviceinusebyanotherclient.md) — An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableWithMultipleForegroundApps](videodevicenotavailablewithmultipleforegroundapps.md) — An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSessionInterruptionReasonSensitiveContentMitigationActivated](sensitivecontentmitigationactivated.md) — An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [AVCaptureDeviceInput](../../avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.
