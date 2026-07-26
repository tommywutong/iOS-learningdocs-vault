---
title: 'addPeriodicTimeObserver(forInterval:queue:using:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/addperiodictimeobserver(forinterval:queue:using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/addperiodictimeobserver(forinterval:queue:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/addperiodictimeobserver%28forinterval%3Aqueue%3Ausing%3A%29.json'
content_hash: 'sha256:3ff643aba22e0e4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# addPeriodicTimeObserver(forInterval:queue:using:)

<sub>Instance Method</sub>

Requests the periodic invocation of a given block during playback to report changing time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func addPeriodicTimeObserver(forInterval interval: CMTime, queue: dispatch_queue_t?, using block: @escaping @Sendable (CMTime) -> Void) -> Any
```

## Parameters

- `interval` — The time interval at which the system invokes the block during normal playback, according to progress of the player’s current time.

- `queue` — The dispatch queue on which the system calls the block. Passing a concurrent queue isn’t supported and results in undefined behavior. If you pass `NULL`, the system uses the main queue.

- `block` — The block that the system periodically invokes. The block takes a single parameter: - **time** — The time at which the system invokes the block.

## Return Value

An opaque object that you pass as the argument to [- removeTimeObserver:](<removetimeobserver(__).md>) to cancel observation.

## Discussion

You must maintain a strong reference to the returned value as long as you want the time observer to be invoked by the player. You must pair each invocation of this method with a corresponding call to [- removeTimeObserver:](<removetimeobserver(__).md>). Releasing the observer object without invoking [- removeTimeObserver:](<removetimeobserver(__).md>) results in undefined behavior.

The system invokes the block periodically at the interval specified, interpreted according to the timeline of the current item. It also invokes the block whenever time jumps or playback starts or stops. If the interval corresponds to a very short interval in real time, the player may invoke the block less frequently than your app requested. Even so, the player will invoke the block sufficiently often for the client to update indications of the current time appropriately in its end-user interface.

The following example illustrates how you set up a callback the system invokes every half second during normal playback.

**Swift**

```swift
func addPeriodicTimeObserver() {
    // Invoke callback every half second
    let interval = CMTime(seconds: 0.5,
                          preferredTimescale: CMTimeScale(NSEC_PER_SEC))
    // Add time observer. Invoke closure on the main queue.
    timeObserverToken =
        player.addPeriodicTimeObserver(forInterval: interval, queue: .main) {
            [weak self] time in
            // update player transport UI
    }
}
```

**Objective-C**

```objc
- (void)addPeriodicTimeObserver {
    // Invoke callback every half second
    CMTime interval = CMTimeMakeWithSeconds(0.5, NSEC_PER_SEC);
    // Queue on which to invoke the callback
    dispatch_queue_t mainQueue = dispatch_get_main_queue();
    // Add time observer
    self.timeObserverToken =
        [self.player addPeriodicTimeObserverForInterval:interval
                                                  queue:mainQueue
                                             usingBlock:^(CMTime time) {
            // Use weak reference to self
            // Update player transport UI
        }];
}
```

> [!important] Important
> Use a `weak` reference to `self` in the callback block to prevent creating a retain cycle.

## See Also

### Observing playback time

- [- currentTime](<currenttime().md>) — Returns the current time of the current player item.
- [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<addboundarytimeobserver(fortimes_queue_using_).md>) — Requests the invocation of a block when specified times are traversed during normal playback.
- [- removeTimeObserver:](<removetimeobserver(__).md>) — Cancels a previously registered periodic or boundary time observer.
