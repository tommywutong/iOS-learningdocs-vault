---
title: kernelEndTime
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/kernelendtime
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/kernelendtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/kernelendtime.json'
content_hash: 'sha256:24fc8857a3a65ca7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# kernelEndTime

<sub>Instance Property</sub>

The host time, in seconds, when the CPU finishes scheduling the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var kernelEndTime: CFTimeInterval { get }
```

## Discussion

You can calculate how much time the kernel spends scheduling a command buffer by subtracting [kernelStartTime](kernelstarttime.md) from this value.

The kernel start and end times remain `0.0` until the GPU driver (on the CPU) schedules the command buffer to run on the GPU. Apps typically use these values after the [- waitUntilScheduled](<waituntilscheduled().md>) method returns, or within a completion handler (see [- addScheduledHandler:](<addscheduledhandler(__).md>) and [- addCompletedHandler:](<addcompletedhandler(__).md>)).

## See Also

### Checking scheduling times on the CPU

- [kernelStartTime](kernelstarttime.md) — The host time, in seconds, when the CPU begins to schedule the command buffer.
