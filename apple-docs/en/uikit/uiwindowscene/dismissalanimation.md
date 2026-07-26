---
title: UIWindowScene.DismissalAnimation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/dismissalanimation
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/dismissalanimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/dismissalanimation.json'
content_hash: 'sha256:4b391b293128e0e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# UIWindowScene.DismissalAnimation

<sub>Enumeration</sub>

Constants that indicate the types of animations available for dismissing a scene’s windows.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum DismissalAnimation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Animation styles

- [UIWindowSceneDismissalAnimationStandard](dismissalanimation/standard.md) — The standard dismissal animations.
- [UIWindowSceneDismissalAnimationCommit](dismissalanimation/commit.md) — Animations to use when saving changes.
- [UIWindowSceneDismissalAnimationDecline](dismissalanimation/decline.md) — Animations to use when declining changes.

### Initializers

- [init(rawValue:)](<dismissalanimation/init(rawvalue_).md>)

## See Also

### Supporting types

- [ActivationAction](activationaction.md) — A menu element that requests a window scene.
- [ActivationConfiguration](activationconfiguration.md) — An object that provides configuration options for a window scene request.
- [ActivationInteraction](activationinteraction.md) — An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [ActivationRequestOptions](activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [UIWindowSceneDestructionRequestOptions](../uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [UIWindowSceneDragInteraction](../uiwindowscenedraginteraction.md) — An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [ResizingRestrictions](resizingrestrictions.md)
- [UIWindowSceneResizingRestrictions](../uiwindowsceneresizingrestrictions.md)
- [PresentationStyle](presentationstyle.md) — The placement of a window scene relative to other scenes in the workspace. _(deprecated)_
