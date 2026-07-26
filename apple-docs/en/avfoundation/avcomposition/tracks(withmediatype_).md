---
title: 'tracks(withMediaType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcomposition/tracks(withmediatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/tracks(withmediatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/tracks%28withmediatype%3A%29.json'
content_hash: 'sha256:ba93b979397fd002'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# tracks(withMediaType:)

<sub>Instance Method</sub>

Returns tracks that contain media of a specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVCompositionTrack]
```

## Parameters

- `mediaType` — The media type of the tracks to return.

## Return Value

An array of tracks, which is empty if no tracks with the media type exist.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [- loadTracksWithMediaType:completionHandler:](<loadtracks(withmediatype_completionhandler_).md>) instead.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a composition contains.
- [- trackWithTrackID:](<track(withtrackid_).md>) — Returns a track that contains the specified identifier.
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Returns tracks that contain media of a specified characteristic.
- [- unusedTrackID](<unusedtrackid().md>) — Returns an identifier that no other tracks in the asset use.
