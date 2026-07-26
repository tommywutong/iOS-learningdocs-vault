---
title: metadataItemFilter
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/metadataitemfilter
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/metadataitemfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/metadataitemfilter.json'
content_hash: 'sha256:89faa16225cf643e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# metadataItemFilter

<sub>Instance Property</sub>

An object the export session uses to filter the metadata items it transfers to the output asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var metadataItemFilter: AVMetadataItemFilter? { get set }
```

## Discussion

The default value is `nil`.

## See Also

### Configuring metadata

- [metadata](metadata.md) — The metadata an export session writes to the output container file.
