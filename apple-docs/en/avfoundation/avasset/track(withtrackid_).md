---
title: 'track(withTrackID:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasset/track(withtrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/track(withtrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/track%28withtrackid%3A%29.json'
content_hash: 'sha256:60196cd02a30da03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# track(withTrackID:)

<sub>Instance Method</sub>

Returns a track that contains the specified identifier.

> [!warning] Deprecated
> Use [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVAssetTrack?
```

## Parameters

- `trackID` — The identifier of the track to retrieve.

## Return Value

An asset track, or `nil` if there is no track with the identifier.

## Discussion

You can call this method without blocking the current thread when the data in the [tracks](tracks.md) property is already loaded.
