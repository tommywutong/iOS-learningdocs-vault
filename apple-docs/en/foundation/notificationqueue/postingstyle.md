---
title: NotificationQueue.PostingStyle
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationqueue/postingstyle
source_url: 'https://developer.apple.com/documentation/foundation/notificationqueue/postingstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationqueue/postingstyle.json'
content_hash: 'sha256:920dd6629214b32b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationQueue](../notificationqueue.md)

# NotificationQueue.PostingStyle

<sub>Enumeration</sub>

The constants that specify when notifications are posted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PostingStyle
```

## Overview

These constants are used by the [- enqueueNotification:postingStyle:](<enqueue(__postingstyle_).md>) and [- enqueueNotification:postingStyle:coalesceMask:forModes:](<enqueue(__postingstyle_coalescemask_formodes_).md>) methods.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSPostASAP](postingstyle/asap.md) — The notification is posted at the end of the current notification callout or timer.
- [NSPostWhenIdle](postingstyle/whenidle.md) — The notification is posted when the run loop is idle.
- [NSPostNow](postingstyle/now.md) — The notification is posted immediately after coalescing.

### Initializers

- [init(rawValue:)](<postingstyle/init(rawvalue_).md>)

## See Also

### Constants

- [NotificationCoalescing](notificationcoalescing.md) — The constants that specify how notifications are coalesced.
