---
title: 'tracks(withMediaCharacteristic:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmovie/tracks(withmediacharacteristic:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/tracks(withmediacharacteristic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/tracks%28withmediacharacteristic%3A%29.json'
content_hash: 'sha256:b7053e544ac78442'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# tracks(withMediaCharacteristic:)

<sub>Instance Method</sub>

Retrieves tracks in the movie that present media of the specified characteristic.

> [!warning] Deprecated
> Use [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVMovieTrack]
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
- [- trackWithTrackID:](<track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier. _(deprecated)_
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type. _(deprecated)_
