---
title: stackOverflow
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffererror-swift.struct/stackoverflow
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/stackoverflow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererror-swift.struct/stackoverflow.json'
content_hash: 'sha256:cdbed42a9768497a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferError](../mtlcommandbuffererror-swift.struct.md)

# stackOverflow

<sub>Type Property</sub>

An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var stackOverflow: MTLCommandBufferError.Code { get }
```

## Discussion

You can set the largest number of stack frames your pipelines by configuring these properties:

- [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md)`.`[maxCallStackDepth](../mtlcomputepipelinedescriptor/maxcallstackdepth.md) for kernel functions
- [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md)`.`[maxCallStackDepth](../mtltilerenderpipelinedescriptor/maxcallstackdepth.md) for tile shaders

## See Also

### Errors codes

- [none](none.md) — An error code that represents the absence of any problems.
- [timeout](timeout.md) — An error code that indicates the system interrupted and terminated the command buffer before it finished running.
- [pageFault](pagefault.md) — An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [notPermitted](notpermitted.md) — An error code that indicates a process doesn’t have access to a GPU device.
- [outOfMemory](outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.
- [invalidResource](invalidresource.md) — An error code that indicates the command buffer has an invalid reference to resource.
- [memoryless](memoryless.md) — An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [deviceRemoved](deviceremoved.md) — An error code that indicates a person physically removed the GPU device before the command buffer finished running. _(deprecated)_
- [accessRevoked](accessrevoked.md) — An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [internal](internal.md) — An error code that indicates the Metal framework has an internal problem.
- [Code](code.md) — Error codes that indicate why a GPU is unable to finish running a command buffer.
