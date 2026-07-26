---
title: 'navigationBarNSToolbarSection(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbardelegate/navigationbarnstoolbarsection(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbarnstoolbarsection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbardelegate/navigationbarnstoolbarsection%28_%3A%29.json'
content_hash: 'sha256:f7b66c1fc6dcd251'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarDelegate](../uinavigationbardelegate.md)

# navigationBarNSToolbarSection(_:)

<sub>Instance Method</sub>

Asks the delegate which section of the toolbar to host the navigation bar in.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func navigationBarNSToolbarSection(_ navigationBar: UINavigationBar) -> UINavigationBar.NSToolbarSection
```

## Parameters

- `navigationBar` — The navigation bar to host in an [NSToolbar](../../appkit/nstoolbar.md).

## Return Value

An [NSToolbar](../../appkit/nstoolbar.md) section that determines which section to place the navigation bar in, and how to present the navigation bar in that section. Return [UINavigationBarNSToolbarSectionNone](../uinavigationbar/nstoolbarsection/none.md) to disable [NSToolbar](../../appkit/nstoolbar.md) hosting, which is equivalent to setting [preferredBehavioralStyle](../uinavigationbar/preferredbehavioralstyle.md) to [UIBehavioralStylePad](../uibehavioralstyle/pad.md).

## Discussion

The system calls this method to determine how to render your [UINavigationBar](../uinavigationbar.md) when you build your app with Mac Catalyst.
