---
title: finish()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/finish()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/finish()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/finish%28%29.json'
content_hash: 'sha256:b5b4b8857abe0217'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [TaggedPixelBufferGroupReceiver](../taggedpixelbuffergroupreceiver.md)

# finish()

<sub>Instance Method</sub>

Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func finish()
```

## See Also

### Appending tagged buffers

- [append(_:with:)](<append(__with_).md>) — Suspends until the input is ready for more media data, then appends the tagged pixel buffers.
- [appendImmediately(_:with:)](<appendimmediately(__with_).md>) — Appends the tagged pixel buffers synchronously if the input is ready for more media data.
