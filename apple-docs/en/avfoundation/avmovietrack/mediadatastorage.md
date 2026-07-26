---
title: mediaDataStorage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmovietrack/mediadatastorage
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovietrack/mediadatastorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovietrack/mediadatastorage.json'
content_hash: 'sha256:546f08e62457c10a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovieTrack](../avmovietrack.md)

# mediaDataStorage

<sub>Instance Property</sub>

The storage container for media data added to a track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@NSCopying var mediaDataStorage: AVMediaDataStorage? { get }
```

## Discussion

The value of this property is an [AVMediaDataStorage](../avmediadatastorage.md) object that indicates the location to which the system writes media data when it’s inserted or appended.

## See Also

### Retrieving track information

- [alternateGroupID](alternategroupid.md) — A value that identifies the track as a member of a particular alternate group.
- [mediaDecodeTimeRange](mediadecodetimerange.md) — A range of decode times for the track’s media.
- [mediaPresentationTimeRange](mediapresentationtimerange.md) — A range of presentation times for the track’s media.
