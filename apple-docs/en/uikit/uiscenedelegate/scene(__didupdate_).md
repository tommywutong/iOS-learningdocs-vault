---
title: 'scene(_:didUpdate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scene(_:didupdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:didupdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scene%28_%3Adidupdate%3A%29.json'
content_hash: 'sha256:91098d2d5840c5a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# scene(_:didUpdate:)

<sub>Instance Method</sub>

Tells the delegate that the specified activity object was updated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scene(_ scene: UIScene, didUpdate userActivity: NSUserActivity)
```

## Parameters

- `scene` — The scene handling the activity.

- `userActivity` — The user activity object containing the updated data.

## Discussion

Use this method to add any final data to the specified user activity object. UIKit calls this method on your app’s main thread after calling your [- stateRestorationActivityForScene:](<staterestorationactivity(for_).md>) method and after giving other parts of your app an opportunity to update the activity object returned by that method.

## See Also

### Saving the state of the scene

- [Restoring your app’s state](../restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [- stateRestorationActivityForScene:](<staterestorationactivity(for_).md>) — Returns a user activity object encapsulating the current state of the specified scene.
- [- scene:restoreInteractionStateWithUserActivity:](<scene(__restoreinteractionstatewith_).md>)
