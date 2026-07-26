---
title: 'append(_:with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/append(_:with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/append(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/append%28_%3Awith%3A%29.json'
content_hash: 'sha256:4f8f7491b37fadc1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [PixelBufferReceiver](../pixelbufferreceiver.md)

# append(_:with:)

<sub>Instance Method</sub>

Suspends until the input is ready for more media data, then appends the pixel buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated(nonsending) func append(_ pixelBuffer: CVReadOnlyPixelBuffer, with presentationTime: CMTime) async throws
```

## Parameters

- `pixelBuffer` — The pixel buffer to be appended.

- `presentationTime` — The presentation time for the pixel buffer to be appended.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending pixel buffers

- [appendImmediately(_:with:)](<appendimmediately(__with_).md>) — Appends the pixel buffer synchronously if the input is ready for more media data.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
