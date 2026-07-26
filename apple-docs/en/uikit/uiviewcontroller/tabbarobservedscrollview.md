---
title: tabBarObservedScrollView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 13.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/tabbarobservedscrollview
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/tabbarobservedscrollview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/tabbarobservedscrollview.json'
content_hash: 'sha256:704e6e5646645f12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# tabBarObservedScrollView

<sub>Instance Property</sub>

The full-screen scroll view to synchronize with a scrolling tab bar.

> [!warning] Deprecated
> Use [- setContentScrollView:forEdge:](<setcontentscrollview(__for_).md>) instead.

<sub>tvOS</sub>

```swift
var tabBarObservedScrollView: UIScrollView? { get set }
```

## Discussion

Typically, the position of the tab bar remains fixed while content scrolls underneath it. Use this property in your tvOS apps to create an interface where the tab bar scrolls with the rest of your content. When you set the value of this property to a scroll view, UIKit synchronizes the position of the tab bar with the current scroll position of that scroll view. The default value of this property is `nil`.

## See Also

### Configuring tab bar content

- [tab](tab.md) — The `UITab` instance that was used to create the receiver, and represents the view controller. Default is nil.
- [tabBarItem](tabbaritem.md) — The tab bar item that represents the view controller when added to a tab bar controller.
