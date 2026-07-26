---
title: optimizationLevel
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcompileoptions/optimizationlevel
source_url: 'https://developer.apple.com/documentation/metal/mtlcompileoptions/optimizationlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcompileoptions/optimizationlevel.json'
content_hash: 'sha256:46856537f783de7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCompileOptions](../mtlcompileoptions.md)

# optimizationLevel

<sub>Instance Property</sub>

An option that tells the compiler what to prioritize when it compiles Metal shader code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var optimizationLevel: MTLLibraryOptimizationLevel { get set }
```

## See Also

### Configuring the compiler options

- [enableLogging](enablelogging.md) — A Boolean value that enables shader logging.
- [mathMode](mathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [mathFloatingPointFunctions](mathfloatingpointfunctions.md) — The FP32 math functions Metal uses.
- [preserveInvariance](preserveinvariance.md) — A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.
- [languageVersion](languageversion.md) — The language version for interpreting the library source code.
- [preprocessorMacros](preprocessormacros.md) — A list of preprocessor macros to apply when compiling the library source.
- [libraries](libraries.md) — An array of dynamic libraries the Metal compiler links against.
- [fastMathEnabled](fastmathenabled.md) — A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard. _(deprecated)_
