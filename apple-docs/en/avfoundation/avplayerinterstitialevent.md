---
title: AVPlayerInterstitialEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent.json'
content_hash: 'sha256:09c35a5202c4fed0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerInterstitialEvent

<sub>Class</sub>

An object that provides instructions for how a player presents interstitial content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerInterstitialEvent
```

## Overview

An interstitial event defines a [date](avplayerinterstitialevent/date.md) or [time](avplayerinterstitialevent/time.md), on the timeline of its [primaryItem](avplayerinterstitialevent/primaryitem.md), at which playback of interstitial content begins. It specifies the alternative interstitial content to play as an array of one or more template player items. The system uses the configuration of the event’s [templateItems](avplayerinterstitialevent/templateitems.md) to build new player item instances to present the interstitial content.

Use [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md) to observe the scheduling and progress of interstitial events. If your app requires specifying the schedule of interstitial events, use [AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md) instead.

> [!note] Note
> [AVPlayerInterstitialEvent](avplayerinterstitialevent.md) was previously an immutable type. Starting in iOS 16, tvOS 16, macOS 13, and watchOS 9, it’s now a mutable type, which allows you to create and customize an event before setting it on an [AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an event

- [+ interstitialEventWithPrimaryItem:time:](<avplayerinterstitialevent/init(primaryitem_time_).md>) — Creates an interstitial event for the specified time.
- [+ interstitialEventWithPrimaryItem:date:](<avplayerinterstitialevent/init(primaryitem_date_).md>) — Creates an interstitial event for the specified date.
- [init(primaryItem:identifier:time:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:)](<avplayerinterstitialevent/init(primaryitem_identifier_time_templateitems_restrictions_resumptionoffset_playoutlimit_userdefinedattributes_).md>) — Creates an interstitial event, with user-defined attributes, for the specified time.
- [init(primaryItem:identifier:date:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:)](<avplayerinterstitialevent/init(primaryitem_identifier_date_templateitems_restrictions_resumptionoffset_playoutlimit_userdefinedattributes_).md>) — Creates an interstitial event, with user-defined attributes, for the specified date.

### Identifying events

- [identifier](avplayerinterstitialevent/identifier.md) — An identifier for the event.

### Accessing player items

- [primaryItem](avplayerinterstitialevent/primaryitem.md) — The player item that represents the primary content.
- [templateItems](avplayerinterstitialevent/templateitems.md) — An array of player item configurations to use as templates for player items that play interstitial content.

### Configuring cues

- [cue](avplayerinterstitialevent/cue-swift.property.md) — A cue to schedule interstitial event playback at a predefined position during primary playback.
- [Cue](avplayerinterstitialevent/cue-swift.struct.md) — A structure that defines standard cues to play interstitial content.

### Inspecting timing

- [time](avplayerinterstitialevent/time.md) — A time within the timeline of the primary content that playback of interstitial content begins.
- [date](avplayerinterstitialevent/date.md) — A date within the date range of the primary content that playback of interstitial content begins.
- [willPlayOnce](avplayerinterstitialevent/willplayonce.md) — A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.
- [resumptionOffset](avplayerinterstitialevent/resumptionoffset.md) — A time offset at which playback of primary content resumes after interstitial content finishes.
- [playoutLimit](avplayerinterstitialevent/playoutlimit.md) — The time offset at which playback of the interstitial ends.
- [alignsStartWithPrimarySegmentBoundary](avplayerinterstitialevent/alignsstartwithprimarysegmentboundary.md) — A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
- [alignsResumptionWithPrimarySegmentBoundary](avplayerinterstitialevent/alignsresumptionwithprimarysegmentboundary.md) — A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.

### Managing restrictions

- [restrictions](avplayerinterstitialevent/restrictions-swift.property.md) — The restrictions the event imposes on the playback of interstitial content.
- [Restrictions](avplayerinterstitialevent/restrictions-swift.struct.md) — Constants that define restrictions on the playback of interstitial content.

### Accessing asset lists

- [assetListResponse](avplayerinterstitialevent/assetlistresponse.md) — The asset list JSON response as a dictionary.

### Accessing attributes

- [userDefinedAttributes](avplayerinterstitialevent/userdefinedattributes.md) — Attributes of the event that the vendor or app defines.

### Inspecting timeline occupancy

- [timelineOccupancy](avplayerinterstitialevent/timelineoccupancy-swift.property.md) — An event’s occupancy on the integrated timeline.
- [TimelineOccupancy](avplayerinterstitialevent/timelineoccupancy-swift.enum.md) — Constants that specify how an event occupies time on an integrated timeline.
- [supplementsPrimaryContent](avplayerinterstitialevent/supplementsprimarycontent.md) — A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [contentMayVary](avplayerinterstitialevent/contentmayvary.md) — A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.
- [plannedDuration](avplayerinterstitialevent/plannedduration.md) — The planned duration of the event.

### Managing skipping behavior

- [skipControlLocalizedLabelBundleKey](avplayerinterstitialevent/skipcontrollocalizedlabelbundlekey.md) — The key defined in the AVPlayerInterstitialEventController’s localizedStringsBundle that points to the localized label for the skip button.
- [skipControlTimeRange](avplayerinterstitialevent/skipcontroltimerange.md) — The time range within the duration of the interstitial event for which a skip button should be displayed.
- [SkippableEventState](avplayerinterstitialevent/skippableeventstate.md) — These constants describe the state for a skippable AVPlayerInterstitialEvent.

### Instance Properties

- [scheduleIdentifier](avplayerinterstitialevent/scheduleidentifier.md) — The identifier of the daterange-schedule that produced this event. nil if the event was not a product of a daterange-schedule.

## See Also

### Interstitials

- [Providing an integrated view of your timeline when playing HLS interstitials](providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md) — Go beyond simple ad insertion with point and fill occupancy HLS interstitials.
- [AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md) — An object that schedules interstitial events for items played by the primary player.
- [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md) — An object that monitors the scheduling and progress of interstitial events.
- [AVPlayerInterstitialEventMonitorScheduleRequestErrorKey](avplayerinterstitialeventmonitorschedulerequesterrorkey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSError. Absent if the request succeeded
- [AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey](avplayerinterstitialeventmonitorschedulerequestidentifierkey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSString.
- [AVPlayerInterstitialEventMonitorScheduleRequestResponseKey](avplayerinterstitialeventmonitorschedulerequestresponsekey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSData. Absent if the request failed.
- [AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md) — An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.
