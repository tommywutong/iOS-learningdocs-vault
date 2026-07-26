---
title: MTLStepFunction.perPatchControlPoint
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstepfunction/perpatchcontrolpoint
source_url: 'https://developer.apple.com/documentation/metal/mtlstepfunction/perpatchcontrolpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstepfunction/perpatchcontrolpoint.json'
content_hash: 'sha256:877256c6acaba18f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStepFunction](../mtlstepfunction.md)

# MTLStepFunction.perPatchControlPoint

<sub>Case</sub>

The post-tessellation function fetches data based on the control-point indices associated with the patch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case perPatchControlPoint
```

## See Also

### Step options

- [MTLStepFunctionConstant](constant.md) — The function fetches attribute data once.
- [MTLStepFunctionPerInstance](perinstance.md) — The function fetches data based on the instance index.
- [MTLStepFunctionPerPatch](perpatch.md) — The post-tessellation function fetches data based on the patch index of the patch.
- [MTLStepFunctionPerVertex](pervertex.md) — The vertex function fetches data for every vertex.
- [MTLStepFunctionThreadPositionInGridX](threadpositioningridx.md) — The compute function fetches data based on the thread’s `x` coordinate.
- [MTLStepFunctionThreadPositionInGridY](threadpositioningridy.md) — The compute function fetches data based on the thread’s `y` coordinate.
- [MTLStepFunctionThreadPositionInGridXIndexed](threadpositioningridxindexed.md) — The compute function fetches data by using the thread’s `x` coordinate to look up a value in the index buffer.
- [MTLStepFunctionThreadPositionInGridYIndexed](threadpositioningridyindexed.md) — The compute function fetches data by using the thread’s `y` coordinate to look up a value in the index buffer.
