---
title: finish()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/metadatareceiver/finish()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver/finish()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/metadatareceiver/finish%28%29.json'
content_hash: 'sha256:540d7b1b44f30117'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [MetadataReceiver](../metadatareceiver.md)

# finish()

<sub>Instance Method</sub>

Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finish()
```

## See Also

### Appending metadata

- [append(_:)](<append(__).md>) — Suspends until the input is ready for more media data, then appends the timed metadata group.
- [appendImmediately(_:)](<appendimmediately(__).md>) — Appends the timed metadata group synchronously if the input is ready for more media data.
