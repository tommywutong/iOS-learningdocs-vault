---
title: motionEndTime
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionendtime
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionendtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionendtime.json'
content_hash: 'sha256:9c31231aa43582de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectAccelerationStructureMotionInstanceDescriptor](../mtlindirectaccelerationstructuremotioninstancedescriptor.md)

# motionEndTime

<sub>Instance Property</sub>

The end time of the motion instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionEndTime: Float
```

## See Also

### Specifying motion data

- [motionStartTime](motionstarttime.md) — The start time of the motion instance.
- [motionStartBorderMode](motionstartbordermode.md) — The motion border mode describing what happens if Metal samples the acceleration structure before the motion start time.
- [motionEndBorderMode](motionendbordermode.md) — The motion border mode describing what happens if Metal samples the acceleration structure after the motion end time.
- [motionTransformsCount](motiontransformscount.md) — The number of motion transforms belonging to the motion instance.
- [motionTransformsStartIndex](motiontransformsstartindex.md) — The index of the first set of transforms describing one keyframe of the animation.
