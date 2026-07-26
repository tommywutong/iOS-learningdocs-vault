---
title: 'mutableTrack(compatibleWith:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/mutabletrack(compatiblewith:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/mutabletrack(compatiblewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/mutabletrack%28compatiblewith%3A%29.json'
content_hash: 'sha256:11a3d8777bf8439a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# mutableTrack(compatibleWith:)

<sub>Instance Method</sub>

Provides a reference to a track from a mutable movie into which you can insert any time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func mutableTrack(compatibleWith track: AVAssetTrack) -> AVMutableMovieTrack?
```

## Parameters

- `track` — The [AVAssetTrack](../avassettrack.md) containing the desired time range.

## Return Value

An [AVMutableMovieTrack](../avmutablemovietrack.md) object that can accommodate the time range insertion. Returns nil when no track is available.

## Discussion

Keep the number of tracks in a movie to a minimum, corresponding to the number of tracks for which media data must be presented in parallel. If media data of the same type is presented serially, even from multiple assets, a single track of that media type should be used. This method can help the client to identify an existing target track for an insertion.

## See Also

### Managing tracks

- [- addMutableTrackWithMediaType:copySettingsFromTrack:options:](<addmutabletrack(withmediatype_copysettingsfrom_options_).md>) — Adds an empty track to the target movie.
- [- addMutableTracksCopyingSettingsFromTracks:options:](<addmutabletrackscopyingsettings(from_options_).md>) — Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.
- [- removeTrack:](<removetrack(__).md>) — Removes the specified track from the target movie.
