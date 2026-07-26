---
title: MTLTessellationControlPointIndexType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltessellationcontrolpointindextype
source_url: 'https://developer.apple.com/documentation/metal/mtltessellationcontrolpointindextype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltessellationcontrolpointindextype.json'
content_hash: 'sha256:72fc744197297630'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTessellationControlPointIndexType

<sub>Enumeration</sub>

Options for specifying the size of the control point indices in a control point index buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLTessellationControlPointIndexType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Index types

- [MTLTessellationControlPointIndexTypeNone](mtltessellationcontrolpointindextype/none.md) — No size. This value should only be used when drawing patches without a control point index buffer.
- [MTLTessellationControlPointIndexTypeUInt16](mtltessellationcontrolpointindextype/uint16.md) — The size of a 16-bit unsigned integer.
- [MTLTessellationControlPointIndexTypeUInt32](mtltessellationcontrolpointindextype/uint32.md) — The size of a 32-bit unsigned integer.

### Initializers

- [init(rawValue:)](<mtltessellationcontrolpointindextype/init(rawvalue_).md>)

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
- [MTLTessellationFactorStepFunction](mtltessellationfactorstepfunction.md) — Options for specifying the step function that determines the tessellation factors for a patch from the tessellation factor buffer.
- [MTLTessellationPartitionMode](mtltessellationpartitionmode.md) — Options for choosing the partition mode that the tessellator applies when deriving the number and spacing of segments for subdividing a corresponding edge.
