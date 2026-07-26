---
title: AVPlayerItemIntegratedTimelineObserver
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimelineobserver
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelineobserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimelineobserver.json'
content_hash: 'sha256:a94da7533ee573af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemIntegratedTimelineObserver

<sub>Protocol</sub>

A protocol for objects that perform timeline observations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVPlayerItemIntegratedTimelineObserver : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Observing time changes

- [periodicTimes(forInterval:)](<avplayeritemintegratedtimeline/periodictimes(forinterval_).md>) — Returns an asynchronous sequence of times periodically as playback progresses.
- [boundaryTimes(for:offsetsIntoSegment:)](<avplayeritemintegratedtimeline/boundarytimes(for_offsetsintosegment_).md>) — Returns an asynchronous sequence of times whenever playback reaches a segment time in the segment.
- [BoundaryTimes](avplayeritemintegratedtimeline/boundarytimes.md) — An asynchronous sequence of boundary time values.
- [PeriodicTimes](avplayeritemintegratedtimeline/periodictimes.md) — An asynchronous sequence of periodic time values.
