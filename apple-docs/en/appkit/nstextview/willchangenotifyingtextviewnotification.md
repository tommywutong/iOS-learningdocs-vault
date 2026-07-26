---
title: willChangeNotifyingTextViewNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextview/willchangenotifyingtextviewnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstextview/willchangenotifyingtextviewnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextview/willchangenotifyingtextviewnotification.json'
content_hash: 'sha256:f8a5b7fe1d48d4a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextView](../nstextview.md)

# willChangeNotifyingTextViewNotification

<sub>Type Property</sub>

Posted when a new text view is established as the text view that sends notifications.

<sub>macOS</sub>

```swift
class let willChangeNotifyingTextViewNotification: NSNotification.Name
```

## Discussion

This notification allows observers to reregister themselves for the new text view. Methods such as [- removeTextContainerAtIndex:](<../nslayoutmanager/removetextcontainer(at_).md>), [- textContainerChangedTextView:](<../nslayoutmanager/textcontainerchangedtextview(__).md>), and [- insertTextContainer:atIndex:](<../nslayoutmanager/inserttextcontainer(__at_).md>) cause this notification to be posted.

The notification object is the old notifying text view, or `nil`. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `@"NSOldNotifyingTextView"` | The old `NSTextView`, if one exists, otherwise `nil`. |
| `@"NSNewNotifyingTextView"` | The new `NSTextView`, if one exists, otherwise `nil`. |

There’s no delegate method associated with this notification. The text-handling system ensures that when a new text view replaces an old one as the notifying text view, the existing delegate becomes the delegate of the new text view, and the delegate is registered to receive text view notifications from the new notifying text view. All other observers are responsible for registering themselves on receiving this notification.

## See Also

### Related Documentation

- [removeObserver(_:)](<../../foundation/notificationcenter/removeobserver(__)-2yciv.md>) — Removes all entries specifying an observer from the notification center’s dispatch table.
- [addObserver(_:selector:name:object:)](<../../foundation/notificationcenter/addobserver(__selector_name_object_).md>) — Adds an entry to the notification center to call the provided selector with the notification.

### Notifications

- [NSTextViewDidChangeSelectionNotification](didchangeselectionnotification.md) — Posted when the selected range of characters changes.
- [NSTextViewDidChangeTypingAttributesNotification](didchangetypingattributesnotification.md) — Posted when there is a change in the typing attributes within a text view.
- [NSTextViewDidSwitchToNSLayoutManagerNotification](didswitchtonslayoutmanagernotification.md) — Posted by the framework after switching to using the compatibility mode layout manager.
- [NSTextViewWillSwitchToNSLayoutManagerNotification](willswitchtonslayoutmanagernotification.md) — Posted by the framework before switching to the compatibility mode layout manager.
