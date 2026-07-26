---
title: ImmersiveEnvironmentBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersiveenvironmentbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/immersiveenvironmentbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersiveenvironmentbehavior.json'
content_hash: 'sha256:2e4ac06f50bf577e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ImmersiveEnvironmentBehavior

<sub>Structure</sub>

The behavior of the system-provided immersive environments when a scene is opened by your app.

<sub>visionOS</sub>

```swift
struct ImmersiveEnvironmentBehavior
```

## Overview

Use one of these values with the [immersiveEnvironmentBehavior(_:)](<scene/immersiveenvironmentbehavior(__).md>) scene modifier to indicate how the immersive environment should behave when your app opens a scene.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](immersiveenvironmentbehavior/automatic.md) — A behavior that matches the system default behavior.
- [coexist](immersiveenvironmentbehavior/coexist.md) — A behavior that keeps the system’s immersive environment as is when opening a scene.
- [replace](immersiveenvironmentbehavior/replace.md) — A behavior that replaces any currently opened immersive environment with the new scene.

## See Also

### Creating an immersive space

- [ImmersiveSpace](immersivespace.md) — A scene that presents its content in an unbounded space.
- [ImmersiveSpaceContentBuilder](immersivespacecontentbuilder.md) — A result builder for composing a collection of immersive space elements.
- [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>) — Sets the style for an immersive space.
- [ImmersionStyle](immersionstyle.md) — The styles that an immersive space can have.
- [immersiveSpaceDisplacement](environmentvalues/immersivespacedisplacement.md) — The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [ProgressiveImmersionAspectRatio](progressiveimmersionaspectratio.md)
