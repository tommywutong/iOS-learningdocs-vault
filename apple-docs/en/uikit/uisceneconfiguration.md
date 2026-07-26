---
title: UISceneConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uisceneconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneconfiguration.json'
content_hash: 'sha256:3e597c729718ef58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneConfiguration

<sub>Class</sub>

Information about the objects and storyboard for UKit to use when creating a particular scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISceneConfiguration
```

## Overview

Use a [UISceneConfiguration](uisceneconfiguration.md) object to specify information that UIKit can use to create a new scene for your app. Specifically, you must provide the class of the specific scene you want, the class of the scene delegate object your app uses to manage scenes of that type, and a storyboard containing the scene’s initial view controller.

When the user requests a new instance of your app’s user interface, UIKit looks in your app’s `Info.plist` file for the configuration data it needs to create the corresponding scene object. It then packages that information into a [UISceneConfiguration](uisceneconfiguration.md) object and delivers it as part of the session it passes to the [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>) method of your app delegate. You can accept that configuration data as is or create a return a new [UISceneConfiguration](uisceneconfiguration.md) object with a different set of configuration details.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a configuration object

- [- initWithName:sessionRole:](<uisceneconfiguration/init(name_sessionrole_).md>) — Creates a scene-configuration object with the specified role and app-specific name.
- [- initWithName:](<uisceneconfiguration/init(name_).md>) — Creates a scene-configuration object with the specified name. _(beta)_
- [- init](<uisceneconfiguration/init().md>) — Creates a scene-configuration object.

### Specifying the scene creation details

- [sceneClass](uisceneconfiguration/sceneclass.md) — The class of the scene object that you want UIKit to create.
- [delegateClass](uisceneconfiguration/delegateclass.md) — The class of the custom delegate object that you want UIKit to create.
- [storyboard](uisceneconfiguration/storyboard.md) — The storyboard object that contains your scene’s initial view controller.

### Getting the configuration attributes

- [name](uisceneconfiguration/name.md) — The app-specific name assigned to the scene configuration.
- [role](uisceneconfiguration/role.md) — The role assigned to the scene configuration.
- [Role](uiscenesession/role-swift.struct.md) — Constants that indicate the possible roles for a scene.

### Initializers

- [init(coder:)](<uisceneconfiguration/init(coder_).md>)

## See Also

### Configuration

- [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md) — Tell the system about your app’s scenes, including the objects you use to manage each scene and its initial user interface.
- [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) — The information about the app’s scene-based life-cycle support.
- [UISceneSession](uiscenesession.md) — An object that contains information about one of your app’s scenes.
