---
title: 'append(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/captionreceiver/append(_:)-4opbd'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/append(_:)-4opbd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/captionreceiver/append%28_%3A%29-4opbd.json'
content_hash: 'sha256:78b7e5747ced83b8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [CaptionReceiver](../captionreceiver.md)

# append(_:)

<sub>Instance Method</sub>

Suspends until the input is ready for more media data, then appends the caption group.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated(nonsending) func append(_ captionGroup: AVCaptionGroup) async throws
```

## Parameters

- `captionGroup` — The caption group to be appended.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending captions

- [append(_:)](<append(__)-4wpi2.md>) — Suspends until the input is ready for more media data, then appends the caption.
- [appendImmediately(_:)](<appendimmediately(__)-7q21r.md>) — Appends the caption group synchronously if the input is ready for more media data.
- [appendImmediately(_:)](<appendimmediately(__)-9uy14.md>) — Appends the caption synchronously if the input is ready for more media data.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
