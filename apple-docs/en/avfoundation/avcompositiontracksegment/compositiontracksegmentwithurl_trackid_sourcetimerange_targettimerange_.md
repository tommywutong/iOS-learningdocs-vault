---
title: 'compositionTrackSegmentWithURL:trackID:sourceTimeRange:targetTimeRange:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcompositiontracksegment/compositiontracksegmentwithurl:trackid:sourcetimerange:targettimerange:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/compositiontracksegmentwithurl:trackid:sourcetimerange:targettimerange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontracksegment/compositiontracksegmentwithurl%3Atrackid%3Asourcetimerange%3Atargettimerange%3A.json'
content_hash: 'sha256:ec7a6ff2c99e01bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrackSegment](../avcompositiontracksegment.md)

# compositionTrackSegmentWithURL:trackID:sourceTimeRange:targetTimeRange:

<sub>Type Method</sub>

Returns a new an object that presents a segment of a media file that the specified URL references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) compositionTrackSegmentWithURL:(NSURL *) URL trackID:(CMPersistentTrackID) trackID sourceTimeRange:(CMTimeRange) sourceTimeRange targetTimeRange:(CMTimeRange) targetTimeRange;
```

## Parameters

- `URL` — A URL of the source media file.

- `trackID` — The identifier of the track whose media this segment presents.

- `sourceTimeRange` — The time range of the track whose media this segment presents.

- `targetTimeRange` — The time range of the composition track to present the segment’s media.

## Return Value

A new composition track segment.

## See Also

### Creating a segment

- [compositionTrackSegmentWithTimeRange:](compositiontracksegmentwithtimerange_.md) — Returns a new object that presents an empty composition track segment.
- [- initWithTimeRange:](<init(timerange_).md>) — Creates an object that presents an empty composition track segment.
- [- initWithURL:trackID:sourceTimeRange:targetTimeRange:](<init(url_trackid_sourcetimerange_targettimerange_)-4rc2g.md>) — Creates an object that presents a segment of a media file that the specified URL references.
