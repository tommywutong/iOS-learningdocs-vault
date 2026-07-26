---
title: gpuEndTime
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/gpuendtime
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpuendtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/gpuendtime.json'
content_hash: 'sha256:9cfd39f282604de7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# gpuEndTime

<sub>Instance Property</sub>

The host time, in seconds, when the GPU finishes execution of the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var gpuEndTime: CFTimeInterval { get }
```

## Discussion

You can calculate how much time the GPU spends running a command buffer by subtracting [GPUStartTime](gpustarttime.md) from this value. Both values are relative to system mach time.

The GPU start and end times remain `0.0` until the GPU finishes running the command buffer. Check this value after the [- waitUntilCompleted](<waituntilcompleted().md>) method returns, or within a completion handler passed to the [- addCompletedHandler:](<addcompletedhandler(__).md>) method.

## See Also

### Checking execution times on the GPU

- [GPUStartTime](gpustarttime.md) — The host time, in seconds, when the GPU starts command buffer execution.
