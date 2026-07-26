---
title: 'tracks(withMediaCharacteristic:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/tracks(withmediacharacteristic:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/tracks(withmediacharacteristic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/tracks%28withmediacharacteristic%3A%29.json'
content_hash: 'sha256:b7c35fc6fa3ebaa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# tracks(withMediaCharacteristic:)

<sub>Instance Method</sub>

Retrieve tracks in the movie that present media of the specified characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVMutableMovieTrack]
```

## Parameters

- `mediaCharacteristic` — The media characteristic of the tracks to return.

## Return Value

An array of tracks, which is empty if there are no tracks with the media characteristic.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) instead.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a movie contains.
- [- trackWithTrackID:](<track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type.
- [- unusedTrackID](<unusedtrackid().md>) — Returns an identifier that no other tracks in the asset use.
