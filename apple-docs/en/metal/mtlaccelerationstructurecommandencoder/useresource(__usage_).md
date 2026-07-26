---
title: 'useResource(_:usage:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/useresource(_:usage:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useresource(_:usage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/useresource%28_%3Ausage%3A%29.json'
content_hash: 'sha256:6808024e9398b17a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# useResource(_:usage:)

<sub>Instance Method</sub>

Makes a resource available to the acceleration structure pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func useResource(_ resource: any MTLResource, usage: MTLResourceUsage)
```

## Parameters

- `resource` — A specific resource within an argument buffer.

- `usage` — The options that describe how the compute function uses the resource.

## Discussion

This method makes the resource resident for the duration of a compute pass and ensures that it’s in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the resource. Calling this method again, or calling [- useHeap:](<../mtlcomputecommandencoder/useheap(__).md>), overwrites any previously specified usage options for future dispatch calls within the same compute command encoder.

> [!note] Note
> You can track resource access and dependency hazards with [MTLFence](../mtlfence.md) instances.

## See Also

### Making indirect resources resident

- [- useHeap:](<useheap(__).md>) — Makes the resources contained in the specified heap available to the acceleration structure pass.
- [useHeaps(_:)](<useheaps(__).md>) — Makes the resources contained in the specified heaps available to the acceleration structure pass.
- [useResources(_:usage:)](<useresources(__usage_).md>) — Makes multiple resources available to the acceleration structure pass.
- [MTLResourceUsage](../mtlresourceusage.md) — Options that describe how a graphics or compute function uses an argument buffer’s resource.
