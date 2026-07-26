---
title: multipleSelectionBackgroundView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/multipleselectionbackgroundview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/multipleselectionbackgroundview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/multipleselectionbackgroundview.json'
content_hash: 'sha256:79e7580411b548cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# multipleSelectionBackgroundView

<sub>Instance Property</sub>

The background view to use for a selected cell when the table view allows multiple row selections.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var multipleSelectionBackgroundView: UIView? { get set }
```

## Discussion

If this property isn’t `nil`, this view becomes the background view for a selected cell when the table view allows multiple row selections. You enable multiple row selections through the [allowsMultipleSelection](../uitableview/allowsmultipleselection.md) and [allowsMultipleSelectionDuringEditing](../uitableview/allowsmultipleselectionduringediting.md) properties of [UITableView](../uitableview.md).

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets [backgroundConfiguration](backgroundconfiguration-24e8e.md) to `nil`.

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](backgroundconfiguration-24e8e.md) — The current background configuration of the cell.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The view to use as the background of the cell.
- [selectedBackgroundView](selectedbackgroundview.md) — The view to use as the background for a selected cell.
