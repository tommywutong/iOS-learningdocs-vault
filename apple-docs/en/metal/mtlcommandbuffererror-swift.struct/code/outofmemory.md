---
title: MTLCommandBufferError.Code.outOfMemory
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffererror-swift.struct/code/outofmemory
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/code/outofmemory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererror-swift.struct/code/outofmemory.json'
content_hash: 'sha256:4122ad3db3ad1657'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Metal](../../../metal.md) · [MTLCommandBufferError](../../mtlcommandbuffererror-swift.struct.md) · [Code](../code.md)

# MTLCommandBufferError.Code.outOfMemory

<sub>Case</sub>

An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case outOfMemory
```

## See Also

### Error codes

- [MTLCommandBufferErrorNone](none.md) — An error code that represents the absence of any problems.
- [MTLCommandBufferErrorTimeout](timeout.md) — An error code that indicates the system interrupted and terminated the command buffer before it finished running.
- [MTLCommandBufferErrorPageFault](pagefault.md) — An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [MTLCommandBufferErrorNotPermitted](notpermitted.md) — An error code that indicates a process doesn’t have access to a GPU device.
- [MTLCommandBufferErrorInvalidResource](invalidresource.md) — An error code that indicates the command buffer has an invalid reference to resource.
- [MTLCommandBufferErrorMemoryless](memoryless.md) — An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [MTLCommandBufferErrorDeviceRemoved](deviceremoved.md) — An error code that indicates a person physically removed the GPU device before the command buffer finished running. _(deprecated)_
- [MTLCommandBufferErrorStackOverflow](stackoverflow.md) — An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.
- [accessRevoked](accessrevoked.md) — An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [MTLCommandBufferErrorInternal](internal.md) — An error code that indicates the Metal framework has an internal problem.
