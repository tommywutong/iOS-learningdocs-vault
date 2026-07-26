---
title: MTLIntersectionFunctionTable
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlintersectionfunctiontable
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable.json'
content_hash: 'sha256:d113797cfd05e9d7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIntersectionFunctionTable

<sub>Protocol</sub>

A table of intersection functions that Metal calls to perform ray-tracing intersection tests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLIntersectionFunctionTable : MTLResource
```

## Overview

Don’t implement this protocol yourself. Instead create an [MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md) instance and configure its properties. Then call the appropriate method on the pipeline state that you want to use this table with:

- **Compute pipeline** — [- newIntersectionFunctionTableWithDescriptor:](<mtlcomputepipelinestate/makeintersectionfunctiontable(descriptor_).md>)
- **Render pipeline** — [- newIntersectionFunctionTableWithDescriptor:stage:](<mtlrenderpipelinestate/makeintersectionfunctiontable(descriptor_stage_).md>)

If you use the same ray-tracing functions with more than one pipeline, make a separate table for each.

Use the methods on this instance to set the table entries to point at the intersection functions, and to provide buffers as arguments for those functions. For more information about intersection functions, see [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## Relationships

- **Inherits From**: [MTLAllocation](mtlallocation.md), [MTLResource](mtlresource.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting a table entry

- [- setFunction:atIndex:](<mtlintersectionfunctiontable/setfunction(__index_).md>) — Sets an entry in the table.
- [setFunctions(_:range:)](<mtlintersectionfunctiontable/setfunctions(__range_).md>) — Sets a range of entries in the table.

### Specifying arguments for intersection functions

- [- setBuffer:offset:atIndex:](<mtlintersectionfunctiontable/setbuffer(__offset_index_).md>) — Sets a buffer for the intersection functions.
- [setBuffers(_:offsets:range:)](<mtlintersectionfunctiontable/setbuffers(__offsets_range_).md>) — Sets a range of buffers for the intersection functions.
- [- setVisibleFunctionTable:atBufferIndex:](<mtlintersectionfunctiontable/setvisiblefunctiontable(__bufferindex_).md>) — Sets a visible function table for the intersection functions.
- [setVisibleFunctionTables(_:bufferRange:)](<mtlintersectionfunctiontable/setvisiblefunctiontables(__bufferrange_).md>) — Sets a range of visible function tables for the intersection functions.

### Specifying opaque triangle intersection testing

- [- setOpaqueTriangleIntersectionFunctionWithSignature:atIndex:](<mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature_index_).md>) — Sets an entry in the intersection table to point to a system-defined opaque triangle intersection function.
- [- setOpaqueTriangleIntersectionFunctionWithSignature:withRange:](<mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature_range_).md>) — Sets a range of entries in the intersection table to point to a system-defined opaque triangle intersection function.

### Instance Properties

- [gpuResourceID](mtlintersectionfunctiontable/gpuresourceid.md)

### Instance Methods

- [- setOpaqueCurveIntersectionFunctionWithSignature:atIndex:](<mtlintersectionfunctiontable/setopaquecurveintersectionfunction(signature_index_).md>)
- [- setOpaqueCurveIntersectionFunctionWithSignature:withRange:](<mtlintersectionfunctiontable/setopaquecurveintersectionfunction(signature_range_).md>)

## See Also

### Intersection function tables

- [MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md) — A specification of how to create an intersection function table.
- [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md) — A description of an intersection function that performs an intersection test.
- [MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature.md) — Constants for specifying different types of custom intersection functions.
- [MTLIntersectionFunctionBufferArguments](mtlintersectionfunctionbufferarguments.md)
