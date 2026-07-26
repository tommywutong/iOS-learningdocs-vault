---
title: NSPreferencePaneUpdateHelpMenu
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nspreferencepaneupdatehelpmenu
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferencepaneupdatehelpmenu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nspreferencepaneupdatehelpmenu.json'
content_hash: 'sha256:b68588597a1285e4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSPreferencePaneUpdateHelpMenu

<sub>Type Property</sub>

Notifies observers that your help menu content changed.

<sub>macOS</sub>

```swift
static let NSPreferencePaneUpdateHelpMenu: NSNotification.Name
```

## Discussion

The object of the notification is an array of dictionaries containing the new help menu contents.

## See Also

### PreferencePanes

- [NSPreferencePaneCancelUnselect](nspreferencepanecancelunselect.md) — Notifies observers that the preference pane should not be deselected.
- [NSPreferencePaneDoUnselect](nspreferencepanedounselect.md) — Notifies observers that the preference pane may be deselected.
- [NSPreferencePaneSwitchToPane](nspreferencepaneswitchtopane.md) — Notifies observers that the user selected a new preference pane.
- [NSPreferencePrefPaneIsAvailable](nspreferenceprefpaneisavailable.md) — Notifies observers that the system preferences app is available to display your preferences.
