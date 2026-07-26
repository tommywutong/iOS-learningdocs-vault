---
title: motionStartBorderMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4primitiveaccelerationstructuredescriptor/motionstartbordermode
source_url: 'https://developer.apple.com/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/motionstartbordermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/motionstartbordermode.json'
content_hash: 'sha256:f0e5fcbd8ddc20f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4PrimitiveAccelerationStructureDescriptor](../mtl4primitiveaccelerationstructuredescriptor.md)

# motionStartBorderMode

<sub>Instance Property</sub>

Configures the behavior when the ray-tracing system samples the acceleration structure before the motion start time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionStartBorderMode: MTLMotionBorderMode { get set }
```

## Discussion

Use this property to control the behavior when the ray-tracing system samples the acceleration structure at a time prior to the one you set for [motionStartTime](motionstarttime.md).

The default value of this property is `MTLMotionBorderModeClamp`.
