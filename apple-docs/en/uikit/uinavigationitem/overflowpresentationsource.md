---
title: overflowPresentationSource
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/overflowpresentationsource
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/overflowpresentationsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/overflowpresentationsource.json'
content_hash: 'sha256:583d44f1483fbc7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# overflowPresentationSource

<sub>Instance Property</sub>

The item you can use as an anchor to present a custom UI from the overflow menu button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var overflowPresentationSource: (any UIPopoverPresentationControllerSourceItem)? { get }
```

## Discussion

If the overflow menu button for the navigation item is visible, this property returns a non-`nil` item that you can use as a presentation source — for example, to present a custom popover that anchors to the overflow menu button. Otherwise, this property returns `nil`.

## See Also

### Working with the overflow menu

- [additionalOverflowItems](additionaloverflowitems.md) — Additional items to present in the overflow menu.
