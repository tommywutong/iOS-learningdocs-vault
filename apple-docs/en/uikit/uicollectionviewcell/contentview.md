---
title: contentView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcell/contentview
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/contentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/contentview.json'
content_hash: 'sha256:ec7fe3196439fd68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# contentView

<sub>Instance Property</sub>

The main view that you add your cell’s custom content to.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentView: UIView { get }
```

## Discussion

When configuring a cell, you add any custom views representing your cell’s content to this view. The cell object places the content in this view in front of any background views.

## See Also

### Managing the content

- [contentConfiguration](contentconfiguration-13e7k.md) — The current content configuration of the cell.
- [automaticallyUpdatesContentConfiguration](automaticallyupdatescontentconfiguration.md) — A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.
