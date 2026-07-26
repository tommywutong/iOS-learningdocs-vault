---
title: didCloseNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nsdrawer/didclosenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsdrawer/didclosenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsdrawer/didclosenotification.json'
content_hash: 'sha256:cf171adeb45017b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSDrawer](../nsdrawer.md)

# didCloseNotification

<sub>Type Property</sub>

Posted whenever the drawer is closed.

> [!warning] Deprecated
> Drawers are deprecated; consider using NSSplitViewController

<sub>macOS</sub>

```swift
class let didCloseNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSDrawer` object that closed. This notification does not contain a `userInfo` dictionary.

## See Also

### Notifications

- [NSDrawerDidOpenNotification](didopennotification.md) — Posted whenever the drawer is opened. _(deprecated)_
- [NSDrawerWillCloseNotification](willclosenotification.md) — Posted whenever the drawer is about to close. _(deprecated)_
- [NSDrawerWillOpenNotification](willopennotification.md) — Posted whenever the drawer is about to open. _(deprecated)_
