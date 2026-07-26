---
title: 'appendImmediately(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/appendimmediately(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/appendimmediately(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/appendimmediately%28_%3A%29.json'
content_hash: 'sha256:b4a4cc203a5bd5ee'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [SampleBufferReceiver](../samplebufferreceiver.md)

# appendImmediately(_:)

<sub>Instance Method</sub>

Appends the sample buffer synchronously if the input is ready for more media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func appendImmediately(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> Bool
```

## Parameters

- `sampleBuffer` — The sample buffer to be appended

## Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending samples

- [append(_:)](<append(__).md>) — Suspends until the input is ready for more media data, then appends the sample buffer.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
