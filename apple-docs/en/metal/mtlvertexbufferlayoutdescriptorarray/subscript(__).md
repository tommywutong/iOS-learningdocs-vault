---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlvertexbufferlayoutdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexbufferlayoutdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:5b7b1f6590b2f577'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexBufferLayoutDescriptorArray](../mtlvertexbufferlayoutdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the state of the specified vertex buffer layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(index: Int) -> MTLVertexBufferLayoutDescriptor! { get set }
```

## Parameters

- `index` — A specified index in the array of vertex buffer layouts.

## Return Value

A descriptor that contains vertex buffer layout state.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
