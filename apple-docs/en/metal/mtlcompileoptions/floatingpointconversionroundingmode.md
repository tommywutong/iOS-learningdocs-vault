---
title: floatingPointConversionRoundingMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/metal/mtlcompileoptions/floatingpointconversionroundingmode
source_url: 'https://developer.apple.com/documentation/metal/mtlcompileoptions/floatingpointconversionroundingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcompileoptions/floatingpointconversionroundingmode.json'
content_hash: 'sha256:03542ab29f141657'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCompileOptions](../mtlcompileoptions.md)

# floatingPointConversionRoundingMode

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var floatingPointConversionRoundingMode: MTLFloatingPointConversionRoundingMode { get set }
```

## Discussion

Sets the rounding mode for narrowing floating-point conversions. Default is MTLFloatingPointConversionRoundingModeToNearestEven.
