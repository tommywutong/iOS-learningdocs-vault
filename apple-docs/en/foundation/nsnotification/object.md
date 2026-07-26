---
title: object
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/object
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/object'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/object.json'
content_hash: 'sha256:0ac2a7664769ef8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNotification](../nsnotification.md)

# object

<sub>Instance Property</sub>

The object associated with the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var object: Any? { get }
```

## Discussion

This is often the object that posted this notification. In Objective-C, it may be `nil`.

Typically you use this method to find out what object a notification applies to when you receive a notification.

For example, suppose you’ve registered an object to receive the message `handlePortDeath:` when the `PortInvalid` notification is posted to the notification center and that `handlePortDeath:` needs to access the object monitoring the port that is now invalid. `handlePortDeath:` can retrieve that object as shown here:

Example of accessing notification object in Objective-C:

```objc
- (void)handlePortDeath:(NSNotification *)notification
{
    ...
    [self reclaimResourcesForPort:notification.object];
    ...
}
```

## See Also

### Getting Notification Information

- [name](name-swift.property.md) — The name of the notification.
- [userInfo](userinfo.md) — The user information dictionary associated with the notification.
