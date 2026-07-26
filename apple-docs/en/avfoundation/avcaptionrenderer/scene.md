---
title: AVCaptionRenderer.Scene
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionrenderer/scene
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/scene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer/scene.json'
content_hash: 'sha256:c40cf9c21ca416c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRenderer](../avcaptionrenderer.md)

# AVCaptionRenderer.Scene

<sub>Class</sub>

An object that holds a time range and an associated state which indicates when the renderer draws output.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class Scene
```

## Overview

To render a scene, the object considers state like the existence of captions and regions, their temporal overlaps, and whether captions use animation effects. Your app can request time ranges where visual differences exist and use these time ranges to optimize drawing performance, like drawing once per scene. Alternatively, it can ignore scenes, and instead call [- renderInContext:forTime:](<render(in_for_).md>) repeatedly, but this may have additional performance impact.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Inspecting the scene

- [timeRange](scene/timerange.md) — The time range during which the system doesn’t modify the scene.
- [hasActiveCaptions](scene/hasactivecaptions.md) — A Boolean value that indicates whether the scene contains one or more active captions.
- [needsPeriodicRefresh](scene/needsperiodicrefresh.md) — A Boolean value that indicates whether the scene requires redrawing while your app progresses through the content.

## See Also

### Determining scene changes

- [- captionSceneChangesInRange:](<captionscenechanges(in_).md>) — Determine render time ranges within an enclosing time range to account for visual changes among captions.
