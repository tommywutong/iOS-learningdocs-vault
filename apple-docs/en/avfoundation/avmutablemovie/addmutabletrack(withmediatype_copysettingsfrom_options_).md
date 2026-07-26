---
title: 'addMutableTrack(withMediaType:copySettingsFrom:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/addmutabletrack(withmediatype:copysettingsfrom:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/addmutabletrack(withmediatype:copysettingsfrom:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/addmutabletrack%28withmediatype%3Acopysettingsfrom%3Aoptions%3A%29.json'
content_hash: 'sha256:afe31743285f5460'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# addMutableTrack(withMediaType:copySettingsFrom:options:)

<sub>Instance Method</sub>

Adds an empty track to the target movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func addMutableTrack(withMediaType mediaType: AVMediaType, copySettingsFrom track: AVAssetTrack?, options: [String : Any]? = nil) -> AVMutableMovieTrack?
```

## Parameters

- `mediaType` — The media type for the new track.

- `track` — An [AVAssetTrack](../avassettrack.md) containing the desired track settings to be transferred. Set to `nil` to create a track with default settings.

- `options` — A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.

## Return Value

An [AVMutableMovieTrack](../avmutablemovietrack.md) object.

## See Also

### Managing tracks

- [- mutableTrackCompatibleWithTrack:](<mutabletrack(compatiblewith_).md>) — Provides a reference to a track from a mutable movie into which you can insert any time range.
- [- addMutableTracksCopyingSettingsFromTracks:options:](<addmutabletrackscopyingsettings(from_options_).md>) — Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.
- [- removeTrack:](<removetrack(__).md>) — Removes the specified track from the target movie.
