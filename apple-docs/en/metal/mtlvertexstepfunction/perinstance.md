---
title: MTLVertexStepFunction.perInstance
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexstepfunction/perinstance
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexstepfunction/perinstance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexstepfunction/perinstance.json'
content_hash: 'sha256:ffd8a40e6e43acf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexStepFunction](../mtlvertexstepfunction.md)

# MTLVertexStepFunction.perInstance

<sub>Case</sub>

The vertex function regularly fetches new attribute data for a number of instances that is determined by `stepRate`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case perInstance
```

## See Also

### Step functions

- [MTLVertexStepFunctionConstant](constant.md) — The vertex function fetches attribute data once and uses that data for every vertex.
- [MTLVertexStepFunctionPerVertex](pervertex.md) — The vertex function fetches and uses new attribute data for every vertex.
- [MTLVertexStepFunctionPerPatch](perpatch.md) — The post-tessellation vertex function fetches data based on the patch index of the patch.
- [MTLVertexStepFunctionPerPatchControlPoint](perpatchcontrolpoint.md) — The post-tessellation vertex function fetches data based on the control-point indices associated with the patch.
