---
title: AVVideoCompositionCoreAnimationTool
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioncoreanimationtool
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioncoreanimationtool.json'
content_hash: 'sha256:2005c7e6e60d0a90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCompositionCoreAnimationTool

<sub>Class</sub>

An object used to incorporate Core Animation into a video composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVVideoCompositionCoreAnimationTool
```

## Overview

Any animations will be interpreted on the video’s timeline, not real-time, so you should:

1. Set animations’ [beginTime](../quartzcore/camediatiming/begintime.md) property to [AVCoreAnimationBeginTimeAtZero](avcoreanimationbegintimeatzero.md) rather than `0` (which CoreAnimation replaces with [CACurrentMediaTime()](<../quartzcore/cacurrentmediatime().md>));
2. Set [isRemovedOnCompletion](../quartzcore/caanimation/isremovedoncompletion.md) to [false](../swift/false.md) on animations so they are not automatically removed;
3. Avoid using layers that are associated with [UIView](../uikit/uiview.md) objects.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a composition tool

- [+ videoCompositionCoreAnimationToolWithAdditionalLayer:asTrackID:](<avvideocompositioncoreanimationtool/init(additionallayer_astrackid_).md>) — Adds a Core Animation layer to the video composition.
- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:inLayer:](<avvideocompositioncoreanimationtool/init(postprocessingasvideolayer_in_).md>) — Composes the composited video frame with a Core Animation layer. _(deprecated)_
- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:inLayer:](<avvideocompositioncoreanimationtool/init(postprocessingasvideolayers_in_).md>) — Composes the composited video frames with the Core Animation layer.
- [init(configuration:)](<avvideocompositioncoreanimationtool/init(configuration_).md>) — Compose the composited video frames with the Core Animation layer.
- [Configuration](avvideocompositioncoreanimationtool/configuration.md) — Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.

### Initializers

- [init(postProcessingAsVideoLayer:inLayer:)](<avvideocompositioncoreanimationtool/init(postprocessingasvideolayer_inlayer_).md>) _(deprecated)_
- [init(postProcessingAsVideoLayers:inLayer:)](<avvideocompositioncoreanimationtool/init(postprocessingasvideolayers_inlayer_).md>)
