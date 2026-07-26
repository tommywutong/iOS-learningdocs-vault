---
title: UISplitViewController.Style.unspecified
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisplitviewcontroller/style-swift.enum/unspecified
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/style-swift.enum/unspecified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/style-swift.enum/unspecified.json'
content_hash: 'sha256:d30bb1ffb411739c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [Style](../style-swift.enum.md)

# UISplitViewController.Style.unspecified

<sub>Case</sub>

The split view interface uses the classic split view style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case unspecified
```

## Discussion

A split view controller with this style represents a classic split view controller created using any other approach than [- initWithStyle:](<../init(style_).md>). You cannot create a split view controller with a style of [UISplitViewControllerStyleUnspecified](unspecified.md) using this initializer.

Split view controllers with this style don’t support any column-style APIs, such as [- setViewController:forColumn:](<../setviewcontroller(__for_).md>).

## See Also

### Constants

- [UISplitViewControllerStyleDoubleColumn](doublecolumn.md) — The split view interface displays two columns.
- [UISplitViewControllerStyleTripleColumn](triplecolumn.md) — The split view interface displays three columns.
