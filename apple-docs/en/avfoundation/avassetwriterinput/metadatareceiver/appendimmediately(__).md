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
doc_path: '/documentation/avfoundation/avassetwriterinput/metadatareceiver/appendimmediately(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver/appendimmediately(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/metadatareceiver/appendimmediately%28_%3A%29.json'
content_hash: 'sha256:738238fedcdf9eb0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [MetadataReceiver](../metadatareceiver.md)

# appendImmediately(_:)

<sub>Instance Method</sub>

Appends the timed metadata group synchronously if the input is ready for more media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func appendImmediately(_ timedMetadataGroup: AVTimedMetadataGroup) throws -> Bool
```

## Parameters

- `timedMetadataGroup` — The timed metadata group to be appended

## Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

## Discussion

> [!danger] Throws
> An error if the underlying writer failed.

## See Also

### Appending metadata

- [append(_:)](<append(__).md>) — Suspends until the input is ready for more media data, then appends the timed metadata group.
- [finish()](<finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
