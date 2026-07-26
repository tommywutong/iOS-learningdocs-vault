---
title: copyNextSampleBuffer
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutput/copynextsamplebuffer
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/copynextsamplebuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutput/copynextsamplebuffer.json'
content_hash: 'sha256:68ef2b00a08318c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSampleBufferOutput](../avplayeritemsamplebufferoutput.md)

# copyNextSampleBuffer

<sub>Instance Method</sub>

Copies the next sample buffer for the output synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (CMSampleBufferRef) copyNextSampleBuffer;
```

## Return Value

A CMSampleBuffer object referencing the output sample buffer.

## Discussion

The client is responsible for calling `CFRelease` on the returned `CMSampleBuffer` object when finished with it. This method will return `NULL` if there are no more sample buffers currently available for the receiver. Clients may use the delegate method `outputMediaDataAvailable:` to be informed when the next `CMSampleBuffer` becomes available.
