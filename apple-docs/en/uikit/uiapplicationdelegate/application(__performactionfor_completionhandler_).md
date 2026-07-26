---
title: 'application(_:performActionFor:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（26.0 起废弃）, iPadOS 9.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:performactionfor:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:performactionfor:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Aperformactionfor%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:c784bd7aeaac84c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:performActionFor:completionHandler:)

<sub>Instance Method</sub>

Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method.

> [!warning] Deprecated
> Use UIScene lifecycle and windowScene(_:performActionFor:completionHandler:) from UIWindowSceneDelegate instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func application(_ application: UIApplication, performActionFor shortcutItem: UIApplicationShortcutItem, completionHandler: @escaping (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func application(_ application: UIApplication, performActionFor shortcutItem: UIApplicationShortcutItem) async -> Bool
```

## Parameters

- `application` — Your shared app object.

- `shortcutItem` — The quick action for which you’re providing an implementation in this method.

- `completionHandler` — The block you call after your quick action implementation completes, returning [true](../../swift/true.md) or [false](../../swift/false.md) depending on the success or failure of your implementation code. - **succeeded** — A Boolean value that indicates whether or not your implementation succeeded.

## Discussion

> [!important] Important
> This method is not called for scene-based apps. If you have a scene-based app, implement [- windowScene:performActionForShortcutItem:completionHandler:](<../uiwindowscenedelegate/windowscene(__performactionfor_completionhandler_).md>) in your scene delegate instead.

Implement this method to respond to the user’s selection of a Home screen quick action for your app. When finished, call the completion handler, with an appropriate Boolean value.

It’s your responsibility to ensure the system calls this method conditionally, depending on whether or not one of your app launch methods ([- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) or [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>)) has already handled a quick action invocation. The system calls a launch method (before calling this method) when a user selects a quick action for your app and your app _launches_ instead of _activating_.

The requested quick action might employ code paths different than those used otherwise when your app launches. For example, your app normally launches to display view A, but your app was launched in response to a quick action that needs view B. To handle such cases, upon launch, check whether your app is being launched via a quick action. Perform this check in your [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) or [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) method by checking for the [UIApplicationLaunchOptionsShortcutItemKey](../uiapplication/launchoptionskey/shortcutitem.md) launch option key. The [UIApplicationShortcutItem](../uiapplicationshortcutitem.md) object is available as the value of the launch option key.

If you find that your app was indeed launched using a quick action, perform the requested quick action within the launch method and return a value of [false](../../swift/false.md) from that method. When you return a value of [false](../../swift/false.md), the system doesn’t call the [- application:performActionForShortcutItem:completionHandler:](<application(__performactionfor_completionhandler_).md>) method.

## See Also

### Continuing user activity and handling quick actions

- [- application:willContinueUserActivityWithType:](<application(__willcontinueuseractivitywithtype_).md>) — Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected. _(deprecated)_
- [- application:continueUserActivity:restorationHandler:](<application(__continue_restorationhandler_).md>) — Tells the delegate that the data for continuing an activity is available. _(deprecated)_
- [- application:didUpdateUserActivity:](<application(__didupdate_).md>) — Tells the delegate that the activity was updated. _(deprecated)_
- [- application:didFailToContinueUserActivityWithType:error:](<application(__didfailtocontinueuseractivitywithtype_error_).md>) — Tells the delegate that the activity couldn’t be continued. _(deprecated)_
