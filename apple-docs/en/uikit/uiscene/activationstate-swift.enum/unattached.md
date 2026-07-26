---
title: UIScene.ActivationState.unattached
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/activationstate-swift.enum/unattached
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.enum/unattached'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/activationstate-swift.enum/unattached.json'
content_hash: 'sha256:90951293c8363d38'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ActivationState](../activationstate-swift.enum.md)

# UIScene.ActivationState.unattached

<sub>Case</sub>

A state that indicates that the scene is not currently connected to your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case unattached
```

## Discussion

A scene starts in the unattached state and remains in that state until the system sends a connection notification to it. A scene reenters the attached state when the user dismisses the interface from the app switcher or to reclaim its resources.

## See Also

### Scene States

- [UISceneActivationStateForegroundInactive](foregroundinactive.md) — A state that indicates that the scene is running in the foreground but is not receiving events.
- [UISceneActivationStateForegroundActive](foregroundactive.md) — A state that indicates that the scene is running in the foreground and is currently receiving events.
- [UISceneActivationStateBackground](background.md) — A state that indicates that the scene is running in the background and is not onscreen.
