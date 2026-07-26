---
title: currentEventSkipControlLabel
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskipcontrollabel
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskipcontrollabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskipcontrollabel.json'
content_hash: 'sha256:d854d038419929e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# currentEventSkipControlLabel

<sub>Instance Property</sub>

The skip control label for the currentEvent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentEventSkipControlLabel: String? { get }
```

## Discussion

If a localizedStringsBundle has been set on the AVPlayerInterstitialEventController, and a skipControlLocalizedLabelBundleKey is set on the currentEvent, then this value will be the localized string that was matched to the event’s skipControlLocalizedLabelBundleKey for the corresponding system language in the supplied Bundle, if any. If currentEvent is nil, then the value will be nil.

## See Also

### Monitoring skipping

- [AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification](currenteventskippablestatedidchangenotification.md) — A notification that’s posted whenever the currentEventSkippableState of an AVPlayerInterstitialEventMonitor changes.
- [AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeEventKey](currenteventskippablestatedidchangeeventkey.md) — The dictionary key for the AVPlayerInterstitial event that had its skippable event state changed in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeStateKey](currenteventskippablestatedidchangestatekey.md) — The dictionary key for the skippable event state in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeSkipControlLabelKey](currenteventskippablestatedidchangeskipcontrollabelkey.md) — The dictionary key for the skip label of the event in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification](currenteventskippednotification.md) — A notification that’s posted whenever an event was skipped via skip control.
- [AVPlayerInterstitialEventMonitorCurrentEventSkippedEventKey](currenteventskippedeventkey.md) — The dictionary key for the AVPlayerInterstitialEvent that was skipped in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification.
- [currentEventSkippableState](currenteventskippablestate.md) — The skippable event state for the currentEvent.
