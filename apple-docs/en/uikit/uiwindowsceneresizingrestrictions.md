---
title: UIWindowSceneResizingRestrictions
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowsceneresizingrestrictions
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowsceneresizingrestrictions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowsceneresizingrestrictions.json'
content_hash: 'sha256:bf21d976fca807b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWindowSceneResizingRestrictions

<sub>Enumeration</sub>

<sub>visionOS</sub>

```swift
enum UIWindowSceneResizingRestrictions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UIWindowSceneResizingRestrictionsFreeform](uiwindowsceneresizingrestrictions/freeform.md) — User resizes are only restricted by the system and other restrictions put in place
- [UIWindowSceneResizingRestrictionsNone](uiwindowsceneresizingrestrictions/none.md) — The user cannot resize the scene
- [UIWindowSceneResizingRestrictionsUniform](uiwindowsceneresizingrestrictions/uniform.md) — User resizes are restricted to the current aspect ratio
- [UIWindowSceneResizingRestrictionsUnspecified](uiwindowsceneresizingrestrictions/unspecified.md) — App has no preference on user resize

### Initializers

- [init(rawValue:)](<uiwindowsceneresizingrestrictions/init(rawvalue_).md>)

## See Also

### Supporting types

- [ActivationAction](uiwindowscene/activationaction.md) — A menu element that requests a window scene.
- [ActivationConfiguration](uiwindowscene/activationconfiguration.md) — An object that provides configuration options for a window scene request.
- [ActivationInteraction](uiwindowscene/activationinteraction.md) — An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [ActivationRequestOptions](uiwindowscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [DismissalAnimation](uiwindowscene/dismissalanimation.md) — Constants that indicate the types of animations available for dismissing a scene’s windows.
- [UIWindowSceneDragInteraction](uiwindowscenedraginteraction.md) — An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [ResizingRestrictions](uiwindowscene/resizingrestrictions.md)
- [PresentationStyle](uiwindowscene/presentationstyle.md) — The placement of a window scene relative to other scenes in the workspace. _(deprecated)_
