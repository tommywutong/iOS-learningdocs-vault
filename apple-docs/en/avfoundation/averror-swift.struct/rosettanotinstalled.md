---
title: rosettaNotInstalled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/averror-swift.struct/rosettanotinstalled
source_url: 'https://developer.apple.com/documentation/avfoundation/averror-swift.struct/rosettanotinstalled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/averror-swift.struct/rosettanotinstalled.json'
content_hash: 'sha256:54b67f316659b00e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVError](../averror-swift.struct.md)

# rosettaNotInstalled

<sub>Type Property</sub>

The system doesn’t have Rosetta installed and can’t perform the requested operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var rosettaNotInstalled: AVError.Code { get }
```

## Discussion

Apple silicon devices can use Intel-only codecs and file parsers, but only if you’ve installed the Rosetta translation environment on the host system.

## See Also

### Error codes

- [Code](code.md) — An enumeration that defines the errors that framework operations can generate.
- [airPlayControllerRequiresInternet](airplaycontrollerrequiresinternet.md) — The AirPlay controller requires an internet connection to function.
- [airPlayReceiverRequiresInternet](airplayreceiverrequiresinternet.md) — The AirPlay receiver requires an internet connection to function.
- [airPlayReceiverTemporarilyUnavailable](airplayreceivertemporarilyunavailable.md) — An AirPlay receiver is temporarily unavailable.
- [applicationIsNotAuthorizedToUseDevice](applicationisnotauthorizedtousedevice.md) — The user denied this app permission to capture media.
- [applicationIsNotAuthorized](applicationisnotauthorized.md) — The app isn’t authorized to play media.
- [autoWhiteBalanceNotLocked](autowhitebalancenotlocked.md)
- [compositionTrackSegmentsNotContiguous](compositiontracksegmentsnotcontiguous.md) — The composition can’t add the source media because it contains gaps.
- [contentIsNotAuthorized](contentisnotauthorized.md) — The user isn’t authorized to play the media.
- [contentIsProtected](contentisprotected.md) — The app isn’t authorized to open the media.
- [contentIsUnavailable](contentisunavailable.md) — The captured content is unavailable.
- [contentKeyRequestCancelled](contentkeyrequestcancelled.md) — The app canceled a request to retrieve a content key.
- [contentNotUpdated](contentnotupdated.md) — The system couldn’t update the captured content.
- [createContentKeyRequestFailed](createcontentkeyrequestfailed.md) — The app couldn’t create a content key request.
- [decodeFailed](decodefailed.md) — The system failed to decode the media.
