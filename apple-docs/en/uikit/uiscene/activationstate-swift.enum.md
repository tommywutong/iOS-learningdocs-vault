---
title: UIScene.ActivationState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/activationstate-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/activationstate-swift.enum.json'
content_hash: 'sha256:eb7458674bbe5d1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# UIScene.ActivationState

<sub>Enumeration</sub>

Constants that indicate the foreground or background execution state of your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ActivationState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Scene States

- [UISceneActivationStateUnattached](activationstate-swift.enum/unattached.md) — A state that indicates that the scene is not currently connected to your app.
- [UISceneActivationStateForegroundInactive](activationstate-swift.enum/foregroundinactive.md) — A state that indicates that the scene is running in the foreground but is not receiving events.
- [UISceneActivationStateForegroundActive](activationstate-swift.enum/foregroundactive.md) — A state that indicates that the scene is running in the foreground and is currently receiving events.
- [UISceneActivationStateBackground](activationstate-swift.enum/background.md) — A state that indicates that the scene is running in the background and is not onscreen.

### Initializers

- [init(rawValue:)](<activationstate-swift.enum/init(rawvalue_).md>)

## See Also

### Getting the scene attributes

- [activationState](activationstate-swift.property.md) — The current execution state of the scene.
- [title](title.md) — A user-visible string you supply to help users differentiate among your app’s scenes.
- [subtitle](subtitle.md) — A string that the app displays in the title bar of a window when running in macOS.
