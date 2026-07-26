---
title: AVMovieTrack
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmovietrack
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovietrack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovietrack.json'
content_hash: 'sha256:9b69138f54536f72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMovieTrack

<sub>Class</sub>

A track in a movie that conforms to the QuickTime or ISO base media file format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class AVMovieTrack
```

## Relationships

- **Inherits From**: [AVAssetTrack](avassettrack.md)

- **Inherited By**: [AVFragmentedMovieTrack](avfragmentedmovietrack.md), [AVMutableMovieTrack](avmutablemovietrack.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Retrieving track information

- [alternateGroupID](avmovietrack/alternategroupid.md) — A value that identifies the track as a member of a particular alternate group.
- [mediaDataStorage](avmovietrack/mediadatastorage.md) — The storage container for media data added to a track.
- [mediaDecodeTimeRange](avmovietrack/mediadecodetimerange.md) — A range of decode times for the track’s media.
- [mediaPresentationTimeRange](avmovietrack/mediapresentationtimerange.md) — A range of presentation times for the track’s media.

## See Also

### Movies

- [AVMovie](avmovie.md) — An object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.
