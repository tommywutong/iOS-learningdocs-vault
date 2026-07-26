---
title: MTLVisibleFunctionTable
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvisiblefunctiontable
source_url: 'https://developer.apple.com/documentation/metal/mtlvisiblefunctiontable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvisiblefunctiontable.json'
content_hash: 'sha256:f66ab3ef1a53a22c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVisibleFunctionTable

<sub>Protocol</sub>

A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLVisibleFunctionTable : MTLResource
```

## Relationships

- **Inherits From**: [MTLAllocation](mtlallocation.md), [MTLResource](mtlresource.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting a table entry

- [- setFunction:atIndex:](<mtlvisiblefunctiontable/setfunction(__index_).md>) — Sets a table entry to point to a callable function.
- [setFunctions(_:range:)](<mtlvisiblefunctiontable/setfunctions(__range_).md>) — Sets a range of table entries to point to an array of callable functions.

### Instance Properties

- [gpuResourceID](mtlvisiblefunctiontable/gpuresourceid.md)

## See Also

### Shader functions

- [MTLFunctionDescriptor](mtlfunctiondescriptor.md) — A description of a function object to create.
- [MTLFunction](mtlfunction.md) — A interface that represents a public shader function in a Metal library.
- [MTLFunctionHandle](mtlfunctionhandle.md) — An object representing a function that you can add to a visible function table.
- [MTLVisibleFunctionTableDescriptor](mtlvisiblefunctiontabledescriptor.md) — A specification of how to create a visible function table.
- [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md) — A description of an intersection function that performs an intersection test.
- [MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md) — A specification of how to create an intersection function table.
- [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md) — A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
