---
title: 'tracks(withMediaType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avfragmentedasset/tracks(withmediatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedasset/tracks(withmediatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedasset/tracks%28withmediatype%3A%29.json'
content_hash: 'sha256:ef07e3e11fbbdbbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedAsset](../avfragmentedasset.md)

# tracks(withMediaType:)

<sub>Instance Method</sub>

Returns tracks that present media of a specified type.

> [!warning] Deprecated
> Use [- loadTracksWithMediaType:completionHandler:](<loadtracks(withmediatype_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVFragmentedAssetTrack]
```

## Parameters

- `mediaType` — The media type according to which the asset filters its tracks. For valid values see [AVMediaType](../avmediatype.md).

## Return Value

An array of tracks of a specific media characteristic.

## Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load tracks asynchronously using [- loadTracksWithMediaType:completionHandler:](<loadtracks(withmediatype_completionhandler_).md>) instead.

You may call this method without blocking the current thread after you’ve asynchronously loaded the [tracks](../avasset/tracks.md) property.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks an asset contains. _(deprecated)_
- [- trackWithTrackID:](<track(withtrackid_).md>) — Returns a track that contains the specified identifier. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Returns tracks that present media of a specified characteristic. _(deprecated)_
