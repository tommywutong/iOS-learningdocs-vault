---
title: 'compatibleTrack(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avurlasset/compatibletrack(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/compatibletrack(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/compatibletrack%28for%3A%29.json'
content_hash: 'sha256:61241902afd06c3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# compatibleTrack(for:)

<sub>Instance Method</sub>

Returns an asset track from which you can insert any time range into a given composition track.

> [!warning] Deprecated
> Use [- findCompatibleTrackForCompositionTrack:completionHandler:](<findcompatibletrack(for_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func compatibleTrack(for compositionTrack: AVCompositionTrack) -> AVAssetTrack?
```

## Parameters

- `compositionTrack` — The composition track.

## Return Value

An asset track managed by the asset from which any time range can be inserted into a given composition track.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load compatible tracks asynchronously using [- findCompatibleTrackForCompositionTrack:completionHandler:](<findcompatibletrack(for_completionhandler_).md>) instead.

This method is the logical complement of [- mutableTrackCompatibleWithTrack:](<../avmutablecomposition/mutabletrack(compatiblewith_).md>).
