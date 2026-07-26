---
title: radiusBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusbuffers
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusbuffers.json'
content_hash: 'sha256:cee12aee893d8565'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionCurveGeometryDescriptor](../mtl4accelerationstructuremotioncurvegeometrydescriptor.md)

# radiusBuffers

<sub>Instance Property</sub>

Assigns a reference to a buffer containing, in turn, references to curve radii buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var radiusBuffers: MTL4BufferRange { get set }
```

## Discussion

This property references a buffer that conceptually represents an array with one entry for each keyframe in the motion animation. Each one of these entries consists of a [MTL4BufferRange](../mtl4bufferrange.md) that, in turn, references a buffer containing the radii corresponding to the keyframe.

Metal interpolates curve radii according to the basis function you specify via [curveBasis](curvebasis.md).

You are responsible for ensuring the type of each radius matches the type property [radiusFormat](radiusformat.md) specifies, that each radius is at least zero, and that the buffer address of the top-level buffer, as well as of buffer it references, is not zero.
