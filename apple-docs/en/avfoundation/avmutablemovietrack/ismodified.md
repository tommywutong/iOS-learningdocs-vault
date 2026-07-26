---
title: isModified
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/ismodified
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/ismodified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/ismodified.json'
content_hash: 'sha256:8c7c7568a4efa3ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# isModified

<sub>Instance Property</sub>

A Boolean value that indicates whether a track is in a modified state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var isModified: Bool { get set }
```

## Discussion

This property is `YES` when the `AVMutableMovieTrack` object has been modified since it was created, was last written, or had its modified state cleared.

## See Also

### Configuring track information

- [alternateGroupID](alternategroupid.md) — A number that identifies the track as a member of a particular alternate group.
- [mediaDataStorage](mediadatastorage.md) — A storage container for the media data to be added to a track.
- [sampleReferenceBaseURL](samplereferencebaseurl.md) — The base URL for sample references.
