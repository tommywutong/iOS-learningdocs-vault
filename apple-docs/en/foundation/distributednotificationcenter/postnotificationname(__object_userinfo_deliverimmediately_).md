---
title: 'postNotificationName(_:object:userInfo:deliverImmediately:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:)'
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/postnotificationname%28_%3Aobject%3Auserinfo%3Adeliverimmediately%3A%29.json'
content_hash: 'sha256:23aa71c30d7511e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# postNotificationName(_:object:userInfo:deliverImmediately:)

<sub>Instance Method</sub>

Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func postNotificationName(_ name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]? = nil, deliverImmediately: Bool)
```

## Parameters

- `name` — Name of the notification to post. Must not be `nil`.

- `object` — Sender of the notification. May be `nil`.

- `userInfo` — Dictionary containing additional information. May be `nil`. > [!important] Important > Sandboxed apps can send notifications only if they do not contain a dictionary. If the sending application is in an App Sandbox, `userInfo` _must_ be `nil`.

- `deliverImmediately` — Specifies when to deliver the notification. When [false](../../swift/false.md), the receiver delivers notifications to their observers according to the suspended-notification behavior specified in the corresponding dispatch table entry. When [true](../../swift/true.md), the receiver delivers the notification immediately to its observers.

## Discussion

This is the preferred method for posting notifications.

The `notificationInfo` dictionary is serialized as a property list, so it can be passed to another task. In the receiving task, it is deserialized back into a dictionary. This serialization imposes some restrictions on the objects that can be placed in the `notificationInfo` dictionary. See XML Property Lists for details.

## See Also

### Related Documentation

- [+ unarchiveObjectWithData:](<../nsunarchiver/unarchiveobject(with_).md>) — Decodes and returns the object archived in a given `NSData` object. _(deprecated)_
- [- encodeRootObject:](<../nsarchiver/encoderootobject(__).md>) — Archives a given object along with all the objects to which it is connected. _(deprecated)_

### Posting Notifications

- [- postNotificationName:object:](<post(name_object_).md>) — Creates a notification, and posts it to the receiver.
- [- postNotificationName:object:userInfo:](<post(name_object_userinfo_).md>) — Creates a notification with information, and posts it to the receiver.
- [- postNotificationName:object:userInfo:options:](<postnotificationname(__object_userinfo_options_).md>) — Creates a notification with information, and posts it to the receiver.
