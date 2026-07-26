---
title: interstitialEventWasUnscheduledEventKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventwasunscheduledeventkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventwasunscheduledeventkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventwasunscheduledeventkey.json'
content_hash: 'sha256:1e0042906ba4302d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# interstitialEventWasUnscheduledEventKey

<sub>Type Property</sub>

The dictionary key for the AVPlayerInterstitialEvent that was unscheduled in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let interstitialEventWasUnscheduledEventKey: String
```

## Discussion

The value corresponding to this key is of type AVPlayerInterstitialEvent.

## See Also

### Monitoring the event schedule

- [events](events.md) — The schedule of interstitial events.
- [AVPlayerInterstitialEventMonitorEventsDidChangeNotification](eventsdidchangenotification.md) — A notification the system posts when the monitor’s schedule of interstitial events changes.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification](interstitialeventwasunschedulednotification.md) — A notification that is posted whenever an AVPlayerInterstitialEvent with loaded assets was unscheduled prior to playing.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledErrorKey](interstitialeventwasunschedulederrorkey.md) — The dictionary key to indicate whether the event that was unscheduled was due to an error.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification](interstitialeventdidfinishnotification.md) — A notification that is posted whenever an AVPlayerInterstitialEvent finished playing.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishEventKey](interstitialeventdidfinisheventkey.md) — The dictionary key for the AVPlayerInterstitialEvent that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishPlayoutTimeKey](interstitialeventdidfinishplayouttimekey.md) — The dictionary key for the playout time of the event that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishDidPlayEntireEventKey](interstitialeventdidfinishdidplayentireeventkey.md) — The dictionary key to indicate whether the event that finished playing was fully played out in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
