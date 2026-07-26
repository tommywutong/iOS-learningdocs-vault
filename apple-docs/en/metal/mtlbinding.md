---
title: MTLBinding
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbinding
source_url: 'https://developer.apple.com/documentation/metal/mtlbinding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinding.json'
content_hash: 'sha256:6516dd1acbf44933'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBinding

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLBinding : NSObjectProtocol, Sendable
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [MTLBufferBinding](mtlbufferbinding.md), [MTLObjectPayloadBinding](mtlobjectpayloadbinding.md), [MTLTensorBinding](mtltensorbinding.md), [MTLTextureBinding](mtltexturebinding.md), [MTLThreadgroupBinding](mtlthreadgroupbinding.md)

## Topics

### Instance Properties

- [access](mtlbinding/access.md)
- [index](mtlbinding/index.md)
- [argument](mtlbinding/isargument.md)
- [used](mtlbinding/isused.md)
- [name](mtlbinding/name.md)
- [type](mtlbinding/type.md)

## See Also

### Introspection data

- [MTLComputePipelineReflection](mtlcomputepipelinereflection.md) — Information about the arguments of a compute function.
- [MTLAutoreleasedComputePipelineReflection](mtlautoreleasedcomputepipelinereflection.md) — A convenience type alias for an autoreleased compute pipeline reflection object.
- [MTLRenderPipelineReflection](mtlrenderpipelinereflection.md) — Information about the arguments of a graphics function.
- [MTLAutoreleasedRenderPipelineReflection](mtlautoreleasedrenderpipelinereflection.md) — A convenience type alias for an autoreleased pipeline reflection instance.
- [MTLBindingType](mtlbindingtype.md)
- [MTLBindingAccess](mtlbindingaccess.md)
- [MTLBufferBinding](mtlbufferbinding.md)
- [MTLTextureBinding](mtltexturebinding.md)
- [MTLThreadgroupBinding](mtlthreadgroupbinding.md)
- [MTLObjectPayloadBinding](mtlobjectpayloadbinding.md)
