---
title: 'setActive(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisearchdisplaycontroller/setactive(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/setactive(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaycontroller/setactive%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:9ed3864ad072d482'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayController](../uisearchdisplaycontroller.md)

# setActive(_:animated:)

<sub>Instance Method</sub>

Displays or hides the search interface, optionally with animation.

> [!warning] Deprecated
> UISearchDisplayController has been replaced with UISearchController

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setActive(_ visible: Bool, animated: Bool)
```

## Parameters

- `visible` — [true](../../swift/true.md) to display the search interface if it is not already displayed; [false](../../swift/false.md) to hide the search interface if it is currently displayed.

- `animated` — [true](../../swift/true.md) to use animation for a change in visible state, otherwise [false](../../swift/false.md).

## Discussion

When the user focus in the search field of a managed search bar, the search display controller automatically displays the search interface. You can use this method to force the search interface to appear.

## See Also

### Displaying the search Interface

- [active](isactive.md) — The visibility state of the search interface. _(deprecated)_
