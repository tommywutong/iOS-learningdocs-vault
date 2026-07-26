---
title: currentEvent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/currentevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/currentevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/currentevent.json'
content_hash: 'sha256:0be715448886dcc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# currentEvent

<sub>Instance Property</sub>

The current interstitial event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentEvent: AVPlayerInterstitialEvent? { get }
```

## Discussion

The value is `nil` when primary content is playing.

## See Also

### Monitoring the current event

- [AVPlayerInterstitialEventMonitorCurrentEventDidChangeNotification](currenteventdidchangenotification.md) — A notification the system posts when the monitor’s current interstitial event changes.
