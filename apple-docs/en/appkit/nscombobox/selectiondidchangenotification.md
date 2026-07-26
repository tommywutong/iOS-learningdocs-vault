---
title: selectionDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscombobox/selectiondidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nscombobox/selectiondidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscombobox/selectiondidchangenotification.json'
content_hash: 'sha256:5994628c41233da0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSComboBox](../nscombobox.md)

# selectionDidChangeNotification

<sub>Type Property</sub>

Posted after the pop-up list selection of the `NSComboBox` changes.

<sub>macOS</sub>

```swift
class let selectionDidChangeNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSComboBox` whose selection changed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [SelectionDidChangeMessage](selectiondidchangemessage.md).

## See Also

### Notifications

- [NSComboBoxSelectionIsChangingNotification](selectionischangingnotification.md) — Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [NSComboBoxWillDismissNotification](willdismissnotification.md) — Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [NSComboBoxWillPopUpNotification](willpopupnotification.md) — Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.
