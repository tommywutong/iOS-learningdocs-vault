---
title: 'cancelCurrentEvent(withResumptionOffset:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerinterstitialeventcontroller/cancelcurrentevent(withresumptionoffset:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/cancelcurrentevent(withresumptionoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventcontroller/cancelcurrentevent%28withresumptionoffset%3A%29.json'
content_hash: 'sha256:f0113ae3ccfb673b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventController](../avplayerinterstitialeventcontroller.md)

# cancelCurrentEvent(withResumptionOffset:)

<sub>Instance Method</sub>

Cancels the playback of all currently playing and scheduled interstitial events, and resumes playback of primary content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelCurrentEvent(withResumptionOffset resumptionOffset: CMTime)
```

## Parameters

- `resumptionOffset` — The time offset at which playback of the primary content resumes after interstitial playback finishes.

## Discussion

When you cancel interstitial events using this method, the resumption offset value that you specify overrides the events’s [resumptionOffset](../avplayerinterstitialevent/resumptionoffset.md) value.

> [!note] Note
> If you call this method during the handling of coinciding interstitial events, the system cancels all events for that time. Calling this method has no impact on schedule events that have dates or times later than this event.

## See Also

### Configuring the event schedule

- [events](events.md) — The current schedule of interstitial events.
- [- skipCurrentEvent](<skipcurrentevent().md>) — Causes the playback of the currently playing interstital event to be abandoned.
