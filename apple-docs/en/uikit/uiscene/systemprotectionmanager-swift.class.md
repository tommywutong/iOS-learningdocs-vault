---
title: UIScene.SystemProtectionManager
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/systemprotectionmanager-swift.class
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/systemprotectionmanager-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/systemprotectionmanager-swift.class.json'
content_hash: 'sha256:e9a9cd49d023ba15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# UIScene.SystemProtectionManager

<sub>Class</sub>

A class that represents the status of system protection for the scene.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class SystemProtectionManager
```

## Overview

Use this class to determine if the system protects a scene, such as by locking the app and requiring authentication with Face ID or Touch ID. You may want to disable your own app’s privacy shielding if the system already requires authentication.

The following example shows how a scene can use the manager’s [userAuthenticationEnabled](systemprotectionmanager-swift.class/isuserauthenticationenabled.md) property to decide whether to provide its own UI shielding. When the scene becomes active, the app shows an authentication challenge if the system doesn’t already provide protection. When the scene resigns the active role, the app provides its own shielding only if the system isn’t already doing so.

**Swift**

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
    guard scene.systemProtectionManager?.isUserAuthenticationEnabled ?? false else {
        // Show custom authentication.
    }
}

func sceneWillResignActive(_ scene: UIScene) {
    guard scene.systemProtectionManager?.isUserAuthenticationEnabled ?? false else {
        // Show custom shield to hide sensitive information.
    }
}

```

**Objective-C**

```objc
- (void)sceneDidBecomeActive:(UIScene *)scene {
    if ( scene.systemProtectionManager.userAuthenticationEnabled ) {
        // Don't show custom authentication.
    } else {
        // Show custom shield to hide sensitive information.
    }
}

- (void)sceneWillResignActive:(UIScene *)scene {
    if ( scene.systemProtectionManager.userAuthenticationEnabled ) {
        // Don't show custom shield; system already does so.
    } else {
        // Show custom shield to hide sensitive information.
    }
}
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Inspecting protection state

- [userAuthenticationEnabled](systemprotectionmanager-swift.class/isuserauthenticationenabled.md) — The current status of system user authentication.

## See Also

### Working with system protection manager

- [systemProtectionManager](systemprotectionmanager-swift.property.md) — The system protection manager associated with this scene.
- [UISceneSystemProtectionDidChangeNotification](systemprotectiondidchangenotification.md) — A notification posted when the system-protection attributes of a scene change.
