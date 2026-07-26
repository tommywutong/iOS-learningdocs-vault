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
doc_path: /documentation/avfoundation/avassetwriterinput/samplebufferreceiver/finish()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/finish()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/finish%28%29.json'
content_hash: 'sha256:179f6793d43cf305'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [SampleBufferReceiver](../samplebufferreceiver.md)

# finish()

<sub>Instance Method</sub>

Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finish()
```

## See Also

### Appending samples

- [append(_:)](<append(__).md>) — Suspends until the input is ready for more media data, then appends the sample buffer.
- [appendImmediately(_:)](<appendimmediately(__).md>) — Appends the sample buffer synchronously if the input is ready for more media data.
