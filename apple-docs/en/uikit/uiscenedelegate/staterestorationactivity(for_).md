---
title: 'stateRestorationActivity(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/staterestorationactivity(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/staterestorationactivity(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/staterestorationactivity%28for%3A%29.json'
content_hash: 'sha256:9c69ddb1600ca111'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# stateRestorationActivity(for:)

<sub>Instance Method</sub>

Returns a user activity object encapsulating the current state of the specified scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func stateRestorationActivity(for scene: UIScene) -> NSUserActivity?
```

## Parameters

- `scene` — The scene whose state information is needed.

## Discussion

Use this method to return an [NSUserActivity](../../foundation/nsuseractivity.md) object with information about your scene’s current state. Save enough information to be able to restore that state again after UIKit disconnects and then reconnects the scene. User activity objects are a mechanism to record what the user is doing, so you don’t need to manually persist the state of your scene’s UI.

After calling this method, and before archiving the [NSUserActivity](../../foundation/nsuseractivity.md) object and saving it to disk, UIKit lets you add state information as follows:

- If you set a delegate for the [NSUserActivity](../../foundation/nsuseractivity.md) object in your app, UIKit calls the delegate’s [userActivityWillSave(_:)](<../../foundation/nsuseractivitydelegate/useractivitywillsave(__).md>) method.
- If you assign the [NSUserActivity](../../foundation/nsuseractivity.md) object to the [userActivity](../uiresponder/useractivity.md) property of any responders, UIKit calls each responder’s [- updateUserActivityState:](<../uiresponder/updateuseractivitystate(__).md>) method.

When reconnecting the scene and restoring state, the user activity provided by this method will be provided in the [stateRestorationActivity](../uiscenesession/staterestorationactivity.md) property of [UISceneSession](../uiscenesession.md).

## See Also

### Saving the state of the scene

- [Restoring your app’s state](../restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [- scene:restoreInteractionStateWithUserActivity:](<scene(__restoreinteractionstatewith_).md>)
- [- scene:didUpdateUserActivity:](<scene(__didupdate_).md>) — Tells the delegate that the specified activity object was updated.
