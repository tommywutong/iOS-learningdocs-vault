---
title: CFNotificationSuspensionBehavior
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationsuspensionbehavior
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationsuspensionbehavior.json'
content_hash: 'sha256:a98710fa535dc454'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationSuspensionBehavior

<sub>Enumeration</sub>

Suspension flags that indicate how distributed notifications should be handled when the receiving application is in the background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFNotificationSuspensionBehavior
```

## Overview

An application selects the suspension behavior for a given notification when it registers an observer for that notification with [CFNotificationCenterAddObserver](<cfnotificationcenteraddobserver(____________).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [CFNotificationSuspensionBehaviorDrop](cfnotificationsuspensionbehavior/drop.md) — The server will not queue any notifications of the specified name and object while the receiving application is in the background.
- [CFNotificationSuspensionBehaviorCoalesce](cfnotificationsuspensionbehavior/coalesce.md) — The server will only queue the last notification of the specified name and object; earlier notifications are dropped.
- [CFNotificationSuspensionBehaviorHold](cfnotificationsuspensionbehavior/hold.md) — The server will hold all matching notifications until the queue has been filled (queue size determined by the server) at which point the server may flush queued notifications.
- [CFNotificationSuspensionBehaviorDeliverImmediately](cfnotificationsuspensionbehavior/deliverimmediately.md) — The server will deliver notifications of the specified name and object whether or not the application is in the background. When a notification with this suspension behavior is matched, it has the effect of first flushing any queued notifications.

### Initializers

- [init(rawValue:)](<cfnotificationsuspensionbehavior/init(rawvalue_).md>)

## See Also

### Constants

- [Notification Posting Options](1569610-notification-posting-options.md) — Possible options when posting notifications.
