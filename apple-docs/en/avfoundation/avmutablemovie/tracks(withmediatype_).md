---
title: 'tracks(withMediaType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/tracks(withmediatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/tracks(withmediatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/tracks%28withmediatype%3A%29.json'
content_hash: 'sha256:4062f3cd7ea1aaf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# tracks(withMediaType:)

<sub>Instance Method</sub>

Retrieves tracks in the movie that present media of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVMutableMovieTrack]
```

## Parameters

- `mediaType` — The media type of the tracks to return.

## Return Value

An array of tracks, which is empty if there are no tracks with the media type.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [- loadTracksWithMediaType:completionHandler:](<loadtracks(withmediatype_completionhandler_).md>) instead.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a movie contains.
- [- trackWithTrackID:](<track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier.
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Retrieve tracks in the movie that present media of the specified characteristic.
- [- unusedTrackID](<unusedtrackid().md>) — Returns an identifier that no other tracks in the asset use.
