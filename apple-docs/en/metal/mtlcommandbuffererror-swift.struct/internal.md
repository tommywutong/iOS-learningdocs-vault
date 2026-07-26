---
title: internal
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffererror-swift.struct/internal
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/internal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererror-swift.struct/internal.json'
content_hash: 'sha256:6abf757f656a3982'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferError](../mtlcommandbuffererror-swift.struct.md)

# internal

<sub>Type Property</sub>

An error code that indicates the Metal framework has an internal problem.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var `internal`: MTLCommandBufferError.Code { get }
```

## Discussion

The local description contains the underlying error code. You can report the scenario that generated this error code with [Feedback Assistant](https://feedbackassistant.apple.com).

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
- [stackOverflow](stackoverflow.md) — An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.
- [accessRevoked](accessrevoked.md) — An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [Code](code.md) — Error codes that indicate why a GPU is unable to finish running a command buffer.
