---
title: 'track(withTrackID:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avfragmentedasset/track(withtrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedasset/track(withtrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedasset/track%28withtrackid%3A%29.json'
content_hash: 'sha256:59027378cbaf4409'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedAsset](../avfragmentedasset.md)

# track(withTrackID:)

<sub>Instance Method</sub>

Returns a track that contains the specified identifier.

> [!warning] Deprecated
> Use [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?
```

## Parameters

- `trackID` — The identifier of the track to return.

## Return Value

A fragmented asset track, or `nil` if no track with the specified identifier is available.

## Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load a track asynchronously using [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) instead.

You may call this method without blocking the current thread after you’ve asynchronously loaded the [tracks](../avasset/tracks.md) property.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks an asset contains. _(deprecated)_
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Returns tracks that present media of a specified type. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Returns tracks that present media of a specified characteristic. _(deprecated)_
