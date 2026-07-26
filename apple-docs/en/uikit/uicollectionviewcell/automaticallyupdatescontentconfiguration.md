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
doc_path: /documentation/uikit/uicollectionviewcell/automaticallyupdatescontentconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/automaticallyupdatescontentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/automaticallyupdatescontentconfiguration.json'
content_hash: 'sha256:ef158bd67f510ca5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# automaticallyUpdatesContentConfiguration

<sub>Instance Property</sub>

A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyUpdatesContentConfiguration: Bool { get set }
```

## Discussion

When this value is [true](../../swift/true.md), the cell automatically calls [updated(for:)](<../uicontentconfiguration-9eib5/updated(for_).md>) on its [contentConfiguration](contentconfiguration-1lcqh.md) when the cell’s [configurationState](configurationstate-4269k.md) changes, and applies the updated configuration back to the cell. The default value is [true](../../swift/true.md).

If you override [updateConfiguration(using:)](<updateconfiguration(using_).md>) to manually update and customize the content configuration, disable automatic updates by setting this property to [false](../../swift/false.md).

## See Also

### Managing the content

- [contentConfiguration](contentconfiguration-13e7k.md) — The current content configuration of the cell.
- [contentView](contentview.md) — The main view that you add your cell’s custom content to.
