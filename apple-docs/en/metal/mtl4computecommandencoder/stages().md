---
title: stages()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4computecommandencoder/stages()
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/stages()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/stages%28%29.json'
content_hash: 'sha256:61dec52e9d2e3881'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# stages()

<sub>Instance Method</sub>

Queries a bitmask representing the shader stages on which commands currently present in this command encoder operate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func stages() -> MTLStages
```

## Return Value

A bitmask representing shader stages that commands currently present in this command encoder operate on.

## Discussion

Metal dynamically updates this property based on the commands you encode into the command encoder, for example, it sets the bit [MTLStageDispatch](../mtlstages/dispatch.md) if this encoder contains any commands that dispatch a compute kernel.

Similarly, it sets the bit [MTLStageBlit](../mtlstages/blit.md) if this encoder contains any commands to copy or modify buffers, textures, or indirect command buffers.

Finally, Metal sets the bit [MTLStageAccelerationStructure](../mtlstages/accelerationstructure.md) if this encoder contains any commands that build, copy, or refit acceleration structures.
