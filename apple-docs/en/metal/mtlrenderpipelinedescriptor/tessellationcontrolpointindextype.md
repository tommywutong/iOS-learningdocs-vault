---
title: tessellationControlPointIndexType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/tessellationcontrolpointindextype
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/tessellationcontrolpointindextype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/tessellationcontrolpointindextype.json'
content_hash: 'sha256:fd839978141faf4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# tessellationControlPointIndexType

<sub>Instance Property</sub>

The size of the control point indices in a control point index buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tessellationControlPointIndexType: MTLTessellationControlPointIndexType { get set }
```

## Discussion

The default value is [MTLTessellationControlPointIndexTypeNone](../mtltessellationcontrolpointindextype/none.md); use this value when drawing patches without a control point index buffer. This value needs to be either [MTLTessellationControlPointIndexTypeUInt16](../mtltessellationcontrolpointindextype/uint16.md) or [MTLTessellationControlPointIndexTypeUInt32](../mtltessellationcontrolpointindextype/uint32.md) when drawing patches with indexed control points.

## See Also

### Related Documentation

- [- drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:](<../mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints_patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffse-12f3c1a50f.md>) — Encodes a draw command that renders multiple instances of tessellated patches with a control point index buffer.
- [- drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:](<../mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffset_indirectbuffer_indirectbufferoffset_).md>) — Encodes a draw command that renders multiple instances of tessellated patches with a control point index buffer and indirect arguments.

### Specifying tessellation state

- [maxTessellationFactor](maxtessellationfactor.md) — The maximum tessellation factor that the tessellator uses when tessellating patches.
- [tessellationFactorScaleEnabled](istessellationfactorscaleenabled.md) — A Boolean value that determines whether the pipeline scales the tessellation factor.
- [tessellationFactorFormat](tessellationfactorformat.md) — The format of the tessellation factors in the tessellation factor buffer.
- [tessellationFactorStepFunction](tessellationfactorstepfunction.md) — The step function for determining the tessellation factors for a patch from the tessellation factor buffer.
- [tessellationOutputWindingOrder](tessellationoutputwindingorder.md) — The winding order of triangles from the tessellator.
- [tessellationPartitionMode](tessellationpartitionmode.md) — The partitioning mode that the tessellator uses to derive the number and spacing of segments for subdividing a corresponding edge.
- [MTLTessellationFactorFormat](../mtltessellationfactorformat.md) — Options for specifying the format of the tessellation factors in a tessellation factor buffer.
- [MTLTessellationControlPointIndexType](../mtltessellationcontrolpointindextype.md) — Options for specifying the size of the control point indices in a control point index buffer.
- [MTLTessellationFactorStepFunction](../mtltessellationfactorstepfunction.md) — Options for specifying the step function that determines the tessellation factors for a patch from the tessellation factor buffer.
- [MTLTessellationPartitionMode](../mtltessellationpartitionmode.md) — Options for choosing the partition mode that the tessellator applies when deriving the number and spacing of segments for subdividing a corresponding edge.
