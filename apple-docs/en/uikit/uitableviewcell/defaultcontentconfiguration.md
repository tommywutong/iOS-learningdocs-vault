---
title: defaultContentConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/defaultcontentconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/defaultcontentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/defaultcontentconfiguration.json'
content_hash: 'sha256:04845f4ca976b6bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# defaultContentConfiguration

<sub>Instance Method</sub>

Retrieves a default list content configuration for the cell’s style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UIListContentConfiguration *) defaultContentConfiguration;
```

## Return Value

A default list content configuration. The system determines default values for the configuration according to the section where the cell appears.

## Discussion

The default content configuration has preconfigured default styling, but doesn’t contain any content. After you get the default configuration, you assign your content to it, customize any other properties, and assign it to the cell as the current [contentConfiguration](contentconfiguration-9ktox.md).

```swift
var content = cell.defaultContentConfiguration()

// Configure content.
content.image = UIImage(systemName: "star")
content.text = "Favorites"

// Customize appearance.
content.imageProperties.tintColor = .purple

cell.contentConfiguration = content
```

## See Also

### Managing the content

- [contentConfiguration](contentconfiguration-2lzvp.md) — The current content configuration of the cell.
- [automaticallyUpdatesContentConfiguration](automaticallyupdatescontentconfiguration.md) — A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.
- [contentView](contentview.md) — The content view of the cell object.
