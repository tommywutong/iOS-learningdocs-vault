---
title: 'application(_:configurationForConnecting:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:configurationforconnecting:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:configurationforconnecting:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Aconfigurationforconnecting%3Aoptions%3A%29.json'
content_hash: 'sha256:f3dd5fe524d8065f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:configurationForConnecting:options:)

<sub>Instance Method</sub>

Retrieves the configuration data for UIKit to use when creating a new scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration
```

## Parameters

- `application` — The singleton app object.

- `connectingSceneSession` — The session object associated with the scene. This object contains the initial configuration data loaded from the app’s `Info.plist` file, if any.

- `options` — System-specific options for configuring the scene.

## Return Value

The configuration object containing the information needed to create the scene.

## Discussion

Implement this method if you don’t include scene-configuration data in your app’s `Info.plist` file, or if you want to alter the scene configuration data dynamically. UIKit calls this method shortly before creating a new scene. In your implementation, return a [UISceneConfiguration](../uisceneconfiguration.md) object with the scene details, including the type of scene to create, the delegate object you use to manage the scene, and the storyboard containing the initial view controller to display.

If you don’t implement this method, you must provide scene-configuration data in your app’s `Info.plist` file.

## See Also

### Configuring and discarding scenes

- [- application:didDiscardSceneSessions:](<application(__diddiscardscenesessions_).md>) — Tells the delegate that the user closed one or more of the app’s scenes from the app switcher.
