---
title: MTLTessellationFactorStepFunction
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltessellationfactorstepfunction
source_url: 'https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltessellationfactorstepfunction.json'
content_hash: 'sha256:93e9fd6ed8c43742'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTessellationFactorStepFunction

<sub>Enumeration</sub>

Options for specifying the step function that determines the tessellation factors for a patch from the tessellation factor buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLTessellationFactorStepFunction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Factor step functions

- [MTLTessellationFactorStepFunctionConstant](mtltessellationfactorstepfunction/constant.md) — A constant step function. For all instances, the tessellation factor for all patches in a patch draw call is at the `offset` location in the tessellation factor buffer.
- [MTLTessellationFactorStepFunctionPerPatch](mtltessellationfactorstepfunction/perpatch.md) — A per-patch step function. For all instances, the tessellation factor for all patches in a patch draw call is at the `offset + (drawPatchIndex * tessellationFactorStride)` location in the tessellation factor buffer.
- [MTLTessellationFactorStepFunctionPerInstance](mtltessellationfactorstepfunction/perinstance.md) — A per-instance step function. For a given instance ID, the tessellation factor for a patch in a patch draw call is at the `offset + (instanceID * instanceStride)` location in the tessellation factor buffer.
- [MTLTessellationFactorStepFunctionPerPatchAndPerInstance](mtltessellationfactorstepfunction/perpatchandperinstance.md) — A per-patch and per-instance step function. For a given instance ID, the tessellation factor for a patch in a patch draw call is at the `offset + (drawPatchIndex * tessellationFactorStride + instanceID * instanceStride)` location in the tessellation factor buffer.

### Initializers

- [init(rawValue:)](<mtltessellationfactorstepfunction/init(rawvalue_).md>)

## See Also

### Specifying tessellation state

- [maxTessellationFactor](mtlrenderpipelinedescriptor/maxtessellationfactor.md) — The maximum tessellation factor that the tessellator uses when tessellating patches.
- [tessellationFactorScaleEnabled](mtlrenderpipelinedescriptor/istessellationfactorscaleenabled.md) — A Boolean value that determines whether the pipeline scales the tessellation factor.
- [tessellationFactorFormat](mtlrenderpipelinedescriptor/tessellationfactorformat.md) — The format of the tessellation factors in the tessellation factor buffer.
- [tessellationControlPointIndexType](mtlrenderpipelinedescriptor/tessellationcontrolpointindextype.md) — The size of the control point indices in a control point index buffer.
- [tessellationFactorStepFunction](mtlrenderpipelinedescriptor/tessellationfactorstepfunction.md) — The step function for determining the tessellation factors for a patch from the tessellation factor buffer.
- [tessellationOutputWindingOrder](mtlrenderpipelinedescriptor/tessellationoutputwindingorder.md) — The winding order of triangles from the tessellator.
- [tessellationPartitionMode](mtlrenderpipelinedescriptor/tessellationpartitionmode.md) — The partitioning mode that the tessellator uses to derive the number and spacing of segments for subdividing a corresponding edge.
- [MTLTessellationFactorFormat](mtltessellationfactorformat.md) — Options for specifying the format of the tessellation factors in a tessellation factor buffer.
- [MTLTessellationControlPointIndexType](mtltessellationcontrolpointindextype.md) — Options for specifying the size of the control point indices in a control point index buffer.
- [MTLTessellationPartitionMode](mtltessellationpartitionmode.md) — Options for choosing the partition mode that the tessellator applies when deriving the number and spacing of segments for subdividing a corresponding edge.
