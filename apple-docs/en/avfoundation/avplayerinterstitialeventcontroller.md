---
title: AVPlayerInterstitialEventController
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventcontroller
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventcontroller.json'
content_hash: 'sha256:e59a74e59559bf1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerInterstitialEventController

<sub>Class</sub>

An object that schedules interstitial events for items played by the primary player.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerInterstitialEventController
```

## Overview

This class is a subclass of [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md) that you use to manage the schedule of interstitial events to present during playback of primary content.

> [!important] Important
> Creating an event controller and setting a schedule causes playback to ignore interstitial events present in the source media.

## Relationships

- **Inherits From**: [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an event controller

- [- initWithPrimaryPlayer:](<avplayerinterstitialeventcontroller/init(primaryplayer_).md>) — Creates an event controller with a player item.

### Configuring the event schedule

- [events](avplayerinterstitialeventcontroller/events.md) — The current schedule of interstitial events.
- [- cancelCurrentEventWithResumptionOffset:](<avplayerinterstitialeventcontroller/cancelcurrentevent(withresumptionoffset_).md>) — Cancels the playback of all currently playing and scheduled interstitial events, and resumes playback of primary content.
- [- skipCurrentEvent](<avplayerinterstitialeventcontroller/skipcurrentevent().md>) — Causes the playback of the currently playing interstital event to be abandoned.

### Accessing strings

- [localizedStringsBundle](avplayerinterstitialeventcontroller/localizedstringsbundle.md) — The bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.
- [localizedStringsTableName](avplayerinterstitialeventcontroller/localizedstringstablename.md) — The name of the table in the bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.

## See Also

### Interstitials

- [Providing an integrated view of your timeline when playing HLS interstitials](providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md) — Go beyond simple ad insertion with point and fill occupancy HLS interstitials.
- [AVPlayerInterstitialEvent](avplayerinterstitialevent.md) — An object that provides instructions for how a player presents interstitial content.
- [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md) — An object that monitors the scheduling and progress of interstitial events.
- [AVPlayerInterstitialEventMonitorScheduleRequestErrorKey](avplayerinterstitialeventmonitorschedulerequesterrorkey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSError. Absent if the request succeeded
- [AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey](avplayerinterstitialeventmonitorschedulerequestidentifierkey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSString.
- [AVPlayerInterstitialEventMonitorScheduleRequestResponseKey](avplayerinterstitialeventmonitorschedulerequestresponsekey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSData. Absent if the request failed.
- [AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md) — An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.
