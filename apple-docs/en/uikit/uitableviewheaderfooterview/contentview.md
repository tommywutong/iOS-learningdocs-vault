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
doc_path: /documentation/uikit/uitableviewheaderfooterview/contentview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/contentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/contentview.json'
content_hash: 'sha256:6ec171debf672cca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# contentView

<sub>Instance Property</sub>

The content view of the header or footer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentView: UIView { get }
```

## Discussion

To create your header or footer content, you add subviews to the view in this property. Your custom subviews represent the main content of your header or footer. Be sure to configure all subviews.

## See Also

### Managing the content

- [defaultContentConfiguration()](<defaultcontentconfiguration().md>) — Retrieves a default list content configuration for the view’s style.
- [contentConfiguration](contentconfiguration-6b4eg.md) — The current content configuration of the view.
- [automaticallyUpdatesContentConfiguration](automaticallyupdatescontentconfiguration.md) — A Boolean value that determines whether the view automatically updates its content configuration when its state changes.
