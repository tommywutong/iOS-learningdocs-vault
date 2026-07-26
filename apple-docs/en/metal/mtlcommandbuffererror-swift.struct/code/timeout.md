---
title: MTLCommandBufferError.Code.timeout
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffererror-swift.struct/code/timeout
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/code/timeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererror-swift.struct/code/timeout.json'
content_hash: 'sha256:4b86cdd587f690fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Metal](../../../metal.md) · [MTLCommandBufferError](../../mtlcommandbuffererror-swift.struct.md) · [Code](../code.md)

# MTLCommandBufferError.Code.timeout

<sub>Case</sub>

An error code that indicates the system interrupted and terminated the command buffer before it finished running.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case timeout
```

## Discussion

Possible causes include:

- The commands in the buffer took more time to run than the system allows.
- The command buffer timed out waiting for another workload to signal an [MTLEvent](../../mtlevent.md).

## See Also

### Error codes

- [MTLCommandBufferErrorNone](none.md) — An error code that represents the absence of any problems.
- [MTLCommandBufferErrorPageFault](pagefault.md) — An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [MTLCommandBufferErrorNotPermitted](notpermitted.md) — An error code that indicates a process doesn’t have access to a GPU device.
- [MTLCommandBufferErrorOutOfMemory](outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.
- [MTLCommandBufferErrorInvalidResource](invalidresource.md) — An error code that indicates the command buffer has an invalid reference to resource.
- [MTLCommandBufferErrorMemoryless](memoryless.md) — An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [MTLCommandBufferErrorDeviceRemoved](deviceremoved.md) — An error code that indicates a person physically removed the GPU device before the command buffer finished running. _(deprecated)_
- [MTLCommandBufferErrorStackOverflow](stackoverflow.md) — An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.
- [accessRevoked](accessrevoked.md) — An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [MTLCommandBufferErrorInternal](internal.md) — An error code that indicates the Metal framework has an internal problem.
