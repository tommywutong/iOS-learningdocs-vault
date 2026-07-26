---
title: willDismissNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscombobox/willdismissnotification
source_url: 'https://developer.apple.com/documentation/appkit/nscombobox/willdismissnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscombobox/willdismissnotification.json'
content_hash: 'sha256:1e88d587fb912ef2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSComboBox](../nscombobox.md)

# willDismissNotification

<sub>Type Property</sub>

Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.

<sub>macOS</sub>

```swift
class let willDismissNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSComboBox` whose pop-up list will be dismissed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [WillDismissMessage](willdismissmessage.md).

## See Also

### Notifications

- [NSComboBoxSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after the pop-up list selection of the `NSComboBox` changes.
- [NSComboBoxSelectionIsChangingNotification](selectionischangingnotification.md) — Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [NSComboBoxWillPopUpNotification](willpopupnotification.md) — Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.
