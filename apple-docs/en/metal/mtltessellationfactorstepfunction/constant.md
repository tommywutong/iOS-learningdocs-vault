---
title: MTLTessellationFactorStepFunction.constant
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltessellationfactorstepfunction/constant
source_url: 'https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/constant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltessellationfactorstepfunction/constant.json'
content_hash: 'sha256:b4105c557203452e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTessellationFactorStepFunction](../mtltessellationfactorstepfunction.md)

# MTLTessellationFactorStepFunction.constant

<sub>Case</sub>

A constant step function. For all instances, the tessellation factor for all patches in a patch draw call is at the `offset` location in the tessellation factor buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case constant
```

## See Also

### Factor step functions

- [MTLTessellationFactorStepFunctionPerPatch](perpatch.md) — A per-patch step function. For all instances, the tessellation factor for all patches in a patch draw call is at the `offset + (drawPatchIndex * tessellationFactorStride)` location in the tessellation factor buffer.
- [MTLTessellationFactorStepFunctionPerInstance](perinstance.md) — A per-instance step function. For a given instance ID, the tessellation factor for a patch in a patch draw call is at the `offset + (instanceID * instanceStride)` location in the tessellation factor buffer.
- [MTLTessellationFactorStepFunctionPerPatchAndPerInstance](perpatchandperinstance.md) — A per-patch and per-instance step function. For a given instance ID, the tessellation factor for a patch in a patch draw call is at the `offset + (drawPatchIndex * tessellationFactorStride + instanceID * instanceStride)` location in the tessellation factor buffer.
