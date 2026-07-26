---
title: 'track(withTrackID:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avfragmentedmovie/track(withtrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedmovie/track(withtrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedmovie/track%28withtrackid%3A%29.json'
content_hash: 'sha256:09cac8530f4b5903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedMovie](../avfragmentedmovie.md)

# track(withTrackID:)

<sub>Instance Method</sub>

Retrieves a track in the movie that contains the specified identifier.

> [!warning] Deprecated
> Use loadTrack(withTrackID:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVFragmentedMovieTrack?
```

## Parameters

- `trackID` — The persistent track identifier.

## Return Value

A movie track, or `nil` if there is no track with the identifier.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a track asynchronously using [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) instead.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a movie contains.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Retrieves tracks in the movie that present media of the specified characteristic. _(deprecated)_
