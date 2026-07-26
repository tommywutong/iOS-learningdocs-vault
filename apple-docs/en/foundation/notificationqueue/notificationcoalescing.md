---
title: NotificationQueue.NotificationCoalescing
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationqueue/notificationcoalescing
source_url: 'https://developer.apple.com/documentation/foundation/notificationqueue/notificationcoalescing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationqueue/notificationcoalescing.json'
content_hash: 'sha256:9c5509a373bad1ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationQueue](../notificationqueue.md)

# NotificationQueue.NotificationCoalescing

<sub>Structure</sub>

The constants that specify how notifications are coalesced.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NotificationCoalescing
```

## Overview

These constants are used by the [- enqueueNotification:postingStyle:coalesceMask:forModes:](<enqueue(__postingstyle_coalescemask_formodes_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSNotificationNoCoalescing](notificationcoalescing/none.md) — Do not coalesce notifications in the queue.
- [NSNotificationCoalescingOnName](notificationcoalescing/onname.md) — Coalesce notifications with the same name.
- [NSNotificationCoalescingOnSender](notificationcoalescing/onsender.md) — Coalesce notifications with the same object.

### Initializers

- [init(rawValue:)](<notificationcoalescing/init(rawvalue_).md>)

## See Also

### Constants

- [PostingStyle](postingstyle.md) — The constants that specify when notifications are posted.
