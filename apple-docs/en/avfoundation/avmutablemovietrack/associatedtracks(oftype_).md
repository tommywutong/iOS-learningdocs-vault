---
title: 'associatedTracks(ofType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovietrack/associatedtracks(oftype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/associatedtracks(oftype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/associatedtracks%28oftype%3A%29.json'
content_hash: 'sha256:e147d32c4fc2c3d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# associatedTracks(ofType:)

<sub>Instance Method</sub>

Returns an array of associated tracks that have the specified association type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func associatedTracks(ofType trackAssociationType: AVAssetTrack.AssociationType) -> [AVAssetTrack]
```

## Parameters

- `trackAssociationType` — The requested track association type.

## Return Value

An array of tracks matching the specified track association type, or an empty array if none are found.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load associated tracks asynchronously using [- loadAssociatedTracksOfType:completionHandler:](<../avassettrack/loadassociatedtracks(oftype_completionhandler_).md>) instead.

You can call this method without blocking the current thread after you’ve loaded the [availableTrackAssociationTypes](../avassettrack/availabletrackassociationtypes.md) property.

## See Also

### Managing track associations

- [availableTrackAssociationTypes](availabletrackassociationtypes.md) — An array of association types that the track uses to associate with other tracks.
- [- addTrackAssociationToTrack:type:](<addtrackassociation(to_type_).md>) — Creates a specific type of track association between two tracks.
- [- removeTrackAssociationToTrack:type:](<removetrackassociation(to_type_).md>) — Removes a specific type of track association between two tracks.
