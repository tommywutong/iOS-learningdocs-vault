---
title: 'application(_:didDiscardSceneSessions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:diddiscardscenesessions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:diddiscardscenesessions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Adiddiscardscenesessions%3A%29.json'
content_hash: 'sha256:917f8dd7b17d66b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:didDiscardSceneSessions:)

<sub>Instance Method</sub>

Tells the delegate that the user closed one or more of the app’s scenes from the app switcher.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>)
```

## Parameters

- `application` — The singleton app object.

- `sceneSessions` — The session objects associated with the discarded scenes.

## Discussion

When the user removes a scene from the app switcher, UIKit calls this method before discarding the scene’s associated session object altogether. (UIKit also calls this method to discard scenes that it can no longer display.) If your app isn’t running, UIKit calls this method the next time your app launches.

Use this method to update your app’s data structures and to release any resources associated with the scene. For example, you might use this method to update your app’s interface to incorporate the content associated with the scenes.

UIKit calls this method only when dismissing scenes permanently. It doesn’t call it when the system disconnects a scene to free up memory. Memory reclamation deletes the scene objects, but preserves the sessions associated with those scenes.

## See Also

### Configuring and discarding scenes

- [- application:configurationForConnectingSceneSession:options:](<application(__configurationforconnecting_options_).md>) — Retrieves the configuration data for UIKit to use when creating a new scene.
