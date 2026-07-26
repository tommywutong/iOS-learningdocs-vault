---
title: AVPlayerItemIntegratedTimeline.PeriodicTimes
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimeline/periodictimes
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/periodictimes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/periodictimes.json'
content_hash: 'sha256:54b6351e1c2e16c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# AVPlayerItemIntegratedTimeline.PeriodicTimes

<sub>Structure</sub>

An asynchronous sequence of periodic time values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PeriodicTimes
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Iterating elements

- [Iterator](periodictimes/iterator.md)

## See Also

### Observing time changes

- [periodicTimes(forInterval:)](<periodictimes(forinterval_).md>) — Returns an asynchronous sequence of times periodically as playback progresses.
- [boundaryTimes(for:offsetsIntoSegment:)](<boundarytimes(for_offsetsintosegment_).md>) — Returns an asynchronous sequence of times whenever playback reaches a segment time in the segment.
- [BoundaryTimes](boundarytimes.md) — An asynchronous sequence of boundary time values.
- [AVPlayerItemIntegratedTimelineObserver](../avplayeritemintegratedtimelineobserver.md) — A protocol for objects that perform timeline observations.
