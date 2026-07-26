---
title: contentConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcell/contentconfiguration-1lcqh
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/contentconfiguration-1lcqh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/contentconfiguration-1lcqh.json'
content_hash: 'sha256:0778ddda43383e5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# contentConfiguration

<sub>Instance Property</sub>

The current content configuration of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) id<UIContentConfiguration> contentConfiguration;
```

## Discussion

Using a content configuration, you can set the cell’s content and styling for a variety of different cell states.

Setting a content configuration replaces the existing [contentView](contentview.md) of the cell with a new content view instance from the configuration, or directly applies the configuration to the existing content view if the configuration is compatible with the existing content view type.

The default value is `nil`. After you set a content configuration to this property, setting this property back to `nil` replaces the current content view with a new, empty content view.

## See Also

### Managing the content

- [automaticallyUpdatesContentConfiguration](automaticallyupdatescontentconfiguration.md) — A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.
- [contentView](contentview.md) — The main view that you add your cell’s custom content to.
