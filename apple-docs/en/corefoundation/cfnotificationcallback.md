---
title: CFNotificationCallback
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationcallback.json'
content_hash: 'sha256:65e4117cc759c4a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationCallback

<sub>Type Alias</sub>

Callback function invoked for each observer of a notification when the notification is posted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFNotificationCallback = (CFNotificationCenter?, UnsafeMutableRawPointer?, CFNotificationName?, UnsafeRawPointer?, CFDictionary?) -> Void
```

## Parameters

- `center` — The notification center handling the notification.

- `observer` — An arbitrary value, other than `NULL`, that identifies the observer.

- `name` — The name of the notification being posted.

- `object` — An arbitrary value that identifies the object posting the notification. For distributed notifications, `object` is always a CFString object. This value could be `NULL`.

- `userInfo` — A dictionary containing additional information regarding the notification. This value could be `NULL`. If the notification center is a Darwin notification center, this value must be ignored.
