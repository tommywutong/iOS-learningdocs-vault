---
title: 'removeTrack(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/removetrack(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/removetrack(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/removetrack%28_%3A%29.json'
content_hash: 'sha256:a3a0480ef82be32d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# removeTrack(_:)

<sub>Instance Method</sub>

Removes a specified track from the composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeTrack(_ track: AVCompositionTrack)
```

## Parameters

- `track` — The track to remove.

## Discussion

When you remove a track, the system sets its composition value to nil.

## See Also

### Managing composition tracks

- [- mutableTrackCompatibleWithTrack:](<mutabletrack(compatiblewith_).md>) — Returns a composition track into which you can insert any time range of the specified asset track.
- [- addMutableTrackWithMediaType:preferredTrackID:](<addmutabletrack(withmediatype_preferredtrackid_).md>) — Adds an empty track to a composition.
