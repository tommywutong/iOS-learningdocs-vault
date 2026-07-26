---
title: preprocessorMacros
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcompileoptions/preprocessormacros
source_url: 'https://developer.apple.com/documentation/metal/mtlcompileoptions/preprocessormacros'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcompileoptions/preprocessormacros.json'
content_hash: 'sha256:5939e00e5977f280'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCompileOptions](../mtlcompileoptions.md)

# preprocessorMacros

<sub>Instance Property</sub>

A list of preprocessor macros to apply when compiling the library source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preprocessorMacros: [String : NSObject]? { get set }
```

## Discussion

Define the macros as a dictionary where each key is a string, and the values can be either an [NSString](../../foundation/nsstring.md) or [NSNumber](../../foundation/nsnumber.md) instance.

The default value is `nil`.

## See Also

### Configuring the compiler options

- [enableLogging](enablelogging.md) — A Boolean value that enables shader logging.
- [mathMode](mathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [mathFloatingPointFunctions](mathfloatingpointfunctions.md) — The FP32 math functions Metal uses.
- [preserveInvariance](preserveinvariance.md) — A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.
- [languageVersion](languageversion.md) — The language version for interpreting the library source code.
- [optimizationLevel](optimizationlevel.md) — An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [libraries](libraries.md) — An array of dynamic libraries the Metal compiler links against.
- [fastMathEnabled](fastmathenabled.md) — A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard. _(deprecated)_
