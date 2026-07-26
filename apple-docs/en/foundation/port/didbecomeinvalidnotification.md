---
title: didBecomeInvalidNotification
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/port/didbecomeinvalidnotification
source_url: 'https://developer.apple.com/documentation/foundation/port/didbecomeinvalidnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/port/didbecomeinvalidnotification.json'
content_hash: 'sha256:8f32cadd499da8d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Port](../port.md)

# didBecomeInvalidNotification

<sub>Type Property</sub>

Posted from the [- invalidate](<invalidate().md>) method, which is invoked when the `NSPort` is deallocated or when it notices that its communication channel has been damaged. The notification object is the `NSPort` object that has become invalid. This notification does not contain a `userInfo` dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let didBecomeInvalidNotification: NSNotification.Name
```

## Discussion

An `NSSocketPort` object cannot detect when its connection to a remote port is lost, even if the remote port is on the same machine. Therefore, it cannot invalidate itself and post this notification. Instead, you must detect the timeout error when the next message is sent.

The `NSPort` object posting this notification is no longer useful, so all receivers should unregister themselves for any notifications involving the `NSPort`. A method receiving this notification should check to see which port became invalid before attempting to do anything. In particular, observers that receive all [NSPortDidBecomeInvalidNotification](didbecomeinvalidnotification.md) messages should be aware that communication with the window server is handled through an `NSPort`. If this port becomes invalid, drawing operations will cause a fatal error.
