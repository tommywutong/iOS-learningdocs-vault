---
title: 'init(options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:userID:motionTransformsStartIndex:motionTransformsCount:motionStartBorderMode:motionEndBorderMode:motionStartTime:motionEndTime:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/init(options:mask:intersectionfunctiontableoffset:accelerationstructureindex:userid:motiontransformsstartindex:motiontransformscount:motionstartbordermode:motionendbordermode:motionstarttime:motionendtime:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/init(options:mask:intersectionfunctiontableoffset:accelerationstructureindex:userid:motiontransformsstartindex:motiontransformscount:motionstartbordermode:motionendbordermode:motionstarttime:motionendtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/init%28options%3Amask%3Aintersectionfunctiontableoffset%3Aaccelerationstructureindex%3Auserid%3Amotiontransformsstartindex%3Amotiontransformscount%3Amotionstartbordermode%3Amotionendbordermode%3Amotionstarttime%3Amotionendtime%3A%29.json'
content_hash: 'sha256:82a10e401f5fb59d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)

# init(options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:userID:motionTransformsStartIndex:motionTransformsCount:motionStartBorderMode:motionEndBorderMode:motionStartTime:motionEndTime:)

<sub>Initializer</sub>

Creates an acceleration-structure motion instance with the property values you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, accelerationStructureIndex: UInt32, userID: UInt32, motionTransformsStartIndex: UInt32, motionTransformsCount: UInt32, motionStartBorderMode: MTLMotionBorderMode, motionEndBorderMode: MTLMotionBorderMode, motionStartTime: Float, motionEndTime: Float)
```

## Parameters

- `options` — An option set for new acceleration-structure motion instances.

- `mask` — A mask for testing ray-tracing rays in a scene’s geometry for new acceleration-structure motion-instances.

- `intersectionFunctionTableOffset` — An offset into the intersection-function table for ray tracing.

- `accelerationStructureIndex` — The index of an acceleration structure that applies to new acceleration-structure motion-instances.

- `userID` — An unique identifier for an acceleration-structure motion-instance.

- `motionTransformsStartIndex` — An index of the motion data that represents the first key-frame’s motion data.

- `motionTransformsCount` — The number of motion data key-frames that begin at [motionTransformsStartIndex](motiontransformsstartindex.md).

- `motionStartBorderMode` — A behavior that configures how an acceleration-structure motion-instance handles timestamps before [motionStartTime](motionstarttime.md).

- `motionEndBorderMode` — A behavior that configures how an acceleration-structure motion-instance handles timestamps after [motionEndTime](motionendtime.md).

- `motionStartTime` — A starting time for the range of motion that the key-frame data (see [motionTransformsStartIndex](motiontransformsstartindex.md) and [motionTransformsCount](motiontransformscount.md)) represent.

- `motionEndTime` — An ending time for the range of motion that the key-frame data (see [motionTransformsStartIndex](motiontransformsstartindex.md) and [motionTransformsCount](motiontransformscount.md)) represent.

## Discussion

The initializer sets the descriptor instance’s properties to the values you pass to the initializer’s parameters. However, you can change the descriptor’s property values at any time, such as between creating separate acceleration-structure motion instances. For example, apps typically assign a unique value to [userID](userid.md) before they create each motion instance with the same descriptor.

## See Also

### Creating an instance descriptor

- [init()](<init().md>) — Creates an acceleration-structure motion instance with default property values.
