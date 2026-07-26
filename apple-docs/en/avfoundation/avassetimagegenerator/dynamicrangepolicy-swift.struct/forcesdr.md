---
title: forceSDR
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct/forcesdr
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct/forcesdr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct/forcesdr.json'
content_hash: 'sha256:79615c213bfac3a7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetImageGenerator](../../avassetimagegenerator.md) · [DynamicRangePolicy](../dynamicrangepolicy-swift.struct.md)

# forceSDR

<sub>Type Property</sub>

A policy that forces conversion to standard dynamic range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let forceSDR: AVAssetImageGenerator.DynamicRangePolicy
```

## Discussion

This policy converts PQ or HLG transfer functions to 709, while maintaining color primaries and matrix.

## See Also

### Policies

- [AVAssetImageGeneratorDynamicRangePolicyMatchSource](matchsource.md) — A policy that preserves the color parameters of the source media.
