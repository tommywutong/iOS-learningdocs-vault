---
title: matchSource
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct/matchsource
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct/matchsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct/matchsource.json'
content_hash: 'sha256:b9d991805e7f6ec1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetImageGenerator](../../avassetimagegenerator.md) · [DynamicRangePolicy](../dynamicrangepolicy-swift.struct.md)

# matchSource

<sub>Type Property</sub>

A policy that preserves the color parameters of the source media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let matchSource: AVAssetImageGenerator.DynamicRangePolicy
```

## Discussion

By default, an image generator converts images to standard dynamic range. When working with HDR video, use this policy to preserve HDR color in the resulting images.

## See Also

### Policies

- [AVAssetImageGeneratorDynamicRangePolicyForceSDR](forcesdr.md) — A policy that forces conversion to standard dynamic range.
