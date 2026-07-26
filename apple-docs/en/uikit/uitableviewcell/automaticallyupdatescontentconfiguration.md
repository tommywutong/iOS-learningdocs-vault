---
title: automaticallyUpdatesContentConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/automaticallyupdatescontentconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/automaticallyupdatescontentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/automaticallyupdatescontentconfiguration.json'
content_hash: 'sha256:60ccdb1d4c1bd131'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# automaticallyUpdatesContentConfiguration

<sub>Instance Property</sub>

A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyUpdatesContentConfiguration: Bool { get set }
```

## Discussion

When this value is [true](../../swift/true.md), the cell automatically calls [updated(for:)](<../uicontentconfiguration-9eib5/updated(for_).md>) on its [contentConfiguration](contentconfiguration-9ktox.md) when the cell’s [configurationState](configurationstate-4xwj0.md) changes, and applies the updated configuration back to the cell. The default value is [true](../../swift/true.md).

If you override [updateConfiguration(using:)](<updateconfiguration(using_).md>) to manually update and customize the content configuration, disable automatic updates by setting this property to [false](../../swift/false.md).

## See Also

### Managing the content

- [defaultContentConfiguration()](<defaultcontentconfiguration().md>) — Retrieves a default list content configuration for the cell’s style.
- [contentConfiguration](contentconfiguration-9ktox.md) — The current content configuration of the cell.
- [contentView](contentview.md) — The content view of the cell object.
