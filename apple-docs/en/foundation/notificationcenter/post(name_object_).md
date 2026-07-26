---
title: 'post(name:object:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/post(name:object:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/post(name:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/post%28name%3Aobject%3A%29.json'
content_hash: 'sha256:8a8db0e8a78d74a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# post(name:object:)

<sub>Instance Method</sub>

Creates a notification with a given name and sender and posts it to the notification center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func post(name aName: NSNotification.Name, object anObject: Any?)
```

## Parameters

- `aName` — The name of the notification.

- `anObject` — The object posting the notification.

## Discussion

This is a convenience method for calling [- postNotificationName:object:userInfo:](<post(name_object_userinfo_).md>) and passing `nil` to `aUserInfo`.

## See Also

### Posting notifications

- [- postNotification:](<post(__)-3x2st.md>) — Posts a given notification to the notification center.
- [- postNotificationName:object:userInfo:](<post(name_object_userinfo_).md>) — Creates a notification with a given name, sender, and information and posts it to the notification center.
