---
title: MTLTessellationPartitionMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltessellationpartitionmode
source_url: 'https://developer.apple.com/documentation/metal/mtltessellationpartitionmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltessellationpartitionmode.json'
content_hash: 'sha256:41c435317e00aa22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTessellationPartitionMode

<sub>Enumeration</sub>

Options for choosing the partition mode that the tessellator applies when deriving the number and spacing of segments for subdividing a corresponding edge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLTessellationPartitionMode
```

## Overview

The table lists the tessellation factor range for each partitioning mode.

| Partitioning mode | Tessellation factor range |
|---|---|
| [MTLTessellationPartitionModePow2](mtltessellationpartitionmode/pow2.md) | [`1`, [maxTessellationFactor](mtlrenderpipelinedescriptor/maxtessellationfactor.md)] |
| [MTLTessellationPartitionModeInteger](mtltessellationpartitionmode/integer.md) | [`1`, [maxTessellationFactor](mtlrenderpipelinedescriptor/maxtessellationfactor.md)] |
| [MTLTessellationPartitionModeFractionalOdd](mtltessellationpartitionmode/fractionalodd.md) | [`1`, [maxTessellationFactor](mtlrenderpipelinedescriptor/maxtessellationfactor.md)-1] |
| [MTLTessellationPartitionModeFractionalEven](mtltessellationpartitionmode/fractionaleven.md) | [`2`, [maxTessellationFactor](mtlrenderpipelinedescriptor/maxtessellationfactor.md)] |

The floating-point tessellation level is always clamped to its corresponding range before calculating the final tessellation factor. After clamping, the calculation depends on the chosen partitioning mode:

- For the [MTLTessellationPartitionModePow2](mtltessellationpartitionmode/pow2.md) partitioning mode, the result is rounded up to the nearest integer `n`, where `n` is a power of two. The corresponding edge is divided into `n` segments of equal length in (u, v) space.
- For the [MTLTessellationPartitionModeInteger](mtltessellationpartitionmode/integer.md) partitioning mode, the result is rounded up to the nearest integer `n`. The corresponding edge is divided into `n` segments of equal length in (u, v) space.
- For the [MTLTessellationPartitionModeFractionalOdd](mtltessellationpartitionmode/fractionalodd.md) partitioning mode, the tessellation level is rounded up the the nearest odd integer `n`. If `n` is `1`, the edge is not subdivided. Otherwise, the corresponding edge is divided into `n-2` segments of equal length, and two additional segments of equal length that are typically shorter than the other segments. The length of the two additional segments relative to the others decreases monotonically by the value of `n-f`, where `f` is the clamped floating-point tessellation level. If `n-f` is `0` the additional segments equal length to the other segments. As `n-f` approaches `2`, the relative length of the additional segments approaches `0`. The two additional segments should be placed symmetrically on opposite sides of the subdivided edge. The relative location of these two segments is undefined, but needs to be identical for any pair of subdivided edges with identical values of `f`.
- For the [MTLTessellationPartitionModeFractionalEven](mtltessellationpartitionmode/fractionaleven.md) partitioning mode, the tessellation level is rounded up the the nearest even integer `n`.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Partition modes

- [MTLTessellationPartitionModePow2](mtltessellationpartitionmode/pow2.md) — A power of two partitioning mode.
- [MTLTessellationPartitionModeInteger](mtltessellationpartitionmode/integer.md) — An integer partitioning mode.
- [MTLTessellationPartitionModeFractionalOdd](mtltessellationpartitionmode/fractionalodd.md) — A fractional odd partitioning mode.
- [MTLTessellationPartitionModeFractionalEven](mtltessellationpartitionmode/fractionaleven.md) — A fractional even partitioning mode.

### Initializers

- [init(rawValue:)](<mtltessellationpartitionmode/init(rawvalue_).md>)

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
- [MTLTessellationFactorStepFunction](mtltessellationfactorstepfunction.md) — Options for specifying the step function that determines the tessellation factors for a patch from the tessellation factor buffer.
