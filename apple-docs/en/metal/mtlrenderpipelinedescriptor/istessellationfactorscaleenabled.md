---
title: isTessellationFactorScaleEnabled
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/istessellationfactorscaleenabled
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/istessellationfactorscaleenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/istessellationfactorscaleenabled.json'
content_hash: 'sha256:b227084e5c6ed1cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# isTessellationFactorScaleEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether the pipeline scales the tessellation factor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isTessellationFactorScaleEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

If this value is [true](../../swift/true.md), a scale factor is applied to the tessellation factors after the patch cull check is performed but before the tessellation factors are clamped to the value of [maxTessellationFactor](maxtessellationfactor.md). The scale factor is applied only if the patch is not culled.

## See Also

### Related Documentation

- [- setTessellationFactorScale:](<../mtlrendercommandencoder/settessellationfactorscale(__).md>) — Configures the scale factor for per-patch tessellation factors.

### Specifying tessellation state

- [maxTessellationFactor](maxtessellationfactor.md) — The maximum tessellation factor that the tessellator uses when tessellating patches.
- [tessellationFactorFormat](tessellationfactorformat.md) — The format of the tessellation factors in the tessellation factor buffer.
- [tessellationControlPointIndexType](tessellationcontrolpointindextype.md) — The size of the control point indices in a control point index buffer.
- [tessellationFactorStepFunction](tessellationfactorstepfunction.md) — The step function for determining the tessellation factors for a patch from the tessellation factor buffer.
- [tessellationOutputWindingOrder](tessellationoutputwindingorder.md) — The winding order of triangles from the tessellator.
- [tessellationPartitionMode](tessellationpartitionmode.md) — The partitioning mode that the tessellator uses to derive the number and spacing of segments for subdividing a corresponding edge.
- [MTLTessellationFactorFormat](../mtltessellationfactorformat.md) — Options for specifying the format of the tessellation factors in a tessellation factor buffer.
- [MTLTessellationControlPointIndexType](../mtltessellationcontrolpointindextype.md) — Options for specifying the size of the control point indices in a control point index buffer.
- [MTLTessellationFactorStepFunction](../mtltessellationfactorstepfunction.md) — Options for specifying the step function that determines the tessellation factors for a patch from the tessellation factor buffer.
- [MTLTessellationPartitionMode](../mtltessellationpartitionmode.md) — Options for choosing the partition mode that the tessellator applies when deriving the number and spacing of segments for subdividing a corresponding edge.
