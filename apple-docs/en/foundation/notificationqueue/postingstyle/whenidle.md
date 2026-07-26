---
title: NotificationQueue.PostingStyle.whenIdle
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationqueue/postingstyle/whenidle
source_url: 'https://developer.apple.com/documentation/foundation/notificationqueue/postingstyle/whenidle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationqueue/postingstyle/whenidle.json'
content_hash: 'sha256:99048d08011fe3f1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationQueue](../../notificationqueue.md) · [PostingStyle](../postingstyle.md)

# NotificationQueue.PostingStyle.whenIdle

<sub>Case</sub>

The notification is posted when the run loop is idle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case whenIdle
```

## See Also

### Constants

- [NSPostASAP](asap.md) — The notification is posted at the end of the current notification callout or timer.
- [NSPostNow](now.md) — The notification is posted immediately after coalescing.
