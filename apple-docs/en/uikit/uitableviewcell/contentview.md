---
title: contentView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/contentview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/contentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/contentview.json'
content_hash: 'sha256:f0ea6429c39c41b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# contentView

<sub>Instance Property</sub>

The content view of the cell object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentView: UIView { get }
```

## Discussion

The content view of a [UITableViewCell](../uitableviewcell.md) object is the default superview for content that the cell displays. If you want to customize cells by simply adding additional views, you should add them to the content view so they position appropriately as the cell transitions in to and out of editing mode.

## See Also

### Related Documentation

- [backgroundView](backgroundview.md) — The view to use as the background of the cell.

### Managing the content

- [defaultContentConfiguration()](<defaultcontentconfiguration().md>) — Retrieves a default list content configuration for the cell’s style.
- [contentConfiguration](contentconfiguration-9ktox.md) — The current content configuration of the cell.
- [automaticallyUpdatesContentConfiguration](automaticallyupdatescontentconfiguration.md) — A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.
