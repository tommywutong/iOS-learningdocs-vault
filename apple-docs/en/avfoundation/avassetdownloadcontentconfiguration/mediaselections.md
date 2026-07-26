---
title: mediaSelections
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadcontentconfiguration/mediaselections
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadcontentconfiguration/mediaselections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadcontentconfiguration/mediaselections.json'
content_hash: 'sha256:3fbca2ac296f6852'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadContentConfiguration](../avassetdownloadcontentconfiguration.md)

# mediaSelections

<sub>Instance Property</sub>

The media selections of an asset that a task downloads.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mediaSelections: [AVMediaSelection] { get set }
```

## Discussion

If your configuration doesn’t indicate a media selection, the system uses the asset’s automatic media selection.

## See Also

### Accessing configuration details

- [variantQualifiers](variantqualifiers.md) — The variant qualifiers for this configuration.
- [AVAssetVariantQualifier](../avassetvariantqualifier.md) — An object that represents an HTTP Live Streaming asset variant.
