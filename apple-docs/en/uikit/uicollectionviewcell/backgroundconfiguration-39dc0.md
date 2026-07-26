---
title: backgroundConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcell/backgroundconfiguration-39dc0
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/backgroundconfiguration-39dc0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/backgroundconfiguration-39dc0.json'
content_hash: 'sha256:2a8fb64081c4e603'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# backgroundConfiguration

<sub>Instance Property</sub>

The current background configuration of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) UIBackgroundConfiguration * backgroundConfiguration;
```

## Discussion

Using a background configuration, you can obtain system default background styling for a variety of different cell states. Create a background configuration with one of the default system styles, customize the configuration to match your cell’s style as needed, and assign the configuration to this property.

```objc
UIBackgroundConfiguration *backgroundConfig = [UIBackgroundConfiguration listPlainCellConfiguration];

// Set a nil background color to use the view's tint color.
[backgroundConfig setBackgroundColor:nil];

[cell setBackgroundConfiguration:backgroundConfig];
```

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets the following APIs to `nil`:

- [backgroundColor](../uiview/backgroundcolor.md)
- [backgroundView](backgroundview.md)
- [selectedBackgroundView](selectedbackgroundview.md)

## See Also

### Configuring the background

- [defaultBackgroundConfiguration](defaultbackgroundconfiguration.md) — Retrieves a background configuration with system default values.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The view that displays behind the cell’s other content.
- [selectedBackgroundView](selectedbackgroundview.md) — The view that displays just above the background view for a selected cell.
