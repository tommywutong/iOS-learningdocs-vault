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
doc_path: '/documentation/avfoundation/avcomposition/track(withtrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/track(withtrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/track%28withtrackid%3A%29.json'
content_hash: 'sha256:562a404145cc339d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# track(withTrackID:)

<sub>Instance Method</sub>

Returns a track that contains the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVCompositionTrack?
```

## Parameters

- `trackID` — The identifier of the track to retrieve.

## Return Value

A composition track, or `nil` if no track with the identifier exists.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a track asynchronously using [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) instead.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a composition contains.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Returns tracks that contain media of a specified type.
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Returns tracks that contain media of a specified characteristic.
- [- unusedTrackID](<unusedtrackid().md>) — Returns an identifier that no other tracks in the asset use.
