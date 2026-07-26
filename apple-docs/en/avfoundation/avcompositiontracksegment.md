---
title: AVCompositionTrackSegment
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontracksegment
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontracksegment.json'
content_hash: 'sha256:991c53739cf3adb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCompositionTrackSegment

<sub>Class</sub>

A track segment that maps a time from the source media track to the composition track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVCompositionTrackSegment
```

## Overview

You typically use this class to save a low-level representation of a composition.

## Relationships

- **Inherits From**: [AVAssetTrackSegment](avassettracksegment.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a segment

- [- initWithTimeRange:](<avcompositiontracksegment/init(timerange_).md>) — Creates an object that presents an empty composition track segment.
- [- initWithURL:trackID:sourceTimeRange:targetTimeRange:](<avcompositiontracksegment/init(url_trackid_sourcetimerange_targettimerange_)-4rc2g.md>) — Creates an object that presents a segment of a media file that the specified URL references.

### Accessing segment properties

- [sourceURL](avcompositiontracksegment/sourceurl.md) — A URL of the container file whose media this track segment presents.
- [sourceTrackID](avcompositiontracksegment/sourcetrackid.md) — An identifier of a track in the container file whose media this track segment presents.
- [empty](avcompositiontracksegment/isempty.md) — A Boolean value that indicates whether the segment is empty.

### Initializers

- [init(URL:trackID:sourceTimeRange:targetTimeRange:)](<avcompositiontracksegment/init(url_trackid_sourcetimerange_targettimerange_)-9shbx.md>)
- [init(URL:trackID:sourceTimeRange:targetTimeRange:)](<avcompositiontracksegment/init(url_trackid_sourcetimerange_targettimerange_)-qoz.md>)

## See Also

### Compositions

- [AVComposition](avcomposition.md) — An object that combines and arranges media from multiple assets into a single composite asset that you can play or process.
- [AVCompositionTrack](avcompositiontrack.md) — A track in a composition that presents media of a uniform type.
