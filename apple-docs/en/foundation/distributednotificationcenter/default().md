---
title: default()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/default()
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/default()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/default%28%29.json'
content_hash: 'sha256:8dac73c972f382bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# default()

<sub>Type Method</sub>

Returns the default distributed notification center, representing the local notification center for the computer.

<sub>Mac Catalyst, macOS</sub>

```swift
class func `default`() -> DistributedNotificationCenter
```

## Return Value

Default distributed notification center for the computer.

## Discussion

This method calls [+ notificationCenterForType:](<fortype(__).md>) with an argument of `NSLocalNotificationCenterType`.

## See Also

### Related Documentation

- [Notification Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)

### Getting Distributed Notification Centers

- [+ notificationCenterForType:](<fortype(__).md>) — Returns the distributed notification center for a particular notification center type.
