---
title: contentConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/contentconfiguration-9ktox
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/contentconfiguration-9ktox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/contentconfiguration-9ktox.json'
content_hash: 'sha256:da2d3f89099aa6d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# contentConfiguration

<sub>Instance Property</sub>

The current content configuration of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var contentConfiguration: (any UIContentConfiguration)? { get set }
```

## Discussion

Using a content configuration, you can set the cell’s content and styling for a variety of different cell states. You can get the default configuration using [defaultContentConfiguration()](<defaultcontentconfiguration().md>), assign your content to the configuration, customize any other properties, and assign it to the view as the current [contentConfiguration](contentconfiguration-9ktox.md).

Setting a content configuration replaces the existing [contentView](contentview.md) of the cell with a new content view instance from the configuration, or directly applies the configuration to the existing content view if the configuration is compatible with the existing content view type.

The default value is `nil`. After you set a content configuration to this property, setting this property back to `nil` replaces the current content view with a new, empty content view.

## See Also

### Managing the content

- [defaultContentConfiguration()](<defaultcontentconfiguration().md>) — Retrieves a default list content configuration for the cell’s style.
- [automaticallyUpdatesContentConfiguration](automaticallyupdatescontentconfiguration.md) — A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.
- [contentView](contentview.md) — The content view of the cell object.
