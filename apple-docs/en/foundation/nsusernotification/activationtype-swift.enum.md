---
title: NSUserNotification.ActivationType
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/activationtype-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/activationtype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/activationtype-swift.enum.json'
content_hash: 'sha256:5fb934bcf24f562f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# NSUserNotification.ActivationType

<sub>Enumeration</sub>

These constants describe how the user notification was activated.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
enum ActivationType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSUserNotificationActivationTypeNone](activationtype-swift.enum/none.md) — The user did not interact with the notification alert. _(deprecated)_
- [NSUserNotificationActivationTypeContentsClicked](activationtype-swift.enum/contentsclicked.md) — The user clicked on the contents of the notification alert. _(deprecated)_
- [NSUserNotificationActivationTypeActionButtonClicked](activationtype-swift.enum/actionbuttonclicked.md) — The user clicked on the action button of the notification alert. _(deprecated)_
- [NSUserNotificationActivationTypeReplied](activationtype-swift.enum/replied.md) — The user replied to the notification. _(deprecated)_
- [NSUserNotificationActivationTypeAdditionalActionClicked](activationtype-swift.enum/additionalactionclicked.md) — The user clicked on the additional action button of the notification alert. _(deprecated)_

### Initializers

- [init(rawValue:)](<activationtype-swift.enum/init(rawvalue_).md>) _(deprecated)_

## See Also

### Constants

- [NSUserNotificationDefaultSoundName](../nsusernotificationdefaultsoundname.md) — The default notification sound. _(deprecated)_
