---
title: events
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/events
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/events'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/events.json'
content_hash: 'sha256:606772f6c761974e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# events

<sub>Instance Property</sub>

The schedule of interstitial events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var events: [AVPlayerInterstitialEvent] { get }
```

## Discussion

When the primary player’s content specifies the schedule of interstitial events intrinsically, this property value typically changes whenever primary player’s [currentItem](../avplayer/currentitem.md) changes. For HLS content that specifies interstitials using of `DATERANGE` tags, the value of this property may also change whenever the set of `DATERANGE` tags in the current item’s media playlist changes.

When you specify the schedule of interstitial events using an [AVPlayerInterstitialEventController](../avplayerinterstitialeventcontroller.md), this property value changes only when you update the interstitial event controller’s schedule.

> [!note] Note
> The elements in the [events](events.md) array are immutable. Attempting to modify them generates an exception. To alter an event, make a copy and modify the new instance.

## See Also

### Monitoring the event schedule

- [AVPlayerInterstitialEventMonitorEventsDidChangeNotification](eventsdidchangenotification.md) — A notification the system posts when the monitor’s schedule of interstitial events changes.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification](interstitialeventwasunschedulednotification.md) — A notification that is posted whenever an AVPlayerInterstitialEvent with loaded assets was unscheduled prior to playing.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledEventKey](interstitialeventwasunscheduledeventkey.md) — The dictionary key for the AVPlayerInterstitialEvent that was unscheduled in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledErrorKey](interstitialeventwasunschedulederrorkey.md) — The dictionary key to indicate whether the event that was unscheduled was due to an error.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification](interstitialeventdidfinishnotification.md) — A notification that is posted whenever an AVPlayerInterstitialEvent finished playing.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishEventKey](interstitialeventdidfinisheventkey.md) — The dictionary key for the AVPlayerInterstitialEvent that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishPlayoutTimeKey](interstitialeventdidfinishplayouttimekey.md) — The dictionary key for the playout time of the event that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishDidPlayEntireEventKey](interstitialeventdidfinishdidplayentireeventkey.md) — The dictionary key to indicate whether the event that finished playing was fully played out in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
