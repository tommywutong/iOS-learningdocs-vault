---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/metadata.json'
content_hash: 'sha256:fdf33fab99388846'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# metadata

<sub>Instance Property</sub>

The metadata an export session writes to the output container file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var metadata: [AVMetadataItem]? { get set }
```

## See Also

### Configuring metadata

- [metadataItemFilter](metadataitemfilter.md) — An object the export session uses to filter the metadata items it transfers to the output asset.
