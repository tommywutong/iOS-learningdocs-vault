---
title: MTLVisibleFunctionTableDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvisiblefunctiontabledescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlvisiblefunctiontabledescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvisiblefunctiontabledescriptor.json'
content_hash: 'sha256:a976b83090b4484d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVisibleFunctionTableDescriptor

<sub>Class</sub>

A specification of how to create a visible function table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLVisibleFunctionTableDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the function table

- [functionCount](mtlvisiblefunctiontabledescriptor/functioncount.md) — The number of entries in the function table.

## See Also

### Shader functions

- [MTLFunctionDescriptor](mtlfunctiondescriptor.md) — A description of a function object to create.
- [MTLFunction](mtlfunction.md) — A interface that represents a public shader function in a Metal library.
- [MTLFunctionHandle](mtlfunctionhandle.md) — An object representing a function that you can add to a visible function table.
- [MTLVisibleFunctionTable](mtlvisiblefunctiontable.md) — A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.
- [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md) — A description of an intersection function that performs an intersection test.
- [MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md) — A specification of how to create an intersection function table.
- [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md) — A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
