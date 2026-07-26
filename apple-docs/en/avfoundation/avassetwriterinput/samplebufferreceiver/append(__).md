---
title: 'append(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/append(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/append%28_%3A%29.json'
content_hash: 'sha256:64e1f649078d1939'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [SampleBufferReceiver](../samplebufferreceiver.md)

# append(_:)

<sub>Instance Method</sub>

Suspends until the input is ready for more media data, then appends the sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated(nonsending) func append(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws
```

## Parameters

- `sampleBuffer` — The sample buffer to be appended.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending samples

- [appendImmediately(_:)](<appendimmediately(__).md>) — Appends the sample buffer synchronously if the input is ready for more media data.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
