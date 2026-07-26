---
title: 'useResources(_:usage:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/useresources(_:usage:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useresources(_:usage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/useresources%28_%3Ausage%3A%29.json'
content_hash: 'sha256:3fd36ad80bf1ad3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# useResources(_:usage:)

<sub>Instance Method</sub>

Makes multiple resources available to the acceleration structure pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func useResources(_ resources: [any MTLResource], usage: MTLResourceUsage)
```

## Parameters

- `resources` — An array of resources within an argument buffer.

- `usage` — Options that indicate how a GPU function accesses each resource in `resources`.

## Discussion

This method makes the resources resident for the duration of a compute pass and ensures that they are in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the resource. Calling this method again, or calling [- useHeap:](<../mtlcomputecommandencoder/useheap(__).md>), overwrites any previously specified usage options for future dispatch calls within the same compute command encoder.

> [!note] Note
> You can track resource access and dependency hazards with [MTLFence](../mtlfence.md) instances.

## See Also

### Making indirect resources resident

- [- useHeap:](<useheap(__).md>) — Makes the resources contained in the specified heap available to the acceleration structure pass.
- [useHeaps(_:)](<useheaps(__).md>) — Makes the resources contained in the specified heaps available to the acceleration structure pass.
- [- useResource:usage:](<useresource(__usage_).md>) — Makes a resource available to the acceleration structure pass.
- [MTLResourceUsage](../mtlresourceusage.md) — Options that describe how a graphics or compute function uses an argument buffer’s resource.
