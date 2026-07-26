---
title: retainedReferences
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferdescriptor/retainedreferences
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferdescriptor/retainedreferences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferdescriptor/retainedreferences.json'
content_hash: 'sha256:adff9a9c44d2b102'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferDescriptor](../mtlcommandbufferdescriptor.md)

# retainedReferences

<sub>Instance Property</sub>

A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var retainedReferences: Bool { get set }
```

## Discussion

Set this property to [true](../../swift/true.md) (its default) to create a command buffer that maintains strong references to resource instances that its commands need. Otherwise, set it to [false](../../swift/false.md) to create a command buffer that doesn’t maintain strong references to its resources.

Apps typically create command buffers that don’t maintain references to resources for extremely performance-critical situations. Even though the runtime cost for retaining or releasing a single resource is trivial, the aggregate time savings may be worth it.

It’s your app’s responsibility to maintain strong references to all the resources the command buffer uses until it finishes running on the GPU.

> [!important] Important
> Releasing a resource before a command buffer’s commands complete may trigger a runtime error or erratic behavior.

You can determine whether an existing command buffer retains references by checking its [retainedReferences](../mtlcommandbuffer/retainedreferences.md) property.

## See Also

### Configuring the command buffer

- [logState](logstate.md) — The shader logging configuration that the command buffer uses.
- [errorOptions](erroroptions.md) — The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.
- [MTLCommandBufferErrorOption](../mtlcommandbuffererroroption.md) — Options for reporting errors from a command buffer.
