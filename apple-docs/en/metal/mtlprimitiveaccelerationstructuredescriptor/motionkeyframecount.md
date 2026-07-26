---
title: motionKeyframeCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionkeyframecount
source_url: 'https://developer.apple.com/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionkeyframecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionkeyframecount.json'
content_hash: 'sha256:450f56667082d51e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPrimitiveAccelerationStructureDescriptor](../mtlprimitiveaccelerationstructuredescriptor.md)

# motionKeyframeCount

<sub>Instance Property</sub>

The number of keyframes in the geometry data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionKeyframeCount: Int { get set }
```

## Discussion

The default value is `1`. If the value is greater than `1`, all geometry descriptors that you attach to this descriptor need to be motion descriptors, and each needs to have exactly that many [MTLMotionKeyframeData](../mtlmotionkeyframedata.md) objects.

## See Also

### Related Documentation

- [geometryDescriptors](geometrydescriptors.md) — An array that contains the individual pieces of geometry that compose the acceleration structure.

### Specifying motion behavior

- [motionStartTime](motionstarttime.md) — The start time for the range of motion that the keyframe data describes.
- [motionEndTime](motionendtime.md) — The end time for the range of motion that the keyframe data describes.
- [motionStartBorderMode](motionstartbordermode.md) — The mode to use when handling timestamps before the start time.
- [motionEndBorderMode](motionendbordermode.md) — The mode to use when handling timestamps after the end time.
- [MTLMotionBorderMode](../mtlmotionbordermode.md) — Options for specifying how the acceleration structure handles timestamps that are outside the specified range.
