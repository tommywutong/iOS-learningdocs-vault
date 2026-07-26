---
title: interstitialEventWasUnscheduledNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventwasunschedulednotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventwasunschedulednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventwasunschedulednotification.json'
content_hash: 'sha256:4c533eae2e160353'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# interstitialEventWasUnscheduledNotification

<sub>Type Property</sub>

A notification that is posted whenever an AVPlayerInterstitialEvent with loaded assets was unscheduled prior to playing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let interstitialEventWasUnscheduledNotification: NSNotification.Name
```

## Discussion

Carries a userInfo dictionary that can contain the following keys and values:

1. AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledEventKey, with a value that indicates which AVPlayerInterstitialEvent was unscheduled.
2. AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledErrorKey, with an NSError value. This key will only be present if the AVPlayerInterstitialEvent was unscheduled due to an error.

## See Also

### Monitoring the event schedule

- [events](events.md) — The schedule of interstitial events.
- [AVPlayerInterstitialEventMonitorEventsDidChangeNotification](eventsdidchangenotification.md) — A notification the system posts when the monitor’s schedule of interstitial events changes.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledEventKey](interstitialeventwasunscheduledeventkey.md) — The dictionary key for the AVPlayerInterstitialEvent that was unscheduled in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledErrorKey](interstitialeventwasunschedulederrorkey.md) — The dictionary key to indicate whether the event that was unscheduled was due to an error.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification](interstitialeventdidfinishnotification.md) — A notification that is posted whenever an AVPlayerInterstitialEvent finished playing.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishEventKey](interstitialeventdidfinisheventkey.md) — The dictionary key for the AVPlayerInterstitialEvent that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishPlayoutTimeKey](interstitialeventdidfinishplayouttimekey.md) — The dictionary key for the playout time of the event that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [AVPlayerInterstitialEventMonitorInterstitialEventDidFinishDidPlayEntireEventKey](interstitialeventdidfinishdidplayentireeventkey.md) — The dictionary key to indicate whether the event that finished playing was fully played out in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
