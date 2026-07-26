---
title: 'scene(_:restoreInteractionStateWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scene(_:restoreinteractionstatewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:restoreinteractionstatewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scene%28_%3Arestoreinteractionstatewith%3A%29.json'
content_hash: 'sha256:db048acfa9eeb744'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# scene(_:restoreInteractionStateWith:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scene(_ scene: UIScene, restoreInteractionStateWith stateRestorationActivity: NSUserActivity)
```

## See Also

### Saving the state of the scene

- [Restoring your app’s state](../restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [- stateRestorationActivityForScene:](<staterestorationactivity(for_).md>) — Returns a user activity object encapsulating the current state of the specified scene.
- [- scene:didUpdateUserActivity:](<scene(__didupdate_).md>) — Tells the delegate that the specified activity object was updated.
