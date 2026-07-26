---
title: UISceneSession
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesession
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesession.json'
content_hash: 'sha256:6bae842cb53f5dc7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneSession

<sub>Class</sub>

An object that contains information about one of your app’s scenes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISceneSession
```

## Overview

A [UISceneSession](uiscenesession.md) object manages a unique runtime instance of your scene. When the user adds a new scene to your app, or when you request one programmatically, the system creates a session object to track that scene. The session contains a unique identifier and the configuration details of the scene. UIKit maintains the session information for the lifetime of the scene itself, destroying the session in response to the user closing the scene in the app switcher.

You don’t create session objects directly. UIKit creates sessions in response to user interactions with your app. You can also ask UIKit to create a new scene and session programmatically by calling the [- requestSceneSessionActivation:userActivity:options:errorHandler:](<uiapplication/requestscenesessionactivation(__useractivity_options_errorhandler_).md>) method of [UIApplication](uiapplication.md). UIKit initializes the session with default configuration data based on the contents of your app’s `Info.plist` file.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the scene information

- [scene](uiscenesession/scene.md) — The scene associated with the current session.
- [role](uiscenesession/role-swift.property.md) — The role played by the scene’s content.
- [Role](uiscenesession/role-swift.struct.md) — Constants that indicate the possible roles for a scene.

### Getting the scene configuration details

- [configuration](uiscenesession/configuration.md) — The configuration data for creating the scene.
- [UISceneConfiguration](uisceneconfiguration.md) — Information about the objects and storyboard for UKit to use when creating a particular scene.

### Identifying the scene

- [persistentIdentifier](uiscenesession/persistentidentifier.md) — A unique identifier that persists for the lifetime of the session.

### Getting additional session information

- [stateRestorationActivity](uiscenesession/staterestorationactivity.md) — An activity object you can use to restore the previous contents of your scene’s interface.
- [userInfo](uiscenesession/userinfo.md) — Custom attributes that you can associate with the scene.

### Initializers

- [init(coder:)](<uiscenesession/init(coder_).md>)

## See Also

### Configuration

- [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md) — Tell the system about your app’s scenes, including the objects you use to manage each scene and its initial user interface.
- [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) — The information about the app’s scene-based life-cycle support.
- [UISceneConfiguration](uisceneconfiguration.md) — Information about the objects and storyboard for UKit to use when creating a particular scene.
