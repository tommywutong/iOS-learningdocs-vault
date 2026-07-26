---
title: 'appendImmediately(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/captionreceiver/appendimmediately(_:)-7q21r'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/appendimmediately(_:)-7q21r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/captionreceiver/appendimmediately%28_%3A%29-7q21r.json'
content_hash: 'sha256:a3ebd3dc869652b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [CaptionReceiver](../captionreceiver.md)

# appendImmediately(_:)

<sub>Instance Method</sub>

Appends the caption group synchronously if the input is ready for more media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func appendImmediately(_ captionGroup: AVCaptionGroup) throws -> Bool
```

## Parameters

- `captionGroup` — The caption group to be appended.

## Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending captions

- [append(_:)](<append(__)-4opbd.md>) — Suspends until the input is ready for more media data, then appends the caption group.
- [append(_:)](<append(__)-4wpi2.md>) — Suspends until the input is ready for more media data, then appends the caption.
- [appendImmediately(_:)](<appendimmediately(__)-9uy14.md>) — Appends the caption synchronously if the input is ready for more media data.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
