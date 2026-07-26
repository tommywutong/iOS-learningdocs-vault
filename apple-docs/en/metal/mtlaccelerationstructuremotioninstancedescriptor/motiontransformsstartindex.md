---
title: motionTransformsStartIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.json'
content_hash: 'sha256:4776fb45ea532f3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)

# motionTransformsStartIndex

<sub>Instance Property</sub>

The index of motion data that represents the first key-frame motion data, which applies to the next acceleration-structure motion instance you create with the descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformsStartIndex: UInt32
```

## Discussion

The index points to an entry in an [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md) instance’s transform data, which it stores in its [motionTransformBuffer](../mtlinstanceaccelerationstructuredescriptor/motiontransformbuffer.md) property.

## See Also

### Specifying motion data

- [motionStartTime](motionstarttime.md) — A starting time for the range of motion that the key-frame data represents.
- [motionEndTime](motionendtime.md) — An ending time for the range of motion that the key-frame data represents.
- [motionStartBorderMode](motionstartbordermode.md) — A behavior that configures how a motion instance handles timestamps before a starting time.
- [motionEndBorderMode](motionendbordermode.md) — A behavior that configures how a motion instance handles timestamps after an ending time.
- [motionTransformsCount](motiontransformscount.md) — The number of motion data key-frames, which applies to the next acceleration-structure motion instance you create with the descriptor.
