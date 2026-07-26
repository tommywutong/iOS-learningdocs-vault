---
title: UIWindowScene.ActivationAction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activationaction
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationaction.json'
content_hash: 'sha256:cc3ba1d789e4a738'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# UIWindowScene.ActivationAction

<sub>Class</sub>

A menu element that requests a window scene.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class ActivationAction
```

## Overview

Create a [ActivationAction](activationaction.md) object to facilitate activating a new window scene from a menu item. You initialize the action with a closure that the system executes when a user selects the item. The closure should return a [ActivationConfiguration](activationconfiguration.md) object. You can specify an alternate action to display on iPhone and apps that don’t support multiple windows.

## Relationships

- **Inherits From**: [UIAction](../uiaction.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCoding](../../foundation/nscoding.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [NSSecureCoding](../../foundation/nssecurecoding.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [UIAccessibilityIdentification](../uiaccessibilityidentification.md), [UIMenuLeaf](../uimenuleaf.md)

## Topics

### Creating an activation action

- [init(title:subtitle:image:identifier:discoverabilityTitle:attributes:alternate:_:)](<activationaction/init(title_subtitle_image_identifier_discoverabilitytitle_attributes_alternate___).md>) — Creates an activation action using the specified parameters.
- [ConfigurationProvider](activationaction/configurationprovider.md) — A type alias defining a closure that provides an activation configuration for the activation action.

### Getting information about the activation action

- [title](activationaction/title.md) — The action’s title.

## See Also

### Supporting types

- [ActivationConfiguration](activationconfiguration.md) — An object that provides configuration options for a window scene request.
- [ActivationInteraction](activationinteraction.md) — An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [ActivationRequestOptions](activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [UIWindowSceneDestructionRequestOptions](../uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [DismissalAnimation](dismissalanimation.md) — Constants that indicate the types of animations available for dismissing a scene’s windows.
- [UIWindowSceneDragInteraction](../uiwindowscenedraginteraction.md) — An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [ResizingRestrictions](resizingrestrictions.md)
- [UIWindowSceneResizingRestrictions](../uiwindowsceneresizingrestrictions.md)
- [PresentationStyle](presentationstyle.md) — The placement of a window scene relative to other scenes in the workspace. _(deprecated)_
