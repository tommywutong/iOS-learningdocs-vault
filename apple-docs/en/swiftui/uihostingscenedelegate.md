---
title: UIHostingSceneDelegate
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 27.0+ beta, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingscenedelegate
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingscenedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingscenedelegate.json'
content_hash: 'sha256:15074be91c64257d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIHostingSceneDelegate

<sub>Protocol</sub>

Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIHostingSceneDelegate : UISceneDelegate
```

## Overview

Declare any SwiftUI scenes you wish to activate from UIKit in the static `rootScene` property of your conforming class:

```swift
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "swiftui-window") {
            ContentView()
        }
    }

    // Add UISceneDelegate lifecycle callbacks here
}
```

Use a class conforming to [UIHostingSceneDelegate](uihostingscenedelegate.md) to  activate a scene by its ID or presented value with `UISceneSessionActivationRequest`:

```swift
if let requestWithID = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    id: "swiftui-window"
) {
    UIApplication.shared.activateSceneSession(for: requestWithID)
}

if let requestWithData = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    value: FavoriteNumber(13)
) {
    UIApplication.shared.activateSceneSession(for: requestWithData)
}
```

When a SwiftUI scene declared in your `rootScene` property is activated, an instance of your conforming class will be created by SwiftUI and receive window scene lifecycle callbacks.

Your `UIHostingSceneDelegate` class can be used with a `UISceneConfiguration` in your app delegate’s `application(_:configurationForConnecting:options:)`method to activate a SwiftUI scene in response to an external event:

```swift
class AppDelegate: UIApplicationDelegate {

    func application(
        _ app: UIApplication,
        configurationForConnecting sceneSession: UISceneSession,
        options: UIScene.ConnectionOptions
    ) -> UISceneConfiguration {
        let config = UISceneConfiguration(
            name: nil, sessionRole: sceneSession.role)
        config.delegateClass = HostingSceneDelegate.self
        return config
    }

}
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UISceneDelegate](../uikit/uiscenedelegate.md)

## Topics

### Associated Types

- [RootScene](uihostingscenedelegate/rootscene-swift.associatedtype.md)

### Type Properties

- [rootScene](uihostingscenedelegate/rootscene-swift.type.property.md)

## See Also

### Displaying SwiftUI views in UIKit

- [Using SwiftUI with UIKit](../uikit/using-swiftui-with-uikit.md) — Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [UIHostingController](uihostingcontroller.md) — A UIKit view controller that manages a SwiftUI view hierarchy.
- [UIHostingControllerSizingOptions](uihostingcontrollersizingoptions.md) — Options for how a hosting controller tracks its content’s size.
- [UIHostingConfiguration](uihostingconfiguration.md) — A content configuration suitable for hosting a hierarchy of SwiftUI views.
