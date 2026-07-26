---
title: motionEndBorderMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4primitiveaccelerationstructuredescriptor/motionendbordermode
source_url: 'https://developer.apple.com/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/motionendbordermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/motionendbordermode.json'
content_hash: 'sha256:e8ea49ac457fd974'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4PrimitiveAccelerationStructureDescriptor](../mtl4primitiveaccelerationstructuredescriptor.md)

# motionEndBorderMode

<sub>Instance Property</sub>

Configures the motion border mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionEndBorderMode: MTLMotionBorderMode { get set }
```

## Discussion

This property controls what happens if Metal samples the acceleration structure after [motionEndTime](motionendtime.md).

Its default value is `MTLMotionBorderModeClamp`.
