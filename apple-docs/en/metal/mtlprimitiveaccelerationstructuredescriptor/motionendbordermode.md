---
title: motionEndBorderMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionendbordermode
source_url: 'https://developer.apple.com/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionendbordermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionendbordermode.json'
content_hash: 'sha256:5d65a64796b6f7e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPrimitiveAccelerationStructureDescriptor](../mtlprimitiveaccelerationstructuredescriptor.md)

# motionEndBorderMode

<sub>Instance Property</sub>

The mode to use when handling timestamps after the end time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionEndBorderMode: MTLMotionBorderMode { get set }
```

## Discussion

The default value is [MTLMotionBorderModeClamp](../mtlmotionbordermode/clamp.md).

## See Also

### Specifying motion behavior

- [motionKeyframeCount](motionkeyframecount.md) — The number of keyframes in the geometry data.
- [motionStartTime](motionstarttime.md) — The start time for the range of motion that the keyframe data describes.
- [motionEndTime](motionendtime.md) — The end time for the range of motion that the keyframe data describes.
- [motionStartBorderMode](motionstartbordermode.md) — The mode to use when handling timestamps before the start time.
- [MTLMotionBorderMode](../mtlmotionbordermode.md) — Options for specifying how the acceleration structure handles timestamps that are outside the specified range.
