---
title: MTLCommandBufferError.Code.deviceRemoved
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.13+（27.0 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlcommandbuffererror-swift.struct/code/deviceremoved
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/code/deviceremoved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererror-swift.struct/code/deviceremoved.json'
content_hash: 'sha256:2567916c7709eab1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Metal](../../../metal.md) · [MTLCommandBufferError](../../mtlcommandbuffererror-swift.struct.md) · [Code](../code.md)

# MTLCommandBufferError.Code.deviceRemoved

<sub>Case</sub>

An error code that indicates a person physically removed the GPU device before the command buffer finished running.

> [!warning] Deprecated
> MTLCommandBufferErrorDeviceRemoved cannot occur on Apple Silicon

<sub>macOS</sub>

```swift
case deviceRemoved
```

## See Also

### Error codes

- [MTLCommandBufferErrorNone](none.md) — An error code that represents the absence of any problems.
- [MTLCommandBufferErrorTimeout](timeout.md) — An error code that indicates the system interrupted and terminated the command buffer before it finished running.
- [MTLCommandBufferErrorPageFault](pagefault.md) — An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [MTLCommandBufferErrorNotPermitted](notpermitted.md) — An error code that indicates a process doesn’t have access to a GPU device.
- [MTLCommandBufferErrorOutOfMemory](outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.
- [MTLCommandBufferErrorInvalidResource](invalidresource.md) — An error code that indicates the command buffer has an invalid reference to resource.
- [MTLCommandBufferErrorMemoryless](memoryless.md) — An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [MTLCommandBufferErrorStackOverflow](stackoverflow.md) — An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.
- [accessRevoked](accessrevoked.md) — An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [MTLCommandBufferErrorInternal](internal.md) — An error code that indicates the Metal framework has an internal problem.
