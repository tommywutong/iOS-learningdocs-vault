---
title: backgroundView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcell/backgroundview
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/backgroundview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/backgroundview.json'
content_hash: 'sha256:2debb55fea6a6db9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# backgroundView

<sub>Instance Property</sub>

The view that displays behind the cell’s other content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundView: UIView? { get set }
```

## Discussion

Use this property to assign a custom background view to the cell. The background view appears behind the content view and its frame automatically adjusts so that it fills the bounds of the cell.

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets [backgroundConfiguration](backgroundconfiguration-rgj4.md) to `nil`.

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](backgroundconfiguration-rgj4.md) — The current background configuration of the cell.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [selectedBackgroundView](selectedbackgroundview.md) — The view that displays just above the background view for a selected cell.
