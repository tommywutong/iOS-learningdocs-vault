---
title: 'tracks(withMediaType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasset/tracks(withmediatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/tracks(withmediatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/tracks%28withmediatype%3A%29.json'
content_hash: 'sha256:dad22d35e6c34da6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# tracks(withMediaType:)

<sub>Instance Method</sub>

Returns tracks that contain media of a specified type.

> [!warning] Deprecated
> Use [- loadTracksWithMediaType:completionHandler:](<loadtracks(withmediatype_completionhandler_).md>)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVAssetTrack]
```

## Parameters

- `mediaType` — The media type of the tracks to return.

## Return Value

An array of tracks, which is empty if there are no tracks with the media type.

## Discussion

\\You can call this method without blocking the current thread when the data in the [tracks](tracks.md) property is already loaded.
