---
title: defaultBackgroundConfiguration()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/defaultbackgroundconfiguration()
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/defaultbackgroundconfiguration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/defaultbackgroundconfiguration%28%29.json'
content_hash: 'sha256:d74d9ce2c18be863'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# defaultBackgroundConfiguration()

<sub>Instance Method</sub>

Retrieves a background configuration with system default values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func defaultBackgroundConfiguration() -> UIBackgroundConfiguration
```

## Return Value

A default background configuration. The system determines default values for the configuration according to the section where the cell appears.

## See Also

### Configuring the background

- [backgroundConfiguration](backgroundconfiguration-24e8e.md) — The current background configuration of the cell.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The view to use as the background of the cell.
- [selectedBackgroundView](selectedbackgroundview.md) — The view to use as the background for a selected cell.
- [multipleSelectionBackgroundView](multipleselectionbackgroundview.md) — The background view to use for a selected cell when the table view allows multiple row selections.
