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
doc_path: '/documentation/avfoundation/avsamplebufferrendersynchronizer/addperiodictimeobserver(forinterval:queue:using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/addperiodictimeobserver(forinterval:queue:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/addperiodictimeobserver%28forinterval%3Aqueue%3Ausing%3A%29.json'
content_hash: 'sha256:eca5445b05b7911b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# addPeriodicTimeObserver(forInterval:queue:using:)

<sub>Instance Method</sub>

Requests invocation of a block during rendering at specified time intervals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addPeriodicTimeObserver(forInterval interval: CMTime, queue: dispatch_queue_t?, using block: @escaping @Sendable (CMTime) -> Void) -> Any
```

## Parameters

- `interval` — The specified time interval requesting block invocation during rendering.

- `queue` — The serial queue the block should be unqueued on. If you pass `NULL`, the main queue is used. Passing a concurrent queue results in undefined behavior.

- `block` — The block to be invoked periodically.

## Return Value

An object that conforms to [NSObject](../../objectivec/nsobject-swift.class.md). You must retain this value as long as you want the time observer to be invoked by the synchronizer. Pass this object to [- removeTimeObserver:](<removetimeobserver(__).md>) to cancel time observation.

## Discussion

The block associated with this method is invoked at the specified time intervals, interpreted according to the timeline of the timebase. The block is also invoked whenever there is a time jump or rendering starts or stops.

If a very short time interval is used, the synchronizer may invoke the block less frequently than requested. However, the synchronizer will invoke the block often enough for the client to update indications of the current time appropriately in its end-user interface.

Always pair a call to this method with a call to [- removeTimeObserver:](<removetimeobserver(__).md>). Releasing the observer without calling `removeTimeObserver(_:)` results in undefined behavior.

## See Also

### Observing time

- [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<addboundarytimeobserver(fortimes_queue_using_).md>) — Requests invocation of a block when specified times are traversed during normal rendering.
- [- removeTimeObserver:](<removetimeobserver(__).md>) — Cancels the specified time observer.
