---
title: skipCurrentEvent()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventcontroller/skipcurrentevent()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/skipcurrentevent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventcontroller/skipcurrentevent%28%29.json'
content_hash: 'sha256:828e94edab4c6387'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventController](../avplayerinterstitialeventcontroller.md)

# skipCurrentEvent()

<sub>Instance Method</sub>

Causes the playback of the currently playing interstital event to be abandoned.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func skipCurrentEvent()
```

## Discussion

Note that coinciding events will NOT be skipped. This results in AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification being posted. Has no effect while the currentEvent is nil.

## See Also

### Configuring the event schedule

- [events](events.md) — The current schedule of interstitial events.
- [- cancelCurrentEventWithResumptionOffset:](<cancelcurrentevent(withresumptionoffset_).md>) — Cancels the playback of all currently playing and scheduled interstitial events, and resumes playback of primary content.
