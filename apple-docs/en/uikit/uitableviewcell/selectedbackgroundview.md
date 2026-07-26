---
title: selectedBackgroundView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/selectedbackgroundview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/selectedbackgroundview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/selectedbackgroundview.json'
content_hash: 'sha256:aed66299c0eb7af6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# selectedBackgroundView

<sub>Instance Property</sub>

The view to use as the background for a selected cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectedBackgroundView: UIView? { get set }
```

## Discussion

[UITableViewCell](../uitableviewcell.md) adds the value of this property as a subview only when the cell has a selected state. It adds the selected background view as a subview directly above the background view ([backgroundView](backgroundview.md)) if it isn’t `nil`, or behind all other views. Calling [- setSelected:animated:](<setselected(__animated_).md>) causes the selected background view to animate in and out with an alpha fade.

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets [backgroundConfiguration](backgroundconfiguration-24e8e.md) to `nil`.

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](backgroundconfiguration-24e8e.md) — The current background configuration of the cell.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The view to use as the background of the cell.
- [multipleSelectionBackgroundView](multipleselectionbackgroundview.md) — The background view to use for a selected cell when the table view allows multiple row selections.
