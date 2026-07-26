---
title: CFNotificationCenterGetDistributedCenter()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationcentergetdistributedcenter()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationcentergetdistributedcenter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationcentergetdistributedcenter%28%29.json'
content_hash: 'sha256:7f0022fe35c0d8ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationCenterGetDistributedCenter()

<sub>Function</sub>

Returns the application’s distributed notification center.

<sub>macOS</sub>

```swift
func CFNotificationCenterGetDistributedCenter() -> CFNotificationCenter!
```

## Return Value

The application’s distributed notification center. An application has only one distributed notification center, so this function returns the same value each time it is called.

## Discussion

A distributed notification center delivers notifications between applications. A notification object used with a distributed notification center must always be a CFString object and the notification dictionary must contain only property list values.

## See Also

### Accessing a Notification Center

- [CFNotificationCenterGetDarwinNotifyCenter](<cfnotificationcentergetdarwinnotifycenter().md>) — Returns the application’s Darwin notification center.
- [CFNotificationCenterGetLocalCenter](<cfnotificationcentergetlocalcenter().md>) — Returns the application’s local notification center.
