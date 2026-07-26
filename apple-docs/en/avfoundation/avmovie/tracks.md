---
title: tracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmovie/tracks
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/tracks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/tracks.json'
content_hash: 'sha256:84f6462ecaedc8ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# tracks

<sub>Instance Property</sub>

The tracks that a movie contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var tracks: [AVMovieTrack] { get }
```

## See Also

### Accessing tracks

- [- trackWithTrackID:](<track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier. _(deprecated)_
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Retrieves tracks in the movie that present media of the specified characteristic. _(deprecated)_
