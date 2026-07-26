---
title: UIUserNotificationActivationMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationactivationmode
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationactivationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationactivationmode.json'
content_hash: 'sha256:dba26a4c8bcf9a28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserNotificationActivationMode

<sub>Enumeration</sub>

Constants indicating whether the app should activate to the foreground or background.

> [!warning] Deprecated
> For more information, see [UIUserNotificationAction](uiusernotificationaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum UIUserNotificationActivationMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIUserNotificationActivationModeForeground](uiusernotificationactivationmode/foreground.md) — Activate the app and put it in the foreground. _(deprecated)_
- [UIUserNotificationActivationModeBackground](uiusernotificationactivationmode/background.md) — Activate the app and put it in the background. If the app is already in the foreground, it remains in the foreground. _(deprecated)_

### Initializers

- [init(rawValue:)](<uiusernotificationactivationmode/init(rawvalue_).md>) _(deprecated)_

## See Also

### Constants

- [UIUserNotificationActionBehavior](uiusernotificationactionbehavior.md) — Constants indicating additional behavior that the action supports. _(deprecated)_
- [Action Parameter Key](action-parameter-key.md) — Key to include among the parameters of the action.
- [Behavior Key](behavior-key.md) — Key related to action-related behaviors.
