---
title: availableMetadataFormats
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/availablemetadataformats
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/availablemetadataformats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/availablemetadataformats.json'
content_hash: 'sha256:e5042e39f0dc1ba2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# availableMetadataFormats

<sub>Instance Property</sub>

The metadata formats this asset contains.

> [!warning] Deprecated
> Load the value of [availableMetadataFormats](../avpartialasyncproperty/availablemetadataformats-4yiq8.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var availableMetadataFormats: [AVMetadataFormat] { get }
```

## Discussion

Metadata formats may include ID3, iTunes metadata, and so on.
