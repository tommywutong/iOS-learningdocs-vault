---
title: activationState
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/activationstate-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/activationstate-swift.property.json'
content_hash: 'sha256:6b52f625a83b9764'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# activationState

<sub>Instance Property</sub>

The current execution state of the scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var activationState: UIScene.ActivationState { get }
```

## Discussion

When it is running, a scene is usually in the [UISceneActivationStateForegroundActive](activationstate-swift.enum/foregroundactive.md) or [UISceneActivationStateBackground](activationstate-swift.enum/background.md) state. A state may also enter other states for a short time as part of a transition.

## See Also

### Getting the scene attributes

- [ActivationState](activationstate-swift.enum.md) — Constants that indicate the foreground or background execution state of your app.
- [title](title.md) — A user-visible string you supply to help users differentiate among your app’s scenes.
- [subtitle](subtitle.md) — A string that the app displays in the title bar of a window when running in macOS.
