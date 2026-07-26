---
title: didOpenNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nsdrawer/didopennotification
source_url: 'https://developer.apple.com/documentation/appkit/nsdrawer/didopennotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsdrawer/didopennotification.json'
content_hash: 'sha256:50d37dfd136cfba0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSDrawer](../nsdrawer.md)

# didOpenNotification

<sub>Type Property</sub>

Posted whenever the drawer is opened.

> [!warning] Deprecated
> Drawers are deprecated; consider using NSSplitViewController

<sub>macOS</sub>

```swift
class let didOpenNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSDrawer` object that opened. This notification does not contain a `userInfo` dictionary.

## See Also

### Notifications

- [NSDrawerDidCloseNotification](didclosenotification.md) — Posted whenever the drawer is closed. _(deprecated)_
- [NSDrawerWillCloseNotification](willclosenotification.md) — Posted whenever the drawer is about to close. _(deprecated)_
- [NSDrawerWillOpenNotification](willopennotification.md) — Posted whenever the drawer is about to open. _(deprecated)_
