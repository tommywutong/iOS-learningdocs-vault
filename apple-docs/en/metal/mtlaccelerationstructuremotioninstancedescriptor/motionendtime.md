---
title: motionEndTime
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionendtime
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionendtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionendtime.json'
content_hash: 'sha256:e40d31587b4b1f91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)

# motionEndTime

<sub>Instance Property</sub>

An ending time for the range of motion that the key-frame data represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionEndTime: Float
```

## Discussion

The [motionTransformsStartIndex](motiontransformsstartindex.md) and [motionTransformsCount](motiontransformscount.md) properties represent the key-frame motion data.

The property’s default value is  `1.0`.

## See Also

### Specifying motion data

- [motionStartTime](motionstarttime.md) — A starting time for the range of motion that the key-frame data represents.
- [motionStartBorderMode](motionstartbordermode.md) — A behavior that configures how a motion instance handles timestamps before a starting time.
- [motionEndBorderMode](motionendbordermode.md) — A behavior that configures how a motion instance handles timestamps after an ending time.
- [motionTransformsStartIndex](motiontransformsstartindex.md) — The index of motion data that represents the first key-frame motion data, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [motionTransformsCount](motiontransformscount.md) — The number of motion data key-frames, which applies to the next acceleration-structure motion instance you create with the descriptor.
