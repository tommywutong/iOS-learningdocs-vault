---
title: NSUserNotificationAction
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.10+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotificationaction
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationaction.json'
content_hash: 'sha256:8ddcd6328df8e531'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserNotificationAction

<sub>Class</sub>

An action that the user can take in response to receiving a notification.

> [!warning] Deprecated
> Use the [User Notifications](../usernotifications.md) framework instead.

<sub>macOS</sub>

```swift
class NSUserNotificationAction
```

## Overview

User notifications can specify one or more actions to show to the user by using the [additionalActivationAction](nsusernotification/additionalactivationaction.md) or [additionalActions](nsusernotification/additionalactions.md) properties. [NSUserNotificationAction](nsusernotificationaction.md) objects contain the localized title shown to the user and an identifier used to differentiate between presented actions.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating User Notification Actions

- [+ actionWithIdentifier:title:](<nsusernotificationaction/init(identifier_title_).md>) — Creates a user notification action with a specified identifier and title. _(deprecated)_

### Getting the Identifier and Title

- [identifier](nsusernotificationaction/identifier.md) — The identifier for the user notification action. _(deprecated)_
- [title](nsusernotificationaction/title.md) — The localized title shown to the user. _(deprecated)_

## See Also

### User Notifications

- [NSUserNotification](nsusernotification.md) — A notification that can be scheduled for display in the notification center. _(deprecated)_
- [NSUserNotificationCenter](nsusernotificationcenter.md) — An object that delivers notifications from apps to the user. _(deprecated)_
- [NSUserNotificationCenterDelegate](nsusernotificationcenterdelegate.md) — An interface that enables customizing the behavior of the default notification center.
