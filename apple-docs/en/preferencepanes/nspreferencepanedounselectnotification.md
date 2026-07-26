---
title: NSPreferencePaneDoUnselectNotification
framework: Preference Panes
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 14.0+, macOS 10.1+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/preferencepanes/nspreferencepanedounselectnotification
source_url: 'https://developer.apple.com/documentation/preferencepanes/nspreferencepanedounselectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/preferencepanes/nspreferencepanedounselectnotification.json'
content_hash: 'sha256:a87090e1e4172ef9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Preference Panes](../preferencepanes.md)

# NSPreferencePaneDoUnselectNotification

<sub>Global Variable</sub>

Notifies observers that the preference pane may be deselected.

<sub>macOS</sub>

```objc
extern NSString * const NSPreferencePaneDoUnselectNotification;
```

## Discussion

Posted when [- replyToShouldUnselect:](<nspreferencepane/reply(toshouldunselect_).md>) is invoked with an argument of [true](../swift/true.md) after [shouldUnselect](nspreferencepane/shouldunselect.md) has returned a value of [NSUnselectLater](nspreferencepaneunselectreply/unselectlater.md).

## See Also

### Notifications

- [NSPreferencePrefPaneIsAvailableNotification](nspreferenceprefpaneisavailablenotification.md) — Notifies observers that the system preferences app is available to display your preferences.
- [NSPreferencePaneCancelUnselectNotification](nspreferencepanecancelunselectnotification.md) — Notifies observers that the preference pane should not be deselected.
- [NSPreferencePaneSwitchToPaneNotification](nspreferencepaneswitchtopanenotification.md) — Notifies observers that the user selected a new preference pane.
- [NSPreferencePaneUpdateHelpMenuNotification](nspreferencepaneupdatehelpmenunotification.md) — Notifies observers that your help menu content changed.
