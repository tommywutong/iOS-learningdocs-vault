---
title: 'removeTrack(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/removetrack(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/removetrack(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/removetrack%28_%3A%29.json'
content_hash: 'sha256:f2d681c1fa1e27b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# removeTrack(_:)

<sub>Instance Method</sub>

Removes the specified track from the target movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func removeTrack(_ track: AVMovieTrack)
```

## Parameters

- `track` — The movie to be removed.

## See Also

### Managing tracks

- [- mutableTrackCompatibleWithTrack:](<mutabletrack(compatiblewith_).md>) — Provides a reference to a track from a mutable movie into which you can insert any time range.
- [- addMutableTrackWithMediaType:copySettingsFromTrack:options:](<addmutabletrack(withmediatype_copysettingsfrom_options_).md>) — Adds an empty track to the target movie.
- [- addMutableTracksCopyingSettingsFromTracks:options:](<addmutabletrackscopyingsettings(from_options_).md>) — Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.
