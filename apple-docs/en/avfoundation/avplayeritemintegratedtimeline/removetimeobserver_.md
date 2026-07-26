---
title: 'removeTimeObserver:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemintegratedtimeline/removetimeobserver:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/removetimeobserver:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/removetimeobserver%3A.json'
content_hash: 'sha256:eebb1e19b29f3703'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# removeTimeObserver:

<sub>Instance Method</sub>

Cancels a previously registered time observer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) removeTimeObserver:(id<AVPlayerItemIntegratedTimelineObserver>) observer;
```

## See Also

### Observing time changes

- [addPeriodicTimeObserverForInterval:queue:usingBlock:](addperiodictimeobserverforinterval_queue_usingblock_.md) — Requests invocation of a block during playback to report changing time.
- [addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:](addboundarytimeobserverforsegment_offsetsintosegment_queue_usingblock_.md) — Requests invocation of a block when traversing an offset in a segment during playback.
- [AVPlayerItemIntegratedTimelineObserver](../avplayeritemintegratedtimelineobserver.md) — A protocol for objects that perform timeline observations.
