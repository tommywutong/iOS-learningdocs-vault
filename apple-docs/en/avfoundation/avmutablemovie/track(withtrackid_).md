---
title: 'track(withTrackID:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/track(withtrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/track(withtrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/track%28withtrackid%3A%29.json'
content_hash: 'sha256:6fad6c9a8a18a73b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# track(withTrackID:)

<sub>Instance Method</sub>

Retrieves a track in the movie that contains the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVMutableMovieTrack?
```

## Parameters

- `trackID` — The track identifier for the requested track.

## Return Value

A movie track, or `nil` if there is no track with the identifier.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a track asynchronously using [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) instead.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a movie contains.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type.
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Retrieve tracks in the movie that present media of the specified characteristic.
- [- unusedTrackID](<unusedtrackid().md>) — Returns an identifier that no other tracks in the asset use.
