---
title: MTLComputePipelineReflection
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinereflection
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinereflection.json'
content_hash: 'sha256:362714db3b479a79'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLComputePipelineReflection

<sub>Class</sub>

Information about the arguments of a compute function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLComputePipelineReflection
```

## Overview

An [MTLComputePipelineReflection](mtlcomputepipelinereflection.md) object provides access to the arguments of the compute function used in an [MTLComputePipelineState](mtlcomputepipelinestate.md) object. An [MTLComputePipelineReflection](mtlcomputepipelinereflection.md) object can be created along with an [MTLComputePipelineState](mtlcomputepipelinestate.md) object. Don’t create an [MTLComputePipelineReflection](mtlcomputepipelinereflection.md) object directly. Instead, call either the [- newComputePipelineStateWithFunction:options:reflection:error:](<mtldevice/makecomputepipelinestate(function_options_reflection_).md>) or [- newComputePipelineStateWithFunction:options:completionHandler:](<mtldevice/makecomputepipelinestate(function_options_completionhandler_).md>) method of [MTLDevice](mtldevice.md) to create both an [MTLComputePipelineState](mtlcomputepipelinestate.md) object and an [MTLComputePipelineReflection](mtlcomputepipelinereflection.md) object.

[MTLComputePipelineReflection](mtlcomputepipelinereflection.md) objects can use a significant amount of memory; release any strong references to them after you finish creating pipeline objects.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Obtaining the arguments of the compute function

- [arguments](mtlcomputepipelinereflection/arguments.md) — An array of instances that describe the arguments of a compute function. _(deprecated)_

### Instance Properties

- [bindings](mtlcomputepipelinereflection/bindings.md)

## See Also

### Introspection data

- [MTLAutoreleasedComputePipelineReflection](mtlautoreleasedcomputepipelinereflection.md) — A convenience type alias for an autoreleased compute pipeline reflection object.
- [MTLRenderPipelineReflection](mtlrenderpipelinereflection.md) — Information about the arguments of a graphics function.
- [MTLAutoreleasedRenderPipelineReflection](mtlautoreleasedrenderpipelinereflection.md) — A convenience type alias for an autoreleased pipeline reflection instance.
- [MTLBindingType](mtlbindingtype.md)
- [MTLBinding](mtlbinding.md)
- [MTLBindingAccess](mtlbindingaccess.md)
- [MTLBufferBinding](mtlbufferbinding.md)
- [MTLTextureBinding](mtltexturebinding.md)
- [MTLThreadgroupBinding](mtlthreadgroupbinding.md)
- [MTLObjectPayloadBinding](mtlobjectpayloadbinding.md)
