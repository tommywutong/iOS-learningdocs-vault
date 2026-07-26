---
title: 'post(name:object:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/distributednotificationcenter/post(name:object:)'
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/post(name:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/post%28name%3Aobject%3A%29.json'
content_hash: 'sha256:3225fbd9e61e8337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# post(name:object:)

<sub>Instance Method</sub>

Creates a notification, and posts it to the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func post(name aName: NSNotification.Name, object anObject: String?)
```

## Parameters

- `aName` — Name of the notification to post. Must not be `nil`.

- `anObject` — Sender of the notification. May be `nil`.

## Discussion

This method invokes [- postNotificationName:object:userInfo:deliverImmediately:](<postnotificationname(__object_userinfo_deliverimmediately_).md>) with `userInfo:nil deliverImmediately:NO`.

## See Also

### Posting Notifications

- [- postNotificationName:object:userInfo:](<post(name_object_userinfo_).md>) — Creates a notification with information, and posts it to the receiver.
- [- postNotificationName:object:userInfo:deliverImmediately:](<postnotificationname(__object_userinfo_deliverimmediately_).md>) — Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.
- [- postNotificationName:object:userInfo:options:](<postnotificationname(__object_userinfo_options_).md>) — Creates a notification with information, and posts it to the receiver.
