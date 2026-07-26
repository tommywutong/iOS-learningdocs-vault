---
title: AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableinbackground
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableinbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableinbackground.json'
content_hash: 'sha256:cf9cff5ace803f98'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureSession](../../avcapturesession.md) · [InterruptionReason](../interruptionreason.md)

# AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground

<sub>Case</sub>

An interruption caused by the app being sent to the background while using a camera.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case videoDeviceNotAvailableInBackground
```

## Discussion

Camera usage is prohibited while in the background. If you attempt to start running a camera while in the background, the capture session sends an [AVCaptureSessionWasInterruptedNotification](../wasinterruptednotification.md) with this interruption reason. If you don’t explicitly call the [- stopRunning](<../stoprunning().md>) method, your [- startRunning](<../startrunning().md>) request is preserved, and when your app comes back to foreground, you receive [AVCaptureSessionInterruptionEndedNotification](../interruptionendednotification.md) and your session starts running.

## See Also

### Constants

- [AVCaptureSessionInterruptionReasonAudioDeviceInUseByAnotherClient](audiodeviceinusebyanotherclient.md) — An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSessionInterruptionReasonVideoDeviceInUseByAnotherClient](videodeviceinusebyanotherclient.md) — An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableWithMultipleForegroundApps](videodevicenotavailablewithmultipleforegroundapps.md) — An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableDueToSystemPressure](videodevicenotavailableduetosystempressure.md) — An interruption due to system pressure, such as thermal duress.
- [AVCaptureSessionInterruptionReasonSensitiveContentMitigationActivated](sensitivecontentmitigationactivated.md) — An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [AVCaptureDeviceInput](../../avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.
