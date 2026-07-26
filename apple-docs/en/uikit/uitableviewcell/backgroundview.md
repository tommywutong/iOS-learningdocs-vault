---
title: backgroundView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/backgroundview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/backgroundview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/backgroundview.json'
content_hash: 'sha256:8b6bd8fe8372476c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# backgroundView

<sub>Instance Property</sub>

The view to use as the background of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundView: UIView? { get set }
```

## Discussion

[UITableViewCell](../uitableviewcell.md) adds the background view as a subview behind all other views and uses its current frame location.

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets [backgroundConfiguration](backgroundconfiguration-24e8e.md) to `nil`.

## See Also

### Related Documentation

- [contentView](contentview.md) — The content view of the cell object.

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](backgroundconfiguration-24e8e.md) — The current background configuration of the cell.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [selectedBackgroundView](selectedbackgroundview.md) — The view to use as the background for a selected cell.
- [multipleSelectionBackgroundView](multipleselectionbackgroundview.md) — The background view to use for a selected cell when the table view allows multiple row selections.
