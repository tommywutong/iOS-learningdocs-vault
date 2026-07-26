---
title: currentTime()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/currenttime()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/currenttime()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/currenttime%28%29.json'
content_hash: 'sha256:53a8a8e2b1880b35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# currentTime()

<sub>Instance Method</sub>

Returns the current time of the current player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func currentTime() -> CMTime
```

## Return Value

The current time of the current player item.

## Discussion

This property isn’t key-value observable. To observe the player’s time, use [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<addperiodictimeobserver(forinterval_queue_using_).md>) or [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<addboundarytimeobserver(fortimes_queue_using_).md>).

## See Also

### Observing playback time

- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<addperiodictimeobserver(forinterval_queue_using_).md>) — Requests the periodic invocation of a given block during playback to report changing time.
- [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<addboundarytimeobserver(fortimes_queue_using_).md>) — Requests the invocation of a block when specified times are traversed during normal playback.
- [- removeTimeObserver:](<removetimeobserver(__).md>) — Cancels a previously registered periodic or boundary time observer.
