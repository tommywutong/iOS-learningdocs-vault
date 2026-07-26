---
title: finish()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/captionreceiver/finish()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/finish()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/captionreceiver/finish%28%29.json'
content_hash: 'sha256:d33dbb51f97a1fa8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [CaptionReceiver](../captionreceiver.md)

# finish()

<sub>Instance Method</sub>

Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func finish()
```

## See Also

### Appending captions

- [append(_:)](<append(__)-4opbd.md>) — Suspends until the input is ready for more media data, then appends the caption group.
- [append(_:)](<append(__)-4wpi2.md>) — Suspends until the input is ready for more media data, then appends the caption.
- [appendImmediately(_:)](<appendimmediately(__)-7q21r.md>) — Appends the caption group synchronously if the input is ready for more media data.
- [appendImmediately(_:)](<appendimmediately(__)-9uy14.md>) — Appends the caption synchronously if the input is ready for more media data.
