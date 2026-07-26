---
title: tracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/tracks
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/tracks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/tracks.json'
content_hash: 'sha256:9970d0699a02aa5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# tracks

<sub>Instance Property</sub>

The tracks that a movie contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var tracks: [AVMutableMovieTrack] { get }
```

## See Also

### Accessing tracks

- [- trackWithTrackID:](<track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type.
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Retrieve tracks in the movie that present media of the specified characteristic.
- [- unusedTrackID](<unusedtrackid().md>) — Returns an identifier that no other tracks in the asset use.
