---
title: availableTrackAssociationTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/availabletrackassociationtypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/availabletrackassociationtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/availabletrackassociationtypes.json'
content_hash: 'sha256:a98a3d0dd2a72eda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# availableTrackAssociationTypes

<sub>Instance Property</sub>

An array of association types that the track uses to associate with other tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var availableTrackAssociationTypes: [AVAssetTrack.AssociationType] { get }
```

## See Also

### Managing track associations

- [- associatedTracksOfType:](<associatedtracks(oftype_).md>) — Returns an array of associated tracks that have the specified association type.
- [- addTrackAssociationToTrack:type:](<addtrackassociation(to_type_).md>) — Creates a specific type of track association between two tracks.
- [- removeTrackAssociationToTrack:type:](<removetrackassociation(to_type_).md>) — Removes a specific type of track association between two tracks.
