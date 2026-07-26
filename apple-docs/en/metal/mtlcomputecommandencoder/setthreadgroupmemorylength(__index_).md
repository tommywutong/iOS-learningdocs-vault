---
title: 'setThreadgroupMemoryLength(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setthreadgroupmemorylength(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setthreadgroupmemorylength(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setthreadgroupmemorylength%28_%3Aindex%3A%29.json'
content_hash: 'sha256:1a6ea390f2cf7f59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setThreadgroupMemoryLength(_:index:)

<sub>Instance Method</sub>

Configures the size of a block of threadgroup memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setThreadgroupMemoryLength(_ length: Int, index: Int)
```

## Parameters

- `length` — The size of the threadgroup memory, in bytes, which needs to be a multiple of `16` bytes.

- `index` — The index in the threadgroup memory argument table using this allocation.

## Discussion

> [!important] Important
> The sum of all threadgroup memory allocations (whether made using this method or directly in the shader) can’t exceed the device limits for threadgroup memory. Check threadgroup memory limits with the [staticThreadgroupMemoryLength](../mtlcomputepipelinestate/staticthreadgroupmemorylength.md) property.

The `threadgroup` memory space allows for sharing data between multiple threads in a threadgroup, which can be faster than using `device` memory in your kernels. Before using any threadgroup memory, call this method to configure the threadgroup memory argument table. Kernels accessing their arguments from threadgroup memory have the `[[threadgroup]]` attribute.

To learn more about using the threadgroup address space, see the [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf#//apple_ref/doc/uid/TP40014364-CH4-SW5) section 4.4.

## See Also

### Configuring tile memory

- [- setImageblockWidth:height:](<setimageblockwidth(__height_).md>) — Sets the size, in pixels, of imageblock data in tile memory.
