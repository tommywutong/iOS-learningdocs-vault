---
title: 'barrier(afterEncoderStages:beforeEncoderStages:visibilityOptions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandencoder/barrier(afterencoderstages:beforeencoderstages:visibilityoptions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandencoder/barrier(afterencoderstages:beforeencoderstages:visibilityoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandencoder/barrier%28afterencoderstages%3Abeforeencoderstages%3Avisibilityoptions%3A%29.json'
content_hash: 'sha256:ccff4a5d8e9c5457'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandEncoder](../mtl4commandencoder.md)

# barrier(afterEncoderStages:beforeEncoderStages:visibilityOptions:)

<sub>Instance Method</sub>

Encodes an intra-pass barrier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func barrier(afterEncoderStages: MTLStages, beforeEncoderStages: MTLStages, visibilityOptions: MTL4VisibilityOptions = [ .device ])
```

## Parameters

- `afterEncoderStages` — [MTLStages](../mtlstages.md) mask that represents the stages of work to wait for. This argument only applies to subsequent work you encode in the current command encoder.

- `beforeEncoderStages` — [MTLStages](../mtlstages.md) mask that represents the stages of work that wait. This argument only applies to work you encode in the current command encoder prior to this barrier.

- `visibilityOptions` — [MTL4VisibilityOptions](../mtl4visibilityoptions.md) of the barrier, controlling cache flush behavior.

## Discussion

Encode a barrier that guarantees that any subsequent work you encode in the _current command encoder_, corresponding to `beforeEncoderStages`, doesn’t begin until all prior commands in this command encoder, corresponding to `afterEncoderStages`, completes.

When calling this method, it’s your responsibility to ensure parameters `afterEncoderStages` and `beforeEncoderStages` contain a combination of [MTLStages](../mtlstages.md) for which this encoder can encode commands. For example, for a [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md) instance, you can provide any combination of [MTLStageDispatch](../mtlstages/dispatch.md), [MTLStageBlit](../mtlstages/blit.md) and [MTLStageAccelerationStructure](../mtlstages/accelerationstructure.md).
