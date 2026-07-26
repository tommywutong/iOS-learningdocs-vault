---
title: 'windowScene(_:performActionFor:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindowscenedelegate/windowscene(_:performactionfor:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:performactionfor:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenedelegate/windowscene%28_%3Aperformactionfor%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:fe1ff9d5956ae619'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowSceneDelegate](../uiwindowscenedelegate.md)

# windowScene(_:performActionFor:completionHandler:)

<sub>Instance Method</sub>

Asks the delegate to perform the user-selected action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func windowScene(_ windowScene: UIWindowScene, performActionFor shortcutItem: UIApplicationShortcutItem, completionHandler: @escaping (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func windowScene(_ windowScene: UIWindowScene, performActionFor shortcutItem: UIApplicationShortcutItem) async -> Bool
```

## Parameters

- `windowScene` — The window scene object receiving the shortcut item.

- `shortcutItem` — The action selected by the user. Your app defines the actions that it supports, and the user chooses from among those actions. For information about how to create and configure shortcut items for your app, see [UIApplicationShortcutItem](../uiapplicationshortcutitem.md).

- `completionHandler` — A handler block to call after you complete the action. This block has no return value and takes the following parameter: - **succeeded** — A Boolean value indicating whether you successfully completed the specified action. Specify [true](../../swift/true.md) if you completed the action or [false](../../swift/false.md) if you didn’t.

## Discussion

When the user selects one of your app’s shortcut items, use this method to perform the selected action. After you finish the action, execute the specified `completionHandler` block to report your success or failure in performing the action.

## See Also

### Performing tasks

- [- windowScene:userDidAcceptCloudKitShareWithMetadata:](<windowscene(__userdidacceptcloudkitsharewith_).md>) — Tells the delegate that the window scene now has access to shared information in CloudKit.
