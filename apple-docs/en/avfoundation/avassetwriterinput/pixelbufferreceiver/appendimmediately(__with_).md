---
title: 'appendImmediately(_:with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/appendimmediately(_:with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/appendimmediately(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/appendimmediately%28_%3Awith%3A%29.json'
content_hash: 'sha256:0a2c2ac34a5e3980'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [PixelBufferReceiver](../pixelbufferreceiver.md)

# appendImmediately(_:with:)

<sub>Instance Method</sub>

Appends the pixel buffer synchronously if the input is ready for more media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func appendImmediately(_ pixelBuffer: CVReadOnlyPixelBuffer, with presentationTime: CMTime) throws -> Bool
```

## Parameters

- `pixelBuffer` — The pixel buffer to be appended.

- `presentationTime` — The presentation time for the pixel buffer to be appended.

## Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending pixel buffers

- [append(_:with:)](<append(__with_).md>) — Suspends until the input is ready for more media data, then appends the pixel buffer.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
