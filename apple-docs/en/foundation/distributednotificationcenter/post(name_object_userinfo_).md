---
title: 'post(name:object:userInfo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/distributednotificationcenter/post(name:object:userinfo:)'
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/post(name:object:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/post%28name%3Aobject%3Auserinfo%3A%29.json'
content_hash: 'sha256:6c2774f9ace28c41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# post(name:object:userInfo:)

<sub>Instance Method</sub>

Creates a notification with information, and posts it to the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func post(name aName: NSNotification.Name, object anObject: String?, userInfo aUserInfo: [AnyHashable : Any]? = nil)
```

## Parameters

- `aName` — Name of the notification to post. Must not be `nil`.

- `anObject` — Sender of the notification. May be `nil`.

- `aUserInfo` — Dictionary containing additional information. May be `nil`. > [!important] Important > Sandboxed apps can send notifications only if they do not contain a dictionary. If the sending application is in an App Sandbox, `notificationInfo` _must_ be `nil`.

## Discussion

This method invokes [- postNotificationName:object:userInfo:deliverImmediately:](<postnotificationname(__object_userinfo_deliverimmediately_).md>) with `deliverImmediately:NO`.

## See Also

### Posting Notifications

- [- postNotificationName:object:](<post(name_object_).md>) — Creates a notification, and posts it to the receiver.
- [- postNotificationName:object:userInfo:deliverImmediately:](<postnotificationname(__object_userinfo_deliverimmediately_).md>) — Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.
- [- postNotificationName:object:userInfo:options:](<postnotificationname(__object_userinfo_options_).md>) — Creates a notification with information, and posts it to the receiver.
