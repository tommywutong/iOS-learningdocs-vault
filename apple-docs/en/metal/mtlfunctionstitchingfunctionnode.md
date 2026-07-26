---
title: MTLFunctionStitchingFunctionNode
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchingfunctionnode
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchingfunctionnode.json'
content_hash: 'sha256:40f99e67d0e34068'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionStitchingFunctionNode

<sub>Class</sub>

A call graph node that describes a function call and its inputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLFunctionStitchingFunctionNode
```

## Overview

When the Metal device object evaluates the function graph to compile the stitched function, it evaluates the nodes stored in the [arguments](mtlfunctionstitchingfunctionnode/arguments.md) property that it hasn’t already evaluated, and then calls the function specified by [name](mtlfunctionstitchingfunctionnode/name.md) to generate the node’s output.

If the function has side effects on the input data, use the [controlDependencies](mtlfunctionstitchingfunctionnode/controldependencies.md) property on other nodes to specify whether the Metal device object needs to evaluate this node first.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MTLFunctionStitchingNode](mtlfunctionstitchingnode.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a function node

- [- initWithName:arguments:controlDependencies:](<mtlfunctionstitchingfunctionnode/init(name_arguments_controldependencies_).md>) — Creates a new function node.

### Configuring a function node

- [name](mtlfunctionstitchingfunctionnode/name.md) — The name of the function to call.
- [arguments](mtlfunctionstitchingfunctionnode/arguments.md) — An ordered list of the nodes that provide the function’s arguments.
- [controlDependencies](mtlfunctionstitchingfunctionnode/controldependencies.md) — The list of nodes that need to execute before executing the node.

## See Also

### Stitched function libraries

- [Customizing shaders using function pointers and stitching](customizing-shaders-using-function-pointers-and-stitching.md) — Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md) — A description of a new library of procedurally generated functions.
- [MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md) — A description of a new stitched function.
- [MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md) — A call graph node that describes an input to the call graph.
- [MTLFunctionStitchingNode](mtlfunctionstitchingnode.md) — A protocol to identify call graph nodes.
- [MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md) — An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md) — A protocol to identify types that customize how the Metal compiler stitches a function together.
