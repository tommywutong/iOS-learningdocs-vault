---
title: UISceneDestructionRequestOptions
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenedestructionrequestoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedestructionrequestoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedestructionrequestoptions.json'
content_hash: 'sha256:3ba27515afcd795f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneDestructionRequestOptions

<sub>Class</sub>

An object you pass to UIKit to permanently remove a scene and its associated session from your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISceneDestructionRequestOptions
```

## Overview

Create a [UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md) object before calling the [- requestSceneSessionDestruction:options:errorHandler:](<uiapplication/requestscenesessiondestruction(__options_errorhandler_).md>) method of [UIApplication](uiapplication.md). When destroying a [UIWindowScene](uiwindowscene.md), create a [UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md) object instead and use it to configure the dismissal animations.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## See Also

### Managing a scene’s life cycle

- [activateSceneSession(for:errorHandler:)](<uiapplication/activatescenesession(for_errorhandler_).md>) — Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [- requestSceneSessionDestruction:options:errorHandler:](<uiapplication/requestscenesessiondestruction(__options_errorhandler_).md>) — Asks the system to dismiss an existing scene and remove it from the app switcher.
- [- requestSceneSessionRefresh:](<uiapplication/requestscenesessionrefresh(__).md>) — Asks the system to update any system UI associated with the specified scene.
- [UISceneSessionActivationRequest](uiscenesessionactivationrequest-swift.struct.md) — A collection of properties that you use to request activation of a scene.
- [ActivationRequestOptions](uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
