---
title: MTLTessellationFactorStepFunction.perInstance
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltessellationfactorstepfunction/perinstance
source_url: 'https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/perinstance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltessellationfactorstepfunction/perinstance.json'
content_hash: 'sha256:d100b7fa40a1d2c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTessellationFactorStepFunction](../mtltessellationfactorstepfunction.md)

# MTLTessellationFactorStepFunction.perInstance

<sub>Case</sub>

A per-instance step function. For a given instance ID, the tessellation factor for a patch in a patch draw call is at the `offset + (instanceID * instanceStride)` location in the tessellation factor buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case perInstance
```

## See Also

### Factor step functions

- [MTLTessellationFactorStepFunctionConstant](constant.md) — A constant step function. For all instances, the tessellation factor for all patches in a patch draw call is at the `offset` location in the tessellation factor buffer.
- [MTLTessellationFactorStepFunctionPerPatch](perpatch.md) — A per-patch step function. For all instances, the tessellation factor for all patches in a patch draw call is at the `offset + (drawPatchIndex * tessellationFactorStride)` location in the tessellation factor buffer.
- [MTLTessellationFactorStepFunctionPerPatchAndPerInstance](perpatchandperinstance.md) — A per-patch and per-instance step function. For a given instance ID, the tessellation factor for a patch in a patch draw call is at the `offset + (drawPatchIndex * tessellationFactorStride + instanceID * instanceStride)` location in the tessellation factor buffer.
