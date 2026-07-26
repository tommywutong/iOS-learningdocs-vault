---
title: sourceFormatHint
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/sourceformathint
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/sourceformathint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/sourceformathint.json'
content_hash: 'sha256:c0c61c67af0a1270'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# sourceFormatHint

<sub>Instance Property</sub>

A hint about the format of the sample buffers to append to the input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceFormatHint: CMFormatDescription? { get }
```

## Discussion

An input may use this hint to fill in missing output settings or perform additional upfront validation of samples.

> [!note] Note
> To ensure successful file writing when you initialize an input with a source format hint, only append samples of this type.

## See Also

### Inspecting an input

- [mediaType](mediatype.md) — The media type of the samples that the input accepts.
- [outputSettings](outputsettings.md) — The settings to use for encoding media data you append to the output.
