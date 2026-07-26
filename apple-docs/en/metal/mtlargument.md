---
title: MTLArgument
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument
source_url: 'https://developer.apple.com/documentation/metal/mtlargument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument.json'
content_hash: 'sha256:be71e7fa0a2949ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLArgument

<sub>Class</sub>

Information about an argument of a graphics or compute function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLArgument
```

## Overview

An [MTLArgument](mtlargument.md) instance describes a single argument to a Metal function. Your app uses the [MTLArgument](mtlargument.md) properties to read details about a function argument as it was defined in the Metal Shading Language. You can determine the argument’s data type, access restrictions, and its associated resource type. For buffer, texture, and threadgroup memory arguments, additional properties can be read to determine more details about the argument.

Your app does not create an [MTLArgument](mtlargument.md) instance directly. Creating an [MTLRenderPipelineState](mtlrenderpipelinestate.md) or [MTLComputePipelineState](mtlcomputepipelinestate.md) instance can generate a reflection instance ([MTLRenderPipelineReflection](mtlrenderpipelinereflection.md) or [MTLComputePipelineReflection](mtlcomputepipelinereflection.md)) that contains [MTLArgument](mtlargument.md) instances.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Describing the argument

- [name](mtlargument/name.md) — The name of the argument. _(deprecated)_
- [active](mtlargument/isactive.md) — A Boolean that indicates whether the compiled function uses the argument. _(deprecated)_
- [index](mtlargument/index.md) — The index in the argument table that corresponds to the function argument. _(deprecated)_
- [type](mtlargument/type.md) — The argument’s resource type. _(deprecated)_
- [access](mtlargument/access.md) — The argument’s read and/or write access. _(deprecated)_

### Describing a buffer argument

- [bufferAlignment](mtlargument/bufferalignment.md) — The required byte alignment in memory for the buffer data. _(deprecated)_
- [bufferDataSize](mtlargument/bufferdatasize.md) — The size, in bytes, of the buffer data. _(deprecated)_
- [bufferDataType](mtlargument/bufferdatatype.md) — The data type of the buffer data. _(deprecated)_
- [bufferStructType](mtlargument/bufferstructtype.md) — A description of the structure data of a buffer argument. _(deprecated)_
- [bufferPointerType](mtlargument/bufferpointertype.md) — A description of the pointer to a buffer argument. _(deprecated)_

### Describing a texture argument

- [textureDataType](mtlargument/texturedatatype.md) — The data type of a texture argument. _(deprecated)_
- [textureType](mtlargument/texturetype.md) — The texture type of a texture argument. _(deprecated)_
- [isDepthTexture](mtlargument/isdepthtexture.md) — A Boolean value that indicates whether the texture is a depth texture. _(deprecated)_

### Describing an array argument

- [arrayLength](mtlargument/arraylength.md) — The number of elements, if the argument is an array. _(deprecated)_

### Describing a threadgroup memory argument

- [threadgroupMemoryAlignment](mtlargument/threadgroupmemoryalignment.md) — The required byte alignment in memory for the threadgroup data. _(deprecated)_
- [threadgroupMemoryDataSize](mtlargument/threadgroupmemorydatasize.md) — The size, in bytes, of the threadgroup data. _(deprecated)_

## See Also

### Function arguments

- [MTLAttribute](mtlattribute.md) — An object that describes an attribute defined in the stage-in argument for a shader.
- [MTLVertexAttribute](mtlvertexattribute.md) — An instance that represents an attribute of a vertex function.
- [MTLAutoreleasedArgument](mtlautoreleasedargument.md) — A convenience type alias for an autoreleased argument instance. _(deprecated)_
- [MTLArgumentType](mtlargumenttype.md) — The resource type for an argument of a function. _(deprecated)_
- [MTLArgumentAccess](mtlargumentaccess.md) — Function access restrictions to argument data in the shading language code. _(deprecated)_
