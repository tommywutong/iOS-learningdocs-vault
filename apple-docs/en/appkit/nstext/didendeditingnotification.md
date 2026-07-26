---
title: didEndEditingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstext/didendeditingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstext/didendeditingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstext/didendeditingnotification.json'
content_hash: 'sha256:6e22ea974e28ac9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSText](../nstext.md)

# didEndEditingNotification

<sub>Type Property</sub>

Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.

<sub>macOS</sub>

```swift
class let didEndEditingNotification: NSNotification.Name
```

## Discussion

The notification object is the notifying `NSText` object. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| [NSTextMovementUserInfoKey](movementuserinfokey.md) | One of the values in [NSTextMovement](../nstextmovement.md). |

| Key | Value |
|---|---|
| `@"NSTextMovement"` | Possible movement code values are described in [Movement Codes](../movement-codes.md). |

> [!note] Note
> It is common for [NSTextDidEndEditingNotification](didendeditingnotification.md) to be sent without a matching [NSTextDidBeginEditingNotification](didbegineditingnotification.md). The begin notification is only sent if the user actually makes changes (that is, types something or changes formatting attributes). However, the end notification is sent when focus leaves the text view, regardless of whether there was a change.
>
> This distinction enables an application to know whether the user actually made a change to the text or just clicked in the text view and then clicked outside it. In both cases, [NSTextDidEndEditingNotification](didendeditingnotification.md) is sent, but to tell the difference, the application can listen for [NSTextDidBeginEditingNotification](didbegineditingnotification.md).

To observe this notification using Swift concurrency, use [DidEndEditingMessage](../nstextview/didendeditingmessage.md).

## See Also

### Notifications

- [NSTextDidBeginEditingNotification](didbegineditingnotification.md) — Posted when an `NSText` object begins any operation that changes characters or formatting attributes.
- [NSTextDidChangeNotification](didchangenotification.md) — Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [NSTextMovementUserInfoKey](movementuserinfokey.md) — The `userInfo` dictionary key for the [NSTextDidEndEditingNotification](didendeditingnotification.md) notification.
- [NSTextMovement](../nstextmovement.md)
