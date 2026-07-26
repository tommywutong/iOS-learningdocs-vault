---
title: AVMetricPlayerItemPlaybackSummaryEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricplayeritemplaybacksummaryevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricplayeritemplaybacksummaryevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricplayeritemplaybacksummaryevent.json'
content_hash: 'sha256:2d9872937f05dc8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricPlayerItemPlaybackSummaryEvent

<sub>Class</sub>

An event that represents the combined metrics for the entire playback session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetricPlayerItemPlaybackSummaryEvent
```

## Relationships

- **Inherits From**: [AVMetricEvent](avmetricevent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the event

- [errorEvent](avmetricplayeritemplaybacksummaryevent/errorevent.md)
- [mediaResourceRequestCount](avmetricplayeritemplaybacksummaryevent/mediaresourcerequestcount.md)
- [playbackDuration](avmetricplayeritemplaybacksummaryevent/playbackduration.md)
- [recoverableErrorCount](avmetricplayeritemplaybacksummaryevent/recoverableerrorcount.md)
- [stallCount](avmetricplayeritemplaybacksummaryevent/stallcount.md)
- [timeSpentInInitialStartup](avmetricplayeritemplaybacksummaryevent/timespentininitialstartup.md)
- [timeSpentRecoveringFromStall](avmetricplayeritemplaybacksummaryevent/timespentrecoveringfromstall.md)
- [timeWeightedAverageBitrate](avmetricplayeritemplaybacksummaryevent/timeweightedaveragebitrate.md)
- [timeWeightedPeakBitrate](avmetricplayeritemplaybacksummaryevent/timeweightedpeakbitrate.md)
- [variantSwitchCount](avmetricplayeritemplaybacksummaryevent/variantswitchcount.md)

## See Also

### Transport control

- [AVMetricPlayerItemRateChangeEvent](avmetricplayeritemratechangeevent.md) — An event that represents when the playback rate changes.
- [AVMetricPlayerItemSeekDidCompleteEvent](avmetricplayeritemseekdidcompleteevent.md) — An event that represents when the playback seek completes.
- [AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md) — An event that represents when a playback seek occurs.
