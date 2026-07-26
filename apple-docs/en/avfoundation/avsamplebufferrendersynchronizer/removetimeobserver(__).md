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
doc_path: '/documentation/avfoundation/avsamplebufferrendersynchronizer/removetimeobserver(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/removetimeobserver(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/removetimeobserver%28_%3A%29.json'
content_hash: 'sha256:ad956c0c0c1a2aa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# removeTimeObserver(_:)

<sub>Instance Method</sub>

Cancels the specified time observer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeTimeObserver(_ observer: Any)
```

## Parameters

- `observer` — The time observer to be cancelled.

## Discussion

Use this method to explicitly cancel time observers added using [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<addperiodictimeobserver(forinterval_queue_using_).md>) or [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<addboundarytimeobserver(fortimes_queue_using_).md>)

Upon return, the caller is guaranteed that no new time observer blocks will begin executing. Depending on the calling thread and the queue used to add the time observer, an in-flight block may continue to execute after this method returns. You can guarantee synchronous time observer removal by enqueuing the call to `removeTimeObserver:` on that queue. Call [sync(execute:)](<../../dispatch/dispatchqueue/sync(execute_)-3segw.md>) after `removeTimeObserver:` to wait for any in-flight blocks to finish executing.

## See Also

### Observing time

- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<addperiodictimeobserver(forinterval_queue_using_).md>) — Requests invocation of a block during rendering at specified time intervals.
- [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<addboundarytimeobserver(fortimes_queue_using_).md>) — Requests invocation of a block when specified times are traversed during normal rendering.
