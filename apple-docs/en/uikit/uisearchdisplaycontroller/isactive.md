---
title: isActive
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisearchdisplaycontroller/isactive
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/isactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaycontroller/isactive.json'
content_hash: 'sha256:d898aeffd346d251'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayController](../uisearchdisplaycontroller.md)

# isActive

<sub>Instance Property</sub>

The visibility state of the search interface.

> [!warning] Deprecated
> For more information, see [UISearchDisplayController](../uisearchdisplaycontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isActive: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

If you set this value directly, any change is performed without animation. Use [- setActive:animated:](<setactive(__animated_).md>) if a change in state should be animated.

When the user focus in the search field of a managed search bar, the search display controller automatically displays the search interface. You can use this property to force the search interface to appear.

## See Also

### Displaying the search Interface

- [- setActive:animated:](<setactive(__animated_).md>) — Displays or hides the search interface, optionally with animation. _(deprecated)_
