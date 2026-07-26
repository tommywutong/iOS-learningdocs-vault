---
title: maxVertexBufferBindCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandbufferdescriptor/maxvertexbufferbindcount
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/maxvertexbufferbindcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbufferdescriptor/maxvertexbufferbindcount.json'
content_hash: 'sha256:c9134d1f071b33b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBufferDescriptor](../mtlindirectcommandbufferdescriptor.md)

# maxVertexBufferBindCount

<sub>Instance Property</sub>

The maximum number of buffers that you can set per command for the vertex stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxVertexBufferBindCount: Int { get set }
```

## Discussion

Metal ignores this property if [inheritBuffers](inheritbuffers.md) is [true](../../swift/true.md) or if you configured [commandTypes](commandtypes.md) for compute commands. Metal needs to reserve enough memory in each command to store this many arguments. Use the smallest value that works for all commands you plan to encode into the indirect command buffer.

## See Also

### Declaring the maximum number of argument buffers per command

- [maxFragmentBufferBindCount](maxfragmentbufferbindcount.md) — The maximum number of buffers that you can set per command for the fragment stage.
- [maxKernelBufferBindCount](maxkernelbufferbindcount.md) — The maximum number of buffers that you can set per command for the compute kernel.
