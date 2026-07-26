---
title: 'loadMetadata(for:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassettrack/loadmetadata(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/loadmetadata(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/loadmetadata%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:f6aaf0bc4938d2b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# loadMetadata(for:completionHandler:)

<sub>Instance Method</sub>

Loads metadata items that a track contains for the specified format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadMetadata(for format: AVMetadataFormat, completionHandler: @escaping @Sendable ([AVMetadataItem]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadMetadata(for format: AVMetadataFormat) async throws -> [AVMetadataItem]
```

## Parameters

- `format` — The format of the metadata items to load.

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **metadata** — The loaded metadata, or an empty array if no metadata items for the specified format exist. The value is `nil` if an error occurs. - **error** — An error object if the request fails; otherwise, nil.

## See Also

### Loading metadata

- [metadata](../avpartialasyncproperty/metadata-6e14c.md) — An array of metadata items for all metadata identifiers that have a value.
- [commonMetadata](../avpartialasyncproperty/commonmetadata-73m58.md) — An array of metadata items for all common metadata keys that have a value.
- [availableMetadataFormats](../avpartialasyncproperty/availablemetadataformats-5p9xg.md) — An array of metadata formats available for the track.
