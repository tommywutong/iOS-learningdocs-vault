---
title: UIWindowSceneDragInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscenedraginteraction
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenedraginteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenedraginteraction.json'
content_hash: 'sha256:1e05b5bb5b972257'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWindowSceneDragInteraction

<sub>Class</sub>

An interaction you add to a view that enables pan gestures to change the containing window scene’s position.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIWindowSceneDragInteraction
```

## Overview

Create and add this interaction to a view that you want to drag to adjust the position of your app’s window. [UINavigationBar](uinavigationbar.md) handles this automatically, so you only need to add this interaction to views in other parts of your window that you want to be draggable.

**Swift**

```swift
var windowDragInteraction = UIWindowSceneDragInteraction()
draggableView.addInteraction(windowDragInteraction)
```

**Objective-C**

```objc
UIWindowSceneDragInteraction *windowDragInteraction = [[UIWindowSceneDragInteraction alloc] init];
[self.draggableView addInteraction:windowDragInteraction];
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Preventing gesture conflicts

- [gestureForFailureRelationships](uiwindowscenedraginteraction/gestureforfailurerelationships.md) — The gesture that the drag interaction adds to the view hierarchy.

## See Also

### Supporting types

- [ActivationAction](uiwindowscene/activationaction.md) — A menu element that requests a window scene.
- [ActivationConfiguration](uiwindowscene/activationconfiguration.md) — An object that provides configuration options for a window scene request.
- [ActivationInteraction](uiwindowscene/activationinteraction.md) — An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [ActivationRequestOptions](uiwindowscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [DismissalAnimation](uiwindowscene/dismissalanimation.md) — Constants that indicate the types of animations available for dismissing a scene’s windows.
- [ResizingRestrictions](uiwindowscene/resizingrestrictions.md)
- [UIWindowSceneResizingRestrictions](uiwindowsceneresizingrestrictions.md)
- [PresentationStyle](uiwindowscene/presentationstyle.md) — The placement of a window scene relative to other scenes in the workspace. _(deprecated)_
