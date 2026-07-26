---
title: 'appendImmediately(_:with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/appendimmediately(_:with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/appendimmediately(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/appendimmediately%28_%3Awith%3A%29.json'
content_hash: 'sha256:b08ff7b896e0f14c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [TaggedPixelBufferGroupReceiver](../taggedpixelbuffergroupreceiver.md)

# appendImmediately(_:with:)

<sub>Instance Method</sub>

Appends the tagged pixel buffers synchronously if the input is ready for more media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func appendImmediately(_ taggedPixelBufferGroup: [CMTaggedDynamicBuffer], with presentationTime: CMTime) throws -> Bool
```

## Parameters

- `taggedPixelBufferGroup` — The tagged pixel buffers to be appended.

- `presentationTime` — The presentation time for the tagged pixel buffers to be appended.

## Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending tagged buffers

- [append(_:with:)](<append(__with_).md>) — Suspends until the input is ready for more media data, then appends the tagged pixel buffers.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
