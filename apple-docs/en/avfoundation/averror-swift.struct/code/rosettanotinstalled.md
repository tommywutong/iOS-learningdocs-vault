---
title: AVError.Code.rosettaNotInstalled
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/averror-swift.struct/code/rosettanotinstalled
source_url: 'https://developer.apple.com/documentation/avfoundation/averror-swift.struct/code/rosettanotinstalled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/averror-swift.struct/code/rosettanotinstalled.json'
content_hash: 'sha256:f055401c75671015'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVError](../../averror-swift.struct.md) · [Code](../code.md)

# AVError.Code.rosettaNotInstalled

<sub>Case</sub>

The system doesn’t have Rosetta installed and can’t perform the requested operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case rosettaNotInstalled
```

## Discussion

Apple Silicon devices can use Intel-only codecs and file parsers, but only if you’ve installed Rosetta on the host system.

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
