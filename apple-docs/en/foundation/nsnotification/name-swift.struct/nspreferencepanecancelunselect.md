---
title: NSPreferencePaneCancelUnselect
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nspreferencepanecancelunselect
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferencepanecancelunselect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nspreferencepanecancelunselect.json'
content_hash: 'sha256:72b20df6090db1c9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSPreferencePaneCancelUnselect

<sub>Type Property</sub>

Notifies observers that the preference pane should not be deselected.

<sub>macOS</sub>

```swift
static let NSPreferencePaneCancelUnselect: NSNotification.Name
```

## Discussion

Posted when [reply(toShouldUnselect:)](<../../../preferencepanes/nspreferencepane/reply(toshouldunselect_).md>) is invoked with an argument of [false](../../../swift/false.md) after [shouldUnselect](../../../preferencepanes/nspreferencepane/shouldunselect.md) has returned a value of [NSPreferencePaneUnselectReply.unselectLater](../../../preferencepanes/nspreferencepaneunselectreply/unselectlater.md).

## See Also

### PreferencePanes

- [NSPreferencePaneDoUnselect](nspreferencepanedounselect.md) — Notifies observers that the preference pane may be deselected.
- [NSPreferencePaneSwitchToPane](nspreferencepaneswitchtopane.md) — Notifies observers that the user selected a new preference pane.
- [NSPreferencePaneUpdateHelpMenu](nspreferencepaneupdatehelpmenu.md) — Notifies observers that your help menu content changed.
- [NSPreferencePrefPaneIsAvailable](nspreferenceprefpaneisavailable.md) — Notifies observers that the system preferences app is available to display your preferences.
