---
title: MTLCurveBasis
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcurvebasis
source_url: 'https://developer.apple.com/documentation/metal/mtlcurvebasis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcurvebasis.json'
content_hash: 'sha256:e07f1cf9f1640899'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCurveBasis

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLCurveBasis
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTLCurveBasisBSpline](mtlcurvebasis/bspline.md)
- [MTLCurveBasisBezier](mtlcurvebasis/bezier.md)
- [MTLCurveBasisCatmullRom](mtlcurvebasis/catmullrom.md)
- [MTLCurveBasisLinear](mtlcurvebasis/linear.md)

### Initializers

- [init(rawValue:)](<mtlcurvebasis/init(rawvalue_).md>)

## See Also

### Geometry descriptors

- [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md) — Base class for all Metal 4 acceleration structure geometry descriptors.
- [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md) — A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md) — Describes triangle geometry suitable for ray tracing.
- [MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md) — A description of a list of triangle primitives to turn into an acceleration structure.
- [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md) — Describes curve geometry suitable for ray tracing.
- [MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md) — A descriptor you configure with curve geometry for building acceleration structures.
- [MTLCurveType](mtlcurvetype.md)
- [MTLCurveEndCaps](mtlcurveendcaps.md)
- [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md) — Describes bounding-box geometry suitable for ray tracing.
- [MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes to turn into an acceleration structure.
