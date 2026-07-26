---
title: errorOptions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferdescriptor/erroroptions
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferdescriptor/erroroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferdescriptor/erroroptions.json'
content_hash: 'sha256:296c68bfe458d54c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferDescriptor](../mtlcommandbufferdescriptor.md)

# errorOptions

<sub>Instance Property</sub>

The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var errorOptions: MTLCommandBufferErrorOption { get set }
```

## Discussion

By default, a GPU driver doesn’t report additional error information.

To create a command buffer that saves additional GPU runtime error information, add the [MTLCommandBufferErrorOptionEncoderExecutionStatus](../mtlcommandbuffererroroption/encoderexecutionstatus.md) option to this property. If the GPU encounters an error as it runs the command buffer, you can retrieve the additional information from the command buffer’s [error](../mtlcommandbuffer/error.md) property.

> [!note] Note
> Enabling the [MTLCommandBufferErrorOptionEncoderExecutionStatus](../mtlcommandbuffererroroption/encoderexecutionstatus.md) option can slightly reduce your app’s CPU runtime performance.

## See Also

### Configuring the command buffer

- [logState](logstate.md) — The shader logging configuration that the command buffer uses.
- [retainedReferences](retainedreferences.md) — A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.
- [MTLCommandBufferErrorOption](../mtlcommandbuffererroroption.md) — Options for reporting errors from a command buffer.
