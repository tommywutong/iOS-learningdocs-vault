---
title: NSPreferencePaneCancelUnselectNotification
framework: Preference Panes
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 14.0+, macOS 10.1+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/preferencepanes/nspreferencepanecancelunselectnotification
source_url: 'https://developer.apple.com/documentation/preferencepanes/nspreferencepanecancelunselectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/preferencepanes/nspreferencepanecancelunselectnotification.json'
content_hash: 'sha256:b9947454ff9750d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Preference Panes](../preferencepanes.md)

# NSPreferencePaneCancelUnselectNotification

<sub>Global Variable</sub>

Notifies observers that the preference pane should not be deselected.

<sub>macOS</sub>

```objc
extern NSString * const NSPreferencePaneCancelUnselectNotification;
```

## Discussion

Posted when [- replyToShouldUnselect:](<nspreferencepane/reply(toshouldunselect_).md>) is invoked with an argument of [false](../swift/false.md) after [shouldUnselect](nspreferencepane/shouldunselect.md) has returned a value of [NSUnselectLater](nspreferencepaneunselectreply/unselectlater.md).

## See Also

### Notifications

- [NSPreferencePrefPaneIsAvailableNotification](nspreferenceprefpaneisavailablenotification.md) — Notifies observers that the system preferences app is available to display your preferences.
- [NSPreferencePaneDoUnselectNotification](nspreferencepanedounselectnotification.md) — Notifies observers that the preference pane may be deselected.
- [NSPreferencePaneSwitchToPaneNotification](nspreferencepaneswitchtopanenotification.md) — Notifies observers that the user selected a new preference pane.
- [NSPreferencePaneUpdateHelpMenuNotification](nspreferencepaneupdatehelpmenunotification.md) — Notifies observers that your help menu content changed.
