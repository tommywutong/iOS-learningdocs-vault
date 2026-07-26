---
title: averageBitRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/averagebitrate-5p1oh
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/averagebitrate-5p1oh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/averagebitrate-5p1oh.json'
content_hash: 'sha256:5c5d0779c1d8f50f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariant](../avassetvariant.md)

# averageBitRate

<sub>Instance Property</sub>

The average bit rate for the variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc var averageBitRate: Double? { get }
```

## Discussion

If the variant doesn’t define a peak bit rate, the value is negative.

## See Also

### Configuring bit rate

- [peakBitRate](peakbitrate-9hzpi.md) — The peak bit rate for the variant.
