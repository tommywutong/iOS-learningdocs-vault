---
title: MTLFunctionStitchingNode
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchingnode
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchingnode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchingnode.json'
content_hash: 'sha256:6961083f03daea7f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionStitchingNode

<sub>Protocol</sub>

A protocol to identify call graph nodes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLFunctionStitchingNode : NSCopying, NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md), [MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md)

## See Also

### Stitched function libraries

- [Customizing shaders using function pointers and stitching](customizing-shaders-using-function-pointers-and-stitching.md) — Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md) — A description of a new library of procedurally generated functions.
- [MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md) — A description of a new stitched function.
- [MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md) — A call graph node that describes an input to the call graph.
- [MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md) — A call graph node that describes a function call and its inputs.
- [MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md) — An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md) — A protocol to identify types that customize how the Metal compiler stitches a function together.
