---
title: selectedBackgroundView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcell/selectedbackgroundview
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/selectedbackgroundview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/selectedbackgroundview.json'
content_hash: 'sha256:04dc02a4d9ae2a5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# selectedBackgroundView

<sub>Instance Property</sub>

The view that displays just above the background view for a selected cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectedBackgroundView: UIView? { get set }
```

## Discussion

You can use this view to give a selected cell a custom appearance. When the cell has a selected state, this view layers above the [backgroundView](backgroundview.md) and behind the [contentView](contentview.md).

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets [backgroundConfiguration](backgroundconfiguration-rgj4.md) to `nil`.

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](backgroundconfiguration-rgj4.md) — The current background configuration of the cell.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The view that displays behind the cell’s other content.
