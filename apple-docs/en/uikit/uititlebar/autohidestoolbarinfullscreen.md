---
title: autoHidesToolbarInFullScreen
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uititlebar/autohidestoolbarinfullscreen
source_url: 'https://developer.apple.com/documentation/uikit/uititlebar/autohidestoolbarinfullscreen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uititlebar/autohidestoolbarinfullscreen.json'
content_hash: 'sha256:11a89d5710a0c026'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITitlebar](../uititlebar.md)

# autoHidesToolbarInFullScreen

<sub>Instance Property</sub>

A Boolean value that determines whether the toolbar automatically hides in full-screen windows.

<sub>Mac Catalyst</sub>

```swift
var autoHidesToolbarInFullScreen: Bool { get set }
```

## Discussion

Set this property to [true](../../swift/true.md) to automatically hide the toolbar when the window enters full-screen mode. While hidden, the user can view the toolbar and menu bar by moving the pointer to the top of the screen. Moving the pointer away from the top of the screen hides the toolbar and menu bar.

The default value is [false](../../swift/false.md).

## See Also

### Configuring the toolbar

- [toolbar](toolbar.md) — The toolbar displayed beneath or integrated with the title bar.
- [toolbarStyle](toolbarstyle.md) — The style of the toolbar determining its appearance and location related to the title bar.
- [UITitlebarToolbarStyle](../uititlebartoolbarstyle.md) — Styles that determine the toolbar’s appearance and location related to the title bar.
