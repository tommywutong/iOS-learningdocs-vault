---
title: MTLFunctionStitchingAttributeAlwaysInline
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchingattributealwaysinline
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchingattributealwaysinline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchingattributealwaysinline.json'
content_hash: 'sha256:b15013f582e1007c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionStitchingAttributeAlwaysInline

<sub>Class</sub>

An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLFunctionStitchingAttributeAlwaysInline
```

## Overview

To inline functions in a call graph, instantiate an instance of this class and assign it as an attribute on the [MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Related Documentation

- [attributes](mtlfunctionstitchinggraph/attributes.md) — A list of attributes to configure how the Metal device object generates the new stitched function.

### Stitched function libraries

- [Customizing shaders using function pointers and stitching](customizing-shaders-using-function-pointers-and-stitching.md) — Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md) — A description of a new library of procedurally generated functions.
- [MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md) — A description of a new stitched function.
- [MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md) — A call graph node that describes an input to the call graph.
- [MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md) — A call graph node that describes a function call and its inputs.
- [MTLFunctionStitchingNode](mtlfunctionstitchingnode.md) — A protocol to identify call graph nodes.
- [MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md) — A protocol to identify types that customize how the Metal compiler stitches a function together.
