---
title: MTLStitchedLibraryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstitchedlibrarydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlstitchedlibrarydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstitchedlibrarydescriptor.json'
content_hash: 'sha256:986f6fb7136ba8cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStitchedLibraryDescriptor

<sub>Class</sub>

A description of a new library of procedurally generated functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLStitchedLibraryDescriptor
```

## Overview

An [MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md) describes a library of new stitched functions. A _stitched function_ is a visible function you create by composing other Metal shader functions together in a function graph.

Configure a stitched library descriptor by assigning an array of one or more [MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md) instances, each describing a stitched function, to the [functionGraphs](mtlstitchedlibrarydescriptor/functiongraphs.md) property. Then assign an [MTLFunction](mtlfunction.md) array that includes all the functions the graphs depend on to the [functions](mtlstitchedlibrarydescriptor/functions.md) property.

Create a stitched library from the descriptor by passing it to the [- newLibraryWithStitchedDescriptor:error:](<mtldevice/makelibrary(stitcheddescriptor_).md>) method of an [MTLDevice](mtldevice.md). You can change the descriptor to create other libraries without affecting any existing ones.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring a stitched library

- [functions](mtlstitchedlibrarydescriptor/functions.md) — The list of functions for creating the stitched library.
- [functionGraphs](mtlstitchedlibrarydescriptor/functiongraphs.md) — The function graphs that define the new stitched library’s functions.

### Instance Properties

- [binaryArchives](mtlstitchedlibrarydescriptor/binaryarchives.md)
- [options](mtlstitchedlibrarydescriptor/options.md)

## See Also

### Stitched function libraries

- [Customizing shaders using function pointers and stitching](customizing-shaders-using-function-pointers-and-stitching.md) — Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md) — A description of a new stitched function.
- [MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md) — A call graph node that describes an input to the call graph.
- [MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md) — A call graph node that describes a function call and its inputs.
- [MTLFunctionStitchingNode](mtlfunctionstitchingnode.md) — A protocol to identify call graph nodes.
- [MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md) — An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md) — A protocol to identify types that customize how the Metal compiler stitches a function together.
