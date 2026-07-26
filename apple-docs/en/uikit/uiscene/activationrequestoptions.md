---
title: UIScene.ActivationRequestOptions
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/activationrequestoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/activationrequestoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/activationrequestoptions.json'
content_hash: 'sha256:12a35e6e00fefab4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# UIScene.ActivationRequestOptions

<sub>Class</sub>

An object that contains information you want the system to use when activating the session associated with a scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class ActivationRequestOptions
```

## Overview

Create a [ActivationRequestOptions](activationrequestoptions.md) object before you activate or create a scene using the [activateSceneSession(for:errorHandler:)](<../uiapplication/activatescenesession(for_errorhandler_).md>) (Swift) or [activateSceneSessionForRequest:errorHandler:](../uiapplication/activatescenesessionforrequest_errorhandler_.md) (Objective-C) method of [UIApplication](../uiapplication.md). Use this object to specify which of your app’s existing scenes originated the request for the new scene.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Inherited By**: [ActivationRequestOptions](../uiwindowscene/activationrequestoptions.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Specifying the originator of the request

- [requestingScene](activationrequestoptions/requestingscene.md) — The scene object that requested the activation of a different scene.

### Specifying collection join behavior

- [collectionJoinBehavior](activationrequestoptions/collectionjoinbehavior.md) — The behavior that specifies how a new scene joins a scene collection.
- [UISceneCollectionJoinBehavior](../uiscenecollectionjoinbehavior.md) — A set of behaviors that specify how a new scene joins a scene collection.

## See Also

### Managing a scene’s life cycle

- [activateSceneSession(for:errorHandler:)](<../uiapplication/activatescenesession(for_errorhandler_).md>) — Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [- requestSceneSessionDestruction:options:errorHandler:](<../uiapplication/requestscenesessiondestruction(__options_errorhandler_).md>) — Asks the system to dismiss an existing scene and remove it from the app switcher.
- [- requestSceneSessionRefresh:](<../uiapplication/requestscenesessionrefresh(__).md>) — Asks the system to update any system UI associated with the specified scene.
- [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md) — A collection of properties that you use to request activation of a scene.
- [UISceneDestructionRequestOptions](../uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.
