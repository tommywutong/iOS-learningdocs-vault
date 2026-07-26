---
title: 'append(_:withPresentationTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/append(_:withpresentationtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/append(_:withpresentationtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/append%28_%3Awithpresentationtime%3A%29.json'
content_hash: 'sha256:f35b60e6b3606077'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputPixelBufferAdaptor](../avassetwriterinputpixelbufferadaptor.md)

# append(_:withPresentationTime:)

<sub>Instance Method</sub>

Appends a pixel buffer to the adaptor.

> [!warning] Deprecated
> Use AVAssetWriter.inputPixelBufferReceiver(for:pixelBufferAttributes:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func append(_ pixelBuffer: CVPixelBuffer, withPresentationTime presentationTime: CMTime) -> Bool
```

## Parameters

- `pixelBuffer` — The pixel buffer to append.

- `presentationTime` — The pixel buffer’s presentation time. The time you specify is relative to the time you called [- startSessionAtSourceTime:](<../avassetwriter/startsession(atsourcetime_).md>) with.

## Return Value

[true](../../swift/true.md) if the adaptor appends the pixel buffer; otherwise, [false](../../swift/false.md).
