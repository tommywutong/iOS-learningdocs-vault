---
title: 'append(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/metadatareceiver/append(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/metadatareceiver/append%28_%3A%29.json'
content_hash: 'sha256:880221bbe295e9b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [MetadataReceiver](../metadatareceiver.md)

# append(_:)

<sub>Instance Method</sub>

Suspends until the input is ready for more media data, then appends the timed metadata group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated(nonsending) func append(_ timedMetadataGroup: AVTimedMetadataGroup) async throws
```

## Parameters

- `timedMetadataGroup` — The timed metadata group to be appended.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending metadata

- [appendImmediately(_:)](<appendimmediately(__).md>) — Appends the timed metadata group synchronously if the input is ready for more media data.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
