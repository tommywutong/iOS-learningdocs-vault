---
title: MTLVertexStepFunction.perPatch
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexstepfunction/perpatch
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexstepfunction/perpatch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexstepfunction/perpatch.json'
content_hash: 'sha256:c05d762f0da3ace8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexStepFunction](../mtlvertexstepfunction.md)

# MTLVertexStepFunction.perPatch

<sub>Case</sub>

The post-tessellation vertex function fetches data based on the patch index of the patch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case perPatch
```

## See Also

### Step functions

- [MTLVertexStepFunctionConstant](constant.md) — The vertex function fetches attribute data once and uses that data for every vertex.
- [MTLVertexStepFunctionPerVertex](pervertex.md) — The vertex function fetches and uses new attribute data for every vertex.
- [MTLVertexStepFunctionPerInstance](perinstance.md) — The vertex function regularly fetches new attribute data for a number of instances that is determined by `stepRate`.
- [MTLVertexStepFunctionPerPatchControlPoint](perpatchcontrolpoint.md) — The post-tessellation vertex function fetches data based on the control-point indices associated with the patch.
