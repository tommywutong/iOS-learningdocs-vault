---
title: primaryOverlay
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, tvOS（14.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/primaryoverlay
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/primaryoverlay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/primaryoverlay.json'
content_hash: 'sha256:eef0bcfd5740e38c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [DisplayMode](../displaymode-swift.enum.md)

# primaryOverlay

<sub>Type Property</sub>

The primary view controller is layered on top of the secondary view controller, leaving the secondary view controller partially visible.

> [!warning] Deprecated
> Use [UISplitViewControllerDisplayModeOneOverSecondary](oneoversecondary.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static var primaryOverlay: UISplitViewController.DisplayMode { get }
```

## See Also

### Deprecated

- [UISplitViewControllerDisplayModePrimaryHidden](primaryhidden.md) — The primary view controller is hidden. _(deprecated)_
- [UISplitViewControllerDisplayModeAllVisible](allvisible.md) — The primary and secondary view controllers are displayed side-by-side onscreen. _(deprecated)_
