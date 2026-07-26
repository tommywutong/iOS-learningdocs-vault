---
title: interstitialEventDidFinishNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventdidfinishnotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventdidfinishnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventdidfinishnotification.json'
content_hash: 'sha256:f47300aaf7859f4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# interstitialEventDidFinishNotification

<sub>Type Property</sub>

A notification that is posted whenever an AVPlayerInterstitialEvent finished playing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let interstitialEventDidFinishNotification: NSNotification.Name
```

## Discussion

Carries a userInfo dictionary that can contain the following keys and values:

1. AVPlayerInterstitialEventMonitorInterstitialEventDidFinishEventKey, with a value that indicates the AVPlayerInterstitialEvent that finished playing.
2. AVPlayerInterstitialEventMonitorInterstitialEventDidFinishPlayoutTimeKey, with a value that indicates how long that AVPlayerInterstitialEvent played out for.
3. AVPlayerInterstitialEventMonitorInterstitialEventDidFinishDidPlayEntireEventKey, with a value that indicates whether the AVPlayerInterstitialEvent was fully played out.

Note that cancelling an AVPlayerInterstitialEvent after playback started but prior to playback finishing will also trigger this event.

## See Also

### Monitoring the event schedule

- [events](events.md) — The schedule of interstitial events.
- [AVPlayerInterstitialEventMonitorEventsDidChangeNotification](eventsdidchangenotification.md) — A notification the system posts when the monitor’s schedule of interstitial events changes.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification](interstitialeventwasunschedulednotification.md) — A notification that is posted whenever an AVPlayerInterstitialEvent with loaded assets was unscheduled prior to playing.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledEventKey](interstitialeventwasunscheduledeventkey.md) — The dictionary key for the AVPlayerInterstitialEvent that was unscheduled in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledErrorKey](interstitialeventwasunschedulederrorkey.md) — The dictionary key to indicate whether the event that was unscheduled was due to an error.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishEventKey](interstitialeventdidfinisheventkey.md) — The dictionary key for the AVPlayerInterstitialEvent that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishPlayoutTimeKey](interstitialeventdidfinishplayouttimekey.md) — The dictionary key for the playout time of the event that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishDidPlayEntireEventKey](interstitialeventdidfinishdidplayentireeventkey.md) — The dictionary key to indicate whether the event that finished playing was fully played out in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
