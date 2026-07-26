---
title: willPopUpNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscombobox/willpopupnotification
source_url: 'https://developer.apple.com/documentation/appkit/nscombobox/willpopupnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscombobox/willpopupnotification.json'
content_hash: 'sha256:12bc96fa1b214d47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSComboBox](../nscombobox.md)

# willPopUpNotification

<sub>Type Property</sub>

Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.

<sub>macOS</sub>

```swift
class let willPopUpNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSComboBox` whose pop-up window will be displayed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [WillPopUpMessage](willpopupmessage.md).

## See Also

### Notifications

- [NSComboBoxSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after the pop-up list selection of the `NSComboBox` changes.
- [NSComboBoxSelectionIsChangingNotification](selectionischangingnotification.md) — Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [NSComboBoxWillDismissNotification](willdismissnotification.md) — Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
