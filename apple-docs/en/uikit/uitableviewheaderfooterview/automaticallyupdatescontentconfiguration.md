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
doc_path: /documentation/uikit/uitableviewheaderfooterview/automaticallyupdatescontentconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/automaticallyupdatescontentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/automaticallyupdatescontentconfiguration.json'
content_hash: 'sha256:597ab4351d304b89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# automaticallyUpdatesContentConfiguration

<sub>Instance Property</sub>

A Boolean value that determines whether the view automatically updates its content configuration when its state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyUpdatesContentConfiguration: Bool { get set }
```

## Discussion

When this value is [true](../../swift/true.md), the cell automatically calls [updated(for:)](<../uicontentconfiguration-9eib5/updated(for_).md>) on its [contentConfiguration](contentconfiguration-6b4eg.md) when the view’s [configurationState](configurationstate-7xj7r.md) changes, and applies the updated configuration back to the view. The default value is [true](../../swift/true.md).

If you override [updateConfiguration(using:)](<updateconfiguration(using_).md>) to manually update and customize the content configuration, disable automatic updates by setting this property to [false](../../swift/false.md).

## See Also

### Managing the content

- [defaultContentConfiguration()](<defaultcontentconfiguration().md>) — Retrieves a default list content configuration for the view’s style.
- [contentConfiguration](contentconfiguration-6b4eg.md) — The current content configuration of the view.
- [contentView](contentview.md) — The content view of the header or footer.
