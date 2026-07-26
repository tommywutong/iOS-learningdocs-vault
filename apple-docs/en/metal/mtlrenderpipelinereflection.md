---
title: MTLRenderPipelineReflection
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinereflection
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinereflection.json'
content_hash: 'sha256:84f5f94f28ae2b4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRenderPipelineReflection

<sub>Class</sub>

Information about the arguments of a graphics function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLRenderPipelineReflection
```

## Overview

The [MTLRenderPipelineReflection](mtlrenderpipelinereflection.md) class is an interface that represents the parameters for the shaders in a render pipeline state (see [MTLRenderPipelineState](mtlrenderpipelinestate.md)). Each pipeline state can include object, mesh, vertex, fragment, and tile shaders.

You create a reflection instance at the same time as the pipeline state that it represents by calling the appropriate [MTLDevice](mtldevice.md) method. For example, the [- newRenderPipelineStateWithDescriptor:options:reflection:error:](<mtldevice/makerenderpipelinestate(descriptor_options_reflection_).md>) and [- newRenderPipelineStateWithDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_options_completionhandler_)-5gdww.md>) methods create the pipeline state and the reflection instances at the same time.

> [!important] Important
> Only create reflection instances if you need them because each one can require a significant amount of memory.

For more information, see [Pipeline state creation](pipeline-state-creation.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting a shader’s parameter

- [fragmentBindings](mtlrenderpipelinereflection/fragmentbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s fragment shader.
- [meshBindings](mtlrenderpipelinereflection/meshbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s mesh shader.
- [objectBindings](mtlrenderpipelinereflection/objectbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s object shader.
- [tileBindings](mtlrenderpipelinereflection/tilebindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s tile shader.
- [vertexBindings](mtlrenderpipelinereflection/vertexbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s vertex shader.

### Deprecated

- [vertexArguments](mtlrenderpipelinereflection/vertexarguments.md) — An array of argument instances, each of which represent a parameter of the pipeline state’s vertex shader. _(deprecated)_
- [fragmentArguments](mtlrenderpipelinereflection/fragmentarguments.md) — An array of argument instances, each of which represent a parameter of the pipeline state’s fragment shader. _(deprecated)_
- [tileArguments](mtlrenderpipelinereflection/tilearguments.md) — An array of argument instances, each of which represent a parameter of the pipeline state’s tile shader. _(deprecated)_

## See Also

### Introspection data

- [MTLComputePipelineReflection](mtlcomputepipelinereflection.md) — Information about the arguments of a compute function.
- [MTLAutoreleasedComputePipelineReflection](mtlautoreleasedcomputepipelinereflection.md) — A convenience type alias for an autoreleased compute pipeline reflection object.
- [MTLAutoreleasedRenderPipelineReflection](mtlautoreleasedrenderpipelinereflection.md) — A convenience type alias for an autoreleased pipeline reflection instance.
- [MTLBindingType](mtlbindingtype.md)
- [MTLBinding](mtlbinding.md)
- [MTLBindingAccess](mtlbindingaccess.md)
- [MTLBufferBinding](mtlbufferbinding.md)
- [MTLTextureBinding](mtltexturebinding.md)
- [MTLThreadgroupBinding](mtlthreadgroupbinding.md)
- [MTLObjectPayloadBinding](mtlobjectpayloadbinding.md)
