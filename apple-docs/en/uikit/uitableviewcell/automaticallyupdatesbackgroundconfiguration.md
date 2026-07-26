---
title: automaticallyUpdatesBackgroundConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/automaticallyupdatesbackgroundconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/automaticallyupdatesbackgroundconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/automaticallyupdatesbackgroundconfiguration.json'
content_hash: 'sha256:66b9d834d0d83c84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# automaticallyUpdatesBackgroundConfiguration

<sub>Instance Property</sub>

A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyUpdatesBackgroundConfiguration: Bool { get set }
```

## Discussion

When this value is [true](../../swift/true.md), the cell automatically calls `updated(for:)` on its [backgroundConfiguration](backgroundconfiguration-24e8e.md) when the cell’s [configurationState](configurationstate-4xwj0.md) changes, and applies the updated configuration back to the cell. The default value is [true](../../swift/true.md).

If you override [updateConfiguration(using:)](<updateconfiguration(using_).md>) to manually update and customize the background configuration, disable automatic updates by setting this property to [false](../../swift/false.md).

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](backgroundconfiguration-24e8e.md) — The current background configuration of the cell.
- [backgroundView](backgroundview.md) — The view to use as the background of the cell.
- [selectedBackgroundView](selectedbackgroundview.md) — The view to use as the background for a selected cell.
- [multipleSelectionBackgroundView](multipleselectionbackgroundview.md) — The background view to use for a selected cell when the table view allows multiple row selections.
