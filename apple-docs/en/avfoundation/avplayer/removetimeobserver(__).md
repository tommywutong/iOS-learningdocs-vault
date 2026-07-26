---
title: 'removeTimeObserver(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/removetimeobserver(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/removetimeobserver(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/removetimeobserver%28_%3A%29.json'
content_hash: 'sha256:c2867924dd2d64f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# removeTimeObserver(_:)

<sub>Instance Method</sub>

Cancels a previously registered periodic or boundary time observer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func removeTimeObserver(_ observer: Any)
```

## Parameters

- `observer` — An object returned by a previous call to [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<addperiodictimeobserver(forinterval_queue_using_).md>) or [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<addboundarytimeobserver(fortimes_queue_using_).md>).

## Discussion

Upon return, the caller is guaranteed that no new time observer blocks will begin executing. Depending on the calling thread and the queue used to add the time observer, an in-flight block may continue to execute after this method returns. You can guarantee synchronous time observer removal by enqueuing the call to `removeTimeObserver` on that queue. Alternatively, call `dispatch_sync(queue, ^{})` after `removeTimeObserver` to wait for any in-flight blocks to finish executing.

You should use this method to explicitly cancel each time observer added using [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<addperiodictimeobserver(forinterval_queue_using_).md>) and [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<addboundarytimeobserver(fortimes_queue_using_).md>).

The following shows a common implementation to remove a registered time observer:

**Swift**

```swift
func removePeriodicTimeObserver() {
    // If a time observer exists, remove it
    if let token = timeObserverToken {
        player.removeTimeObserver(token)
        timeObserverToken = nil
    }
}
```

**Objective-C**

```objc
- (void)removeBoundaryTimeObserver {
    if (self.timeObserverToken) {
        [self.player removeTimeObserver:self.timeObserverToken];
        self.timeObserverToken = nil;
    }
}
```

## See Also

### Observing playback time

- [- currentTime](<currenttime().md>) — Returns the current time of the current player item.
- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<addperiodictimeobserver(forinterval_queue_using_).md>) — Requests the periodic invocation of a given block during playback to report changing time.
- [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<addboundarytimeobserver(fortimes_queue_using_).md>) — Requests the invocation of a block when specified times are traversed during normal playback.
