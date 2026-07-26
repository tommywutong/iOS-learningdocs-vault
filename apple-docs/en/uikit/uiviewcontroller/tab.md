---
title: tab
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/tab
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/tab'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/tab.json'
content_hash: 'sha256:8eecff994cacbb22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# tab

<sub>Instance Property</sub>

The `UITab` instance that was used to create the receiver, and represents the view controller. Default is nil.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var tab: UITab? { get }
```

## See Also

### Configuring tab bar content

- [tabBarItem](tabbaritem.md) — The tab bar item that represents the view controller when added to a tab bar controller.
- [tabBarObservedScrollView](tabbarobservedscrollview.md) — The full-screen scroll view to synchronize with a scrolling tab bar. _(deprecated)_
