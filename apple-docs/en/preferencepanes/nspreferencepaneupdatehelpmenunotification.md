---
title: NSPreferencePaneUpdateHelpMenuNotification
framework: Preference Panes
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 14.0+, macOS 10.1+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/preferencepanes/nspreferencepaneupdatehelpmenunotification
source_url: 'https://developer.apple.com/documentation/preferencepanes/nspreferencepaneupdatehelpmenunotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/preferencepanes/nspreferencepaneupdatehelpmenunotification.json'
content_hash: 'sha256:4afb5662af11651e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Preference Panes](../preferencepanes.md)

# NSPreferencePaneUpdateHelpMenuNotification

<sub>Global Variable</sub>

Notifies observers that your help menu content changed.

<sub>macOS</sub>

```objc
extern NSString * const NSPreferencePaneUpdateHelpMenuNotification;
```

## Discussion

The object of the notification is an array of dictionaries containing the new help menu contents.

## See Also

### Notifications

- [NSPreferencePrefPaneIsAvailableNotification](nspreferenceprefpaneisavailablenotification.md) — Notifies observers that the system preferences app is available to display your preferences.
- [NSPreferencePaneDoUnselectNotification](nspreferencepanedounselectnotification.md) — Notifies observers that the preference pane may be deselected.
- [NSPreferencePaneCancelUnselectNotification](nspreferencepanecancelunselectnotification.md) — Notifies observers that the preference pane should not be deselected.
- [NSPreferencePaneSwitchToPaneNotification](nspreferencepaneswitchtopanenotification.md) — Notifies observers that the user selected a new preference pane.
