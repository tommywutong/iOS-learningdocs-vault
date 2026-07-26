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
doc_path: /documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode.json'
content_hash: 'sha256:9b14e4ecb15e91db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)

# motionEndBorderMode

<sub>Instance Property</sub>

A behavior that configures how a motion instance handles timestamps after an ending time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionEndBorderMode: MTLMotionBorderMode
```

## Discussion

The property’s default value is [MTLMotionBorderModeClamp](../mtlmotionbordermode/clamp.md).

## See Also

### Specifying motion data

- [motionStartTime](motionstarttime.md) — A starting time for the range of motion that the key-frame data represents.
- [motionEndTime](motionendtime.md) — An ending time for the range of motion that the key-frame data represents.
- [motionStartBorderMode](motionstartbordermode.md) — A behavior that configures how a motion instance handles timestamps before a starting time.
- [motionTransformsStartIndex](motiontransformsstartindex.md) — The index of motion data that represents the first key-frame motion data, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [motionTransformsCount](motiontransformscount.md) — The number of motion data key-frames, which applies to the next acceleration-structure motion instance you create with the descriptor.
