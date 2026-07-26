---
title: preferredFocusEnvironments
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusguide/preferredfocusenvironments
source_url: 'https://developer.apple.com/documentation/uikit/uifocusguide/preferredfocusenvironments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusguide/preferredfocusenvironments.json'
content_hash: 'sha256:ebf8c1ba47449452'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusGuide](../uifocusguide.md)

# preferredFocusEnvironments

<sub>Instance Property</sub>

An array of focus environments to which the guide directs focus, ordered by priority.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredFocusEnvironments: [any UIFocusEnvironment]! { get set }
```

## Discussion

Setting this property to a nonempty array marks this guide’s [layoutFrame](../uilayoutguide/layoutframe.md) as focusable. If empty, this guide is effectively disabled.

If focused, the guide attempts to redirect focus to each environment in the array, in order, stopping when a focusable item in an environment has been found.

## See Also

### Enabling focus

- [enabled](isenabled.md) — A Boolean value that indicates whether the guide is focusable.
- [preferredFocusedView](preferredfocusedview.md) — The view that the focus will be redirected to if this guide is focused. _(deprecated)_
