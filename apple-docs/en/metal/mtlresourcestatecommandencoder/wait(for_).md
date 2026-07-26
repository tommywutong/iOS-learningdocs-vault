---
title: 'wait(for:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresourcestatecommandencoder/wait(for:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresourcestatecommandencoder/wait(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourcestatecommandencoder/wait%28for%3A%29.json'
content_hash: 'sha256:ed18cc82c7dde811'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md)

# wait(for:)

<sub>Instance Method</sub>

Encodes a command that instructs the GPU to pause before starting the resource state commands until another pass updates a fence.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func wait(for fence: any MTLFence)
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional func wait(for fence: any MTLFence)
```

## Parameters

- `fence` — An [MTLFence](../mtlfence.md) instance to pause execution on until updated.

## Discussion

Fences maintain order to prevent GPU data hazards as the GPU runs various passes within the same command queue. The encoded resource state commands wait for a pass to update `fence` before running.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [MTLCommandBuffer](../mtlcommandbuffer.md).

## See Also

### Performing fence operations

- [- updateFence:](<update(__).md>) — Encodes a command that instructs the GPU to update a fence, which signals passes waiting on the fence.
