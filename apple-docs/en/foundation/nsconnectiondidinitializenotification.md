---
title: NSConnectionDidInitializeNotification
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnectiondidinitializenotification
source_url: 'https://developer.apple.com/documentation/foundation/nsconnectiondidinitializenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnectiondidinitializenotification.json'
content_hash: 'sha256:84337f9d07aacc59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSConnectionDidInitializeNotification

<sub>Global Variable</sub>

Posted when an `NSConnection` object is initialized using [initWithReceivePort:sendPort:](nsconnection/initwithreceiveport_sendport_.md) (the designated initializer for `NSConnection`). The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary.

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSString * const NSConnectionDidInitializeNotification;
```

## Discussion

## See Also

### Related Documentation

- [initWithReceivePort:sendPort:](nsconnection/initwithreceiveport_sendport_.md) — Returns an `NSConnection` object initialized with given send and receive ports. _(deprecated)_

### Notifications

- [NSConnectionDidDieNotification](nsconnectiondiddienotification.md) — Posted when an `NSConnection` object is deallocated or when it’s notified that its `NSPort` object has become invalid. The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary. _(deprecated)_
