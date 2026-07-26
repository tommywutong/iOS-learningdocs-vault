---
title: 'track(withTrackID:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/track(withtrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/track(withtrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/track%28withtrackid%3A%29.json'
content_hash: 'sha256:c53b548b902c90dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# track(withTrackID:)

<sub>Instance Method</sub>

Returns a track that contains the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVMutableCompositionTrack?
```

## Parameters

- `trackID` — The persistent track identifier.

## Return Value

A composition track or `nil` if no track is available.

## Discussion

Apple discourages using this method. Load a track asynchronously using [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) instead.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a composition contains.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Returns tracks that contain media of a specified type.
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Returns tracks that contain media of a specified characteristic.
