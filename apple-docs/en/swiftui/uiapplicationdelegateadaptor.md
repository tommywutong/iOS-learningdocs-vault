---
title: UIApplicationDelegateAdaptor
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uiapplicationdelegateadaptor
source_url: 'https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiapplicationdelegateadaptor.json'
content_hash: 'sha256:c79a9c9e6d86dd6b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIApplicationDelegateAdaptor

<sub>Structure</sub>

A property wrapper type that you use to create a UIKit app delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency @propertyWrapper struct UIApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : UIApplicationDelegate
```

## Overview

To handle app delegate callbacks in an app that uses the SwiftUI life cycle, define a type that conforms to the [UIApplicationDelegate](../uikit/uiapplicationdelegate.md) protocol, and implement the delegate methods that you need. For example, you can implement the [application(_:didRegisterForRemoteNotificationsWithDeviceToken:)](<../uikit/uiapplicationdelegate/application(__didregisterforremotenotificationswithdevicetoken_).md>) method to handle remote notification registration:

```swift
class MyAppDelegate: NSObject, UIApplicationDelegate, ObservableObject {
    func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        // Record the device token.
    }
}
```

Then use the `UIApplicationDelegateAdaptor` property wrapper inside your [App](app.md) declaration to tell SwiftUI about the delegate type:

```swift
@main
struct MyApp: App {
    @UIApplicationDelegateAdaptor private var appDelegate: MyAppDelegate

    var body: some Scene { ... }
}
```

SwiftUI instantiates the delegate and calls the delegate’s methods in response to life cycle events. Define the delegate adaptor only in your [App](app.md) declaration, and only once for a given app. If you declare it more than once, SwiftUI generates a runtime error.

If your app delegate conforms to the [ObservableObject](../combine/observableobject.md) protocol, as in the example above, then SwiftUI puts the delegate it creates into the [Environment](environment.md). You can access the delegate from any scene or view in your app using the [EnvironmentObject](environmentobject.md) property wrapper:

```swift
@EnvironmentObject private var appDelegate: MyAppDelegate
```

This enables you to use the dollar sign (`$`) prefix to get a binding to published properties that you declare in the delegate. For more information, see [projectedValue](uiapplicationdelegateadaptor/projectedvalue.md).

> [!important] Important
> Manage an app’s life cycle events without using an app delegate whenever possible. For example, prefer to handle changes in [ScenePhase](scenephase.md) instead of relying on delegate callbacks, like [application(_:didFinishLaunchingWithOptions:)](<../uikit/uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>).

### Scene delegates

Some iOS apps define a [UIWindowSceneDelegate](../uikit/uiwindowscenedelegate.md) to handle scene-based events, like app shortcuts:

```swift
class MySceneDelegate: NSObject, UIWindowSceneDelegate, ObservableObject {
    func windowScene(
        _ windowScene: UIWindowScene,
        performActionFor shortcutItem: UIApplicationShortcutItem
    ) async -> Bool {
        // Do something with the shortcut...

        return true
    }
}
```

You can provide this kind of delegate to a SwiftUI app by returning the scene delegate’s type from the [application(_:configurationForConnecting:options:)](<../uikit/uiapplicationdelegate/application(__configurationforconnecting_options_).md>) method inside your app delegate:

```swift
extension MyAppDelegate {
    func application(
        _ application: UIApplication,
        configurationForConnecting connectingSceneSession: UISceneSession,
        options: UIScene.ConnectionOptions
    ) -> UISceneConfiguration {

        let configuration = UISceneConfiguration(
                                name: nil,
                                sessionRole: connectingSceneSession.role)
        if connectingSceneSession.role == .windowApplication {
            configuration.delegateClass = MySceneDelegate.self
        }
        return configuration
    }
}
```

When you configure the [UISceneConfiguration](../uikit/uisceneconfiguration.md) instance, you only need to indicate the delegate class, and not a scene class or storyboard. SwiftUI creates and manages the delegate instance, and sends it any relevant delegate callbacks.

As with the app delegate, if you make your scene delegate an observable object, SwiftUI automatically puts it in the [Environment](environment.md), from where you can access it with the [EnvironmentObject](environmentobject.md) property wrapper, and create bindings to its published properties.

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a delegate adaptor

- [init(_:)](<uiapplicationdelegateadaptor/init(__).md>) — Creates a UIKit app delegate adaptor using an observable delegate.

### Getting the delegate adaptor

- [projectedValue](uiapplicationdelegateadaptor/projectedvalue.md) — A projection of the observed object that provides bindings to its properties.
- [wrappedValue](uiapplicationdelegateadaptor/wrappedvalue.md) — The underlying app delegate.

## See Also

### Targeting iOS and iPadOS

- [UILaunchScreen](../bundleresources/information-property-list/uilaunchscreen.md) — The user interface to show while an app launches.
- [UILaunchScreens](../bundleresources/information-property-list/uilaunchscreens.md) — The user interfaces to show while an app launches in response to different URL schemes.
