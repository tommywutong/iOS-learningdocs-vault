---
title: 'tracks(withMediaCharacteristic:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasset/tracks(withmediacharacteristic:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/tracks(withmediacharacteristic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/tracks%28withmediacharacteristic%3A%29.json'
content_hash: 'sha256:b6ecb33c2a970d61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# tracks(withMediaCharacteristic:)

<sub>Instance Method</sub>

Returns an array of asset tracks matching the specified media characteristic.

> [!warning] Deprecated
> Use [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVAssetTrack]
```

## Parameters

- `mediaCharacteristic` — The media characteristic of the tracks to return.

## Return Value

An array of tracks, which is empty if there are no tracks with the media characteristic.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) instead.

You can call this method without blocking the current thread when the data in the [tracks](tracks.md) property is already loaded.
