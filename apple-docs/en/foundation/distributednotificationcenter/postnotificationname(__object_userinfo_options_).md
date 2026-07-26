---
title: 'postNotificationName(_:object:userInfo:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/distributednotificationcenter/postnotificationname(_:object:userinfo:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/postnotificationname(_:object:userinfo:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/postnotificationname%28_%3Aobject%3Auserinfo%3Aoptions%3A%29.json'
content_hash: 'sha256:35dab7a7787980e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# postNotificationName(_:object:userInfo:options:)

<sub>Instance Method</sub>

Creates a notification with information, and posts it to the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func postNotificationName(_ name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]? = nil, options: DistributedNotificationCenter.Options = [])
```

## Parameters

- `name` — Name of the notification to post. Must not be `nil`.

- `object` — Sender of the notification. May be `nil`.

- `userInfo` — Dictionary containing additional information. May be `nil`. > [!important] Important > Sandboxed apps can send notifications only if they do not contain a dictionary. If the sending application is in an App Sandbox, `userInfo` _must_ be `nil`.

- `options` — Specifies how the notification is posted to the task and when to deliver it to its observers. See `Notification Posting Behavior` for details.

## Discussion

The `userInfo` dictionary is serialized as a property list, so it can be passed to another task. In the receiving task, it is deserialized back into a dictionary. This serialization imposes some restrictions on the objects that can be placed in the `userInfo` dictionary. See XML Property Lists for details.

## See Also

### Posting Notifications

- [- postNotificationName:object:](<post(name_object_).md>) — Creates a notification, and posts it to the receiver.
- [- postNotificationName:object:userInfo:](<post(name_object_userinfo_).md>) — Creates a notification with information, and posts it to the receiver.
- [- postNotificationName:object:userInfo:deliverImmediately:](<postnotificationname(__object_userinfo_deliverimmediately_).md>) — Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.
