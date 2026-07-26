---
title: 'setImageblockWidth(_:height:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setimageblockwidth(_:height:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setimageblockwidth(_:height:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setimageblockwidth%28_%3Aheight%3A%29.json'
content_hash: 'sha256:3aec5941908386c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setImageblockWidth(_:height:)

<sub>Instance Method</sub>

Sets the size, in pixels, of imageblock data in tile memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setImageblockWidth(_ width: Int, height: Int)
```

## Parameters

- `width` — The width of the imageblock, in pixels.

- `height` — The height of the imageblock, in pixels.

## Discussion

> [!important] Important
> The sum of all threadgroup memory allocations (whether made using this method or directly in the shader) can’t exceed the device limits for threadgroup memory. Check threadgroup memory limits with the [staticThreadgroupMemoryLength](../mtlcomputepipelinestate/staticthreadgroupmemorylength.md) property.

Both imageblocks and threadgroup memory share the available space you can reserve in tile memory, so the sum of these allocations can’t exceed the maximum total tile memory limit. To find the amount of memory used by an imageblock, call [- imageblockMemoryLengthForDimensions:](<../mtlcomputepipelinestate/imageblockmemorylength(fordimensions_).md>). Kernels accessing an imageblock argument from threadgroup memory have the `[[threadgroup_imageblock]]` attribute.

To learn more about using imageblocks, see the following sections in the [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf#//apple_ref/doc/uid/TP40014364-CH4-SW5):

- For information on the `threadgroup_imageblock` address space, see Section 4.5.
- For information on the `imageblock` type, see Section 2.11.

## See Also

### Configuring tile memory

- [- setThreadgroupMemoryLength:atIndex:](<setthreadgroupmemorylength(__index_).md>) — Configures the size of a block of threadgroup memory.
