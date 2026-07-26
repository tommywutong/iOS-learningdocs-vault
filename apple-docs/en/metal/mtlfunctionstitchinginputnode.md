---
title: MTLFunctionStitchingInputNode
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchinginputnode
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchinginputnode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchinginputnode.json'
content_hash: 'sha256:70832515c585d9c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionStitchingInputNode

<sub>Class</sub>

A call graph node that describes an input to the call graph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLFunctionStitchingInputNode
```

## Overview

An input node contains data from one of the stitched function’s parameters. The output data type of an input node has the same type as the matching parameter.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MTLFunctionStitchingNode](mtlfunctionstitchingnode.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing an input node

- [- initWithArgumentIndex:](<mtlfunctionstitchinginputnode/init(argumentindex_).md>) — Creates a new input node.

### Configuring an input node

- [argumentIndex](mtlfunctionstitchinginputnode/argumentindex.md) — The index in the command’s buffer argument table that declares which data to read for this input node.

## See Also

### Stitched function libraries

- [Customizing shaders using function pointers and stitching](customizing-shaders-using-function-pointers-and-stitching.md) — Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md) — A description of a new library of procedurally generated functions.
- [MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md) — A description of a new stitched function.
- [MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md) — A call graph node that describes a function call and its inputs.
- [MTLFunctionStitchingNode](mtlfunctionstitchingnode.md) — A protocol to identify call graph nodes.
- [MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md) — An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md) — A protocol to identify types that customize how the Metal compiler stitches a function together.
