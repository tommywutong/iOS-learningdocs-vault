---
title: SceneView
framework: SceneKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+（26.0 起废弃）, iPadOS 14.0+（26.0 起废弃）, Mac Catalyst 14.0+（26.0 起废弃）, macOS 11.0+（26.0 起废弃）, tvOS 14.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 7.0+（26.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/scenekit/sceneview
source_url: 'https://developer.apple.com/documentation/scenekit/sceneview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/scenekit/sceneview.json'
content_hash: 'sha256:faf8b10bd14c98c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SceneKit](../scenekit.md)

# SceneView

<sub>Structure</sub>

A SwiftUI view for displaying 3D SceneKit content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct SceneView
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a Scene View

- [init(scene:pointOfView:options:preferredFramesPerSecond:antialiasingMode:delegate:technique:)](<sceneview/init(scene_pointofview_options_preferredframespersecond_antialiasingmode_delegate_technique_).md>)
- [Options](sceneview/options.md)

## See Also

### Essentials

- [SCNScene](scnscene.md) — A container for the node hierarchy and global properties that together form a displayable 3D scene.
- [SCNView](scnview.md) — A view for displaying 3D SceneKit content.
