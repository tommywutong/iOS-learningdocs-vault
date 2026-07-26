---
title: 'addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemintegratedtimeline/addboundarytimeobserverforsegment:offsetsintosegment:queue:usingblock:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/addboundarytimeobserverforsegment:offsetsintosegment:queue:usingblock:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/addboundarytimeobserverforsegment%3Aoffsetsintosegment%3Aqueue%3Ausingblock%3A.json'
content_hash: 'sha256:11025cc1fbf72191'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:

<sub>Instance Method</sub>

Requests invocation of a block when traversing an offset in a segment during playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (id<AVPlayerItemIntegratedTimelineObserver>) addBoundaryTimeObserverForSegment:(AVPlayerItemSegment *) segment offsetsIntoSegment:(NSArray *) offsetsIntoSegment queue:(dispatch_queue_t) queue usingBlock:(void (^)(BOOL success)) block;
```

## See Also

### Observing time changes

- [addPeriodicTimeObserverForInterval:queue:usingBlock:](addperiodictimeobserverforinterval_queue_usingblock_.md) — Requests invocation of a block during playback to report changing time.
- [removeTimeObserver:](removetimeobserver_.md) — Cancels a previously registered time observer.
- [AVPlayerItemIntegratedTimelineObserver](../avplayeritemintegratedtimelineobserver.md) — A protocol for objects that perform timeline observations.
