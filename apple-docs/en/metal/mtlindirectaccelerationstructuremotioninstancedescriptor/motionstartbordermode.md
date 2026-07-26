---
title: motionStartBorderMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionstartbordermode
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionstartbordermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionstartbordermode.json'
content_hash: 'sha256:d2b104afd5eee290'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectAccelerationStructureMotionInstanceDescriptor](../mtlindirectaccelerationstructuremotioninstancedescriptor.md)

# motionStartBorderMode

<sub>Instance Property</sub>

The motion border mode describing what happens if Metal samples the acceleration structure before the motion start time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionStartBorderMode: MTLMotionBorderMode
```

## See Also

### Specifying motion data

- [motionStartTime](motionstarttime.md) — The start time of the motion instance.
- [motionEndTime](motionendtime.md) — The end time of the motion instance.
- [motionEndBorderMode](motionendbordermode.md) — The motion border mode describing what happens if Metal samples the acceleration structure after the motion end time.
- [motionTransformsCount](motiontransformscount.md) — The number of motion transforms belonging to the motion instance.
- [motionTransformsStartIndex](motiontransformsstartindex.md) — The index of the first set of transforms describing one keyframe of the animation.
