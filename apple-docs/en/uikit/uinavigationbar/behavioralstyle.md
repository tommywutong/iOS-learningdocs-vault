---
title: behavioralStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/behavioralstyle
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/behavioralstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/behavioralstyle.json'
content_hash: 'sha256:6e04b68dbe60b3f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# behavioralStyle

<sub>Instance Property</sub>

The behavioral style of the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var behavioralStyle: UIBehavioralStyle { get }
```

## Discussion

Use this property to determine the actual behavior style when the [preferredBehavioralStyle](preferredbehavioralstyle.md) is [UIBehavioralStyleAutomatic](../uibehavioralstyle/automatic.md).

When the value of this property is [UIBehavioralStyleMac](../uibehavioralstyle/mac.md), [NSToolbar](../../appkit/nstoolbar.md) hosts the navigation bar’s content when you build your app with Mac Catalyst.

## See Also

### Building with Mac Catalyst

- [preferredBehavioralStyle](preferredbehavioralstyle.md) — The preferred behavioral style of the navigation bar.
- [currentNSToolbarSection](currentnstoolbarsection.md) — The toolbar section that the navigation bar is currently using.
- [NSToolbarSection](nstoolbarsection.md) — Constants that determine how the system hosts the navigation bar in an AppKit toolbar.
