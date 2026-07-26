---
title: 'application(_:willFinishLaunchingWithOptions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Awillfinishlaunchingwithoptions%3A%29.json'
content_hash: 'sha256:1a12c884d8be071c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:willFinishLaunchingWithOptions:)

<sub>Instance Method</sub>

Tells the delegate that the launch process has begun.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, willFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool
```

## Parameters

- `application` — The singleton app object.

- `launchOptions` — A dictionary indicating the reason the person or system launched the app. The contents of this dictionary may be empty in situations where a person launched the app directly. If the app supports scenes, this is `nil`. For information about the possible keys in this dictionary and how to handle them, see [LaunchOptionsKey](../uiapplication/launchoptionskey.md).

## Return Value

Return [false](../../swift/false.md) if the app can’t handle the URL resource or continue a user activity, or if the app doesn’t need to perform the [- application:performActionForShortcutItem:completionHandler:](<application(__performactionfor_completionhandler_).md>) method because you’re handling the invocation of a Home Screen quick action in this method; otherwise return [true](../../swift/true.md). The system ignores the return value if the app launches as a result of a remote notification.

## Discussion

Use this method (and the corresponding [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) method) to initialize your app and prepare it to run. In an app that doesn’t support scenes, the system calls this method after your app launches and loads its main storyboard or nib file, but before restoring your app’s state. When the system calls this method, your app is in the inactive state.

If the system launched your app for a specific reason, the `launchOptions` dictionary contains data indicating the reason for the launch. For some launch reasons, the system may call additional methods of your app delegate. For example, if your app launched to open a URL, the system calls the [- application:openURL:options:](<application(__open_options_).md>) method after your app finishes initializing itself. The presence of the launch keys gives you the opportunity to plan for that behavior. In the case of a URL to open, you might want to prevent state restoration if the URL represents a document that the person wanted to open.

When the system asks to open a URL, the system combines the return result from this method with the return result from the [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) method to determine whether to handle a URL. If either method returns [false](../../swift/false.md), the system doesn’t call the [- application:openURL:options:](<application(__open_options_).md>) method. If you don’t implement one of the methods, the system only considers the return value of the implemented method.

In some cases, a person launches your app with a Home Screen quick action. To ensure you handle this launch case correctly, read the discussion in the [- application:performActionForShortcutItem:completionHandler:](<application(__performactionfor_completionhandler_).md>) method.

> [!important] Important
> If your app relies on the state restoration machinery to restore its view controllers, always show your app’s window from this method. Do not show the window in your app’s [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) method. Calling the window’s [- makeKeyAndVisible](<../uiwindow/makekeyandvisible().md>) method does not make the window visible right away anyway. UIKit waits until your app’s [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) method finishes before making the window visible on the screen.

## See Also

### Initializing the app

- [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [LaunchOptionsKey](../uiapplication/launchoptionskey.md) — The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.
- [UIApplicationDidFinishLaunchingNotification](../uiapplication/didfinishlaunchingnotification.md) — A notification that posts immediately after the app finishes launching.
