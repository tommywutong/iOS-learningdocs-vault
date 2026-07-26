---
title: UIWindowScene.ActivationConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activationconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationconfiguration.json'
content_hash: 'sha256:d4bec8ace491f7e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# UIWindowScene.ActivationConfiguration

<sub>Class</sub>

An object that provides configuration options for a window scene request.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class ActivationConfiguration
```

## Overview

Use a [ActivationConfiguration](activationconfiguration.md) object to request a new window scene from the system. An activation configuration requires a [NSUserActivity](../../foundation/nsuseractivity.md) object that represents the scene’s content. You can specify a preferred presentation style for the new scene by including an optional [ActivationRequestOptions](activationrequestoptions.md) object. The system automatically animates the transition to the new scene, but you can customize the transition by providing an optional targeted preview.

To request scene activation from a view interaction, use an instance of this class with [ActivationInteraction](activationinteraction.md). To request scene activation from a context menu, use an instance of this class with [ActivationAction](activationaction.md).

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Creating an activation configuration

- [init(userActivity:options:preview:)](<activationconfiguration/init(useractivity_options_preview_).md>) — Creates an activation configuration.

### Getting information about the activation configuration

- [userActivity](activationconfiguration/useractivity.md) — The user activity used to request a scene.
- [options](activationconfiguration/options.md) — Options for customizing the scene request.
- [ActivationRequestOptions](activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [preview](activationconfiguration/preview.md) — An optional targeted preview that the system uses to animate the transition to the new scene.

## See Also

### Supporting types

- [ActivationAction](activationaction.md) — A menu element that requests a window scene.
- [ActivationInteraction](activationinteraction.md) — An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [ActivationRequestOptions](activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [UIWindowSceneDestructionRequestOptions](../uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [DismissalAnimation](dismissalanimation.md) — Constants that indicate the types of animations available for dismissing a scene’s windows.
- [UIWindowSceneDragInteraction](../uiwindowscenedraginteraction.md) — An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [ResizingRestrictions](resizingrestrictions.md)
- [UIWindowSceneResizingRestrictions](../uiwindowsceneresizingrestrictions.md)
- [PresentationStyle](presentationstyle.md) — The placement of a window scene relative to other scenes in the workspace. _(deprecated)_
