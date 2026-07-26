---
title: MTLMotionBorderMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmotionbordermode
source_url: 'https://developer.apple.com/documentation/metal/mtlmotionbordermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmotionbordermode.json'
content_hash: 'sha256:99090a8544b05a4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLMotionBorderMode

<sub>Enumeration</sub>

Options for specifying how the acceleration structure handles timestamps that are outside the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLMotionBorderMode
```

## Overview

The [motionStartBorderMode](mtlprimitiveaccelerationstructuredescriptor/motionstartbordermode.md) and [motionEndBorderMode](mtlprimitiveaccelerationstructuredescriptor/motionendbordermode.md) properties use this type to describe the behavior for a motion-based object when a timestamp is outside the specified range.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying motion modes

- [MTLMotionBorderModeClamp](mtlmotionbordermode/clamp.md) — A mode that specifies treating times outside the specified endpoint as if they were at the endpoint.
- [MTLMotionBorderModeVanish](mtlmotionbordermode/vanish.md) — A mode that specifies that times outside the specified endpoint need to prevent any ray-intersections with the primitive.

### Initializers

- [init(rawValue:)](<mtlmotionbordermode/init(rawvalue_).md>)

## See Also

### Specifying motion behavior

- [motionKeyframeCount](mtlprimitiveaccelerationstructuredescriptor/motionkeyframecount.md) — The number of keyframes in the geometry data.
- [motionStartTime](mtlprimitiveaccelerationstructuredescriptor/motionstarttime.md) — The start time for the range of motion that the keyframe data describes.
- [motionEndTime](mtlprimitiveaccelerationstructuredescriptor/motionendtime.md) — The end time for the range of motion that the keyframe data describes.
- [motionStartBorderMode](mtlprimitiveaccelerationstructuredescriptor/motionstartbordermode.md) — The mode to use when handling timestamps before the start time.
- [motionEndBorderMode](mtlprimitiveaccelerationstructuredescriptor/motionendbordermode.md) — The mode to use when handling timestamps after the end time.
