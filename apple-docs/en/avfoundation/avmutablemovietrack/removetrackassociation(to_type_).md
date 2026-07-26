---
title: 'removeTrackAssociation(to:type:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovietrack/removetrackassociation(to:type:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/removetrackassociation(to:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/removetrackassociation%28to%3Atype%3A%29.json'
content_hash: 'sha256:319440c09284eb66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# removeTrackAssociation(to:type:)

<sub>Instance Method</sub>

Removes a specific type of track association between two tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func removeTrackAssociation(to movieTrack: AVMovieTrack, type trackAssociationType: AVAssetTrack.AssociationType)
```

## Parameters

- `movieTrack` — The AVMovieTrack object that is associated with the receiver.

- `trackAssociationType` — The type of track association to remove between the receiver and the specified movie track.

## See Also

### Managing track associations

- [availableTrackAssociationTypes](availabletrackassociationtypes.md) — An array of association types that the track uses to associate with other tracks.
- [- associatedTracksOfType:](<associatedtracks(oftype_).md>) — Returns an array of associated tracks that have the specified association type.
- [- addTrackAssociationToTrack:type:](<addtrackassociation(to_type_).md>) — Creates a specific type of track association between two tracks.
