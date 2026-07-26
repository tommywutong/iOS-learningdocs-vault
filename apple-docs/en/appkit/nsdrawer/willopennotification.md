---
title: willOpenNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nsdrawer/willopennotification
source_url: 'https://developer.apple.com/documentation/appkit/nsdrawer/willopennotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsdrawer/willopennotification.json'
content_hash: 'sha256:39660d0e1bda9ee5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSDrawer](../nsdrawer.md)

# willOpenNotification

<sub>Type Property</sub>

Posted whenever the drawer is about to open.

> [!warning] Deprecated
> Drawers are deprecated; consider using NSSplitViewController

<sub>macOS</sub>

```swift
class let willOpenNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSDrawer` object about to open. This notification does not contain a `userInfo` dictionary.

## See Also

### Notifications

- [NSDrawerDidCloseNotification](didclosenotification.md) — Posted whenever the drawer is closed. _(deprecated)_
- [NSDrawerDidOpenNotification](didopennotification.md) — Posted whenever the drawer is opened. _(deprecated)_
- [NSDrawerWillCloseNotification](willclosenotification.md) — Posted whenever the drawer is about to close. _(deprecated)_
