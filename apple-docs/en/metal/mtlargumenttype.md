---
title: MTLArgumentType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargumenttype
source_url: 'https://developer.apple.com/documentation/metal/mtlargumenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumenttype.json'
content_hash: 'sha256:7db53fbbfd93f4b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLArgumentType

<sub>Enumeration</sub>

The resource type for an argument of a function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLArgumentType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Argument types

- [MTLArgumentTypeBuffer](mtlargumenttype/buffer.md) — The argument is a buffer. _(deprecated)_
- [MTLArgumentTypeThreadgroupMemory](mtlargumenttype/threadgroupmemory.md) — The argument is a pointer to threadgroup memory. _(deprecated)_
- [MTLArgumentTypeTexture](mtlargumenttype/texture.md) — The argument is a texture. _(deprecated)_
- [MTLArgumentTypeSampler](mtlargumenttype/sampler.md) — The argument is a texture sampler. _(deprecated)_
- [MTLArgumentTypeImageblock](mtlargumenttype/imageblock.md) — The argument is an imageblock. _(deprecated)_
- [MTLArgumentTypeImageblockData](mtlargumenttype/imageblockdata.md) — The argument is imageblock data. _(deprecated)_
- [MTLArgumentTypeVisibleFunctionTable](mtlargumenttype/visiblefunctiontable.md) — The argument is a visible function table. _(deprecated)_
- [MTLArgumentTypeIntersectionFunctionTable](mtlargumenttype/intersectionfunctiontable.md) — The argument is an intersection function table. _(deprecated)_
- [MTLArgumentTypePrimitiveAccelerationStructure](mtlargumenttype/primitiveaccelerationstructure.md) — The argument is a bottom-level ray tracing acceleraton structure for a set of primitives. _(deprecated)_
- [MTLArgumentTypeInstanceAccelerationStructure](mtlargumenttype/instanceaccelerationstructure.md) — The argument is a top-level ray tracing acceleration structure for a set of instances. _(deprecated)_

### Initializers

- [init(rawValue:)](<mtlargumenttype/init(rawvalue_).md>) _(deprecated)_

## See Also

### Function arguments

- [MTLAttribute](mtlattribute.md) — An object that describes an attribute defined in the stage-in argument for a shader.
- [MTLVertexAttribute](mtlvertexattribute.md) — An instance that represents an attribute of a vertex function.
- [MTLArgument](mtlargument.md) — Information about an argument of a graphics or compute function. _(deprecated)_
- [MTLAutoreleasedArgument](mtlautoreleasedargument.md) — A convenience type alias for an autoreleased argument instance. _(deprecated)_
- [MTLArgumentAccess](mtlargumentaccess.md) — Function access restrictions to argument data in the shading language code. _(deprecated)_
