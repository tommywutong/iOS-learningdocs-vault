---
title: 'forType(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/distributednotificationcenter/fortype(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/fortype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/fortype%28_%3A%29.json'
content_hash: 'sha256:f6c1e816aadcda61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# forType(_:)

<sub>Type Method</sub>

Returns the distributed notification center for a particular notification center type.

<sub>Mac Catalyst, macOS</sub>

```swift
class func forType(_ notificationCenterType: DistributedNotificationCenter.CenterType) -> DistributedNotificationCenter
```

## Parameters

- `notificationCenterType` — Notification center type being inquired about.

## Return Value

Distributed notification center for `notificationCenterType`.

## Discussion

Currently only one type, `NSLocalNotificationCenterType`, is supported.

## See Also

### Getting Distributed Notification Centers

- [+ defaultCenter](<default().md>) — Returns the default distributed notification center, representing the local notification center for the computer.
