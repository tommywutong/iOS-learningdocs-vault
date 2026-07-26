---
title: mathFloatingPointFunctions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcompileoptions/mathfloatingpointfunctions
source_url: 'https://developer.apple.com/documentation/metal/mtlcompileoptions/mathfloatingpointfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcompileoptions/mathfloatingpointfunctions.json'
content_hash: 'sha256:5a19ebbf090f77f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCompileOptions](../mtlcompileoptions.md)

# mathFloatingPointFunctions

<sub>Instance Property</sub>

The FP32 math functions Metal uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mathFloatingPointFunctions: MTLMathFloatingPointFunctions { get set }
```

## Topics

### Supporting types

- [MTLMathFloatingPointFunctions](../mtlmathfloatingpointfunctions.md) — Indicates which FP32 math functions Metal uses.

## See Also

### Configuring the compiler options

- [enableLogging](enablelogging.md) — A Boolean value that enables shader logging.
- [mathMode](mathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [preserveInvariance](preserveinvariance.md) — A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.
- [languageVersion](languageversion.md) — The language version for interpreting the library source code.
- [preprocessorMacros](preprocessormacros.md) — A list of preprocessor macros to apply when compiling the library source.
- [optimizationLevel](optimizationlevel.md) — An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [libraries](libraries.md) — An array of dynamic libraries the Metal compiler links against.
- [fastMathEnabled](fastmathenabled.md) — A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard. _(deprecated)_
