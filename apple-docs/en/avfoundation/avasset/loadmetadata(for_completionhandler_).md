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
doc_path: '/documentation/avfoundation/avasset/loadmetadata(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/loadmetadata(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/loadmetadata%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:9bfaaeba312d8177'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# loadMetadata(for:completionHandler:)

<sub>Instance Method</sub>

Loads an array of metadata items that the asset contains for the specified format.

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

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **metadata** — An array of metadata items, which may be empty if there are no items of the specified format. The value is `nil` if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading metadata

- [metadata](../avpartialasyncproperty/metadata-16qej.md) — The metadata items that an asset contains for all metadata identifiers.
- [commonMetadata](../avpartialasyncproperty/commonmetadata-3j3n4.md) — The metadata items that an asset contains for common metadata identifiers.
- [availableMetadataFormats](../avpartialasyncproperty/availablemetadataformats-4yiq8.md) — The formats of metadata that an asset contains.
- [creationDate](../avpartialasyncproperty/creationdate.md) — A metadata item that indicates the creation date of an asset.
- [lyrics](../avpartialasyncproperty/lyrics.md) — The lyrics of the asset in a language suitable for the current locale.
