---
title: UIWindowScene.ActivationRequestOptions
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activationrequestoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationrequestoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationrequestoptions.json'
content_hash: 'sha256:6f3557bb91963125'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# UIWindowScene.ActivationRequestOptions

<sub>Class</sub>

An object that contains information you want the system to use when activating a new window scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class ActivationRequestOptions
```

## Overview

Create a [ActivationRequestOptions](activationrequestoptions.md) object before you activate a scene using the [activateSceneSession(for:errorHandler:)](<../uiapplication/activatescenesession(for_errorhandler_).md>) (Swift) or [activateSceneSessionForRequest:errorHandler:](../uiapplication/activatescenesessionforrequest_errorhandler_.md) (Objective-C) method of [UIApplication](../uiapplication.md). Use this object to specify the preferred presentation style of the new scene.

## Relationships

- **Inherits From**: [ActivationRequestOptions](../uiscene/activationrequestoptions.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Positioning windows

- [placement](activationrequestoptions/placement.md) — The placement you prefer when the system activates the window scene.
- [UIWindowScenePlacement](../uiwindowsceneplacement-swift.protocol.md) — The placement of a window scene in the workspace.
- [UIWindowSceneProminentPlacement](../uiwindowsceneprominentplacement-swift.struct.md) — A placement that indicates the system should present the window more prominently than others in the space.
- [UIWindowSceneStandardPlacement](../uiwindowscenestandardplacement-swift.struct.md) — A placement that indicates the system should present the window using the default style of the system in the space.
- [UIWindowScenePushPlacement](../uiwindowscenepushplacement-swift.struct.md) — A placement that indicates the system needs to present the window by pushing it onto another window.

### Deprecated

- [preferredPresentationStyle](activationrequestoptions/preferredpresentationstyle.md) — The presentation style of the window scene. _(deprecated)_
- [UIWindowSceneReplacePlacement](../uiwindowscenereplaceplacement-swift.struct.md) _(deprecated)_

## See Also

### Supporting types

- [ActivationAction](activationaction.md) — A menu element that requests a window scene.
- [ActivationConfiguration](activationconfiguration.md) — An object that provides configuration options for a window scene request.
- [ActivationInteraction](activationinteraction.md) — An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [UIWindowSceneDestructionRequestOptions](../uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [DismissalAnimation](dismissalanimation.md) — Constants that indicate the types of animations available for dismissing a scene’s windows.
- [UIWindowSceneDragInteraction](../uiwindowscenedraginteraction.md) — An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [ResizingRestrictions](resizingrestrictions.md)
- [UIWindowSceneResizingRestrictions](../uiwindowsceneresizingrestrictions.md)
- [PresentationStyle](presentationstyle.md) — The placement of a window scene relative to other scenes in the workspace. _(deprecated)_
