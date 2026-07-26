---
title: 'associatedTracks(ofType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（16.0 起废弃）, iPadOS 7.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.9+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassettrack/associatedtracks(oftype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/associatedtracks(oftype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/associatedtracks%28oftype%3A%29.json'
content_hash: 'sha256:c006b5034ea1a9db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# associatedTracks(ofType:)

<sub>Instance Method</sub>

Returns an array of associated tracks that have the specified association type.

> [!warning] Deprecated
> Use [- loadAssociatedTracksOfType:completionHandler:](<loadassociatedtracks(oftype_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func associatedTracks(ofType trackAssociationType: AVAssetTrack.AssociationType) -> [AVAssetTrack]
```

## Parameters

- `trackAssociationType` — The requested track association type.

## Return Value

An array of tracks matching the specified track association type, or an empty array if none are found.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load associated tracks asynchronously using [- loadAssociatedTracksOfType:completionHandler:](<loadassociatedtracks(oftype_completionhandler_).md>) instead.

You can call this method without blocking the current thread after you’ve loaded the [availableTrackAssociationTypes](availabletrackassociationtypes.md) property.
