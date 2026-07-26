---
title: inheritBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandbufferdescriptor/inheritbuffers
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/inheritbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbufferdescriptor/inheritbuffers.json'
content_hash: 'sha256:5353c7ba0158ad15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBufferDescriptor](../mtlindirectcommandbufferdescriptor.md)

# inheritBuffers

<sub>Instance Property</sub>

A Boolean value that determines where commands in the indirect command buffer get their buffer arguments from when you execute them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inheritBuffers: Bool { get set }
```

## Discussion

Always set this property explicitly.

If you set the value to [true](../../swift/true.md), don’t set buffer arguments when you encode commands into the indirect command buffer. The commands use (inherit) the buffer arguments that you set on the parent encoder.

If you set the value to [false](../../swift/false.md), set the buffer arguments when you encode the commands into the indirect command buffer. The commands ignore any buffer arguments set on the parent encoder.

## See Also

### Declaring command inheritance

- [inheritPipelineState](inheritpipelinestate.md) — A Boolean value that determines where commands in the indirect command buffer get their pipeline state from when you execute them.
