---
title: outputSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/outputsettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/outputsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/outputsettings.json'
content_hash: 'sha256:5b62f4374fc4838f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# outputSettings

<sub>Instance Property</sub>

The settings to use for encoding media data you append to the output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputSettings: [String : Any]? { get }
```

## Discussion

A value of `nil` indicates that the input passes the samples through to the output without reencoding them.

## See Also

### Inspecting an input

- [mediaType](mediatype.md) — The media type of the samples that the input accepts.
- [sourceFormatHint](sourceformathint.md) — A hint about the format of the sample buffers to append to the input.
