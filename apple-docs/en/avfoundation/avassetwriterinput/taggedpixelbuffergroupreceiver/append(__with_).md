---
title: 'append(_:with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/append(_:with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/append(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/append%28_%3Awith%3A%29.json'
content_hash: 'sha256:7181d4d67fdbdd81'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [TaggedPixelBufferGroupReceiver](../taggedpixelbuffergroupreceiver.md)

# append(_:with:)

<sub>Instance Method</sub>

Suspends until the input is ready for more media data, then appends the tagged pixel buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated(nonsending) func append(_ taggedPixelBufferGroup: [CMTaggedDynamicBuffer], with presentationTime: CMTime) async throws
```

## Parameters

- `taggedPixelBufferGroup` — The tagged pixel buffers to be appended.

- `presentationTime` — The presentation time for the tagged pixel buffers to be appended.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending tagged buffers

- [appendImmediately(_:with:)](<appendimmediately(__with_).md>) — Appends the tagged pixel buffers synchronously if the input is ready for more media data.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
