---
title: UIScene.ActivationState.foregroundInactive
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/activationstate-swift.enum/foregroundinactive
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.enum/foregroundinactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/activationstate-swift.enum/foregroundinactive.json'
content_hash: 'sha256:303e6db687380779'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ActivationState](../activationstate-swift.enum.md)

# UIScene.ActivationState.foregroundInactive

<sub>Case</sub>

A state that indicates that the scene is running in the foreground but is not receiving events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case foregroundInactive
```

## Discussion

A scene transits through the foreground-inactive state on its way to or from another state.

## See Also

### Scene States

- [UISceneActivationStateUnattached](unattached.md) — A state that indicates that the scene is not currently connected to your app.
- [UISceneActivationStateForegroundActive](foregroundactive.md) — A state that indicates that the scene is running in the foreground and is currently receiving events.
- [UISceneActivationStateBackground](background.md) — A state that indicates that the scene is running in the background and is not onscreen.
