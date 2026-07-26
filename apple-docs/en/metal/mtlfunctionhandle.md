---
title: MTLFunctionHandle
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionhandle
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionhandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionhandle.json'
content_hash: 'sha256:54faf820716606d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionHandle

<sub>Protocol</sub>

An object representing a function that you can add to a visible function table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLFunctionHandle : NSObjectProtocol, Sendable
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Querying handle properties

- [device](mtlfunctionhandle/device.md) — The device object that created the shader function.
- [functionType](mtlfunctionhandle/functiontype.md) — The shader function’s type.
- [name](mtlfunctionhandle/name.md) — The function’s name.

### Instance Properties

- [gpuResourceID](mtlfunctionhandle/gpuresourceid.md)

## See Also

### Shader functions

- [MTLFunctionDescriptor](mtlfunctiondescriptor.md) — A description of a function object to create.
- [MTLFunction](mtlfunction.md) — A interface that represents a public shader function in a Metal library.
- [MTLVisibleFunctionTableDescriptor](mtlvisiblefunctiontabledescriptor.md) — A specification of how to create a visible function table.
- [MTLVisibleFunctionTable](mtlvisiblefunctiontable.md) — A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.
- [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md) — A description of an intersection function that performs an intersection test.
- [MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md) — A specification of how to create an intersection function table.
- [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md) — A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
