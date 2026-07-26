---
title: willCloseNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nsdrawer/willclosenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsdrawer/willclosenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsdrawer/willclosenotification.json'
content_hash: 'sha256:b4cd302c8b3ccd99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSDrawer](../nsdrawer.md)

# willCloseNotification

<sub>Type Property</sub>

Posted whenever the drawer is about to close.

> [!warning] Deprecated
> Drawers are deprecated; consider using NSSplitViewController

<sub>macOS</sub>

```swift
class let willCloseNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSDrawer`object about to close. This notification does not contain a `userInfo` dictionary.

## See Also

### Notifications

- [NSDrawerDidCloseNotification](didclosenotification.md) — Posted whenever the drawer is closed. _(deprecated)_
- [NSDrawerDidOpenNotification](didopennotification.md) — Posted whenever the drawer is opened. _(deprecated)_
- [NSDrawerWillOpenNotification](willopennotification.md) — Posted whenever the drawer is about to open. _(deprecated)_
