---
title: 'addMutableTracksCopyingSettings(from:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/addmutabletrackscopyingsettings(from:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/addmutabletrackscopyingsettings(from:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/addmutabletrackscopyingsettings%28from%3Aoptions%3A%29.json'
content_hash: 'sha256:bd20e2ce86b3c872'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# addMutableTracksCopyingSettings(from:options:)

<sub>Instance Method</sub>

Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func addMutableTracksCopyingSettings(from existingTracks: [AVAssetTrack], options: [String : Any]? = nil) -> [AVMutableMovieTrack]
```

## Parameters

- `existingTracks` — An array of asset tracks to be added.

- `options` — A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.

## Return Value

An array of [AVMutableMovieTrack](../avmutablemovietrack.md) objects. The index of a track in this array is the same as the index of its source track in the `existingTracks` array.

## Discussion

Properties involving pairs of tracks,such as track references, are copied from the source tracks to the target tracks.

## See Also

### Managing tracks

- [- mutableTrackCompatibleWithTrack:](<mutabletrack(compatiblewith_).md>) — Provides a reference to a track from a mutable movie into which you can insert any time range.
- [- addMutableTrackWithMediaType:copySettingsFromTrack:options:](<addmutabletrack(withmediatype_copysettingsfrom_options_).md>) — Adds an empty track to the target movie.
- [- removeTrack:](<removetrack(__).md>) — Removes the specified track from the target movie.
