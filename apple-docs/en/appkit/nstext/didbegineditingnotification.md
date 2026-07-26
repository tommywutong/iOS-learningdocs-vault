---
title: didBeginEditingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstext/didbegineditingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstext/didbegineditingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstext/didbegineditingnotification.json'
content_hash: 'sha256:30788935e6e86b8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSText](../nstext.md)

# didBeginEditingNotification

<sub>Type Property</sub>

Posted when an `NSText` object begins any operation that changes characters or formatting attributes.

<sub>macOS</sub>

```swift
class let didBeginEditingNotification: NSNotification.Name
```

## Discussion

The notification object is the notifying `NSText` object. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [DidBeginEditingMessage](../nstextview/didbegineditingmessage.md).

## See Also

### Notifications

- [NSTextDidChangeNotification](didchangenotification.md) — Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [NSTextDidEndEditingNotification](didendeditingnotification.md) — Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.
- [NSTextMovementUserInfoKey](movementuserinfokey.md) — The `userInfo` dictionary key for the [NSTextDidEndEditingNotification](didendeditingnotification.md) notification.
- [NSTextMovement](../nstextmovement.md)
