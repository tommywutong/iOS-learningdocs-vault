---
title: UIApplication.State
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/state
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/state.json'
content_hash: 'sha256:e64ca1d766dd6728'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# UIApplication.State

<sub>Enumeration</sub>

Constants that indicate the running states of an app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIApplicationStateActive](state/active.md) — The app is running in the foreground and currently receiving events.
- [UIApplicationStateInactive](state/inactive.md) — The app is running in the foreground but isn’t receiving events.
- [UIApplicationStateBackground](state/background.md) — The app is running in the background.

### Initializers

- [init(rawValue:)](<state/init(rawvalue_).md>)

## See Also

### Getting the application state

- [applicationState](applicationstate.md) — The app’s current state, or that of its most active scene.
