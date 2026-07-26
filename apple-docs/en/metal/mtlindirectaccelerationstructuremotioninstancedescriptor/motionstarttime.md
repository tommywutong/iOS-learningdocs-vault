---
title: motionStartTime
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionstarttime
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionstarttime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionstarttime.json'
content_hash: 'sha256:b2b244ac964ab697'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectAccelerationStructureMotionInstanceDescriptor](../mtlindirectaccelerationstructuremotioninstancedescriptor.md)

# motionStartTime

<sub>Instance Property</sub>

The start time of the motion instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionStartTime: Float
```

## See Also

### Specifying motion data

- [motionStartBorderMode](motionstartbordermode.md) — The motion border mode describing what happens if Metal samples the acceleration structure before the motion start time.
- [motionEndTime](motionendtime.md) — The end time of the motion instance.
- [motionEndBorderMode](motionendbordermode.md) — The motion border mode describing what happens if Metal samples the acceleration structure after the motion end time.
- [motionTransformsCount](motiontransformscount.md) — The number of motion transforms belonging to the motion instance.
- [motionTransformsStartIndex](motiontransformsstartindex.md) — The index of the first set of transforms describing one keyframe of the animation.
