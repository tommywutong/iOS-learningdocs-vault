---
title: maxKernelBufferBindCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandbufferdescriptor/maxkernelbufferbindcount
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/maxkernelbufferbindcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbufferdescriptor/maxkernelbufferbindcount.json'
content_hash: 'sha256:79db19af9955475b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBufferDescriptor](../mtlindirectcommandbufferdescriptor.md)

# maxKernelBufferBindCount

<sub>Instance Property</sub>

The maximum number of buffers that you can set per command for the compute kernel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxKernelBufferBindCount: Int { get set }
```

## Discussion

Metal ignores this property if [inheritBuffers](inheritbuffers.md) is [true](../../swift/true.md) or if you configured [commandTypes](commandtypes.md) for rendering commands. Metal needs to reserve enough memory in each command to store this many arguments. Use the smallest value that works for all commands you plan to encode into the indirect command buffer.

## See Also

### Declaring the maximum number of argument buffers per command

- [maxVertexBufferBindCount](maxvertexbufferbindcount.md) — The maximum number of buffers that you can set per command for the vertex stage.
- [maxFragmentBufferBindCount](maxfragmentbufferbindcount.md) — The maximum number of buffers that you can set per command for the fragment stage.
