---
title: MTLCommandBufferError.Code
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffererror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererror-swift.struct/code.json'
content_hash: 'sha256:923f17568f98d4b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferError](../mtlcommandbuffererror-swift.struct.md)

# MTLCommandBufferError.Code

<sub>Enumeration</sub>

Error codes that indicate why a GPU is unable to finish running a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error codes

- [MTLCommandBufferErrorNone](code/none.md) — An error code that represents the absence of any problems.
- [MTLCommandBufferErrorTimeout](code/timeout.md) — An error code that indicates the system interrupted and terminated the command buffer before it finished running.
- [MTLCommandBufferErrorPageFault](code/pagefault.md) — An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [MTLCommandBufferErrorNotPermitted](code/notpermitted.md) — An error code that indicates a process doesn’t have access to a GPU device.
- [MTLCommandBufferErrorOutOfMemory](code/outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.
- [MTLCommandBufferErrorInvalidResource](code/invalidresource.md) — An error code that indicates the command buffer has an invalid reference to resource.
- [MTLCommandBufferErrorMemoryless](code/memoryless.md) — An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [MTLCommandBufferErrorDeviceRemoved](code/deviceremoved.md) — An error code that indicates a person physically removed the GPU device before the command buffer finished running. _(deprecated)_
- [MTLCommandBufferErrorStackOverflow](code/stackoverflow.md) — An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.
- [accessRevoked](code/accessrevoked.md) — An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [MTLCommandBufferErrorInternal](code/internal.md) — An error code that indicates the Metal framework has an internal problem.

### Deprecated

- [MTLCommandBufferErrorBlacklisted](code/blacklisted.md) — A former error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs. _(deprecated)_

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)
