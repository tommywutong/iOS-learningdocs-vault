---
title: motionTransformsCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motiontransformscount
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motiontransformscount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motiontransformscount.json'
content_hash: 'sha256:eafcecf6f2556968'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectAccelerationStructureMotionInstanceDescriptor](../mtlindirectaccelerationstructuremotioninstancedescriptor.md)

# motionTransformsCount

<sub>Instance Property</sub>

The number of motion transforms belonging to the motion instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformsCount: UInt32
```

## See Also

### Specifying motion data

- [motionStartTime](motionstarttime.md) — The start time of the motion instance.
- [motionStartBorderMode](motionstartbordermode.md) — The motion border mode describing what happens if Metal samples the acceleration structure before the motion start time.
- [motionEndTime](motionendtime.md) — The end time of the motion instance.
- [motionEndBorderMode](motionendbordermode.md) — The motion border mode describing what happens if Metal samples the acceleration structure after the motion end time.
- [motionTransformsStartIndex](motiontransformsstartindex.md) — The index of the first set of transforms describing one keyframe of the animation.
