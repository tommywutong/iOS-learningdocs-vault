---
title: 'useResources:count:usage:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/useresources:count:usage:'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useresources:count:usage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/useresources%3Acount%3Ausage%3A.json'
content_hash: 'sha256:6bbb00b78fd8fdf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# useResources:count:usage:

<sub>Instance Method</sub>

Specifies that an array of resources in an argument buffer can be safely used by the acceleration structure pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) useResources:(id<MTLResource> const[]) resources count:(NSUInteger) count usage:(MTLResourceUsage) usage;
```

## Parameters

- `resources` — An array of resources within an argument buffer.

- `count` — The number of resource elements in `resources`.

- `usage` — Options that indicate how a GPU function accesses each resource in `resources`.

## Discussion

This method makes the array of resources resident for the duration of a compute pass and ensures that it’s in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the array of resources. Calling this method again, or calling [- useHeap:](<../mtlcomputecommandencoder/useheap(__).md>), overwrites any previously specified usage options for future dispatch calls within the same compute command encoder.

> [!note] Note
> You can track resource access and dependency hazards with [MTLFence](../mtlfence.md) instances.

## See Also

### Making indirect resources resident

- [- useHeap:](<useheap(__).md>) — Makes the resources contained in the specified heap available to the acceleration structure pass.
- [useHeaps:count:](useheaps_count_.md) — Specifies that an array of heaps containing resources in an argument buffer can be safely used by the acceleration structure pass.
- [- useResource:usage:](<useresource(__usage_).md>) — Makes a resource available to the acceleration structure pass.
- [MTLResourceUsage](../mtlresourceusage.md) — Options that describe how a graphics or compute function uses an argument buffer’s resource.
