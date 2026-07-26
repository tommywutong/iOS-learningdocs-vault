---
title: 'metadata(forFormat:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassettrack/metadata(forformat:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/metadata(forformat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/metadata%28forformat%3A%29.json'
content_hash: 'sha256:d3021a4638131ea5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# metadata(forFormat:)

<sub>Instance Method</sub>

Returns metadata items that a track contains for the specified format.

> [!warning] Deprecated
> Use [- loadMetadataForFormat:completionHandler:](<loadmetadata(for_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func metadata(forFormat format: AVMetadataFormat) -> [AVMetadataItem]
```

## Parameters

- `format` — The format of the metadata items to retrieve.

## Return Value

An array of metadata items matching the specified format, or an empty array if none are found.

## Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load track metadata asynchronously using [- loadMetadataForFormat:completionHandler:](<loadmetadata(for_completionhandler_).md>) instead.

You can call this method without blocking the current thread after you’ve loaded the [availableMetadataFormats](availablemetadataformats.md) property.
