---
title: UIWindowScene.ActivationInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activationinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationinteraction.json'
content_hash: 'sha256:ae4cfa0f64d44664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# UIWindowScene.ActivationInteraction

<sub>Class</sub>

An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class ActivationInteraction
```

## Overview

Create a [ActivationInteraction](activationinteraction.md) object when you want to facilitate requesting scene activation when the user pinches open on a view. You initialize the interaction with a closure that the system executes when the user triggers the interaction. The closure should return a [ActivationConfiguration](activationconfiguration.md) object. You also provide an error-handler closure that the system executes if the scene activation request fails.

To request scene activation from an interaction with a [UICollectionView](../uicollectionview.md) cell, use the [- collectionView:sceneActivationConfigurationForItemAtIndexPath:point:](<../uicollectionviewdelegate/collectionview(__sceneactivationconfigurationforitemat_point_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md), [UIInteraction](../uiinteraction.md)

## Topics

### Creating an activation interaction

- [- initWithConfigurationProvider:errorHandler:](<activationinteraction/init(__errorhandler_).md>) — Creates an activation interaction.
- [ConfigurationProvider](activationinteraction/configurationprovider.md) — A type alias defining a closure that provides an activation configuration for the activation interaction.

### Initializers

- [init(configurationProvider:errorHandler:)](<activationinteraction/init(configurationprovider_errorhandler_).md>)

## See Also

### Supporting types

- [ActivationAction](activationaction.md) — A menu element that requests a window scene.
- [ActivationConfiguration](activationconfiguration.md) — An object that provides configuration options for a window scene request.
- [ActivationRequestOptions](activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [UIWindowSceneDestructionRequestOptions](../uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [DismissalAnimation](dismissalanimation.md) — Constants that indicate the types of animations available for dismissing a scene’s windows.
- [UIWindowSceneDragInteraction](../uiwindowscenedraginteraction.md) — An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [ResizingRestrictions](resizingrestrictions.md)
- [UIWindowSceneResizingRestrictions](../uiwindowsceneresizingrestrictions.md)
- [PresentationStyle](presentationstyle.md) — The placement of a window scene relative to other scenes in the workspace. _(deprecated)_
