---
title: cancel()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffergeneratorbatch/cancel()
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergeneratorbatch/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergeneratorbatch/cancel%28%29.json'
content_hash: 'sha256:64c190c8ea38e968'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferGeneratorBatch](../avsamplebuffergeneratorbatch.md)

# cancel()

<sub>Instance Method</sub>

Cancels any I/O for this batch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

The system invokes the associated sample buffers data ready handlers with an error.
