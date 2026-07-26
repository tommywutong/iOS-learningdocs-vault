---
title: none
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffererror-swift.struct/none
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererror-swift.struct/none.json'
content_hash: 'sha256:a535f0b22d8495b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferError](../mtlcommandbuffererror-swift.struct.md)

# none

<sub>Type Property</sub>

An error code that represents the absence of any problems.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var none: MTLCommandBufferError.Code { get }
```

## See Also

### Errors codes

- [timeout](timeout.md) — An error code that indicates the system interrupted and terminated the command buffer before it finished running.
- [pageFault](pagefault.md) — An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [notPermitted](notpermitted.md) — An error code that indicates a process doesn’t have access to a GPU device.
- [outOfMemory](outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.
- [invalidResource](invalidresource.md) — An error code that indicates the command buffer has an invalid reference to resource.
- [memoryless](memoryless.md) — An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [deviceRemoved](deviceremoved.md) — An error code that indicates a person physically removed the GPU device before the command buffer finished running. _(deprecated)_
- [stackOverflow](stackoverflow.md) — An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.
- [accessRevoked](accessrevoked.md) — An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [internal](internal.md) — An error code that indicates the Metal framework has an internal problem.
- [Code](code.md) — Error codes that indicate why a GPU is unable to finish running a command buffer.
