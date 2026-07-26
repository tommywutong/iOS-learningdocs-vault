---
title: UIUserNotificationActionBehavior
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationactionbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationactionbehavior.json'
content_hash: 'sha256:e2eb75d9d6818eca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserNotificationActionBehavior

<sub>Enumeration</sub>

Constants indicating additional behavior that the action supports.

> [!warning] Deprecated
> For more information, see [UIUserNotificationAction](uiusernotificationaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum UIUserNotificationActionBehavior
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIUserNotificationActionBehaviorDefault](uiusernotificationactionbehavior/default.md) — The default action behavior. When specified, the action supports no additional behaviors. _(deprecated)_
- [UIUserNotificationActionBehaviorTextInput](uiusernotificationactionbehavior/textinput.md) — The text input behavior. _(deprecated)_

### Initializers

- [init(rawValue:)](<uiusernotificationactionbehavior/init(rawvalue_).md>) _(deprecated)_

## See Also

### Constants

- [UIUserNotificationActivationMode](uiusernotificationactivationmode.md) — Constants indicating whether the app should activate to the foreground or background. _(deprecated)_
- [Action Parameter Key](action-parameter-key.md) — Key to include among the parameters of the action.
- [Behavior Key](behavior-key.md) — Key related to action-related behaviors.
