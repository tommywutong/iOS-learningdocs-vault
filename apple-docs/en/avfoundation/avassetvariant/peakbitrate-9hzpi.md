---
title: peakBitRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/peakbitrate-9hzpi
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/peakbitrate-9hzpi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/peakbitrate-9hzpi.json'
content_hash: 'sha256:c239ca8f6749c5ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariant](../avassetvariant.md)

# peakBitRate

<sub>Instance Property</sub>

The peak bit rate for the variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc var peakBitRate: Double? { get }
```

## Discussion

If the variant doesn’t define a peak bit rate, the value is negative.

## See Also

### Configuring bit rate

- [averageBitRate](averagebitrate-5p1oh.md) — The average bit rate for the variant.
