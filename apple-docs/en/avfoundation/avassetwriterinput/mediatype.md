---
title: mediaType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/mediatype
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/mediatype.json'
content_hash: 'sha256:e4389def3161004c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# mediaType

<sub>Instance Property</sub>

The media type of the samples that the input accepts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mediaType: AVMediaType { get }
```

## See Also

### Inspecting an input

- [outputSettings](outputsettings.md) — The settings to use for encoding media data you append to the output.
- [sourceFormatHint](sourceformathint.md) — A hint about the format of the sample buffers to append to the input.
