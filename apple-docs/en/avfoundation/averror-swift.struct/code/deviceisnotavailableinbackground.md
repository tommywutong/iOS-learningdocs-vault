---
title: AVError.Code.deviceIsNotAvailableInBackground
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.3+（9.0 起废弃）, iPadOS 4.3+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/averror-swift.struct/code/deviceisnotavailableinbackground
source_url: 'https://developer.apple.com/documentation/avfoundation/averror-swift.struct/code/deviceisnotavailableinbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/averror-swift.struct/code/deviceisnotavailableinbackground.json'
content_hash: 'sha256:cbe9eb2b5e8c13ff'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVError](../../averror-swift.struct.md) · [Code](../code.md)

# AVError.Code.deviceIsNotAvailableInBackground

<sub>Case</sub>

You attempted to start a capture session in the background, which isn’t allowed in iOS.

> [!warning] Deprecated
> AVCaptureSession no longer produces an AVCaptureSessionRuntimeErrorNotification with this error. See AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableInBackground.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case deviceIsNotAvailableInBackground
```

## See Also

### Error codes

- [AVErrorAirPlayControllerRequiresInternet](airplaycontrollerrequiresinternet.md) — The AirPlay controller requires an internet connection to function.
- [AVErrorAirPlayReceiverRequiresInternet](airplayreceiverrequiresinternet.md) — The AirPlay receiver requires an internet connection to function.
- [AVErrorAirPlayReceiverTemporarilyUnavailable](airplayreceivertemporarilyunavailable.md) — An AirPlay receiver is temporarily unavailable.
- [AVErrorApplicationIsNotAuthorized](applicationisnotauthorized.md) — The app isn’t authorized to play media.
- [AVErrorApplicationIsNotAuthorizedToUseDevice](applicationisnotauthorizedtousedevice.md) — The user denied this app permission to capture media.
- [AVErrorAutoWhiteBalanceNotLocked](autowhitebalancenotlocked.md)
- [AVErrorCompositionTrackSegmentsNotContiguous](compositiontracksegmentsnotcontiguous.md) — The composition can’t add the source media because it contains gaps.
- [AVErrorContentIsNotAuthorized](contentisnotauthorized.md) — The user isn’t authorized to play the media.
- [AVErrorContentIsProtected](contentisprotected.md) — The app isn’t authorized to open the media.
- [AVErrorContentIsUnavailable](contentisunavailable.md) — The captured content is unavailable.
- [AVErrorContentKeyRequestCancelled](contentkeyrequestcancelled.md) — The app canceled a request to retrieve a content key.
- [AVErrorContentNotUpdated](contentnotupdated.md) — The system couldn’t update the captured content.
- [AVErrorCreateContentKeyRequestFailed](createcontentkeyrequestfailed.md) — The app couldn’t create a content key request.
- [AVErrorDecodeFailed](decodefailed.md) — The system failed to decode the media.
- [AVErrorDecoderNotFound](decodernotfound.md) — The system can’t find a suitable decoder for the media.
