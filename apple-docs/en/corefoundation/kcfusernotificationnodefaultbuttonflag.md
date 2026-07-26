---
title: kCFUserNotificationNoDefaultButtonFlag
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfusernotificationnodefaultbuttonflag
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfusernotificationnodefaultbuttonflag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfusernotificationnodefaultbuttonflag.json'
content_hash: 'sha256:1695ffcf9fa9d61e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFUserNotificationNoDefaultButtonFlag

<sub>Global Variable</sub>

Displays the dialog without the default, alternate, or other buttons.

<sub>macOS</sub>

```swift
var kCFUserNotificationNoDefaultButtonFlag: CFOptionFlags { get }
```

## Discussion

The dialog remains on screen until it times out or you cancel it with [CFUserNotificationCancel](<cfusernotificationcancel(__).md>). If you provide a title for the default button in the user notification’s description dictionary, this flag is ignored and buttons show up normally.

## See Also

### Constants

- [kCFUserNotificationUseRadioButtonsFlag](kcfusernotificationuseradiobuttonsflag.md) — Creates a group of radio buttons instead of checkboxes for the elements in the [kCFUserNotificationCheckBoxTitlesKey](kcfusernotificationcheckboxtitleskey.md) array in the user notification’s description dictionary.
