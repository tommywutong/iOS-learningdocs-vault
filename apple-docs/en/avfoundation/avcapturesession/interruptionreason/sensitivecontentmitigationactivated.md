---
title: AVCaptureSession.InterruptionReason.sensitiveContentMitigationActivated
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/interruptionreason/sensitivecontentmitigationactivated
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/sensitivecontentmitigationactivated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/interruptionreason/sensitivecontentmitigationactivated.json'
content_hash: 'sha256:de80c42e45eca1ef'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureSession](../../avcapturesession.md) · [InterruptionReason](../interruptionreason.md)

# AVCaptureSession.InterruptionReason.sensitiveContentMitigationActivated

<sub>Case</sub>

An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [AVCaptureDeviceInput](../../avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case sensitiveContentMitigationActivated
```

## See Also

### Constants

- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableInBackground](videodevicenotavailableinbackground.md) — An interruption caused by the app being sent to the background while using a camera.
- [AVCaptureSessionInterruptionReasonAudioDeviceInUseByAnotherClient](audiodeviceinusebyanotherclient.md) — An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSessionInterruptionReasonVideoDeviceInUseByAnotherClient](videodeviceinusebyanotherclient.md) — An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableWithMultipleForegroundApps](videodevicenotavailablewithmultipleforegroundapps.md) — An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableDueToSystemPressure](videodevicenotavailableduetosystempressure.md) — An interruption due to system pressure, such as thermal duress.
