---
title: 'init(url:trackID:sourceTimeRange:targetTimeRange:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcompositiontracksegment/init(url:trackid:sourcetimerange:targettimerange:)-4rc2g'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/init(url:trackid:sourcetimerange:targettimerange:)-4rc2g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontracksegment/init%28url%3Atrackid%3Asourcetimerange%3Atargettimerange%3A%29-4rc2g.json'
content_hash: 'sha256:74dc5d12146ab15b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrackSegment](../avcompositiontracksegment.md)

# init(url:trackID:sourceTimeRange:targetTimeRange:)

<sub>Initializer</sub>

Creates an object that presents a segment of a media file that the specified URL references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(url URL: URL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)
```

## Parameters

- `URL` — A URL of the source media file.

- `trackID` — The identifier of the track whose media this segment presents.

- `sourceTimeRange` — The time range of the track whose media this segment presents.

- `targetTimeRange` — The time range of the composition track to present the segment’s media.

## See Also

### Creating a segment

- [- initWithTimeRange:](<init(timerange_).md>) — Creates an object that presents an empty composition track segment.
