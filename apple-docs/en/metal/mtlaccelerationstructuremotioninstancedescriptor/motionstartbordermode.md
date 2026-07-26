---
title: motionStartBorderMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionstartbordermode
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionstartbordermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionstartbordermode.json'
content_hash: 'sha256:4df6616e5b85e232'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)

# motionStartBorderMode

<sub>Instance Property</sub>

A behavior that configures how a motion instance handles timestamps before a starting time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionStartBorderMode: MTLMotionBorderMode
```

## Discussion

The property’s default value is [MTLMotionBorderModeClamp](../mtlmotionbordermode/clamp.md).

## See Also

### Specifying motion data

- [motionStartTime](motionstarttime.md) — A starting time for the range of motion that the key-frame data represents.
- [motionEndTime](motionendtime.md) — An ending time for the range of motion that the key-frame data represents.
- [motionEndBorderMode](motionendbordermode.md) — A behavior that configures how a motion instance handles timestamps after an ending time.
- [motionTransformsStartIndex](motiontransformsstartindex.md) — The index of motion data that represents the first key-frame motion data, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [motionTransformsCount](motiontransformscount.md) — The number of motion data key-frames, which applies to the next acceleration-structure motion instance you create with the descriptor.
