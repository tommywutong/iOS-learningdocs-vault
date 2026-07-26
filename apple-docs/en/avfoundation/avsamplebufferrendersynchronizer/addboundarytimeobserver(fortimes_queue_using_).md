---
title: 'addBoundaryTimeObserver(forTimes:queue:using:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebufferrendersynchronizer/addboundarytimeobserver(fortimes:queue:using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/addboundarytimeobserver(fortimes:queue:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/addboundarytimeobserver%28fortimes%3Aqueue%3Ausing%3A%29.json'
content_hash: 'sha256:3d259d3425560e5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# addBoundaryTimeObserver(forTimes:queue:using:)

<sub>Instance Method</sub>

Requests invocation of a block when specified times are traversed during normal rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addBoundaryTimeObserver(forTimes times: [NSValue], queue: dispatch_queue_t?, using block: @escaping @Sendable () -> Void) -> Any
```

## Parameters

- `times` — An array containing the times for which the observer requests notification.

- `queue` — The serial queue the block should be unqueued on. If you pass `NULL`, the main queue is used. Passing a concurrent queue results in undefined behavior.

- `block` — The block to be invoked when any of the specified times is crossed during normal rendering.

## Return Value

An object that conforms to [NSObject](../../objectivec/nsobject-swift.class.md). You must retain this value as long as you want the time observer to be invoked by the synchronizer. Pass this object to [- removeTimeObserver:](<removetimeobserver(__).md>) to cancel time observation.

## Discussion

Always pair a call to this method with a call to [- removeTimeObserver:](<removetimeobserver(__).md>). Releasing the observer without calling `removeTimeObserver(_:)` results in undefined behavior.

## See Also

### Observing time

- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<addperiodictimeobserver(forinterval_queue_using_).md>) — Requests invocation of a block during rendering at specified time intervals.
- [- removeTimeObserver:](<removetimeobserver(__).md>) — Cancels the specified time observer.
