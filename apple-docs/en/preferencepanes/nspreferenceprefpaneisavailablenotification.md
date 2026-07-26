---
title: NSPreferencePrefPaneIsAvailableNotification
framework: Preference Panes
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 14.0+, macOS 10.1+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/preferencepanes/nspreferenceprefpaneisavailablenotification
source_url: 'https://developer.apple.com/documentation/preferencepanes/nspreferenceprefpaneisavailablenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/preferencepanes/nspreferenceprefpaneisavailablenotification.json'
content_hash: 'sha256:ff1a5c0e84243468'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Preference Panes](../preferencepanes.md)

# NSPreferencePrefPaneIsAvailableNotification

<sub>Global Variable</sub>

Notifies observers that the system preferences app is available to display your preferences.

<sub>macOS</sub>

```objc
extern NSString * const NSPreferencePrefPaneIsAvailableNotification;
```

## See Also

### Notifications

- [NSPreferencePaneDoUnselectNotification](nspreferencepanedounselectnotification.md) — Notifies observers that the preference pane may be deselected.
- [NSPreferencePaneCancelUnselectNotification](nspreferencepanecancelunselectnotification.md) — Notifies observers that the preference pane should not be deselected.
- [NSPreferencePaneSwitchToPaneNotification](nspreferencepaneswitchtopanenotification.md) — Notifies observers that the user selected a new preference pane.
- [NSPreferencePaneUpdateHelpMenuNotification](nspreferencepaneupdatehelpmenunotification.md) — Notifies observers that your help menu content changed.
