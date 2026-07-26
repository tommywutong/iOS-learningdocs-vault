---
title: 'removeTrackAssociation(to:type:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecompositiontrack/removetrackassociation(to:type:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/removetrackassociation(to:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecompositiontrack/removetrackassociation%28to%3Atype%3A%29.json'
content_hash: 'sha256:741cdee87e574349'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCompositionTrack](../avmutablecompositiontrack.md)

# removeTrackAssociation(to:type:)

<sub>Instance Method</sub>

Removes an association from a composition track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeTrackAssociation(to compositionTrack: AVCompositionTrack, type trackAssociationType: AVAssetTrack.AssociationType)
```

## Parameters

- `compositionTrack` — A composition track to remove the association from.

- `trackAssociationType` — The type of track association to remove.

## See Also

### Associating tracks

- [- addTrackAssociationToTrack:type:](<addtrackassociation(to_type_).md>) — Establishes a track association of a specific type between two tracks.
