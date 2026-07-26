---
title: NSConnectionDidDieNotification
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnectiondiddienotification
source_url: 'https://developer.apple.com/documentation/foundation/nsconnectiondiddienotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnectiondiddienotification.json'
content_hash: 'sha256:abc0dd58a0d4c82e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSConnectionDidDieNotification

<sub>Global Variable</sub>

Posted when an `NSConnection` object is deallocated or when it’s notified that its `NSPort` object has become invalid. The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary.

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSString * const NSConnectionDidDieNotification;
```

## Discussion

An `NSConnection` object attached to a remote `NSSocketPort` object cannot detect when the remote port becomes invalid, even if the remote port is on the same machine. Therefore, it cannot post this notification when the connection is lost. Instead, you must detect the timeout error when the next message is sent.

The `NSConnection` object posting this notification is no longer useful, so all receivers should unregister themselves for any notifications involving the `NSConnection` object.

## See Also

### Related Documentation

- [NSPortDidBecomeInvalidNotification](port/didbecomeinvalidnotification.md) — Posted from the [- invalidate](<port/invalidate().md>) method, which is invoked when the `NSPort` is deallocated or when it notices that its communication channel has been damaged. The notification object is the `NSPort` object that has become invalid. This notification does not contain a `userInfo` dictionary.

### Notifications

- [NSConnectionDidInitializeNotification](nsconnectiondidinitializenotification.md) — Posted when an `NSConnection` object is initialized using [initWithReceivePort:sendPort:](nsconnection/initwithreceiveport_sendport_.md) (the designated initializer for `NSConnection`). The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary. _(deprecated)_
