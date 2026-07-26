---
title: maxMotionTransformCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount.json'
content_hash: 'sha256:78976e80fc3bdace'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4IndirectInstanceAccelerationStructureDescriptor](../mtl4indirectinstanceaccelerationstructuredescriptor.md)

# maxMotionTransformCount

<sub>Instance Property</sub>

Controls the maximum number of motion transforms in the motion transform buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxMotionTransformCount: Int { get set }
```

## Discussion

You are responsible for ensuring that final number of motion transforms at build time that the buffer [motionTransformCountBuffer](motiontransformcountbuffer.md) references is less than or equal to this number.
