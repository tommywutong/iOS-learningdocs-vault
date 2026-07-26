---
title: 'barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandencoder/barrierafterencoderstages:beforeencoderstages:visibilityoptions:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandencoder/barrierafterencoderstages:beforeencoderstages:visibilityoptions:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandencoder/barrierafterencoderstages%3Abeforeencoderstages%3Avisibilityoptions%3A.json'
content_hash: 'sha256:acd7e096b40f2f0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandEncoder](../mtl4commandencoder.md)

# barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:

<sub>Instance Method</sub>

Encodes an intra-pass barrier that instructs the GPU to pause before running stages of subsequent commands until stages of previous commands complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) barrierAfterEncoderStages:(MTLStages) afterEncoderStages beforeEncoderStages:(MTLStages) beforeEncoderStages visibilityOptions:(MTL4VisibilityOptions) visibilityOptions;
```

## Parameters

- `afterEncoderStages` — [MTLStages](../mtlstages.md) the stages of the previous commands of this pass that need to complete before the stages in `beforeEncoderStages` start for subsequent commands you encode in this pass.

- `beforeEncoderStages` — [MTLStages](../mtlstages.md) the stages of the subsequent commands you encode in this pass that wait for the stages in `afterEncoderStages`, within this pass, to complete.

- `visibilityOptions` — [MTL4VisibilityOptions](../mtl4visibilityoptions.md) of the barrier, controlling cache flush behavior.

## Discussion

Encode a barrier that guarantees that any subsequent work you encode in the _current command encoder_, corresponding to `beforeEncoderStages`, doesn’t begin until all prior commands in this command encoder, corresponding to `afterEncoderStages`, completes.

When calling this method, it’s your responsibility to ensure parameters `afterEncoderStages` and `beforeEncoderStages` contain a combination of [MTLStages](../mtlstages.md) for which this encoder can encode commands. For example, for a [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md) instance, you can provide any combination of [MTLStageDispatch](../mtlstages/dispatch.md), [MTLStageBlit](../mtlstages/blit.md) and [MTLStageAccelerationStructure](../mtlstages/accelerationstructure.md).
