---
title: 'boundaryTimes(for:offsetsIntoSegment:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemintegratedtimeline/boundarytimes(for:offsetsintosegment:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/boundarytimes(for:offsetsintosegment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/boundarytimes%28for%3Aoffsetsintosegment%3A%29.json'
content_hash: 'sha256:bd412f8d8cb857a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# boundaryTimes(for:offsetsIntoSegment:)

<sub>Instance Method</sub>

Returns an asynchronous sequence of times whenever playback reaches a segment time in the segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func boundaryTimes(for segment: AVPlayerItemSegment, offsetsIntoSegment: [CMTime]) -> AVPlayerItemIntegratedTimeline.BoundaryTimes
```

## See Also

### Observing time changes

- [periodicTimes(forInterval:)](<periodictimes(forinterval_).md>) — Returns an asynchronous sequence of times periodically as playback progresses.
- [BoundaryTimes](boundarytimes.md) — An asynchronous sequence of boundary time values.
- [PeriodicTimes](periodictimes.md) — An asynchronous sequence of periodic time values.
- [AVPlayerItemIntegratedTimelineObserver](../avplayeritemintegratedtimelineobserver.md) — A protocol for objects that perform timeline observations.
