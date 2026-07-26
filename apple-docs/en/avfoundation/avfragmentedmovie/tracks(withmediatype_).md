---
title: 'tracks(withMediaType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avfragmentedmovie/tracks(withmediatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedmovie/tracks(withmediatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedmovie/tracks%28withmediatype%3A%29.json'
content_hash: 'sha256:413b5a65c05d69de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedMovie](../avfragmentedmovie.md)

# tracks(withMediaType:)

<sub>Instance Method</sub>

Retrieves tracks in the movie that present media of the specified type.

> [!warning] Deprecated
> Use loadTracks(withMediaType:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVFragmentedMovieTrack]
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
- [- trackWithTrackID:](<track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Retrieves tracks in the movie that present media of the specified characteristic. _(deprecated)_
