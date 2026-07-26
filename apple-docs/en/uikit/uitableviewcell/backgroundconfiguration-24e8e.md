---
title: backgroundConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/backgroundconfiguration-24e8e
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/backgroundconfiguration-24e8e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/backgroundconfiguration-24e8e.json'
content_hash: 'sha256:1162d6a7a6b448c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# backgroundConfiguration

<sub>Instance Property</sub>

The current background configuration of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var backgroundConfiguration: UIBackgroundConfiguration? { get set }
```

## Discussion

[UITableViewCell](../uitableviewcell.md) automatically sets up a default background configuration to provide its default appearance.

Using a background configuration, you can obtain system default background styling for a variety of different cell states. Create a background configuration with one of the default system styles, customize the configuration to match your cell’s style as necessary, and assign the configuration to this property.

```swift
var backgroundConfig = UIBackgroundConfiguration.listPlainCell()

// Set a nil background color to use the view's tint color. 
backgroundConfig.backgroundColor = nil 

cell.backgroundConfiguration = backgroundConfig 
```

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets the following APIs to `nil`:

- [backgroundColor](../uiview/backgroundcolor.md)
- [backgroundView](backgroundview.md)
- [selectedBackgroundView](selectedbackgroundview.md)
- [multipleSelectionBackgroundView](multipleselectionbackgroundview.md)

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The view to use as the background of the cell.
- [selectedBackgroundView](selectedbackgroundview.md) — The view to use as the background for a selected cell.
- [multipleSelectionBackgroundView](multipleselectionbackgroundview.md) — The background view to use for a selected cell when the table view allows multiple row selections.
