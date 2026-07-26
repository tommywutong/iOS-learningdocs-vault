---
title: 'mutableTrack(compatibleWith:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/mutabletrack(compatiblewith:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/mutabletrack(compatiblewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/mutabletrack%28compatiblewith%3A%29.json'
content_hash: 'sha256:6d7ac93296c1502a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# mutableTrack(compatibleWith:)

<sub>Instance Method</sub>

Returns a composition track into which you can insert any time range of the specified asset track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableTrack(compatibleWith track: AVAssetTrack) -> AVMutableCompositionTrack?
```

## Parameters

- `track` — The asset track to find a composition track for.

## Return Value

A mutable composition track, of `nil` if a compatible track isn’t available.

## Discussion

To optimize performance, limit the number of tracks to only what you need to present media data in parallel. To present media data of the same type serially, even from multiple assets, use a single track of that media type. You use this method to identify a suitable existing target track for an insertion.

If there’s no compatible track available, you can create a new track of the same media type as `track` using [- addMutableTrackWithMediaType:preferredTrackID:](<addmutabletrack(withmediatype_preferredtrackid_).md>).

This method is the counterpart to [- compatibleTrackForCompositionTrack:](<../avurlasset/compatibletrack(for_).md>) on [AVAsset](../avasset.md).

## See Also

### Managing composition tracks

- [- addMutableTrackWithMediaType:preferredTrackID:](<addmutabletrack(withmediatype_preferredtrackid_).md>) — Adds an empty track to a composition.
- [- removeTrack:](<removetrack(__).md>) — Removes a specified track from the composition.
