---
title: 'notificationWithName:object:userInfo:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsnotification/notificationwithname:object:userinfo:'
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/notificationwithname:object:userinfo:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/notificationwithname%3Aobject%3Auserinfo%3A.json'
content_hash: 'sha256:e0a7c6ca2b85654a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNotification](../nsnotification.md)

# notificationWithName:object:userInfo:

<sub>Type Method</sub>

Returns a notification object with a specified name, object, and user information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) notificationWithName:(NSNotificationName) aName object:(id) anObject userInfo:(NSDictionary *) aUserInfo;
```

## Parameters

- `aName` — The name for the new notification. May not be `nil`.

- `anObject` — The object for the new notification.

- `aUserInfo` — The user information dictionary for the new notification. May be `nil`.

## See Also

### Related Documentation

- [- postNotificationName:object:userInfo:](<../notificationcenter/post(name_object_userinfo_).md>) — Creates a notification with a given name, sender, and information and posts it to the notification center.

### Creating Notifications

- [init](init.md) — Initializes an empty notification.
- [- initWithCoder:](<init(coder_).md>) — Initializes a notification with the data from an unarchiver.
- [+ notificationWithName:object:](<init(name_object_).md>) — Returns a new notification object with a specified name and object.
- [- initWithName:object:userInfo:](<init(name_object_userinfo_).md>) — Initializes a notification with a specified name, object, and user information.
- [Name](name-swift.struct.md) — A structure that defines the name of a notification.
