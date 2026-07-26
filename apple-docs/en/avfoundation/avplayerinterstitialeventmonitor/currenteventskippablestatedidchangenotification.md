---
title: currentEventSkippableStateDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskippablestatedidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskippablestatedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskippablestatedidchangenotification.json'
content_hash: 'sha256:1cd2524cab30af48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# currentEventSkippableStateDidChangeNotification

<sub>Type Property</sub>

A notification that’s posted whenever the currentEventSkippableState of an AVPlayerInterstitialEventMonitor changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let currentEventSkippableStateDidChangeNotification: NSNotification.Name
```

## See Also

### Monitoring skipping

- [AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeEventKey](currenteventskippablestatedidchangeeventkey.md) — The dictionary key for the AVPlayerInterstitial event that had its skippable event state changed in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeStateKey](currenteventskippablestatedidchangestatekey.md) — The dictionary key for the skippable event state in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeSkipControlLabelKey](currenteventskippablestatedidchangeskipcontrollabelkey.md) — The dictionary key for the skip label of the event in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification](currenteventskippednotification.md) — A notification that’s posted whenever an event was skipped via skip control.
- [AVPlayerInterstitialEventMonitorCurrentEventSkippedEventKey](currenteventskippedeventkey.md) — The dictionary key for the AVPlayerInterstitialEvent that was skipped in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification.
- [currentEventSkipControlLabel](currenteventskipcontrollabel.md) — The skip control label for the currentEvent.
- [currentEventSkippableState](currenteventskippablestate.md) — The skippable event state for the currentEvent.
