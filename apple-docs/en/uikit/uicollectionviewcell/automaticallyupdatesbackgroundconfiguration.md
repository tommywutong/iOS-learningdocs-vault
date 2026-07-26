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
doc_path: /documentation/uikit/uicollectionviewcell/automaticallyupdatesbackgroundconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/automaticallyupdatesbackgroundconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/automaticallyupdatesbackgroundconfiguration.json'
content_hash: 'sha256:041d8d22d26a614c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# automaticallyUpdatesBackgroundConfiguration

<sub>Instance Property</sub>

A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyUpdatesBackgroundConfiguration: Bool { get set }
```

## Discussion

When this value is [true](../../swift/true.md), the cell automatically calls `updated(for:)` on its [backgroundConfiguration](backgroundconfiguration-39dc0.md) when the cell’s [configurationState](configurationstate-4269k.md) changes, and applies the updated configuration back to the cell. The default value is [true](../../swift/true.md).

If you override [updateConfiguration(using:)](<updateconfiguration(using_).md>) to manually update and customize the background configuration, disable automatic updates by setting this property to [false](../../swift/false.md).

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](backgroundconfiguration-rgj4.md) — The current background configuration of the cell.
- [backgroundView](backgroundview.md) — The view that displays behind the cell’s other content.
- [selectedBackgroundView](selectedbackgroundview.md) — The view that displays just above the background view for a selected cell.
