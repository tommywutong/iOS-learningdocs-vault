---
title: UIWindowScene.PresentationStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwindowscene/presentationstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/presentationstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/presentationstyle.json'
content_hash: 'sha256:0786358b790e2224'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# UIWindowScene.PresentationStyle

<sub>Enumeration</sub>

The placement of a window scene relative to other scenes in the workspace.

> [!warning] Deprecated
> Use [placement](activationrequestoptions/placement.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum PresentationStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIWindowScenePresentationStyleAutomatic](presentationstyle/automatic.md) — The system determines the most appropriate style. _(deprecated)_
- [UIWindowScenePresentationStyleProminent](presentationstyle/prominent.md) — Presents prominently above others in the current space. _(deprecated)_
- [UIWindowScenePresentationStyleStandard](presentationstyle/standard.md) — The default style of the system. _(deprecated)_

### Initializers

- [init(rawValue:)](<presentationstyle/init(rawvalue_).md>) _(deprecated)_

## See Also

### Supporting types

- [ActivationAction](activationaction.md) — A menu element that requests a window scene.
- [ActivationConfiguration](activationconfiguration.md) — An object that provides configuration options for a window scene request.
- [ActivationInteraction](activationinteraction.md) — An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [ActivationRequestOptions](activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [UIWindowSceneDestructionRequestOptions](../uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [DismissalAnimation](dismissalanimation.md) — Constants that indicate the types of animations available for dismissing a scene’s windows.
- [UIWindowSceneDragInteraction](../uiwindowscenedraginteraction.md) — An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [ResizingRestrictions](resizingrestrictions.md)
- [UIWindowSceneResizingRestrictions](../uiwindowsceneresizingrestrictions.md)
