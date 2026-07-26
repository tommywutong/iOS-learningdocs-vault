---
title: NotificationCenter.Notifications.Iterator
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/notifications/iterator
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/notifications/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/notifications/iterator.json'
content_hash: 'sha256:6591dc1dc4e59720'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [Notifications](../notifications.md)

# NotificationCenter.Notifications.Iterator

<sub>Structure</sub>

The asynchronous iterator created by this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Iterator
```

## Relationships

- **Conforms To**: [AsyncIteratorProtocol](../../../swift/asynciteratorprotocol.md)

## Topics

### Iterating over Elements

- [next()](<iterator/next().md>) — Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

### Supporting Types

- [Element](element.md) — The type of element produced by this asynchronous sequence.

## See Also

### Creating an Iterator

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
