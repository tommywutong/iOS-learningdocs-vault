---
title: ScenePadding
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenepadding
source_url: 'https://developer.apple.com/documentation/swiftui/scenepadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenepadding.json'
content_hash: 'sha256:9bc4a5559d6aa1db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScenePadding

<sub>Structure</sub>

The padding used to space a view from its containing scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScenePadding
```

## Overview

Add scene padding to a view using the [scenePadding(_:edges:)](<view/scenepadding(__edges_).md>) modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting padding values

- [minimum](scenepadding/minimum.md) — The minimum scene padding value.
- [navigationBar](scenepadding/navigationbar.md) — The navigation bar content scene padding.

## See Also

### Adding padding around a view

- [padding(_:)](<view/padding(__).md>) — Adds a different padding amount to each edge of this view.
- [padding(_:_:)](<view/padding(____).md>) — Adds an equal padding amount to specific edges of this view.
- [padding3D(_:)](<view/padding3d(__).md>) — Pads this view using the edge insets you specify.
- [padding3D(_:_:)](<view/padding3d(____).md>) — Pads this view using the edge insets you specify.
- [scenePadding(_:)](<view/scenepadding(__).md>) — Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [scenePadding(_:edges:)](<view/scenepadding(__edges_).md>) — Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
