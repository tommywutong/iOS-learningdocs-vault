---
title: AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitorschedulerequestidentifierkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitorschedulerequestidentifierkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitorschedulerequestidentifierkey.json'
content_hash: 'sha256:c6b1ef16b0a5006a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey

<sub>Global Variable</sub>

userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSString.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey: String
```

## See Also

### Interstitials

- [Providing an integrated view of your timeline when playing HLS interstitials](providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md) — Go beyond simple ad insertion with point and fill occupancy HLS interstitials.
- [AVPlayerInterstitialEvent](avplayerinterstitialevent.md) — An object that provides instructions for how a player presents interstitial content.
- [AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md) — An object that schedules interstitial events for items played by the primary player.
- [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md) — An object that monitors the scheduling and progress of interstitial events.
- [AVPlayerInterstitialEventMonitorScheduleRequestErrorKey](avplayerinterstitialeventmonitorschedulerequesterrorkey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSError. Absent if the request succeeded
- [AVPlayerInterstitialEventMonitorScheduleRequestResponseKey](avplayerinterstitialeventmonitorschedulerequestresponsekey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSData. Absent if the request failed.
- [AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md) — An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.
