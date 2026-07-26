---
title: CFNotificationCenterGetDarwinNotifyCenter()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationcentergetdarwinnotifycenter()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationcentergetdarwinnotifycenter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationcentergetdarwinnotifycenter%28%29.json'
content_hash: 'sha256:482ce5b5e835e9bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationCenterGetDarwinNotifyCenter()

<sub>Function</sub>

Returns the application’s Darwin notification center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNotificationCenterGetDarwinNotifyCenter() -> CFNotificationCenter!
```

## Return Value

The application’s Darwin notification center.

## Discussion

This notification center is used to cover the `<notify.h>` Core OS notification mechanism (see `/usr/include/notify.h`). An application has only one Darwin notification center, so this function returns the same value each time it is called.

The Darwin Notify Center has no notion of per-user sessions, all notifications are system-wide. As with distributed notifications, the main thread’s run loop must be running in one of the common modes (usually `kCFRunLoopDefaultMode`) for Darwin-style notifications to be delivered.

> [!important] Important
> Several function parameters are ignored by Darwin notification centers. To ensure future compatibility, you should pass `NULL` or `0` for all ignored arguments.

## See Also

### Accessing a Notification Center

- [CFNotificationCenterGetDistributedCenter](<cfnotificationcentergetdistributedcenter().md>) — Returns the application’s distributed notification center.
- [CFNotificationCenterGetLocalCenter](<cfnotificationcentergetlocalcenter().md>) — Returns the application’s local notification center.
