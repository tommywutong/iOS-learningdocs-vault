---
title: Customizing shaders using function pointers and stitching
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 26.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/customizing-shaders-using-function-pointers-and-stitching
source_url: 'https://developer.apple.com/documentation/metal/customizing-shaders-using-function-pointers-and-stitching'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/customizing-shaders-using-function-pointers-and-stitching.json'
content_hash: 'sha256:e10d25ee38975a11'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Shader libraries](shader-libraries.md)

# Customizing shaders using function pointers and stitching

<sub>Sample Code</sub>

Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.

## Overview

> [!note] Note
> This sample code project is associated with WWDC2021 session [10229: Discover compilation workflows in Metal](https://developer.apple.com/wwdc21/10229/) and WWDC2022 session [6596: Target and optimize GPU binaries with Metal 3](https://developer.apple.com/wwdc22/6596).

## See Also

### Stitched function libraries

- [MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md) — A description of a new library of procedurally generated functions.
- [MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md) — A description of a new stitched function.
- [MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md) — A call graph node that describes an input to the call graph.
- [MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md) — A call graph node that describes a function call and its inputs.
- [MTLFunctionStitchingNode](mtlfunctionstitchingnode.md) — A protocol to identify call graph nodes.
- [MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md) — An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md) — A protocol to identify types that customize how the Metal compiler stitches a function together.

## Download

- [CustomizingShadersUsingFunctionPointersAndStitching.zip](https://docs-assets.developer.apple.com/published/9978d349150a/CustomizingShadersUsingFunctionPointersAndStitching.zip)
