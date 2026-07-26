---
title: fastMathEnabled
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（18.0 起废弃）, iPadOS 8.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.11+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlcompileoptions/fastmathenabled
source_url: 'https://developer.apple.com/documentation/metal/mtlcompileoptions/fastmathenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcompileoptions/fastmathenabled.json'
content_hash: 'sha256:f3817dbc94ebef40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCompileOptions](../mtlcompileoptions.md)

# fastMathEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.

> [!warning] Deprecated
> Use [mathMode](mathmode.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fastMathEnabled: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md). A [true](../../swift/true.md) value also enables the high-precision variant of math functions for single-precision floating-point scalar and vector types.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Configuring the compiler options

- [enableLogging](enablelogging.md) — A Boolean value that enables shader logging.
- [mathMode](mathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [mathFloatingPointFunctions](mathfloatingpointfunctions.md) — The FP32 math functions Metal uses.
- [preserveInvariance](preserveinvariance.md) — A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.
- [languageVersion](languageversion.md) — The language version for interpreting the library source code.
- [preprocessorMacros](preprocessormacros.md) — A list of preprocessor macros to apply when compiling the library source.
- [optimizationLevel](optimizationlevel.md) — An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [libraries](libraries.md) — An array of dynamic libraries the Metal compiler links against.
