---
title: UISpringLoadedInteractionEffectState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uispringloadedinteractioneffectstate
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteractioneffectstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteractioneffectstate.json'
content_hash: 'sha256:736db3fc90dbefc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISpringLoadedInteractionEffectState

<sub>Enumeration</sub>

The spring-loaded interaction states that determine the style of the interaction view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UISpringLoadedInteractionEffectState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### States

- [UISpringLoadedInteractionEffectStateActivated](uispringloadedinteractioneffectstate/activated.md) — An interaction state that indicates that the view was spring loaded.
- [UISpringLoadedInteractionEffectStateActivating](uispringloadedinteractioneffectstate/activating.md) — An interaction state that indicates that spring loading is about to start.
- [UISpringLoadedInteractionEffectStateInactive](uispringloadedinteractioneffectstate/inactive.md) — An interaction state that indicates that spring loading is not engaged.
- [UISpringLoadedInteractionEffectStatePossible](uispringloadedinteractioneffectstate/possible.md) — An interaction state that indicates that spring loading is available.

### Initializers

- [init(rawValue:)](<uispringloadedinteractioneffectstate/init(rawvalue_).md>)

## See Also

### Managing state

- [state](uispringloadedinteractioncontext/state.md) — The current view style for the spring-loaded interaction.
- [targetItem](uispringloadedinteractioncontext/targetitem.md) — The specific subview, or associated model object, of the target view to use for the spring-loaded interaction.
- [targetView](uispringloadedinteractioncontext/targetview.md) — The view to which the current spring-loaded interaction view style is applied.
