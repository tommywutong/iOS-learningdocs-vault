---
title: selectionIsChangingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscombobox/selectionischangingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nscombobox/selectionischangingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscombobox/selectionischangingnotification.json'
content_hash: 'sha256:154e9dd6e9e1991a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSComboBox](../nscombobox.md)

# selectionIsChangingNotification

<sub>Type Property</sub>

Posted whenever the pop-up list selection of the `NSComboBox` is changing.

<sub>macOS</sub>

```swift
class let selectionIsChangingNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSComboBox` whose selection is changing. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [SelectionIsChangingMessage](selectionischangingmessage.md).

## See Also

### Notifications

- [NSComboBoxSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after the pop-up list selection of the `NSComboBox` changes.
- [NSComboBoxWillDismissNotification](willdismissnotification.md) — Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [NSComboBoxWillPopUpNotification](willpopupnotification.md) — Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.
