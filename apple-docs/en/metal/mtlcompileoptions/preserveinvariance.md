---
title: preserveInvariance
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcompileoptions/preserveinvariance
source_url: 'https://developer.apple.com/documentation/metal/mtlcompileoptions/preserveinvariance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcompileoptions/preserveinvariance.json'
content_hash: 'sha256:4c2ea5230508aa77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCompileOptions](../mtlcompileoptions.md)

# preserveInvariance

<sub>Instance Property</sub>

A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preserveInvariance: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). When [true](../../swift/true.md), the Metal shader compiler looks at the position value in all vertex output structures that it compiles. If the position value also has the `[[invariant]]` attribute, the compiler compiles the corresponding vertex shader conservatively to guarantee that the GPU performs the calculations the same way. You need to preserve invariance when your renderer contains multiple render passes and requires the same position calculations in each render pass.

## See Also

### Configuring the compiler options

- [enableLogging](enablelogging.md) — A Boolean value that enables shader logging.
- [mathMode](mathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [mathFloatingPointFunctions](mathfloatingpointfunctions.md) — The FP32 math functions Metal uses.
- [languageVersion](languageversion.md) — The language version for interpreting the library source code.
- [preprocessorMacros](preprocessormacros.md) — A list of preprocessor macros to apply when compiling the library source.
- [optimizationLevel](optimizationlevel.md) — An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [libraries](libraries.md) — An array of dynamic libraries the Metal compiler links against.
- [fastMathEnabled](fastmathenabled.md) — A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard. _(deprecated)_
