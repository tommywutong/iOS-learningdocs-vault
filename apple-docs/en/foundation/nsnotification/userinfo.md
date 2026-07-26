---
title: userInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/userinfo.json'
content_hash: 'sha256:b3e8c5c5efcf5a40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNotification](../nsnotification.md)

# userInfo

<sub>Instance Property</sub>

The user information dictionary associated with the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any]? { get }
```

## Discussion

In Objective-C, this may be `nil`.

The user information dictionary stores any additional objects that objects receiving the notification might use.

For example, in AppKit, [NSControl](../../appkit/nscontrol.md) objects post the [textDidChangeNotification](../../appkit/nscontrol/textdidchangenotification.md) whenever the field editor (an [NSText](../../appkit/nstext.md) object) changes text inside the `NSControl`. This notification provides the `NSControl` object as the notification’s associated object. In order to provide access to the field editor, the `NSControl` object posting the notification adds the field editor to the notification’s user information dictionary. Objects receiving the notification can access the field editor and the `NSControl` object posting the notification as follows:

```swift
func controlTextDidChange(_ notification: Notification) {
    if let fieldEditor = notification.userInfo?["NSFieldEditor"] as? NSText,
        let postingObject = notification.object as? NSControl {
        // work with the field editor and posting object
    }
}
```

## See Also

### Getting Notification Information

- [name](name-swift.property.md) — The name of the notification.
- [object](object.md) — The object associated with the notification.
