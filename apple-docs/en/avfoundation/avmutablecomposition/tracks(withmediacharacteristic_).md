---
title: 'tracks(withMediaCharacteristic:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/tracks(withmediacharacteristic:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/tracks(withmediacharacteristic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/tracks%28withmediacharacteristic%3A%29.json'
content_hash: 'sha256:1705c75665740918'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# tracks(withMediaCharacteristic:)

<sub>Instance Method</sub>

Returns tracks that contain media of a specified characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]
```

## Parameters

- `mediaCharacteristic` — The media characteristic of the tracks to return.

## Return Value

An array of composition tracks, which is empty if there are no matching tracks.

## Discussion

Apple discourages using this method. Load tracks asynchronously using [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) instead.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a composition contains.
- [- trackWithTrackID:](<track(withtrackid_).md>) — Returns a track that contains the specified identifier.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Returns tracks that contain media of a specified type.
