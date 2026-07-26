---
title: UIWindowSceneDestructionRequestOptions
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscenedestructionrequestoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenedestructionrequestoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenedestructionrequestoptions.json'
content_hash: 'sha256:bed57c96975ccddc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWindowSceneDestructionRequestOptions

<sub>Class</sub>

An object that contains information to use when removing a window scene from your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIWindowSceneDestructionRequestOptions
```

## Overview

Create a [UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md) object before you close one of your app’s scenes using the [- requestSceneSessionDestruction:options:errorHandler:](<uiapplication/requestscenesessiondestruction(__options_errorhandler_).md>) method of [UIApplication](uiapplication.md). Use this object to specify the dismissal animations to apply to the scene’s UI, if that UI is onscreen.

## Relationships

- **Inherits From**: [UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the dismissal animation

- [windowDismissalAnimation](uiwindowscenedestructionrequestoptions/windowdismissalanimation.md) — The animations to use when dismissing the scene’s windows.
- [DismissalAnimation](uiwindowscene/dismissalanimation.md) — Constants that indicate the types of animations available for dismissing a scene’s windows.

## See Also

### Activation and destruction

- [UISceneActivationConditions](uisceneactivationconditions.md) — The set of conditions that define when UIKit activates the current scene.
- [ActivationRequestOptions](uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
- [UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.
- [UISceneClosureConfirmation](uisceneclosureconfirmation.md) — A configuration specifying a confirmation dialog that will be shown before a user action will result in destruction of the scene session and the disconnection of the scene. _(beta)_
