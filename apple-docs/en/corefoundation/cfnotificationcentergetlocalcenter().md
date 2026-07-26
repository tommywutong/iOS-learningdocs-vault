---
title: CFNotificationCenterGetLocalCenter()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationcentergetlocalcenter()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationcentergetlocalcenter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationcentergetlocalcenter%28%29.json'
content_hash: 'sha256:c485e54a21e4cbbf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationCenterGetLocalCenter()

<sub>Function</sub>

Returns the application’s local notification center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNotificationCenterGetLocalCenter() -> CFNotificationCenter!
```

## Return Value

The application’s local notification center. An application has only one local notification center, so this function returns the same value each time it is called.

## See Also

### Accessing a Notification Center

- [CFNotificationCenterGetDarwinNotifyCenter](<cfnotificationcentergetdarwinnotifycenter().md>) — Returns the application’s Darwin notification center.
- [CFNotificationCenterGetDistributedCenter](<cfnotificationcentergetdistributedcenter().md>) — Returns the application’s distributed notification center.
