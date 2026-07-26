---
title: MTLLibraryOptimizationLevel.size
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibraryoptimizationlevel/size
source_url: 'https://developer.apple.com/documentation/metal/mtllibraryoptimizationlevel/size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibraryoptimizationlevel/size.json'
content_hash: 'sha256:7e014f9cdf0d281c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibraryOptimizationLevel](../mtllibraryoptimizationlevel.md)

# MTLLibraryOptimizationLevel.size

<sub>Case</sub>

An optimization option for the Metal compiler that prioritizes minimizing the size of its output binaries, which may also reduce compile time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case size
```

## Discussion

This option is similar to [MTLLibraryOptimizationLevelDefault](default.md), but adds optimizations that prioritize minimizing a shader’s executable size, which may also reduce compile time.

## See Also

### Optimization options

- [MTLLibraryOptimizationLevelDefault](default.md) — An optimization option for the Metal compiler that prioritizes runtime performance.
