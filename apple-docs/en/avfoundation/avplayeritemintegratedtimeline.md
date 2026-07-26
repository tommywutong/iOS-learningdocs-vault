---
title: AVPlayerItemIntegratedTimeline
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimeline
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline.json'
content_hash: 'sha256:799672dd56e478c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemIntegratedTimeline

<sub>Class</sub>

An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemIntegratedTimeline
```

## Overview

The timeline models all regions to traverse during playback. A player may not present portions of the primary item when exiting an interstitial event with a positive resumption offset.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting snapshots

- [currentSnapshot](avplayeritemintegratedtimeline/currentsnapshot.md) — An immutable representation of the timeline state at time of request.
- [AVPlayerItemIntegratedTimelineSnapshot](avplayeritemintegratedtimelinesnapshot.md) — An immutable representation of inspectable details of an integrated timeline object.
- [AVPlayerIntegratedTimelineSnapshotsOutOfSyncNotification](avplayeritemintegratedtimeline/snapshotsoutofsyncnotification.md) — A notification the system posts when the snapshot objects provided by this timeline become out of sync with the current timeline state.

### Inspecting the time and date

- [currentTime](avplayeritemintegratedtimeline/currenttime.md) — The current time on the integrated timeline.
- [currentDate](avplayeritemintegratedtimeline/currentdate.md) — The current date of playback.

### Seeking

- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<avplayeritemintegratedtimeline/seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Seeks to a particular time in the integrated time domain.
- [- seekToDate:completionHandler:](<avplayeritemintegratedtimeline/seek(to_completionhandler_).md>) — Seeks to a particular date in the integrated time domain.

### Observing time changes

- [periodicTimes(forInterval:)](<avplayeritemintegratedtimeline/periodictimes(forinterval_).md>) — Returns an asynchronous sequence of times periodically as playback progresses.
- [boundaryTimes(for:offsetsIntoSegment:)](<avplayeritemintegratedtimeline/boundarytimes(for_offsetsintosegment_).md>) — Returns an asynchronous sequence of times whenever playback reaches a segment time in the segment.
- [BoundaryTimes](avplayeritemintegratedtimeline/boundarytimes.md) — An asynchronous sequence of boundary time values.
- [PeriodicTimes](avplayeritemintegratedtimeline/periodictimes.md) — An asynchronous sequence of periodic time values.
- [AVPlayerItemIntegratedTimelineObserver](avplayeritemintegratedtimelineobserver.md) — A protocol for objects that perform timeline observations.

## See Also

### Interstitials

- [Providing an integrated view of your timeline when playing HLS interstitials](providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md) — Go beyond simple ad insertion with point and fill occupancy HLS interstitials.
- [AVPlayerInterstitialEvent](avplayerinterstitialevent.md) — An object that provides instructions for how a player presents interstitial content.
- [AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md) — An object that schedules interstitial events for items played by the primary player.
- [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md) — An object that monitors the scheduling and progress of interstitial events.
- [AVPlayerInterstitialEventMonitorScheduleRequestErrorKey](avplayerinterstitialeventmonitorschedulerequesterrorkey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSError. Absent if the request succeeded
- [AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey](avplayerinterstitialeventmonitorschedulerequestidentifierkey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSString.
- [AVPlayerInterstitialEventMonitorScheduleRequestResponseKey](avplayerinterstitialeventmonitorschedulerequestresponsekey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSData. Absent if the request failed.
