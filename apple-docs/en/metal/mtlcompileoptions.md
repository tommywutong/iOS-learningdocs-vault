---
title: MTLCompileOptions
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcompileoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlcompileoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcompileoptions.json'
content_hash: 'sha256:142980cd97ceafee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCompileOptions

<sub>Class</sub>

Compilation settings for a Metal shader library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLCompileOptions
```

## Overview

You can configure the Metal compiler’s options by setting any or all of an [MTLCompileOptions](mtlcompileoptions.md) instance’s properties, including the following:

- Target previous OS releases by assigning the [languageVersion](mtlcompileoptions/languageversion.md) property to an [MTLLanguageVersion](mtllanguageversion.md) case.
- Set preprocessor macros for the Metal compiler by assigning a dictionary to the [preprocessorMacros](mtlcompileoptions/preprocessormacros.md) property.
- Choose what the Metal compiler’s optimizer prioritizes by setting the [optimizationLevel](mtlcompileoptions/optimizationlevel.md) property to an [MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md) case.
- Allow the compiler to optimize for floating-point arithmetic that may violate the IEEE 754 standard by setting [mathMode](mtlcompileoptions/mathmode.md) to [MTLMathModeFast](mtlmathmode/fast.md).

You can compile a library with your compile options instance by calling an [MTLDevice](mtldevice.md) instance’s [- newLibraryWithSource:options:error:](<mtldevice/makelibrary(source_options_).md>) or [- newLibraryWithSource:options:completionHandler:](<mtldevice/makelibrary(source_options_completionhandler_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the compiler options

- [enableLogging](mtlcompileoptions/enablelogging.md) — A Boolean value that enables shader logging.
- [mathMode](mtlcompileoptions/mathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [mathFloatingPointFunctions](mtlcompileoptions/mathfloatingpointfunctions.md) — The FP32 math functions Metal uses.
- [preserveInvariance](mtlcompileoptions/preserveinvariance.md) — A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.
- [languageVersion](mtlcompileoptions/languageversion.md) — The language version for interpreting the library source code.
- [preprocessorMacros](mtlcompileoptions/preprocessormacros.md) — A list of preprocessor macros to apply when compiling the library source.
- [optimizationLevel](mtlcompileoptions/optimizationlevel.md) — An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [libraries](mtlcompileoptions/libraries.md) — An array of dynamic libraries the Metal compiler links against.
- [fastMathEnabled](mtlcompileoptions/fastmathenabled.md) — A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard. _(deprecated)_

### Configuring the library output options

- [libraryType](mtlcompileoptions/librarytype.md) — The kind of library to create.
- [installName](mtlcompileoptions/installname.md) — For a dynamic library, the name to use when installing the library.

### Instance Properties

- [allowReferencingUndefinedSymbols](mtlcompileoptions/allowreferencingundefinedsymbols.md)
- [compileSymbolVisibility](mtlcompileoptions/compilesymbolvisibility.md)
- [floatingPointConversionRoundingMode](mtlcompileoptions/floatingpointconversionroundingmode.md) _(beta)_
- [maxTotalThreadsPerThreadgroup](mtlcompileoptions/maxtotalthreadsperthreadgroup.md)
- [requiredThreadsPerThreadgroup](mtlcompileoptions/requiredthreadsperthreadgroup.md)

## See Also

### Shader library management

- [MTLLibrary](mtllibrary.md) — A collection of Metal shader functions.
- [MTLDynamicLibrary](mtldynamiclibrary.md) — A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [MTLBinaryArchive](mtlbinaryarchive.md) — A container for pipeline state descriptors and their associated compiled shader code.
- [MTLLibraryType](mtllibrarytype.md) — A set of options for Metal library types.
- [MTLLanguageVersion](mtllanguageversion.md) — Metal shading language versions.
- [MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md) — The optimization options for the Metal compiler.
