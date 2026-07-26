---
title: logState
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferdescriptor/logstate
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferdescriptor/logstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferdescriptor/logstate.json'
content_hash: 'sha256:4c4a6211c6cce30c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferDescriptor](../mtlcommandbufferdescriptor.md)

# logState

<sub>Instance Property</sub>

The shader logging configuration that the command buffer uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var logState: (any MTLLogState)? { get set }
```

## See Also

### Configuring the command buffer

- [retainedReferences](retainedreferences.md) — A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.
- [errorOptions](erroroptions.md) — The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.
- [MTLCommandBufferErrorOption](../mtlcommandbuffererroroption.md) — Options for reporting errors from a command buffer.
